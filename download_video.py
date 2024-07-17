import yt_dlp

def download_youtube_video(url, output_path='.'):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Video descargado en: {output_path}")
    except yt_dlp.utils.DownloadError as e:
        print(f"Ha ocurrido un error al descargar el video: {e}")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")


url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  
download_youtube_video(url)
