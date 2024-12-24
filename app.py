from flask import Flask, render_template, request, jsonify
from emotion_detection import detect_emotion
from sad_emotion import respond_to_sadness
from happy_emotion import respond_to_happiness
from frustrated_emotion import respond_to_frustration
from depressed_emotion import respond_to_depression
from angry_emotion import respond_to_anger
from excited_emotion import respond_to_excitement
from bored_emotion import respond_to_boredom
from lonely_emotion import respond_to_loneliness
from anxious_emotion import respond_to_anxiety

from dotenv import load_dotenv  # Import dotenv
import os  # Import os for environment variables
import openai  # OpenAI library

# Load environment variables from .env file
load_dotenv()

# Access the API key
openai.api_key = os.getenv("OPENAI_API_KEY")


# Initialize Flask app
app = Flask(__name__)


# Initialize message history
message_history = [
    {
        "role": "system",
        "content": "You are a helpful and empathetic mental health assistant.",
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"response": "Please provide a valid input."}), 400

    global message_history
    message_history.append({"role": "user", "content": user_message})

    # Detect Emotion
    current_emotion = detect_emotion(user_message, message_history)

    # Generate Emotion-Specific Response
    if current_emotion == "sad":
        bot_reply = respond_to_sadness(user_message, message_history)
    elif current_emotion == "happy":
        bot_reply = respond_to_happiness(user_message, message_history)
    elif current_emotion == "frustrated":
        bot_reply = respond_to_frustration(user_message, message_history)
    elif current_emotion == "depressed":
        bot_reply = respond_to_depression(user_message, message_history)
    elif current_emotion == "angry":
        bot_reply = respond_to_anger(user_message, message_history)
    elif current_emotion == "excited":
        bot_reply = respond_to_excitement(user_message, message_history)
    elif current_emotion == "bored":
        bot_reply = respond_to_boredom(user_message, message_history)
    elif current_emotion == "lonely":
        bot_reply = respond_to_loneliness(user_message, message_history)
    elif current_emotion == "anxious":
        bot_reply = respond_to_anxiety(user_message, message_history)
    else:
        bot_reply = (
            "I'm here to help with whatever you're feeling. Can you tell me more?"
        )

    # Append Bot Reply to History
    message_history.append({"role": "assistant", "content": bot_reply})

    # Send Response and Emotion
    return jsonify({"response": bot_reply, "emotion": current_emotion})


if __name__ == "__main__":
    app.run(debug=True)
