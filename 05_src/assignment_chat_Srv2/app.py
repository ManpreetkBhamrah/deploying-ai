import gradio as gr
from assignment_chat_Srv2.main import music_chat
from dotenv import load_dotenv
from typing import Optional         
import os
load_dotenv('.secrets')

chat = gr.ChatInterface(
    fn=music_chat,    
    type="messages",
    title="Assignment Chat: Service: Thoughts for Music and Dance",
)
chat.launch()
