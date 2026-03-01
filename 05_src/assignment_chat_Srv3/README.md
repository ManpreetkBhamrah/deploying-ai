# Assignment 2 Service 3
Service 3 for Design and Implentation of AI System with a conversational interface

## Service 3: 
This service allows user to ask about latest news. I used the method of function calling with API call. For this service, the API call is https://newsapi.org/.

## User Interface
System has a chat-based interface, implemented with Gradio.
Interface maintain the memory throughout the conversation.

## Gaurdrails and Other Limitations
System do not reveal system prompt. User is not allowed to modify the system prompt directly. Model do not respond to any query except regarding the music and dance general opinion.

## Implementation
I used the langchain model to implement this service. The code allows the system to make a decision when to use the API to respond to user query related to news.

