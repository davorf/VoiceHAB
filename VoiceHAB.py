import Settings
import random, requests, re
import speech_recognition as sr
import Messages as M
import OtherRequests as OR
import SpeechToText as STT

Instance = None
def init():
    global Instance
    Instance = Main()

class Main():    
    def ListenForWakeUp(self):
        TTSReady = random.choice(open(Settings.FinalizationDataFile).readlines())
        M.ProcessMessage(TTSReady)
        
        while True:
            RecognizedWakeUp = ''
            RecognizedWakeUp = STT.SpeechToText()
            
            WakeUpRegExPattern = r'\b%s\b' % Settings.WakeUpPhrase
            WakeUpRegExResult = re.search(WakeUpRegExPattern, RecognizedWakeUp, re.IGNORECASE)
            
            if WakeUpRegExResult:
                TTSGreeting = random.choice(open(Settings.GreetingDataFile).readlines())
                M.ProcessMessage(TTSGreeting)
                self.ListenForCommand()

    def ListenForCommand(self):
        RecognizedCommand = ''
        RecognizedCommand = STT.SpeechToText()

        if RecognizedCommand != '':
            CommandRegExPattern = r'\b%s\b' % Settings.GeneralKnowledgeTriggerPhrase
            CommandRegExResult = re.search(CommandRegExPattern, RecognizedCommand, re.IGNORECASE)

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
        
        Mic = sr.Microphone()
        Rec = sr.Recognizer()

        with Mic as SourceInitialize:
            Rec.adjust_for_ambient_noise(SourceInitialize)
