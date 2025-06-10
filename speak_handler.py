from os import system
from pathlib import Path
from models_handler import models_path, models, download_model


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
        system(f"echo '{text}' | ./piper/piper --model {models_path / model}.onnx --config {models_path / model}.onnx.json --output_file {output_file}")
        return output_file.resolve()
    except Exception as e:
        print(f"Error occurred while generating speech: {e}")
        return None

def speak_raw(model: str = "male" , text: str = "") -> bytes:
    """Generate speech from text and return the output as a string.

    Args:
        model (str): [ male or female ] The name of the model to use.
        text (str): The text to convert to speech.
    Returns:
        bytes: The raw audio data as a string.
    """
    
    if model not in models:
        print(f"Model '{model}' not found. Available models: {models} \n Downloading {model} model...")
        download_model(model)
    
    try:
        return bytes(system(f"echo '{text}' | ./piper/piper --model {models_path / model}.onnx --config {models_path / model}.onnx.json --output-raw"))
    
    except Exception as e:
        print(f"Error occurred while generating speech: {e}")
        return None

