# Multimodal RAG for Context-Aware Information Synthesis in Healthcare

A full-stack web application that leverages Multimodal Retrieval-Augmented Generation (RAG) to provide context-aware information synthesis using both text and images, aimed at enhancing healthcare decision-making and user interaction.

# Features

- 🔍 Real-time retrieval and generation of medical responses from text and image inputs  
- 💬 ChatGPT-style conversational interface  
- 📁 Document and image upload support  
- 🧠 Backend AI integration using Flask and Hugging Face Transformers  

# Tech Stack
Frontend 
- ReactJS  

Backend  
- Flask (Python)  
- PyTorch, Hugging Face Transformers  
- OpenCV (for image processing)  

Development & Tools  
- VS Code  
- Google Colab  
- Git & GitHub  

## Project Structure

/frontend
  ├── assets/
  ├── components/
  ├── layout/
  ├── pages/
  ├── routes/
  ├── App.jsx
  └── main.jsx

/backend
  ├── app.py
  ├── mmrag1.ipynb
  ├── requirements.txt
  └── utils/

# Functionality Overview
 
1. The dashboard provides a chatbot interface with options to input text or upload documents/images.  
3. Queries are processed through a Flask backend integrated with `mmrag1.ipynb` notebook to retrieve relevant information using multimodal data.  
4. Responses are rendered dynamically on the frontend with chat history and contextual information.  

# Setup Instructions

# Prerequisites

- Node.js and npm  
- Python 3.9+   

# Frontend

cd frontend
npm install
npm run dev

# Backend

cd backend
pip install -r requirements.txt
python app.py

# Screenshots

UI screenshots like homepage, chatbot interface, and upload feature here.

# Home Page
![Home Page](./page3.jpeg)

# 💬 Chatbot Interface
![Chatbot Page](./chatbotPage.jpeg)

![Chatbot Page](https://github.com/hrbhoomi/MultiModelRAG/blob/main/backend/chatbotPage.jpeg)
# Author

Bhoomika H R  
GitHub: [@hrbhoomi](https://github.com/hrbhoomi)
