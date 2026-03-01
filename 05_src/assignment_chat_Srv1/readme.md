# Assignment 2 Service 1
Service 1 for Design and Implentation of AI System with a conversational interface

## Service 1: Using API Call at the backend.

API Used is : http://api.ipstack.com/{ip}

This service return information in json format. The response read that information and write it in a natural tone and convert the structured data into written text.

## User Interface
System has a chat-based interface, implemented with Gradio.
Interface maintain the memory throughout the conversation.

## Gaurdrails and Other Limitations
System do not reveal system prompt. User is not allowed to modify the system prompt directly. Model do not respond to any query except regarding the location based on IP

## Implementation
I used the public API IP-Stack, this module is stand-alone coversational interface for this service.
