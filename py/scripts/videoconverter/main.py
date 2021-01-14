import os
import sys
import ffmpeg
from tqdm import tqdm


def convert_to_mp4(input_file: str) -> None:
    
    """ Convert video to mp4.
    :type input_file: str
    :param input_file: path of the video you want to convert into mp4.
    """
    filename = os.path.splitext(os.path.basename(input_file))[0]
    converted_filename = f'{filename}.mp4'
    tqdm(ffmpeg.input(input_file).output(converted_filename).run())
    print(
        f'File {input_file} converted succesfully.\nSaved as: {converted_filename}')


if __name__ == "__main__":

    input_file = sys.argv[1]
    convert_to_mp4(input_file)
