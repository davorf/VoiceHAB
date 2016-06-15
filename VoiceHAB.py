import Settings
import random
import urllib.request
import speech_recognition as sr
import TextToSpeech as TTS

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
                    self.ProcessMessage('Google Speech Recognition denied request for result')

                if RecognizedWakeUp == Settings.WakeUpPhrase:
                    TTSGreeting = random.choice(open(Settings.GreetingDataFile).readlines())
                    self.ProcessMessage(TTSGreeting)
                    self.ListenForCommand()

    def ListenForCommand(self):
        with Mic as SourceCommand:
            AudioCommand = Rec.listen(SourceCommand)

            RecognizedCommand = ''

            try:
                RecognizedCommand = Rec.recognize_google(AudioCommand)
            except sr.UnknownValueError:
                TTSError = random.choice(open(Settings.ErrorDataFile).readlines())
                self.ProcessMessage(TTSError)
            except sr.RequestError:
                self.ProcessMessage('Google Speech Recognition denied request for result')

            if RecognizedCommand != '':
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

    def ProcessMessage(self, Message):
        if Settings.UseTextToSpeech:
            TTS.TextToSpeech(Message)
        else:
            print(Message)

    def InitializeModules(self):
        TTSInitialization = random.choice(open(Settings.InitializationDataFile).readlines())
        self.ProcessMessage(TTSInitialization)
        
        global Rec
        global Mic
        
        Rec = sr.Recognizer()
        Mic = sr.Microphone()

        with Mic as SourceInitialize:
            Rec.adjust_for_ambient_noise(SourceInitialize)
        
