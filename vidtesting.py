import moviepy.editor
import wave
'''video = moviepy.editor.VideoFileClip("videtest.mp4")
audio = video.audio
audio.write_audiofile("extracted_audio.wav")'''

'''my_clip = moviepy.editor.VideoFileClip("videtest.mp4")
audiofile = moviepy.editor.AudioFileClip("extracted_audio.wav")
my_clip = my_clip.set_audio(audiofile)
my_clip.write_videofile("final.mp4", fps=25)'''


'''video = moviepy.editor.VideoFileClip("final.mp4")
audio = video.audio
audio.write_audiofile("dec_audio.wav")'''

audio = wave.open("dec_audio.wav", mode='rb')
frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
string = "".join(chr(int("".join(map(str, extracted[i:i + 8])), 2)) for i in range(0, len(extracted), 8))
decoded = string.split("###")[0]
print(decoded)
audio.close()