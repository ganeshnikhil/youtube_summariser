from transformers import pipeline
from playsound import playsound 
from gtts import gTTS 
from psutil import cpu_percent


# check cpu usage 
def cpu_use() -> int:
   """" return cpu use data"""
   cpu_usage = cpu_percent(interval=1)
   return int(cpu_usage)



def split_text(text:str)->list[str]:
   """ split text into chunks """
   # maximum size of each chunk split 
   #max_chunk_size = 1024
   max_chunk_size = 4000
   chunks = []
   current_chunk = ""
   #split the string using . delimeter 
   for sentence in text.split("."):
      # if stored sentence and new sentence length is less then max_chun size
      if len(current_chunk) + len(sentence) < max_chunk_size:
            current_chunk += f"{sentence}."
      else:
            # append the current_chunk
            chunks.append(current_chunk.strip())
            # reintialize the current_chunk to sentence.
            current_chunk = f"{sentence}."
            
   # if any of strings chunks left then append 
   if current_chunk:
      chunks.append(current_chunk.strip())
   # return the stored string chunks
   return chunks

def load_summarizer_model(aim: str, model: str):
   """Load the summarization model."""
   return pipeline(aim, model)

def process_chunk(summarizer, chunk: str):
   """Process a chunk using the summarization model."""
   response = summarizer(chunk, do_sample=False)
   return response[0]['summary_text']

# we are usind a simple llm model to do this  
def generate_summary(text:str, aim="summarization", model="facebook/bart-large-cnn")->str:
   """ summarize the large text input"""
   # split the large text in chunks 
   input_chunks=split_text(text)
   output_chunks=[]
   
   # if len input_chunks is > 30 means it will so hard fo cpu to process it so exit
   if len(input_chunks) > 30:
      raise ValueError("Input Limit Excedded")
   # call the llm model using pipeline
   summarizer = load_summarizer_model(aim , model)
   #summarizer = pipeline(aim,model)
   # loop through each chunk the pass it to llm mode it will return sumarize 
   # form of input text
   for i , chunk in enumerate(input_chunks):
      
      print(f"{i+1} chunk processing...")
      summary = process_chunk(summarizer , chunk)
      #response = summarizer(chunk,do_sample=False)
      #summary=response[0]['summary_text']
      output_chunks.append(summary.strip())
      # check cpu uses if cpu use is greater then 95 means it so power consuming
      # for cpu to do these llm tasks 
      cpu_limit = cpu_use()
      # if > 95 quit the program and return whatever text we have 
      if cpu_limit > 95:
         print("Cpu is exceded it's limit")
         break
   # if every thing goes find give full sumarray text 
   return "".join(output_chunks)

def text_to_speech(summary:str,filepath) -> None:
   """ text to speech using gtts"""
   myobj = gTTS(text=summary, lang='en', slow=False)
   myobj.save(filepath)
   playsound(filepath)
   #os.system(f"afplay {filename}")
   return None 

def play_sound(path:str) -> None:
   """ play sound file"""
   playsound(path)
   return None
