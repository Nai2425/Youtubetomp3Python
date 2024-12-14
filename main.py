import yt_dlp
from moviepy import *
import os
from dotenv import load_dotenv

load_dotenv()
ffmpeg_path = os.getenv('FFMPEG_PATH')

def youtube_to_mp3(video_url, output_folder):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': ffmpeg_path,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download and conversion completed!")
    except Exception as e:
        print(f"Error: {e}")


video_url = input("Enter YouTube video URL: ")
output_folder = "downloads"
youtube_to_mp3(video_url, output_folder)
