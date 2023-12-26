import re 
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url) -> str:
   """ Extracts the video ID from the YouTube URL. """
   # Regular expression for extracting the video ID from a YouTube URL
   regex = r"(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/" \
      r"|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"

   match = re.search(regex, url)
   if not match:
      raise ValueError("Invalid YouTube URL")
   return match.group(1)

def get_video_length(last_transcript:dict) -> str:
   """ Returns the length of video in seconds"""
   in_sec = int(last_transcript['start']) + int(last_transcript['duration'])
   in_min = in_sec//60
   return in_min 


def get_transcript_string(video_id:str) -> tuple:
   """ Fetches the transcript of the YouTube video using the video ID . """
   try:
      transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
      last_transcipt = transcript_list[-1]
      duration = get_video_length(last_transcipt)
      # Joining the text of the transcript parts and duration 
      return (' '.join([t['text'] for t in transcript_list]), duration)
   except Exception as e:
      return str(e)
   


# url = "https://www.youtube.com/watch?v=Y8Tko2YC5hA"
# video_id = extract_video_id(url)
# content , duration = get_transcript_string(video_id)
# print(content)
# print(duration)