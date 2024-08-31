import subprocess
import sys
import os
from pathlib import Path

def install_dependencies():
    """Install the required dependencies."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])

def add_to_path():
    """Add the script directory to the user's PATH on Windows."""
    script_dir = Path.home() / "AppData" / "Local" / "Packages" / "PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0" / "LocalCache" / "local-packages" / "Python312" / "Scripts"
    
    if script_dir.exists():
        path_var = os.environ.get('PATH', '')
        if str(script_dir) not in path_var:
            try:
                subprocess.run(f'setx PATH "%PATH%;{script_dir}"', shell=True, check=True)
                print(f"Added {script_dir} to PATH.")
            except subprocess.CalledProcessError as e:
                print(f"Failed to add to PATH: {e}")
        else:
            print(f"{script_dir} is already in PATH.")
    else:
        print(f"Script directory {script_dir} does not exist.")

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
    add_to_path()

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
