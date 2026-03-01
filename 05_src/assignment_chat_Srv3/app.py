from assignment_chat_Srv3.main import get_graph
from langchain_core.messages import SystemMessage , HumanMessage
import gradio as gr
from dotenv import load_dotenv
import os   

llm = get_graph()

load_dotenv(".env")
load_dotenv(".secrets")

def assignment_chat(message : str, history : list[dict])->str:
    langchain_messages = []
    n = 0
    for msg in history:
        if msg["role"] == "user":
            langchain_messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            langchain_messages.append(SystemMessage(content=msg["content"]))
        n += 1
    langchain_messages.append(HumanMessage(content=message))

    state = {"messages": langchain_messages , "llm_calls": n}

    response = llm.invoke(state)
    return response["messages"][len(response["messages"]) - 1].content

chat = gr.ChatInterface(
    fn=assignment_chat,
    type="messages",
    title="Assignment Chat: Service: LatestNews",
)
if __name__ == "__main__":
    chat.launch()   