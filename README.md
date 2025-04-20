# Video Transcriber

A simple yet powerful tool for transcribing video and audio files using OpenAI's Whisper model.

## Overview

Video Transcriber is an open-source tool designed to make transcription accessible and efficient. It leverages OpenAI's Whisper, a state-of-the-art speech recognition model, to provide accurate transcriptions of video and audio content in multiple languages.

## Features

- **Multiple File Format Support**: Process common video and audio formats (MP4, MP3, WAV, etc.)
- **Batch Processing**: Transcribe multiple files at once
- **Language Detection**: Automatically detects the language in your media files
- **User-friendly Interface**: Simple command-line interface for easy use
- **Export Options**: Save transcriptions in multiple formats (TXT, SRT, VTT)
- **Progress Tracking**: Monitor transcription progress in real-time

## Installation

### Prerequisites

- Python 3.8 or higher
- FFmpeg (for audio extraction from video files)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Co-vengers/video_transcriber.git
   cd video_transcriber
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Command

```bash
python transcriber.py --input path/to/video.mp4 --output path/to/output.txt
```

### Options

- `--input`, `-i`: Path to input file or directory (for batch processing)
- `--output`, `-o`: Path to output file or directory
- `--format`, `-f`: Output format (txt, srt, vtt). Default: txt
- `--model`, `-m`: Whisper model size (tiny, base, small, medium, large). Default: base
- `--language`, `-l`: Language code (auto for automatic detection). Default: auto
- `--verbose`, `-v`: Enable verbose output
- `--device`, `-d`: Device to use (cpu, cuda). Default: cpu if no GPU available

### Examples

**Transcribe a single file:**
```bash
python transcriber.py -i videos/lecture.mp4 -o transcripts/lecture.txt
```

**Batch processing:**
```bash
python transcriber.py -i videos/ -o transcripts/ -f srt
```

**Specify language and model:**
```bash
python transcriber.py -i audio.mp3 -o transcript.txt -l en -m medium
```

## Performance Tips

- Using a GPU significantly improves transcription speed
- Larger models (medium, large) provide better accuracy but require more resources
- For long content, consider splitting files for more efficient processing

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) for the speech recognition model
- All contributors who have helped build and improve this tool

## Contact

Co-vengers Team - [GitHub](https://github.com/Co-vengers)

Project Link: [https://github.com/Co-vengers/video_transcriber](https://github.com/Co-vengers/video_transcriber)
