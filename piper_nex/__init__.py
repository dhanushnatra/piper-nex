from .unpacker import unpack_piper
unpack_piper()

from .speak_handler import speak, speak_raw
from .models_handler import models
__version__ = "0.1.0"
__author__ = "dhanushnatra"
__license__ = "MIT"
__description__ = "A Python package for text-to-speech using Piper for simple personal assistant projects."
__url__ = "https://github.com/dhanushnatra/piper-nex"
__all__ = ["speak", "speak_raw", "models"]