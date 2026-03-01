from langgraph.graph import StateGraph, START, END,MessagesState
from langchain.chat_models import init_chat_model
from langgraph.prebuilt.tool_node import ToolNode, tools_condition
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import json
import requests
import os
from langchain.tools import tool

from assignment_chat.prompts import return_instructions
from assignment_chat.tools_news import get_latest_news
from assignment_chat.tools_iplocation import ipstack_chat
from assignment_chat.tools_music_dance import music_chat    

open_ai_model = 'gpt-4o-mini'

load_dotenv(".env")
load_dotenv(".secrets")

model = init_chat_model(
    f"openai:{open_ai_model}",
    temperature=0.7,
    base_url='https://k7uffyg03f.execute-api.us-east-1.amazonaws.com/prod/openai/v1',
    api_key='any value',
    default_headers={"x-api-key": os.getenv('API_GATEWAY_KEY')} 
)
# define tools available to the model
tools = [get_latest_news, ipstack_chat, music_chat]

# getting the instructions for the model from prompts.py
instructions = return_instructions()

def call_model(state: MessagesState):
    """LLM decides whether to call a tool or not"""
    messages = [SystemMessage(content=instructions)] + state["messages"]
    response = model.bind_tools(tools).invoke(messages)
    return {
        "messages": [response] 
    }

def get_graph():

    builder = StateGraph(MessagesState)
    builder.add_node(call_model)
    builder.add_node(ToolNode(tools))
    builder.add_edge(START, "call_model")
    builder.add_conditional_edges("call_model", tools_condition)
    builder.add_edge("tools", "call_model")
    graph = builder.compile()
    return graph
