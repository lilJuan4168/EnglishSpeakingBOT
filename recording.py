import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment 

def record(seconds, outputWAVpath, ouputMP3path):
    myrecording = sd.rec(int(seconds * 44100), samplerate=44100, channels=2)
    print("Starting...")
    try:
        sd.wait()
    except KeyboardInterrupt:
        pass
    print("\nFinished...")
    write(outputWAVpath+'/output.wav', 44100, myrecording) 
    sound = AudioSegment.from_wav(outputWAVpath+'/output.wav') 
    sound.export(ouputMP3path+'/myVoice.mp3', format='mp3')
    return True



