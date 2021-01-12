# install youtube_dl
# install ffmpeg
# install ffprobe

from __future__ import unicode_literals
import youtube_dl


def download(link, format='mp3', lang='en'):
    output_audio_path = "/Audios_files/%(upload_date)s %(title)s.%(ext)s"
    ydl_opts = {
        'format': f"{format}/best",
        'writesubtitles': True,
        'subtitleslangs': [lang],
        'subtitlesformat': 'srt/ass/vtt/best',
        'outtmpl': '/Audios_files/%(upload_date)s %(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': format,
            'preferredquality': '192'
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print("Download SUCCESSFUL")

    return
