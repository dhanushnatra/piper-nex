from os import listdir
from pathlib import Path

def get_models_path() -> str:
    
    """Get the path to the models directory."""
    
    return Path(__file__).parent / "piper/model"

models_path:Path  = get_models_path()


def available_models() -> list:
    """Get a list of available models in the models directory."""
    return [d[:-5] for d in listdir(models_path) if d.endswith(".onnx") and not d.startswith(".")]


models: list = available_models()


def download_model(typ:str="male")->None:
    """Download a model based on the type specified in voices.json.
    Args:
        typ (str): [ male or female ]"""
    from requests import get
    import json
    import sys
    
    
    #load voices.json
    with open("voices.json","r")as f:
        voices = json.load(f)

    # getting model 
    model_info = voices.get(typ)
    if not model_info:
        raise ValueError(f"Type '{typ}' not found in voices.json")
    # Extracting model information
    model_name = model_info["filename"]
    onnx_url = model_info["onnx_url"]
    json_url = model_info["json_url"]
    
    
    # Check if the model already exists
    if model_name in models:
        print(f"{model_name} already exists in {models_path}. Skipping download.")
        return
    # Download the model and its config file
    sys.stdout.write(f"Downloading {model_name}...\n")
    def download_with_progress(url, dest_path):
        response = get(url, stream=True)
        total = int(response.headers.get('content-length', 0))
        with open(dest_path, "wb") as f:
            downloaded = 0
            for data in response.iter_content(chunk_size=8192):
                f.write(data)
                downloaded += len(data)
                percent = int(downloaded * 100 / total) if total else 0
                sys.stdout.write(f"\rDownloading {dest_path.name}: {percent}%")
                sys.stdout.flush()
        sys.stdout.write("\n")
    sys.stdout.write(f"Downloading {model_name} and its config file...\n")
    sys.stdout.flush()
    models_path.mkdir(parents=True, exist_ok=True)
    download_with_progress(onnx_url, models_path / (model_name + ".onnx"))
    download_with_progress(json_url, models_path / (model_name + ".onnx.json"))
    print(f"Downloaded {model_name} and its config file to {models_path}")