from fastapi import FastAPI
from pydantic import BaseModel
from pytube import YouTube
from pathlib import Path
import shutil
import os

download_folder_name = os.environ.get('DOWNLOAD_PATH', 'tmp/')
download_folder = Path(download_folder_name)
download_folder.mkdir(parents=True, exist_ok=True)

app = FastAPI()

class Payload(BaseModel):
    url: str = None

class Response(BaseModel):
    status: bool
    message: str = ""

@app.post("/download", response_model=Response)
def download(payload: Payload):
    message = ""
    youtube = YouTube(payload.url)

    best_audio_stream = youtube.streams.get_audio_only()
    if best_audio_stream:
        file_name = best_audio_stream.title
        file_path = best_audio_stream.download(
            output_path=str(download_folder),
            filename=file_name)
        # Change default format to mp3
        new_file_name = ''.join(file_path.split('.')[:-1]) + '.mp3'
        os.rename(file_path, new_file_name)
        return Response(status=True, message="Success")
    else:
        message = "Video has no audio"

    return Response(status=False, message=message)


@app.on_event("shutdown")
def shutdown():
    shutil.rmtree(download_folder)