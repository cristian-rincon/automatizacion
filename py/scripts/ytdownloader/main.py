import os
import re
import sys
import logging

import humanfriendly

import pytube
from pytube.cli import on_progress

# '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

class DownloaderHandler():
    
    def __init__(self):
        pass

    def greeting(self):
        """
        docstring
        """
        pass

def deEmojify(text):
    regrex_pattern = re.compile(pattern="["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                "]+", flags=re.UNICODE)
    return regrex_pattern.sub(r'', text)


def downloader(video_url: str):
    """
    Simple tool to download youtube videos.
    """
    try:
        video = pytube.YouTube(video_url, on_progress_callback=on_progress)
        video_type = video.streams.filter(progressive=True)
        stream = video_type.order_by('resolution').first()
        logger.info(f"\nGetting the video: {stream.title}")
        logger.info(
            f"Size of the video: {humanfriendly.format_size(stream.filesize)}")
        logger.info(
            f"Video saved at: {stream.download(os.path.join(os.path.expanduser('~'), 'Downloads'))}")

    except pytube.exceptions.RegexMatchError:
        logger.error(f"\nLa URL especificada no es válida: {video_url}")
        exit()


if __name__ == "__main__":
    video_url = sys.argv[1]
    downloader(video_url)
