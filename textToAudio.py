from gtts import gTTS

def BotTalk(message, PathToSave, language):
    velocitySlow = False
    audio = gTTS(text=message, lang=language, slow=velocitySlow)
    audio.save(PathToSave+'/botaudio.mp3')
    return True