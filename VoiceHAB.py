import Settings
import speech_recognition as sr
import TextToSpeech as TTS
import urllib.request

Instance = None
def init():
    global Instance
    Instance = Main()

class Main():    
    def ListenForWakeUp(self):
        while True:            
            self.ProcessMessage('Listening for wake-up...')
            with Mic as SourceWakeUp:
                AudioWakeUp = Rec.listen(SourceWakeUp)
                RecognizedWakeUp = ''

                try:
                    RecognizedWakeUp = Rec.recognize_google(AudioWakeUp)
                except sr.UnknownValueError:
                    self.ProcessMessage('Google Speech Recognition could not recognize spoken text')
                except sr.RequestError:
                    self.ProcessMessage('Google Speech Recognition denied request for result')

                if RecognizedWakeUp == Settings.WakeUpPhrase:
                    self.ListenForCommand()

    def ListenForCommand(self):
        self.ProcessMessage('Listening for command...')
        with Mic as SourceCommand:
            AudioCommand = Rec.listen(SourceCommand)

            RecognizedCommand = ''

            try:
                RecognizedCommand = Rec.recognize_google(AudioCommand)
            except sr.UnknownValueError:
                self.ProcessMessage('Google Speech Recognition could not recognize spoken text')
            except sr.RequestError:
                self.ProcessMessage('Google Speech Recognition denied request for result')

            if RecognizedCommand != '':
                if (Settings.Username != '') and (Settings.Password != ''):
                    VoiceCommandItemURL = 'http://' + Settings.Username + ':' + Settings.Password + '@' + Settings.HostName + '/CMD?' + Settings.VoiceCommandItem + '=' + '"' + RecognizedCommand + '"'
                else:
                    VoiceCommandItemURL = 'http://' + Settings.HostName + '/CMD?' + Settings.VoiceCommandItem + '=' + '"' + RecognizedCommand + '"'
                    
                urllib.request.urlopen(VoiceCommandItemURL).read()            

    def ProcessMessage(self, Message):
        if Settings.UseTextToSpeech:
            TTS.TextToSpeech(Message)
        else:
            print(Message)

    def InitializeModules(self):
        self.ProcessMessage('Initializing...')
        
        global Rec
        global Mic
        
        Rec = sr.Recognizer()
        Mic = sr.Microphone()

        with Mic as SourceInitialize:
            Rec.adjust_for_ambient_noise(SourceInitialize)
        
