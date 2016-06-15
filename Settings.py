import configparser
from os import path

ApplicationDir = path.dirname(path.abspath(__file__))
VoiceHABSettings = path.join(ApplicationDir, 'VoiceHAB.ini')
DataDir = path.join(ApplicationDir, 'data')
SpeechDir = path.join(DataDir, 'speech')
InitializationDataFile = path.join(SpeechDir, 'initialization.vhb')
GreetingDataFile = path.join(SpeechDir, 'greeting.vhb')
ReplyDataFile = path.join(SpeechDir, 'reply.vhb')
ErrorDataFile = path.join(SpeechDir, 'error.vhb')
TemporaryAudioFileName = 'Audio.mp3'

Settings = configparser.ConfigParser()
Settings.read(VoiceHABSettings)

WakeUpPhrase = Settings.get('SpeechToText', 'WakeUpPhrase')

UseTextToSpeech = Settings.getboolean('TextToSpeech', 'UseTextToSpeech')
TextToSpeechEngine = Settings.get('TextToSpeech', 'TextToSpeechEngine')

GoogleLanguageCode = Settings.get('GoogleTTS', 'GoogleLanguageCode')

IvonaAccessKey = Settings.get('IvonaTTS', 'IvonaAccessKey')
IvonaSecretKey = Settings.get('IvonaTTS', 'IvonaSecretKey')
IvonaVoice = Settings.get('IvonaTTS', 'IvonaVoice')

HostName = Settings.get('OpenHAB', 'HostName')
Port = Settings.get('OpenHAB', 'Port')
SSLConnection = Settings.getboolean('OpenHAB', 'SSLConnection')
Username = Settings.get('OpenHAB', 'Username')
Password = Settings.get('OpenHAB', 'Password')
VoiceCommandItem = Settings.get('OpenHAB', 'VoiceCommandItem')

