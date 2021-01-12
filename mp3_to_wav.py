from os import path
from pydub import AudioSegment


def convert(input, output):
    # convert wav to mp3
    sound = AudioSegment.from_mp3(input)
    sound.export(output, format="wav")
