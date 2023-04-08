from time import sleep
from pygame import mixer
from os import system
import tempfile
import audioToText, chatGPT, recording, textToAudio
import json

with open('dataConfig.json', 'r') as data: #Import the configuration from json
    vars = json.load(data)
    print(vars['seconds'])
    chatGPT.openai.api_key = vars['openaiAPIkey']
    state = True

    print('\n## English Speaking Bot ##\n')

    with tempfile.TemporaryDirectory() as tempdir: #tmp directory to store audio files
        while state:
            print("Press 'W' to ask and 'CTRL' to stop ")
            userKeyboard = input("your input: ")

            if userKeyboard.upper() == 'W':
               recording.record(vars['seconds'], tempdir) #voice recorder
            elif userKeyboard.upper() != 'W':
               print('Invalid input')
               sleep(2)
               break
            texto = audioToText.ToText(tempdir, vars['modelSet'])  #voice decode to text
            print(texto)   #show the result of the decode
          
            answer = chatGPT.chatingGPT(texto, vars['maxTokens']) #give the text to gpt
            textToAudio.BotTalk(answer, tempdir, vars['languages']) #transform the gpt's answer in audio

            mixer.init()
            mixer.music.load(tempdir+'/botaudio.mp3') #plays the audio response
            mixer.music.play()
            userKeyboard2 = input("continue? [Y/n]: ")
            sleep(1)
            system('clear')
            if userKeyboard2.upper() == 'Y':
               mixer.music.stop()
               continue
            elif userKeyboard2.upper() == 'N':
               state = False
            else:
               print('Insert a valid value')
               sleep(5)
               break

         

    
          

     
    
