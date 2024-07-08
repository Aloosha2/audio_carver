import sys
from audio_conversion import *
from seam_carving import carve_audio

def main(input_wavfile, n_of_seams):
    # Load the audio file
    audio, sampling_rate = load_wavfile(input_wavfile)
    matrix = get_stft(audio)
    magnitude, phase = extract_mag_pha(matrix)
    
    # Carve the audio
    magnitude, phase = carve_audio(n_of_seams, magnitude, phase)
    
    # Create the output filename
    output_filename = f'{input_wavfile.split(".")[0]}_carved{n_of_seams}.wav'
    
    # Save the carved audio to a new wav file
    sig_to_wav(output_filename, magnitude, phase)
    
    print(f"Processed {input_wavfile} and saved as {output_filename} with {n_of_seams} seams carved")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_wavfile> <n_of_seams>")
        sys.exit(1)
    
    input_wavfile = sys.argv[1]
    n_of_seams = int(sys.argv[2])
    
    main(input_wavfile, n_of_seams)
