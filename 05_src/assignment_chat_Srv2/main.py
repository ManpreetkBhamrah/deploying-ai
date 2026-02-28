from dotenv import load_dotenv
from assignment_chat_Srv2.prompts import return_instructions_root       
import json
import requests
import os
from openai import OpenAI
import chromadb

open_ai_model = 'gpt-4o-mini'

load_dotenv(".env")
load_dotenv(".secrets")

client = OpenAI(base_url='https://k7uffyg03f.execute-api.us-east-1.amazonaws.com/prod/openai/v1', 
                api_key='any value',
                default_headers={"x-api-key": os.getenv('API_GATEWAY_KEY')})
tools = [ 
    {
     "type": "function",
     "name": "query_dance_music_info",
     "description": "Searches ChromaDB for the closest matching phrases.", 
     "strict": True,
    "parameters": { 
        "type": "object",      
         "properties":  { 
             "query": {
                "type": "string",
                "description": "User query about music or dance."
                  },
                },
                "required": ["query"],
                "additionalProperties": False }
    }
         ]
    #SAMPLE DATA FOR TESTING PURPOSES
phrases = [
    # Some sentences on Music (10)
    "There’s something about good music that reaches you before you even know you need it.",
    "A great song can stay with you long after it stops playing.",
    "Sometimes a single melody can lift the mood in an entire room.",
    "The right song can make an ordinary moment feel meaningful.",
    "A rhythm you connect with can change the way your whole day feels.",
    "Some songs feel familiar the very first time you hear them.",
    "A powerful track can turn a rough day around in minutes.",
    "Music with real energy can wake you up from the inside out.",
    "Certain lyrics say exactly what you’ve been trying to express.",    
    "A truly good song never loses its magic, no matter how often you play it.",
    # Some sentences on Dance(10)
    "There are moments when dance makes you forget everything except the movement.",
    "When someone dances naturally, it looks like the body already knows the story.",
    "A strong performance can make you feel the emotion without a single word.",
    "Dance has a way of filling a space with joy that feels genuine.",
    "Even simple steps can look beautiful when they’re done with heart.",
    "When the rhythm flows through you, every part of your body responds.",
    "Skilled dancers make even the hardest moves look effortless.",
    "A good routine can communicate more than a conversation ever could.",
    "When dance and music connect perfectly, it feels almost magical.",
    "A memorable performance leaves a warm feeling long after it ends"  
]

response = client.embeddings.create(
    input= phrases, 
    model="text-embedding-3-small"
)

chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="phrases_collection")
embeddings = [item.embedding for item in response.data]
ids = [f"id_{i}" for i in range(len(phrases))]
collection.add(embeddings = embeddings,
               ids =ids,            
                documents = phrases)


def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding

def query_chromadb(query, top_n = 2) -> dict:
    query_embedding = get_embedding(query)
    results = collection.query(query_embeddings=[query_embedding], n_results=top_n)
    
    output = []
    for doc, score in zip(results["documents"][0], results["distances"][0]):
        output.append({"text": doc, "score": score}) 

    return output

def query_dance_music_info(query: str) -> dict:
    return query_chromadb(query)
    
def sanitize_history(history: list[dict]) -> list[dict]:
    clean_history = []
    for msg in history:
        clean_history.append({
            "role": msg.get("role"),
            "content": msg.get("content")
        })
    return clean_history   

def music_chat(message: str, history: list[dict] = []) -> str:
    """
    Chat flow
    """
    instructions = return_instructions_root()
    
    user_msg = {
        "role": "user",
        "content": message
    }
    
    conversation_input = sanitize_history(history)+[user_msg]
    
    response = client.responses.create(
        model=open_ai_model,  
        instructions=instructions,
        input=conversation_input,
        tools=tools,
        
    )
    
    conversation_input += response.output

    # Handle function calls if any
    for item in response.output:
        if item.type == "function_call":
            if item.name == "query_dance_music_info":
                args = json.loads(item.arguments)
                chromadb_result = query_dance_music_info(**args)
                
            func_call_output = {
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": json.dumps({
                        "results": chromadb_result
                    })
                }
                
            conversation_input = conversation_input + [func_call_output]    
                
                
            response = client.responses.create(
                model=open_ai_model,  
                instructions=instructions,
                input=conversation_input,
                tools=tools,
        )
        break

    return response.output_text
