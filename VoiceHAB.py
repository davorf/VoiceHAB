import random, requests, re
import logging as L
import speech_recognition as sr
import Settings
import Messages as M
import OtherRequests as OR
import SpeechToText as STT
import VoiceRecorder as VR
import SoundPlayer as SP

Instance = None
def init():
    L.debug('Initializing')
    
    global Instance
    Instance = Main()

class Main():    
    def ListenForWakeUp(self):
        TTSReady = random.choice(open(Settings.FinalizationDataFile).readlines())
        M.ProcessMessage(TTSReady)
        
        while True:
            L.debug('Listening for a wake-up phrase')
            
            RecognizedWakeUp = ''
            RecognizedWakeUp = STT.SpeechToText(Settings.UseOfflineWakeUp)
            
            WakeUpRegExPattern = r'\b%s\b' % Settings.WakeUpPhrase
            WakeUpRegExResult = re.search(WakeUpRegExPattern, RecognizedWakeUp, re.IGNORECASE)
            
            if WakeUpRegExResult:
                if Settings.UseTextToSpeech:
                    TTSGreeting = random.choice(open(Settings.GreetingDataFile).readlines())
                    M.ProcessMessage(TTSGreeting)
                else:
                    SP.PlayAudioFile(FileName = 'StartBeep.mp3')
                    
                self.ListenForCommand()

    def ListenForCommand(self):
        L.debug('Listening for a voice command')
        
        RecognizedCommand = ''
        RecognizedCommand = STT.SpeechToText()

        if RecognizedCommand != '':
            CommandRegExPattern = r'\b%s\b' % Settings.GeneralKnowledgeTriggerPhrase
            CommandRegExResult = re.search(CommandRegExPattern, RecognizedCommand, re.IGNORECASE)

            SP.PlayAudioFile(FileName = 'EndBeep.mp3')

            if (CommandRegExResult) and (Settings.UseGeneralKnowledge):
                if Settings.GeneralKnowledgeEngine.lower() == 'apiai':
                    OR.QueryApiAI(RecognizedCommand)
            else:            
                VoiceCommandItemURL = ''
                
                if Settings.Port.strip() != '':
                    TrimmedHostAndPort = Settings.HostName.strip() + ':' + Settings.Port.strip()
                else:
                    TrimmedHostAndPort = Settings.HostName.strip()

                if Settings.SSLConnection:
                    URLPrefix = 'https://'
                else:
                    URLPrefix = 'http://' 
                
                VoiceCommandItemURL = URLPrefix + TrimmedHostAndPort + '/CMD?' + Settings.VoiceCommandItem + '=' + '"' + RecognizedCommand + '"'

                if (Settings.Username.strip() != '') and (Settings.Password.strip() != ''):
                    HTTPGetResult = requests.get(VoiceCommandItemURL, auth=(Settings.Username.strip(), Settings.Password.strip()))
                else:
                    HTTPGetResult = requests.get(VoiceCommandItemURL)

    def InitializeModules(self):
        TTSInitialization = random.choice(open(Settings.InitializationDataFile).readlines())
        M.ProcessMessage(TTSInitialization)

        global Mic
        global Rec
        global MicThreshold
        global AuthenticatedUserId
        
        Mic = sr.Microphone()
        Rec = sr.Recognizer()

        AuthenticatedUserId = ''

        with Mic as SourceInitialize:
            Rec.adjust_for_ambient_noise(SourceInitialize)
            MicThreshold = Rec.energy_threshold
