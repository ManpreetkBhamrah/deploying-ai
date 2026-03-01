import gradio as gr
from assignment_chat_Srv1.main import ipstack_chat

from dotenv import load_dotenv
from typing import Optional
import os



load_dotenv('.secrets')

chat = gr.ChatInterface(
    fn=ipstack_chat,    # need to be replaced
    type="messages",
    title="Assignment Chat: Service: Know your Location based on IP",
)


chat.launch()
