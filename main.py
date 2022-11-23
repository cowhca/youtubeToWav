from __future__ import unicode_literals
import youtube_dl
import ffmpeg
import sys

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'output.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([sys.argv[1]])
    stream = ffmpeg.input('output.m4a')
    stream = ffmpeg.output(stream, "output.wav")

