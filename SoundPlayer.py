import os
import logging as L
import Settings
from os import path

if Settings.TextToSpeechAudioEngine.lower() == 'pygame':
    import pygame
else:
    import pyglet

def PlayAudioFile(FileName = Settings.TemporaryAudioFileName, FilePath = Settings.SoundsDir):
    L.debug('Playing audio file using %s' % Settings.TextToSpeechAudioEngine)
    
    if Settings.TextToSpeechAudioEngine.lower() == 'pygame':
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(FilePath, FileName))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    else:
        pyglet.resource.path.clear()
        pyglet.resource.path.append(FilePath)
        pyglet.resource.reindex()
        
        AudioFile = pyglet.resource.media(FileName, streaming = False)
        AudioFile.play()

        def ExitPyglet(self):
            pyglet.app.exit()

        pyglet.clock.schedule_once(ExitPyglet, AudioFile.duration)
        pyglet.app.run()
