# pip install pipwin
# pipwin install pyaudio
# pip install SpeechRecognition
import speech_recognition as sr

rec = sr.Recognizer()
# Lists all mics available
# print(sr.Microphone().list_microphone_names())

# Using "with" so we don't have to worry about
# closing the mic later.
with sr.Microphone(0) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Recording")
    audio = rec.listen(mic)
    text = rec.recognize_google(audio, language="pt-BR")
    # Wait a few seconds in silence to stop recording
    print(text)
