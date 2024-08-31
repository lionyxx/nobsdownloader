import subprocess
import sys
import os
from pathlib import Path

def install_dependencies():
    """Install the required dependencies."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    process = subprocess.Popen(
        [sys.executable, "-m", "pip", "install", "yt-dlp"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    stdout, stderr = process.communicate()

    # Filter out "Requirement already satisfied" messages
    filtered_stdout = '\n'.join([line for line in stdout.decode().split('\n') if 'Requirement already satisfied' not in line])

    if filtered_stdout:
        print(filtered_stdout)
    if stderr:
        print(stderr.decode(), file=sys.stderr)

def download_video(url, output_path):
    """Download a single YouTube video."""
    try:
        command = [
            'yt-dlp',
            '-f', 'bestvideo[height<=1080]+bestaudio/best',
            '-o', f'{output_path}/%(title)s.%(ext)s',
            url
        ]
        subprocess.run(command, check=True)
        print(f"Downloaded: {url}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to download video: {url}. Error: {str(e)}")

def download_playlist(playlist_url, output_path):
    """Download all videos from a YouTube playlist."""
    try:
        command = [
            'yt-dlp',
            '-f', 'bestvideo[height<=1080]+bestaudio/best',
            '-o', f'{output_path}/%(playlist)s/%(title)s.%(ext)s',
            playlist_url
        ]
        subprocess.run(command, check=True)
        print(f"Downloaded playlist: {playlist_url}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to download playlist: {playlist_url}. Error: {str(e)}")

def main():
    install_dependencies()

    if len(sys.argv) < 2:
        print("Usage: nobsdownloader <url> [--playlist]")
        sys.exit(1)

    url = sys.argv[1]
    is_playlist = '--playlist' in sys.argv

    videos_path = Path.home() / "Videos" / "nobsdownloader"
    if not videos_path.exists():
        os.makedirs(videos_path)

    if is_playlist:
        download_playlist(url, str(videos_path))
    else:
        download_video(url, str(videos_path))

if __name__ == "__main__":
    main()
