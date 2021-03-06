import os
import sys
import logging
import humanfriendly
import pytube
from tqdm import tqdm
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

    def download(self, video_url: str, file_extension: str, output_path: str = None):
        """
        Save videos as mp4 by Default.
        """
        if output_path is None:
            output_path = os.path.join(os.path.expanduser('~'), 'Downloads')

        try:
            video = pytube.YouTube(video_url, on_progress_callback=on_progress)
            stream = None

            if file_extension is None:
                video_type = video.streams.filter(progressive=True)
                stream = video_type.order_by('resolution').first()
                logger.info(f"\nGetting the video: {stream.title}")
                logger.info(
                    f"Size of the video: {humanfriendly.format_size(stream.filesize)}")
                logger.info(f"Saved at: {stream.download(output_path)}")
            elif file_extension == 'mp3':
                logger.info("Audio downloader\n")
                stream = video.streams.filter(only_audio=True)[0]
                logger.info(f"\nGetting the video: {stream.title}")
                logger.info(
                    f"Size of the video: {humanfriendly.format_size(stream.filesize)}")
                dl = stream.download(output_path)
                to_mp3 = os.path.join(output_path, f'{stream.title}.mp3')
                os.rename(dl, to_mp3)
                logger.info(f"Saved at: {to_mp3}")

        except pytube.exceptions.RegexMatchError:
            logger.error(f"\nURL is not valid: {self.video_url}")
            exit()

    def batch_download_mp3(self, video_list_path: str):

        video_list = open(video_list_path).readlines()

        for video in tqdm(video_list):
            self.download(video, 'mp3')


if __name__ == "__main__":
    # video_url = sys.argv[1]
    # try:
    #     file_extension = sys.argv[2]
    # except IndexError:
    #     file_extension = None

    # try:
    #     output_path = sys.argv[3]
    # except IndexError:
    #     output_path = None

    yt = DownloaderHandler()
    # yt.download(video_url, file_extension, output_path)
    videos_list_path = sys.argv[1]
    yt.batch_download_mp3(videos_list_path)


