from time import sleep
from pygame import mixer
import tempfile
import audioToText, chatGPT, recording, TextToAudio
from os import system

chatGPT.openai.api_key = chatGPT.openaiKey
state = True
print('## English Speaking Bot ##')
sleep(2)
with tempfile.TemporaryDirectory() as tempdir:
     while state:
          print("Press 'W' to ask and 'CTRL' to stop ")
          userKeyboard = input("your input: ")
          if userKeyboard.upper() == 'W':
             recording.record(10,tempdir,tempdir)
          texto = audioToText.ToText(tempdir)
          print(texto)
          answer = chatGPT.chatingGPT(texto)
          TextToAudio.BotTalk(answer, tempdir)

          mixer.init()
          mixer.music.load(tempdir+'/botaudio.mp3')
          mixer.music.play()
          userKeyboard2 = input("continue? [Y/n]: ")
          sleep(1)
          system('clear')
          if userKeyboard2.upper() == 'Y':
              continue
          elif userKeyboard2.upper() == 'N':
              state = False
          else:
              print('Insert a valid value')
              sleep(5)
              break

         

    
          

     
    
