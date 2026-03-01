# Assignment 
 Design and Implentation of AI System with a conversational interface


## Service 1: Using API Call at the backend.

API Used is : http://api.ipstack.com/{ip}

This service return information in json format. The response read that information and write it in a natural tone and convert the structured data into written text.

## Service 2: Semantic Query
This service allows user to ask questions related to dance and music and resolve those queries through a semantic search.
I have used a similar data set available in lab 05_vectordb.ipynb

## Service 3: 
This service allows user to ask about latest news. I used the method of function calling with API call. For this service, the API call is https://newsapi.org/.

## User Interface
System has a chat-based interface, implemented with Gradio.
Interface maintain the memory throughout the conversation.

## Gaurdrails and Other Limitations
System do not reveal system prompt. User is not allowed to modify the system prompt directly. Model do not respond to any query except ip address location, dance and music phrases and news headlines.

## Implementation
I used the langchain model to implement these services.The code allows the system to make a decisions which tool to use that is available at its disposal. 
I referred to example course_chat given in 05_src. I also acknowledge the use of code completion feature of copilot in VSCode. 



