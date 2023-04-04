from time import sleep
from pygame import mixer
import tempfile
import audioToText, chatGPT, recording, TextToAudio
from os import system

chatGPT.openai.api_key = chatGPT.openaiKey
state = True

print('\n## English Speaking Bot ##\n')

with tempfile.TemporaryDirectory() as tempdir: #tmp directory to store audio files
     while state:
          print("Press 'W' to ask and 'CTRL' to stop ")
          userKeyboard = input("your input: ")
          if userKeyboard.upper() == 'W':
             recording.record(12,tempdir,tempdir) #voice recorder
          texto = audioToText.ToText(tempdir)  #voice decode to text
          print(texto)   #show the result of the decode
          answer = chatGPT.chatingGPT(texto) #give the text to gpt
          TextToAudio.BotTalk(answer, tempdir) #transform the gpt's answer in audio

          mixer.init()
          mixer.music.load(tempdir+'/botaudio.mp3') #plays the audio response
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

         

    
          

     
    
