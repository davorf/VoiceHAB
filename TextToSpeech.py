import Settings, VoiceHAB
import pyglet, os
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
        TTS = gTTS(text = Phrase, lang = Settings.LanguageCode)

        SpeechFileFullPath = path.join(Settings.ApplicationDir, Settings.TemporaryAudioFileName)
        TTS.save(SpeechFileFullPath)

        PlayAudioFile()

        os.remove(SpeechFileFullPath)
    except HTTPError as e:
        print('Google Text-To-Speech module might not be updated: ', e)
    except Exception as e:
        print('Unknown Google Text-To-Speech module error: ', e)
