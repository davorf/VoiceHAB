import pyaudio
import wave
import VoiceHAB as VH
import Settings
from sys import byteorder
from array import array
from struct import pack

def IsRecordingSilent(SoundData):
    return max(SoundData) < VH.MicThreshold

def NormalizeRecording(SoundData):    
    Times = float(16384) / max(abs(i) for i in SoundData)
    r = array('h')
    
    for i in SoundData:
        r.append(int(i * Times))
    return r

def TrimRecording(SoundData):
    def _trim(SoundData):
        RecordingStarted = False
        r = array('h')

        for i in SoundData:
            if not RecordingStarted and abs(i) > VH.MicThreshold:
                RecordingStarted = True
                r.append(i)
            elif RecordingStarted:
                r.append(i)
                
        return r

    SoundData = _trim(SoundData)
    SoundData.reverse()
    SoundData = _trim(SoundData)
    SoundData.reverse()
    
    return SoundData

def AddSilence(SoundData, Seconds):
    r = array('h', [0 for i in range(int(Seconds * int(Settings.VoiceRecorderRate)))])
    
    r.extend(SoundData)
    r.extend([0 for i in range(int(Seconds * int(Settings.VoiceRecorderRate)))])
    
    return r

def RecordSound():
    p = pyaudio.PyAudio()
    
    SoundStream = p.open(
        format = pyaudio.paInt16,
        channels = 1,
        rate = int(Settings.VoiceRecorderRate),
        input = True,
        output = True,
        frames_per_buffer = int(Settings.VoiceRecorderChunkSize))

    CountSilent = 0
    RecordingStarted = False

    r = array('h')

    while 1:
        SoundData = array('h', SoundStream.read(int(Settings.VoiceRecorderChunkSize)))

        if byteorder == 'big':
            SoundData.byteswap()
            
        r.extend(SoundData)

        Silent = IsRecordingSilent(SoundData)

        if Silent and RecordingStarted:
            CountSilent += 1
        elif not Silent and not RecordingStarted:
            RecordingStarted = True

        if RecordingStarted and CountSilent > 30:
            break

    SampleWidth = p.get_sample_size(pyaudio.paInt16)
    SoundStream.stop_stream()
    SoundStream.close()
    
    p.terminate()

    r = NormalizeRecording(r)
    r = TrimRecording(r)
    r = AddSilence(r, 0.5)
    return SampleWidth, r

def RecordToFile(Path):    
    SampleWidth, SoundData = RecordSound()
    
    SoundData = pack('<' + ('h' * len(SoundData)), *SoundData)

    RecordedFile = wave.open(Path, 'wb')
    RecordedFile.setnchannels(1)
    RecordedFile.setsampwidth(SampleWidth)
    RecordedFile.setframerate(int(Settings.VoiceRecorderRate))
    RecordedFile.writeframes(SoundData)
    RecordedFile.close()
