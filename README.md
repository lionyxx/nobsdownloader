# nobsdownloader

**nobsdownloader** is a simple and efficient command-line tool for downloading YouTube videos and playlists in high resolution directly to your Videos folder. It automatically installs all required dependencies, making it easy to use for everyone.

## Features

- **Automatic Installation**: Installs all required dependencies on first use.
- **High-Resolution Downloads**: Downloads videos in 1080p whenever available.
- **Playlist Support**: Easily download entire YouTube playlists with a single command.
- **User-Friendly**: Automatically saves downloaded videos to your `Videos/nobsdownloader` folder.

## Installation

To install `nobsdownloader`, run the following command:

```sh
pip install git+https://github.com/lionyxx/nobsdownloader.git
```
Usage
Once installed, you can use nobsdownloader to download videos or playlists by simply typing the following commands:

Download a Single Video
```sh
nobsdownloader <YouTube_Video_URL>
```
Download an Entire Playlist
```sh
nobsdownloader <YouTube_Playlist_URL> --playlist
```

How It Works
Download Location: By default, all videos are saved to C:\Users\<YourUsername>\Videos\nobsdownloader on Windows.
Format: Downloads are saved in the best available format, with 1080p video quality if available.
