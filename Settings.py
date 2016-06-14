import configparser
from os import path

ApplicationDir = path.dirname(path.abspath(__file__))
VoiceHABSettings = path.join(ApplicationDir, 'VoiceHAB.ini')
TemporaryAudioFileName = 'Audio.mp3'

Settings = configparser.ConfigParser()
Settings.read(VoiceHABSettings)

WakeUpPhrase = Settings.get('SpeechToText', 'WakeUpPhrase')

LanguageCode = Settings.get('TextToSpeech', 'LanguageCode')
UseTextToSpeech = Settings.getboolean('TextToSpeech', 'UseTextToSpeech')

HostName = Settings.get('OpenHAB', 'HostName')
Username = Settings.get('OpenHAB', 'Username')
Password = Settings.get('OpenHAB', 'Password')
VoiceCommandItem = Settings.get('OpenHAB', 'VoiceCommandItem')

