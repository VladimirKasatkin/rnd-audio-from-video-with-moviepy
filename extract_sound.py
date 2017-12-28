import os
from os import path

from moviepy.editor import VideoFileClip

# put sources in this folder
VIDEO_FOLDER = 'video'

VIDEO_FILES = (
    'sample.avi',
    'sample.mov',
    'sample.mp4',
)

# audio files will be put this folder
AUDIO_FOLDER = 'audio'

AUDIO_EXTENSION = 'mp3'


if __name__ == '__main__':
    import os

    if not path.exists(VIDEO_FOLDER):
        os.mkdir(VIDEO_FOLDER)

    if not path.exists(AUDIO_FOLDER):
        os.mkdir(AUDIO_FOLDER)

    for video_file in VIDEO_FILES:
        # prepare file paths
        video_full_path = path.join(VIDEO_FOLDER, video_file)
        audio_file = '.'.join((video_file, AUDIO_EXTENSION))
        audio_full_path = path.join(AUDIO_FOLDER, audio_file)

        print('Process {}'.format(video_file))
        clip = VideoFileClip(video_full_path)
        clip.audio.write_audiofile(audio_full_path)
