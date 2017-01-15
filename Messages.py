import logging as L
import Settings
import TextToSpeech as TTS

def ProcessMessage(Message):
    if Settings.UseTextToSpeech:
        TTS.TextToSpeech(Message)
    else:
        L.info(Message)
