import speech_recognition as sr
import logging as L
import Settings
import VoiceHAB as VH
import Messages as M

def SpeechToText(UseOfflineSpeechRecognition = False):    
    with VH.Mic as SpeechSource:        
        SpeechAudio = VH.Rec.listen(SpeechSource)
        RecognizedSpeech = ''

        SpeechToTextEngine = Settings.SpeechToTextEngine.lower()

        try:
            if UseOfflineSpeechRecognition:
                L.debug('Using Sphinx as offline speech recognition engine')
                
                RecognizedSpeech = VH.Rec.recognize_sphinx(SpeechAudio)
            else:
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

                L.debug('Spoken phrase: %s' % RecognizedSpeech)                
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            M.ProcessMessage('%s Speech Recognition denied request for result' % Settings.SpeechToTextEngine)

        return RecognizedSpeech
