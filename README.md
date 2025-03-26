# **Home.LLC AI Voice Bot**  

## **Project Overview**  
This project is a **Voice Bot** built using an **LLM and text-to-speech (TTS)**. The bot answers personal and behavioral questions based on my pre-stored responses in a **JSON file**. Since my **OpenAI API key was exhausted**, I used an **open-source LLM** instead.  

## **Project Workflow**  

1️⃣ **Data Storage**  
- My biographical details and answers to interview questions are stored in a **JSON file**.  

2️⃣ **LLM Processing**  
- The **JSON data** is loaded as context into an **open-source LLM** for generating responses.  

3️⃣ **Text-to-Speech (TTS) Conversion**  
- The generated response is passed to **gTTS** (Google Text-to-Speech) to convert text into speech.  

4️⃣ **Frontend Development**  
- A **Streamlit** app is used for easy interaction with the voice bot.  

## **Key Features**  
✅ **Predefined responses** based on stored personal and professional details.  
✅ **Voice Output** using **gTTS**.  
✅ **Streamlit UI** for user-friendly interaction.  
✅ **Open-source LLM** (instead of OpenAI API) due to API key exhaustion.  

## **Drawbacks & Latency Considerations**  
⚠ **Latency Issue:** Since I used a **library-based TTS**, there is a **7-8 second delay** in speech output.  
⚠ **Potential Improvement:** If I had an OpenAI API key, I would have used a **low-latency approach** for better real-time responses.  

## **Live Demo**  
🎤 **Test the app here:**  
🔗 [Home.LLC AI Voice Bot](https://sibanink-homellc-assignment-app-jkdcmh.streamlit.app/)  

## **Project Structure**  
```md
📂 HomeLLC_Assignment  
│── 📄 app.py                  # Streamlit frontend  
│── 📄 main.py                  # Core logic: Loads JSON, calls LLM, and TTS  
│── 📄 profile.json           # Stores my biopic  
│── 📄 requirements.txt         # Dependencies  
│── 📄 README.md                # Project documentation (this file)  
