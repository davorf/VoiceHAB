import Settings
import TextToSpeech as TTS

def ProcessMessage(Message):
    if Settings.UseTextToSpeech:
        TTS.TextToSpeech(Message)
    else:
        print(Message)
