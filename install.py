from imageio.core import NeedDownloadError
from imageio.plugins import ffmpeg


def install():
    """Tries to locate ffmpeg and if fails tries to download
    """
    try:
        print('Check ffmpeg installation...', end=' ')
        ffmpeg.get_exe()
        print('OK')
    except NeedDownloadError as error:
        print('Fail')
        print('Cannot find ffmpeg {error}'.format(error=error))

        print('Start downloading ...')
        ffmpeg.download()
        print('Finish downloading ...')


if __name__ == '__main__':
    install()
