import sys
from moviepy.editor import *


def extract():
    video = VideoFileClip(sys.argv[1])  # 2.
    audio = video.audio  # 3.
    audio.write_audiofile(sys.argv[2])  # 4.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    extract()
