# youtube-downloader-core
Python service to download videos in different formats from YouTube

**CURRENTLY ONLY AUDIO SUPPORTED**

## Setup

* Install [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

* Create environment:

    `conda create -n youtube_downloader python=3.9.2`

* Activate environment:

    `conda activate youtube_downloader`

* Install requirements:

    `pip install -r requirements.txt`

* Install package:
    `pip install -e .`

## Usage

* Run service:

    `sh run.sh`

* Go to FastAPI docs URL:

    `http://localhost:5001/docs`

* Click on `/download` and on `Try it out`
* Copy YouTube url you want to download to the `url` field
* Click on `execute`
* Audio will be downloaded to your local folder repository in `/tmp`