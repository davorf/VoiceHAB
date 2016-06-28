import speech_recognition as sr
import VoiceHAB as VH
import Messages as M

def SpeechToText():    
    with VH.Mic as SpeechSource:        
        SpeechAudio = VH.Rec.listen(SpeechSource)
        RecognizedSpeech = ''

        try:
            RecognizedSpeech = VH.Rec.recognize_google(SpeechAudio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            M.ProcessMessage('Google Speech Recognition denied request for result')

        return RecognizedSpeech
        
