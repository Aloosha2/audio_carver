# AudioCarver
Seam Carving as a Data Augmentation Technique 

# Audio Processing Library

A Python library for performing seam carving on audio files, converting audio to matrix and back, and generating spectrograms.

![Build Status](https://img.shields.io/github/workflow/status/Aloosha2/audio_carver/CI)
![License](https://img.shields.io/github/license/Aloosha2/audio_carver)
![PyPI version](https://img.shields.io/pypi/v/audio_processing)

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Examples](#examples)
- [Documentation](#documentation)
- [License](#license)
- [Contact](#contact)

## Installation

You can install the library using pip:

```sh
pip install audio_carver
```

## Usage

Example in a python file:

```python 
from audio_carver import carve_audio, sig_to_wav

# Carving in time domain and writing to output
magnitude, phase = carve_audio(number_of_seams, magnitude, phase, is_vertical=True) # default true
sig_to_wav('output.wav', magnitude, phase)
```


Example in terminal:

```sh
$ python main.py <input_file.wav> <number_of_seams> <--carve_time> # remove to carve in frequency
```


## Features

Current supported audio formats: .wav

Audio processing capabilities: spectral analysis, time-domain operations, signal modification

Input requirements: None

Output: Mono with sampling rate specified by the original input file's sampling rate

*

## Examples

How to load an audio file:

```python 
from audio_carver import *

audio, sampling_rate = load_wavfile('filename.wav')
```

Find the minimum seam:

```python 
from audio_carver import *

minimum_energy_seam = min_vertical_seam_energy(magnitude)
```

## Documentation

Link to documentation.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Please contact alicjam@uw.edu for questions, suggestions, etc. Thank You!
