import pygame
from gtts import gTTS
import time

def play_audio(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    # Чекаємо, поки відтворення завершиться
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

text = "Сергій, пора зробити паузу, відпочинь"
tts = gTTS(text=text, lang='uk')
tts.save("MyProjects/speech/temp.mp3")

play_audio("MyProjects/speech/temp.mp3")
print('Done!')
