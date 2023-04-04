import whisper

def ToText(audioPath):
    ModelSet = 'base'
    model = whisper.load_model(ModelSet)
    result = model.transcribe(audioPath+'/myVoice.wav')#myVoice.mp3
    return result["text"]
    
