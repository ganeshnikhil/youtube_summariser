# youtube_summariser


### Project Title

YouTube Video Summarizer

### Description
This Python script allows you to extract the transcript of a YouTube video, generate a summary using the Hugging Face model facebook/bart-large-cnn trained on the CNN/Daily Mail dataset, and provide both a text and audio summary of the video.

### Project Structure

- `src/` directory contains the main source code
  - `youtube_handler.py` - Handles YouTube video extraction and transcript retrieval
  - `ml_model.py` - Implements the machine learning model for summarization
  - `file_handler.py` - Manages file-related operations
  - `main.py` - The main executable script
- `summary_text/` - Directory to store text summaries
- `summary_voice/` - Directory to store audio summaries

### Usage

1. Install the required modules using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the script:

    ```bash
    python main.py
    ```

    Follow the on-screen instructions to input the YouTube video URL.

### Configuration

- `main.py` - Main script to run the YouTube video summarizer.
- `requirements.txt` - List of required Python modules.

### Video Explanation

[Watch the Video Explanation](https://www.youtube.com/watch?v=j5OdWBJeKLU)

This video provides a detailed explanation of how to use and understand the YouTube Video Summarizer project.

### Cool Stickers

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![YouTube API](https://img.shields.io/badge/Youtube%20API-v3-red)](https://developers.google.com/youtube/v3)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
