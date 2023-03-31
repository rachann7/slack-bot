import slack
import os 
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env' #current directory 
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN']) #part of the slack api 

client.chat_postMessage(channel='#general', text="you are what you don't poop")