import Settings
import random, requests, re
import speech_recognition as sr
import Messages as MSG
import OtherRequests as OTR

Instance = None
def init():
    global Instance
    Instance = Main()

class Main():    
    def ListenForWakeUp(self):
        while True:
            TTSReady = random.choice(open(Settings.FinalizationDataFile).readlines())
            MSG.ProcessMessage(TTSReady)
            
            with Mic as SourceWakeUp:
                AudioWakeUp = Rec.listen(SourceWakeUp)
                RecognizedWakeUp = ''

                try:
                    RecognizedWakeUp = Rec.recognize_google(AudioWakeUp)
                except sr.UnknownValueError:
                    pass
                except sr.RequestError:
                    MSG.ProcessMessage('Google Speech Recognition denied request for result')

                WakeUpRegExPattern = r'\b%s\b' % Settings.WakeUpPhrase
                WakeUpRegExResult = re.search(WakeUpRegExPattern, RecognizedWakeUp, re.IGNORECASE)
                
                if WakeUpRegExResult:
                    TTSGreeting = random.choice(open(Settings.GreetingDataFile).readlines())
                    MSG.ProcessMessage(TTSGreeting)
                    self.ListenForCommand()

    def ListenForCommand(self):
        AudioCommand = Rec.listen(Mic)

        RecognizedCommand = ''

        try:
            RecognizedCommand = Rec.recognize_google(AudioCommand)
        except sr.UnknownValueError:
            TTSError = random.choice(open(Settings.ErrorDataFile).readlines())
            MSG.ProcessMessage(TTSError)
        except sr.RequestError:
            MSG.ProcessMessage('Google Speech Recognition denied request for result')

        if RecognizedCommand != '':
            CommandRegExPattern = r'\b%s\b' % Settings.GeneralKnowledgeTriggerPhrase
            CommandRegExResult = re.search(CommandRegExPattern, RecognizedCommand, re.IGNORECASE)

            if (CommandRegExResult) and (Settings.UseGeneralKnowledge):
                if Settings.GeneralKnowledgeEngine.lower() == 'apiai':
                    OTR.QueryApiAI(RecognizedCommand)
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
        MSG.ProcessMessage(TTSInitialization)
        
        global Rec
        global Mic
        
        Rec = sr.Recognizer()
        Mic = sr.Microphone()        

        with Mic as SourceInitialize:
            Rec.adjust_for_ambient_noise(SourceInitialize)       
