# Voice-Based-Control-System and Assistant
This software application is a digital life monitor, administrator and assistant that is much more than just a digital virtual assistant. As a personal assistant, it assists the end-user with day-to-day activities like general human conversation, searching queries in web-browser, searching for videos, images, live weather conditions, word meanings, searching for medicine details, health recommendations based on symptoms and set reminder and also reminding the user about the scheduled events and tasks. 

It has been designed to provide a user-friendly interface for carrying out a variety of tasks by employing certain well-defined commands. Users can interact with the assistant through voice commands and certain functionalities can also be accessed using mouse\keyboard input.

It can perform all basic tasks on a desktop machine such as: launch applications, play/switch music or videos, set and play reminder, tell date and time, take screenshot, send email, etc. Complex tasks that it can execute include: using system camera (if available) to capture image, record video, perform image face-detection, perform real-time face detection, and execute interactive games to play.
            
            Code Structure
            
            1.	An application invokes the pyttsx3.init() factory function to get a reference to a pyttsx3.egineinstance through this assistant is able to speak after that title() function is called which shows basic text on screen like the assistant name and version.
2.	Then greeting() function is called in which datetime module is used. According to it assistant greets user Good Morning, Afternoon or Evening.
3.	Then takeInput() function is called in which speech recognition module is used which uses different function like recognizer(), microphone() and listen() to take audio input from user and store it to an audio variable and then recognize_google() function converts the audio in English format and saves it in query variable.
4.	Then query is matched with the available commands which triggers the respective functions with different python modules according to that assistant will respond.

