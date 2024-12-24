from dotenv import load_dotenv  # Import dotenv
import os  # Import os for environment variables
import openai  # OpenAI library

# Load environment variables from .env file
load_dotenv()

# Access the API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def respond_to_frustration(user_input, message_history):
    """
    Generate a tailored response for users who are feeling frustrated.
    """
    try:
        messages = (
            [
                {
                    "role": "system",
                    "content": "You are a supportive assistant helping someone manage their frustration. Be patient, calming, and provide constructive advice. Maintain a friendly therapist type of conversation rather than a bot type of response and asking open ended questions only when needed else having small talks and emojis when needed. Be a smart and experienced therapist.",
                },
            ]
            + message_history
            + [{"role": "user", "content": user_input}]
        )

        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error in frustration response: {e}")
        return "It's okay to feel frustrated. I'm here to help you work through it."
