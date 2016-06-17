import Settings
import random
import urllib.request
import speech_recognition as sr
import Messages as MSG

Instance = None
def init():
    global Instance
    Instance = Main()

class Main():    
    def ListenForWakeUp(self):
        while True:            
            with Mic as SourceWakeUp:
                AudioWakeUp = Rec.listen(SourceWakeUp)
                RecognizedWakeUp = ''

                try:
                    RecognizedWakeUp = Rec.recognize_google(AudioWakeUp)
                except sr.UnknownValueError:
                    pass
                except sr.RequestError:
                    MSG.ProcessMessage('Google Speech Recognition denied request for result')

                if RecognizedWakeUp.lower() == Settings.WakeUpPhrase.lower():
                    TTSGreeting = random.choice(open(Settings.GreetingDataFile).readlines())
                    MSG.ProcessMessage(TTSGreeting)
                    self.ListenForCommand()

    def ListenForCommand(self):
        with Mic as SourceCommand:
            AudioCommand = Rec.listen(SourceCommand)

            RecognizedCommand = ''

            try:
                RecognizedCommand = Rec.recognize_google(AudioCommand)
            except sr.UnknownValueError:
                TTSError = random.choice(open(Settings.ErrorDataFile).readlines())
                MSG.ProcessMessage(TTSError)
            except sr.RequestError:
                MSG.ProcessMessage('Google Speech Recognition denied request for result')

            if RecognizedCommand != '':
                VoiceCommandItemURL = ''
                
                if (Settings.Username.strip() != '') and (Settings.Password.strip() != ''):
                    TrimmedUserPasswordString = Settings.Username.strip() + ':' + Settings.Password.strip() + '@'
                else:
                    TrimmedUserPasswordString = ''

                if Settings.Port.strip() != '':
                    TrimmedHostAndPort = Settings.HostName.strip() + ':' + Settings.Port.strip()
                else:
                    TrimmedHostAndPort = Settings.HostName.strip()

                if Settings.SSLConnection:
                    URLPrefix = 'https://'
                else:
                    URLPrefix = 'http://' 
                
                VoiceCommandItemURL = URLPrefix + TrimmedUserPasswordString + TrimmedHostAndPort + '/CMD?' + Settings.VoiceCommandItem + '=' + '"' + RecognizedCommand + '"'
                    
                urllib.request.urlopen(VoiceCommandItemURL).read()            

    def InitializeModules(self):
        TTSInitialization = random.choice(open(Settings.InitializationDataFile).readlines())
        MSG.ProcessMessage(TTSInitialization)
        
        global Rec
        global Mic
        
        Rec = sr.Recognizer()
        Mic = sr.Microphone()

        with Mic as SourceInitialize:
            Rec.adjust_for_ambient_noise(SourceInitialize)
        
