#import pyaudio
#import wave

# def record_audio(filename, duration=5):
#     FORMAT = pyaudio.paInt16
#     CHANNELS = 1
#     RATE = 16000
#     CHUNK = 1024

#     audio = pyaudio.PyAudio()
#     stream = audio.open(format=FORMAT, channels=CHANNELS,
#                         rate=RATE, input=True,
#                         frames_per_buffer=CHUNK)

#     print("Recording...")

#     frames = []

#     for _ in range(0, int(RATE / CHUNK * duration)):
#         data = stream.read(CHUNK)
#         frames.append(data)

#     print("Finished recording")

#     stream.stop_stream()
#     stream.close()
#     audio.terminate()

#     with wave.open(filename, 'wb') as wf:
#         wf.setnchannels(CHANNELS)
#         wf.setsampwidth(audio.get_sample_size(FORMAT))
#         wf.setframerate(RATE)
#         wf.writeframes(b''.join(frames))


import openai
import os
import whisper

audio_filename = "hindi_test.mp3"
# record_audio(audio_filename)
model = whisper.load_model('small')
tr = model.transcribe(audio_filename)
t2 = model.transcribe(audio_filename, task='translate')
print(tr["text"])
print(t2["text"])

#print(t2)
# if name == "main":
#     main()