from dotenv import load_dotenv  # Import dotenv
import os  # Import os for environment variables
import openai  # OpenAI library

# Load environment variables from .env file
load_dotenv()

# Access the API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def detect_emotion(user_input, message_history):
    """
    Detects the user's current emotion based on the message history and latest input.
    """
    try:
        # Only include user messages in the emotion analysis
        user_history = [msg for msg in message_history if msg["role"] == "user"]

        messages = (
            [
                {
                    "role": "system",
                    "content": (
                        "You are an assistant that detects emotions in text. "
                        "Analyze the user's current state and return one of these emotions only these emotions thats it. nothing else all small and one word. if still confused about emotion then map into one of the closest emotion below: I repeat it should strictly reply only one of the emotions: "
                        "frustrated, depressed, angry, sad, excited, happy, bored, lonely, or anxious."
                    ),
                },
            ]
            + user_history
            + [{"role": "user", "content": user_input}]
        )

        # Call OpenAI API
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.5,
            max_tokens=10,  # Limit response to a single emotion keyword
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        # Extract and validate emotion
        emotion = response.choices[0].message.content.strip().lower()
        valid_emotions = [
            "frustrated",
            "depressed",
            "angry",
            "sad",
            "excited",
            "happy",
            "bored",
            "lonely",
            "anxious",
        ]
        return emotion if emotion in valid_emotions else emotion # "neutral"
    except Exception as e:
        print(f"Error in emotion detection: {e}")
        return "neutral"
