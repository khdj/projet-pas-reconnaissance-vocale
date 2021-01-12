# install youtube_dl
# install ffmpeg
# install ffprobe

from __future__ import unicode_literals
import youtube_dl


def download(link, format='mp3', lang='en'):

    ydl_opts = {
        'format': f"{format}/best",
        'writesubtitles': True,
        'subtitleslangs': [lang],
        'subtitlesformat': 'vtt/best',
        'outtmpl': '/Audios_files/%(upload_date)s %(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': format,
            'preferredquality': '192'
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(link, download=False)
    print("Download SUCCESSFUL")

    upload_date = meta['upload_date']
    formatted_title = youtube_dl.utils.sanitize_filename(meta['title'])

    audio_file_name = f"{upload_date} {formatted_title}.mp3"
    subs_file_name = f"{upload_date} {formatted_title}.{lang}.vtt"

    return audio_file_name, subs_file_name
