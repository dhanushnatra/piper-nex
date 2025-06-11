from pathlib import Path
from .models_handler import models_path, models, download_model
from .unpacker import os_typ, path
import subprocess

def speak(model: str = "male", text: str = "", output_file: Path = Path("output.wav")) -> Path:
    """Generate speech from text using the specified model.
    
    Args:
        model (str): The name of the model to use.
        text (str): The text to convert to speech.
        output_file (Path, optional): The file to save the output audio. Defaults to "output.wav".
    """
    if model not in models:
        print(f"Model '{model}' not found. Available models: {models} \n Downloading {model} model...")
        download_model(model)
    try:
        piper_exec = path.parent / ('piper/piper' if os_typ != 'windows' else 'piper/piper.exe')
        cmd = [
            str(piper_exec),
            "--model", str(models_path / f"{model}.onnx"),
            "--config", str(models_path / f"{model}.onnx.json"),
            "--output_file", str(output_file)
        ]
        subprocess.run(['echo', text], stdout=subprocess.PIPE, check=True)
        subprocess.run(f"echo '{text}' | {' '.join(cmd)}", shell=True, check=True)
        return output_file.resolve()
    except Exception as e:
        print(f"Error occurred while generating speech: {e}")
        return None

def speak_raw(model: str = "male", text: str = "") -> bytes:
    """Generate speech from text and return the output as raw audio bytes.

    Args:
        model (str): [ male or female ] The name of the model to use.
        text (str): The text to convert to speech.
    Returns:
        bytes: The raw audio data.
    """
    if model not in models:
        print(f"Model '{model}' not found. Available models: {models} \n Downloading {model} model...")
        download_model(model)
    try:
        piper_exec = path.parent / ('piper/piper' if os_typ != 'windows' else 'piper/piper.exe')
        cmd = [
            str(piper_exec),
            "--model", str(models_path / f"{model}.onnx"),
            "--config", str(models_path / f"{model}.onnx.json"),
            "--output-raw"
        ]
        proc = subprocess.Popen(
            ['echo', text],
            stdout=subprocess.PIPE
        )
        output = subprocess.check_output(' '.join(cmd), stdin=proc.stdout, shell=True)
        proc.stdout.close()
        return output
    except Exception as e:
        print(f"Error occurred while generating speech: {e}")
        return None

