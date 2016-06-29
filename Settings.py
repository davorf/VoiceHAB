import configparser
from os import path

ApplicationDir = path.dirname(path.abspath(__file__))
VoiceHABSettings = path.join(ApplicationDir, 'VoiceHAB.ini')
DataDir = path.join(ApplicationDir, 'data')
SpeechDir = path.join(DataDir, 'speech')
InitializationDataFile = path.join(SpeechDir, 'initialization.vhb')
FinalizationDataFile = path.join(SpeechDir, 'finalization.vhb')
GreetingDataFile = path.join(SpeechDir, 'greeting.vhb')
ReplyDataFile = path.join(SpeechDir, 'reply.vhb')
ErrorDataFile = path.join(SpeechDir, 'error.vhb')
TemporaryAudioFileName = 'Audio.mp3'

Settings = configparser.ConfigParser()
Settings.read(VoiceHABSettings)

WakeUpPhrase = Settings.get('SpeechToText', 'WakeUpPhrase')
SpeechToTextEngine = Settings.get('SpeechToText', 'SpeechToTextEngine')

BingSpeechAPIKey = Settings.get('BingSTT', 'BingSpeechAPIKey')

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

UseGeneralKnowledge = Settings.getboolean('GeneralKnowledge', 'UseGeneralKnowledge')
GeneralKnowledgeTriggerPhrase = Settings.get('GeneralKnowledge', 'GeneralKnowledgeTriggerPhrase')
GeneralKnowledgeEngine = Settings.get('GeneralKnowledge', 'GeneralKnowledgeEngine')

ApiAIClientAccessToken = Settings.get('ApiAI', 'ApiAIClientAccessToken')
ApiAIServerAccessToken = Settings.get('ApiAI', 'ApiAIServerAccessToken')

WitAIClientAccessToken = Settings.get('WitAI', 'WitAIClientAccessToken')
WitAIServerAccessToken = Settings.get('WitAI', 'WitAIServerAccessToken')
