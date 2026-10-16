# SongSpeak 🎙️🎵

**Learn English through music-inspired conversations with AI.**

SongSpeak is a voice-based English tutor built with Sarvam AI. It helps learners practice vocabulary, grammar, idioms, and natural expressions through interactive conversations inspired by songs and storytelling.

## Features

- 🎤 Speak to the tutor using your microphone.
- 📝 Transcribe spoken questions with Sarvam Saaras v4.
- 🤖 Get conversational English lessons using Sarvam-105B.
- 🔊 Listen to spoken responses using Sarvam Bulbul v3.
- 📚 Practice vocabulary, grammar, idioms, and everyday expressions.
- 🎵 Explore music-inspired language lessons with original examples.

## Tech Stack

- Python
- Streamlit
- Sarvam AI: Sarvam-105B, Saaras v4, Bulbul v3

## Setup

1. Clone this repository.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory and add your Sarvam API key:

   ```env
   SARVAM_API_KEY=your_api_key_here
   ```

4. Run the app:

   ```bash
   python -m streamlit run app.py
   ```

5. Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## Project Goal

Make English learning more engaging and accessible through voice-based AI tutoring and music-inspired practice.

## Responsible Use

SongSpeak teaches language through explanations and original examples rather than reproducing copyrighted song lyrics.
