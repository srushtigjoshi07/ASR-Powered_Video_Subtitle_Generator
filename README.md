# 🎙️ ASR-Powered Video Subtitle Generator

An end-to-end Automatic Speech Recognition (ASR) system that automatically generates subtitles from videos and embeds them back into the video.

This project extracts audio from a video, transcribes speech using Facebook's Wav2Vec2 model, generates timestamped subtitles in SRT format, and burns the subtitles directly onto the video using OpenCV and MoviePy.

---

## 🚀 Features

- 🎥 Extract audio from video files
- 🗣️ Convert speech to text using Wav2Vec2
- ⏱️ Generate timestamped subtitles automatically
- 📝 Create standard `.srt` subtitle files
- 🎬 Burn subtitles directly into video frames
- 📹 Produce a final captioned video
- 🔄 Supports long videos through audio chunking

---

## 🛠️ Tech Stack

- Python
- PyTorch
- Hugging Face Transformers
- Facebook Wav2Vec2 Base 960H
- Librosa
- MoviePy
- OpenCV
- NumPy

---

## 📂 Project Structure

```text
├── extract_audio.py          # Extracts audio from video
├── audio_model1_fb_base.py   # Basic transcription using Wav2Vec2
├── audio_transcribe.py       # Subtitle generation pipeline
├── video.mp4                 # Input video
├── audio.mp3                 # Extracted audio
├── subtitles.srt             # Generated subtitles
└── output_with_subs.mp4      # Final subtitled video
```

---

## ⚙️ Workflow

```text
Input Video
      │
      ▼
Audio Extraction
      │
      ▼
Speech-to-Text Transcription
      │
      ▼
Subtitle (.srt) Generation
      │
      ▼
Subtitle Overlay
      │
      ▼
Final Captioned Video
```

---

## 🧠 Model Used

### Facebook Wav2Vec2 Base 960H

A pretrained Automatic Speech Recognition (ASR) model developed by Meta AI.

```python
facebook/wav2vec2-base-960h
```

The model converts raw speech waveforms directly into text and is trained on 960 hours of English speech data.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/asr-powered-video-subtitle-generator.git
cd asr-powered-video-subtitle-generator
```

Install dependencies:

```bash
pip install torch transformers librosa moviepy opencv-python numpy
```

---

## ▶️ Usage

### Step 1: Extract Audio from Video

```bash
python extract_audio.py
```

### Step 2: Generate Transcription and Subtitles

```bash
python audio_transcribe.py
```

Output:

```text
subtitles.srt
```

### Step 3: Burn Subtitles into Video

```bash
python extract_audio.py
```

Output:

```text
output_with_subs.mp4
```

---

## 📊 Applications

- Video Captioning
- Lecture Transcription
- Accessibility Enhancement
- Educational Content Creation
- Meeting and Webinar Summaries
- Automatic Subtitle Generation

---

## 🔮 Future Improvements

- Real-time transcription
- Whisper / WhisperX integration
- Multilingual subtitle generation
- Speaker diarization
- Automatic subtitle translation
- Improved timestamp alignment
- Web-based user interface

---

## 📸 Sample Output

The system automatically converts spoken content from a video into synchronized subtitles and produces a final captioned video.

**Input:** Video with speech  
**Output:** Video with generated subtitles

---

## 👨‍💻 Author

**Srushti G Joshi**  

---

⭐ If you found this project useful, consider giving the repository a star.
