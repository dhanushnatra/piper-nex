
from pathlib import Path


def os_type()-> str:
    """Get the operating system name."""
    import sys
    return sys.platform if sys.platform.startswith("linux") else "windows" if sys.platform.startswith("win") else "macos"
os_typ= os_type()
path=Path(__file__).parent / "piper.zip" if os_typ== "windows" else Path(__file__).parent / "piper.tar.gz"
def download_piper(os_type: str) -> None:
    import requests
    if os_type == "linux":
        url = f"https://github.com/rhasspy/piper/releases/download/2023.11.14-2/piper_linux_x86_64.tar.gz"
    elif os_type == "windows":
        url = f"https://github.com/rhasspy/piper/releases/download/2023.11.14-2/piper_windows_amd64.zip"
    else:
        url="https://github.com/rhasspy/piper/releases/download/2023.11.14-2/piper_macos_x64.tar.gz"
    
    response = requests.get(url, stream=True)
    total = int(response.headers.get('content-length', 0))
    downloaded = 0
    chunk_size = 8192
    from sys import stdout
    print("Downloading Piper...")
    with open(path, "wb") as file:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                file.write(chunk)
                downloaded += len(chunk)
                done = int(50 * downloaded / total) if total else 0
                stdout.write(f"\r[{'=' * done}{' ' * (50 - done)}] {downloaded // 1024}KB/{total // 1024 if total else '?'}KB")
                stdout.flush()
    print("\nDownload complete.")
    print("Unpacking Piper...")
    



def unpack_piper() -> None:
    import os
    if not os.path.exists(path.parent / "piper"):
        # piper directory does not exist, proceed to download and unpack
        if os_typ == "linux" or os_typ == "macos":
            download_piper("linux")
            import tarfile
            with tarfile.open(path, "r:gz") as tar:
                tar.extractall(path=path.parent)    
        elif os_typ == "windows":
            download_piper("windows")
            import zipfile
            with zipfile.ZipFile(path, "r") as zip_ref:
                zip_ref.extractall(path=path.parent)
        os.mkdir(path=path.parent / "piper/model")
        from .models_handler import download_model
        # Download the default model if it doesn't exist
        download_model()
        os.remove(path)
    else:
        print("Piper is already unpacked.")

if __name__ == "__main__":
    unpack_piper()
    print("Piper unpacked successfully.")