import speech_recognition as sr
import Settings
import VoiceHAB as VH
import Messages as M

def SpeechToText():    
    with VH.Mic as SpeechSource:        
        SpeechAudio = VH.Rec.listen(SpeechSource)
        RecognizedSpeech = ''

        SpeechToTextEngine = Settings.SpeechToTextEngine.lower()

        try:
            if SpeechToTextEngine == 'bing':
                RecognizedSpeech = VH.Rec.recognize_bing(SpeechAudio, Settings.BingSpeechAPIKey)
            elif SpeechToTextEngine == 'apiai':
                RecognizedSpeech = VH.Rec.recognize_api(SpeechAudio, client_access_token = Settings.ApiAIClientAccessToken)                
            elif SpeechToTextEngine == 'witai':
                RecognizedSpeech = VH.Rec.recognize_wit(SpeechAudio, key = Settings.WitAIClientAccessToken)
            elif SpeechToTextEngine == 'sphinx':
                RecognizedSpeech = VH.Rec.recognize_sphinx(SpeechAudio)
            else:
                RecognizedSpeech = VH.Rec.recognize_google(SpeechAudio)                
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            M.ProcessMessage('%s Speech Recognition denied request for result' % Settings.SpeechToTextEngine)

        return RecognizedSpeech
        
