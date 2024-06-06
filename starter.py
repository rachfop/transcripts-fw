import os

from faster_whisper import WhisperModel
from pydub import AudioSegment
from tqdm import tqdm

# Define the model size (can be 'tiny', 'tiny.en', 'base', 'base.en', 'small', 'small.en', 'medium', 'medium.en', 'large-v1', 'large-v2')
model_size = "tiny"

# name of the file without the extension
file = "james-errors"

# Run on GPU with FP16
# model = WhisperModel(model_size, device="cuda", compute_type="float16")

# Run on CPU with INT8
model = WhisperModel(model_size, device="cpu", compute_type="int8")

# Extract audio from the video file
video_file = f"{file}.mp4"
audio_file = f"{file}.wav"

if not os.path.exists(audio_file):
    audio = AudioSegment.from_file(video_file)
    audio.export(audio_file, format="wav")

# Transcribe the audio from the audio file
segments, info = model.transcribe(audio_file, beam_size=5, word_timestamps=True)

# Print the detected language and its probability
print(
    "Detected language '%s' with probability %f"
    % (info.language, info.language_probability)
)

# Prepare to save the transcription to a Markdown file
output_lines = []
output_lines.append("# Faster Whisper transcription\n")
output_lines.append(f"## Transcription of {file}\n")
output_lines.append(
    f"Detected language: {info.language} with probability {info.language_probability:.2f}\n"
)
output_lines.append("\n## Transcription:\n")

# Print the transcription segments with a progress bar and save to the list
for segment in tqdm(segments, desc="Transcribing segments"):
    if segment.words is not None:
        for word in segment.words:
            line = f"[{word.start:.2f}s -> {word.end:.2f}s] {word.word}"
            print(line)
            output_lines.append(line)
    else:
        line = f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}"
        print(line)
        output_lines.append(line)

# Save the transcription to a Markdown file
output_file = "transcription.md"
with open(output_file, "w") as f:
    f.write("\n".join(output_lines))

print(f"\nTranscription saved to {output_file}")
