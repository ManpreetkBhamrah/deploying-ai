# Assignment 2 Service 2
Service 2 for Design and Implentation of AI System with a conversational interface

## Service 2: Semantic Query
This service allows user to ask questions related to dance and music and resolve those queries through a semantic search.
I have used a similar data set available in lab 05_vectordb.ipynb

## User Interface
System has a chat-based interface, implemented with Gradio.
Interface maintain the memory throughout the conversation.

Sample Query: Tell some information about dance
![Sample-Output]("C:\Users\erman\Pictures\Screenshots\Screenshot 2026-03-01 101054.png")

## Gaurdrails and Other Limitations
System do not reveal system prompt. User is not allowed to modify the system prompt directly. Model do not respond to any query except regarding the music and dance general opinion.

## Implementation
I used the chromaDb to save embeddings and do the semantic query , this module is stand-alone coversational interface for this service.
