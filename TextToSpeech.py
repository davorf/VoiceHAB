import Settings, VoiceHAB
import pyglet, os, pyvona
from os import path
from requests.exceptions import HTTPError
from gtts import gTTS

def PlayAudioFile(FileName = Settings.TemporaryAudioFileName, FilePath = Settings.ApplicationDir):
    pyglet.resource.path.clear()
    pyglet.resource.path.append(FilePath)
    pyglet.resource.reindex()
    
    AudioFile = pyglet.resource.media(FileName, streaming = False)
    AudioFile.play()

    def ExitPyglet(self):
        pyglet.app.exit()

    pyglet.clock.schedule_once(ExitPyglet, AudioFile.duration)
    pyglet.app.run()
    
def TextToSpeech(Phrase):
    try:
        SpeechFileFullPath = path.join(Settings.ApplicationDir, Settings.TemporaryAudioFileName)
        
        if Settings.TextToSpeechEngine.lower() == 'ivona':
            TTS = pyvona.create_voice(Settings.IvonaAccessKey, Settings.IvonaSecretKey)
            TTS.region = 'eu-west'
            TTS.voice_name = Settings.IvonaVoice
            TTS.codec = 'mp3'
            TTS.fetch_voice(Phrase, SpeechFileFullPath)
        else:
            TTS = gTTS(text = Phrase, lang = Settings.GoogleLanguageCode)            
            TTS.save(SpeechFileFullPath)

        PlayAudioFile()

        os.remove(SpeechFileFullPath)
    except HTTPError as e:
        print('%s Text-To-Speech module might not be updated: ' % Settings.TextToSpeechEngine, e)
    except Exception as e:
        print('Unknown %s Text-To-Speech module error: ' % Settings.TextToSpeechEngine, e)
