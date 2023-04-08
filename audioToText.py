import whisper

def ToText(audioPath, modelSet):
    model = whisper.load_model(modelSet)
    result = model.transcribe(audioPath+'/myVoice.wav')#myVoice.mp3
    return result["text"]
    
