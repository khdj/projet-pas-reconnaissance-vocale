from pydub import AudioSegment


def convert(input_path, output_path=None):
    # convert wav to mp3
    sound = AudioSegment.from_mp3(input_path)
    if not output_path:
        output_path = f"{input_path.rpartition('.')[0]}.wav"
    sound.export(output_path, format="wav")

    return output_path

"https://youtu.be/1j0X9QMF--M"