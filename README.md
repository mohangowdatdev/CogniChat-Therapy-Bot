# CogniChat - Emotion-Aware Mental Therapy Chatbot

CogniChat is an AI-powered, emotion-aware chatbot designed to provide mental health support and assistance. It uses OpenAI's GPT-4o model to detect user emotions based on their inputs and responds empathetically with emotion-specific strategies to help users navigate their feelings.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [File Structure](#file-structure)
6. [Technical Details](#technical-details)
7. [Screenshots](#screenshots)
8. [Dependencies](#dependencies)
9. [Future Enhancements](#future-enhancements)
10. [Contributing](#contributing)
11. [License](#license)

---

## Overview
CogniChat is built with **Flask** as the backend framework and utilizes **OpenAI's GPT-4o** API for NLP capabilities. The chatbot dynamically assesses emotions based on user input and provides tailored responses for emotions such as anger, sadness, happiness, frustration, anxiety, and more.

This application can be used as an interactive mental health support tool for emotional regulation and expression.

---

## Features
- **Emotion Detection**: Accurately identifies user emotions (e.g., happy, sad, anxious) based on text input.
- **Emotion-Specific Responses**: Provides customized responses depending on the detected emotion.
- **Interactive Chat Interface**: Clean and responsive chat UI with an emotion widget displaying the user's current mood.
- **Typing Indicator**: Displays a typing animation when the assistant is processing a response.
- **Empathy-Driven Responses**: Emphasizes open-ended questions, empathetic messages, and emotional validation.
- **Lightweight and Fast**: Built using Flask for quick and seamless performance.

---

## Installation

### Prerequisites
- Python 3.7 or higher
- Node.js (optional for front-end customization)

### Steps
1. **Clone the Repository**:
```bash
$ git clone https://github.com/username/cognichat.git
$ cd cognichat
```
2. **Install Dependencies**:
```bash
$ pip install -r requirements.txt
```
3. **Set OpenAI API Key**:
Update the API key in `app.py`, `emotion_detection.py`, and emotion-specific scripts (e.g., `angry_emotion.py`). Replace the placeholder key with your own OpenAI API key.

4. **Run the Application**:
```bash
$ python app.py
```
5. **Access the Application**:
Open your browser and visit:
```
http://127.0.0.1:5000/
```

---

## Usage
1. Start the server and open the chat interface.
2. Type messages related to your emotions, such as "I'm feeling lonely today."
3. The chatbot detects the emotion (e.g., lonely) and responds empathetically.
4. Observe the emotion widget updating dynamically with icons and descriptions reflecting your mood.
5. Continue the conversation and receive tailored suggestions and support.

---

## File Structure
```
├── app.py                         # Main Flask application
├── emotion_detection.py           # Emotion detection module
├── angry_emotion.py               # Emotion-specific response module (example)
├── static/
│   ├── style.css                  # Chat interface styling
│   ├── script.js                  # Chat interaction logic
├── templates/
│   ├── index.html                 # Main UI template
├── requirements.txt               # Python dependencies
```

---

## Technical Details
### Backend:
- **Framework**: Flask
- **AI Model**: OpenAI GPT-4o (gpt-4o-mini)
- **Emotion Detection**: Processes chat history and input using OpenAI API to identify emotions.

### Frontend:
- **HTML/CSS/JavaScript**: Provides a responsive and dynamic user interface.
- **Dynamic Emotion Widget**: Reflects detected emotions in real-time.

### Key Algorithms:
1. **Emotion Detection**:
   - Analyzes user messages and previous inputs to identify emotional states.
2. **Emotion-Specific Responses**:
   - Generates tailored messages using a distinct prompt for each emotion.

---

## Screenshots
![Chat Interface](screenshots/chat_interface.png)
![Emotion Widget](screenshots/emotion_widget.png)

---

## Dependencies
- Flask
- OpenAI API
- HTML/CSS/JavaScript for UI components

---

## Future Enhancements
- **Voice Input/Output**: Add speech-to-text and text-to-speech capabilities.
- **User Profiles**: Save user data to provide personalized experiences.
- **Multi-Session Support**: Enable conversations across multiple sessions.
- **Analytics Dashboard**: Visualize user emotional trends over time.

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch.
3. Make your changes and test thoroughly.
4. Submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

