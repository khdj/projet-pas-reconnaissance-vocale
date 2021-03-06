import webvtt


# ex title : '20201013 Why is the world warming up _ Kristen Bell + Giant Ant.en.vtt'
def vtt_to_text(vtt_file_name):
    vtt = webvtt.read(vtt_file_name)
    transcript = ""

    lines = []
    for line in vtt:
        lines.extend(line.text.strip().splitlines())

    previous = None
    for line in lines:
        if line == previous:
            continue
        transcript += " " + line
        previous = line
    return transcript
