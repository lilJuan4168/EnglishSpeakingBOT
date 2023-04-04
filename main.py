from time import sleep
from pygame import mixer
import tempfile
import audioToText, chatGPT, recording, TextToAudio

chatGPT.openai.api_key = chatGPT.openaiKey

print('## English Speaking Bot ##')
sleep(2)
with tempfile.TemporaryDirectory() as tempdir:
     print("Press 'W' to ask and 'CTRL' to stop ")
     userKeyboard = input()
     if userKeyboard.upper() == 'W':
          recording.record(15,tempdir,tempdir)
     sleep(15)
     texto = audioToText.ToText(tempdir)
     answer = chatGPT.chatingGPT(texto)
     TextToAudio.BotTalk(answer, tempdir)

     mixer.init()
     mixer.music.load(tempdir+'/botaudio.mp3')
     mixer.music.play()
     input()
         

    
          

     
    
