import logging as L
import os
import Settings, VoiceHAB
import SoundPlayer as SP
from os import path
from requests.exceptions import HTTPError

if Settings.TextToSpeechEngine.lower() == 'ivona':
    import pyvona
else:
    from gtts import gTTS

def TextToSpeech(Phrase):
    L.debug('Phrase to be spoken: %s' % Phrase)
    
    try:
        if Phrase.strip() != '':
            SpeechFileFullPath = path.join(Settings.SoundsDir, Settings.TemporaryAudioFileName)
            
            if Settings.TextToSpeechEngine.lower() == 'ivona':
                TTS = pyvona.create_voice(Settings.IvonaAccessKey, Settings.IvonaSecretKey)
                TTS.region = 'eu-west'
                TTS.voice_name = Settings.IvonaVoice
                TTS.codec = 'mp3'
                TTS.fetch_voice(Phrase, SpeechFileFullPath)
            else:
                TTS = gTTS(text = Phrase, lang = Settings.GoogleLanguageCode)            
                TTS.save(SpeechFileFullPath)

            SP.PlayAudioFile()

            os.remove(SpeechFileFullPath)
    except HTTPError as e:
        L.error('%s Text-To-Speech module might not be updated: ' % Settings.TextToSpeechEngine, e)
    except Exception as e:
        L.error('Unknown %s Text-To-Speech module error: ' % Settings.TextToSpeechEngine, e)
