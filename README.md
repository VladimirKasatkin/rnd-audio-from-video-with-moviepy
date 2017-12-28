# Example of extracting sound from video files

## Getting video files

Put video files into ``video`` folder in root of the project.
Or you can simply run ``download_samples.sh``.

## Installation

You need to install libraries from ``requirements.txt``.

```bash
pip3 install -r requirements.txt
```


iPython is used only for beautifying of shell.

Then run 
```bash
python3 install.py
```

You can work in docker. Just run:

```bash
docker-compose build
```

## Running example

Example is placed in ``extract_sound.py`` file.

Simply run 
```bash
python3 extract_sound.py
```
