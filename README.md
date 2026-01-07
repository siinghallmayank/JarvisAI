# 🤖 JarvisAI - Personal Voice Assistant

Welcome to **JarvisAI**, your personal AI assistant built in **Python**!  
JarvisAI can **understand voice commands**, **open websites**, **search Wikipedia**, **play YouTube videos**, and interact with you through voice.  

## ✨ Features

- 🎤 **Voice Recognition** – Understands what you say using `SpeechRecognition`
- 🗣️ **Text-to-Speech** – Speaks back to you using `pyttsx3` or macOS `say`
- 🌐 **Web Automation** – Opens websites like YouTube, Google, GTBIT pages, and social media
- 📚 **Wikipedia Search** – Gets information instantly via voice
- 🛠️ **Custom Commands** – Easily extendable to open your favorite apps or websites

## 📂 Project Structure

JarvisAI/
│
├─ main.py # Main program
├─ modules/ # Optional: separate modules for commands
│ ├─ speech.py
│ └─ commands.py
├─ requirements.txt # Python dependencies
├─ .venv/ # Virtual environment (ignored in GitHub)
└─ data/ # Optional: logs, audio files, etc
