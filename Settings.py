import configparser
from os import path

ApplicationDir = path.dirname(path.abspath(__file__))
VoiceHABSettings = path.join(ApplicationDir, 'VoiceHAB.ini')
DataDir = path.join(ApplicationDir, 'data')
SpeechDir = path.join(DataDir, 'speech')
SoundsDir = path.join(DataDir, 'sounds')
InitializationDataFile = path.join(SpeechDir, 'initialization.vhb')
FinalizationDataFile = path.join(SpeechDir, 'finalization.vhb')
GreetingDataFile = path.join(SpeechDir, 'greeting.vhb')
ReplyDataFile = path.join(SpeechDir, 'reply.vhb')
ErrorDataFile = path.join(SpeechDir, 'error.vhb')
TemporaryAudioFileName = 'Audio.mp3'
VerificationEnrollFileName = 'Enrollment.wav'
VerificationVerifyFileName = 'Verification.wav'

Settings = configparser.ConfigParser()
Settings.read(VoiceHABSettings)

WakeUpPhrase = Settings.get('SpeechToText', 'WakeUpPhrase')
SpeechToTextEngine = Settings.get('SpeechToText', 'SpeechToTextEngine')
UseOfflineWakeUp = Settings.getboolean('SpeechToText', 'UseOfflineWakeUp')

UseTextToSpeech = Settings.getboolean('TextToSpeech', 'UseTextToSpeech')
TextToSpeechEngine = Settings.get('TextToSpeech', 'TextToSpeechEngine')
TextToSpeechAudioEngine = Settings.get('TextToSpeech', 'TextToSpeechAudioEngine')

HostName = Settings.get('OpenHAB', 'HostName')
Port = Settings.get('OpenHAB', 'Port')
SSLConnection = Settings.getboolean('OpenHAB', 'SSLConnection')
Username = Settings.get('OpenHAB', 'Username')
Password = Settings.get('OpenHAB', 'Password')
VoiceCommandItem = Settings.get('OpenHAB', 'VoiceCommandItem')

UseGeneralKnowledge = Settings.getboolean('GeneralKnowledge', 'UseGeneralKnowledge')
GeneralKnowledgeTriggerPhrase = Settings.get('GeneralKnowledge', 'GeneralKnowledgeTriggerPhrase')
GeneralKnowledgeEngine = Settings.get('GeneralKnowledge', 'GeneralKnowledgeEngine')

UseVoiceVerification = Settings.getboolean('VoiceVerification', 'UseVoiceVerification')

VoiceRecorderChunkSize = Settings.get('VoiceRecorder', 'VoiceRecorderChunkSize')
VoiceRecorderRate = Settings.get('VoiceRecorder', 'VoiceRecorderRate')

GoogleLanguageCode = Settings.get('Google', 'GoogleLanguageCode')

IvonaAccessKey = Settings.get('Ivona', 'IvonaAccessKey')
IvonaSecretKey = Settings.get('Ivona', 'IvonaSecretKey')
IvonaVoice = Settings.get('Ivona', 'IvonaVoice')

ApiAIClientAccessToken = Settings.get('ApiAI', 'ApiAIClientAccessToken')
ApiAIServerAccessToken = Settings.get('ApiAI', 'ApiAIServerAccessToken')

WitAIClientAccessToken = Settings.get('WitAI', 'WitAIClientAccessToken')
WitAIServerAccessToken = Settings.get('WitAI', 'WitAIServerAccessToken')

BingSpeechAPIKey = Settings.get('Bing', 'BingSpeechAPIKey')
