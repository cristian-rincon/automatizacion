import os
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
    """
    docstring
    """

    def __init__(self):
        self.output_path = os.path.join(os.path.expanduser('~'), 'Downloads')

    def download(self, video_url, file_extension):
        """
        Save videos as mp4 by Default.
        """
        try:
            video = pytube.YouTube(video_url, on_progress_callback=on_progress)
            stream = None
            if file_extension is None:
                video_type = video.streams.filter(progressive=True)
                stream = video_type.order_by('resolution').first()
                logger.info(f"\nGetting the video: {stream.title}")
                logger.info(
                    f"Saved at: {stream.download(self.output_path, f'{stream.title}.mp4')}")
            elif file_extension == 'mp3':
                logger.info("Audio downloader\n")
                stream = video.streams.filter(
                    only_audio=True)[0]
                logger.info(f"\nGetting the video: {stream.title}")
                dl = stream.download(self.output_path)
                to_mp3 = os.path.join(
                    self.output_path, f'{stream.title}.mp3')
                dl_rename = os.rename(dl, to_mp3)
                logger.info(
                    f"Saved at: {to_mp3}")

            logger.info(
                f"Size of the video: {humanfriendly.format_size(stream.filesize)}")

        except pytube.exceptions.RegexMatchError:
            logger.error(f"\nURL is not valid: {self.video_url}")
            exit()


if __name__ == "__main__":
    video_url = sys.argv[1]
    try:
        file_extension = sys.argv[2]
    except IndexError:
        file_extension = None

    yt = DownloaderHandler()
    yt.download(video_url, file_extension)
