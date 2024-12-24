from dotenv import load_dotenv  # Import dotenv
import os  # Import os for environment variables
import openai  # OpenAI library

# Load environment variables from .env file
load_dotenv()

# Access the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize a message history list to store conversation context
message_history = [
    {
        "role": "system",
        "content": (
            "Act as a friendly and reliable bot." # Provide detailed context. 
        ),
    }
]


# Define a function to interact with OpenAI's Chat API
def get_medical_assistant_response(user_query):
    # Add the user's query to the conversation history
    message_history.append({"role": "user", "content": user_query})

    # Get the assistant's response
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=message_history,
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    # Append the assistant's response to the conversation history
    assistant_reply = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": assistant_reply})

    # Return the assistant's response
    return assistant_reply


# Main conversation loop
if __name__ == "__main__":
    print("Welcome to the Medical Assistant Bot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("\n\n ➡️ : ")

        # Exit condition
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the conversation. Take care!")
            break

        # Get the assistant's response
        response = get_medical_assistant_response(user_input)
        print("\n 🤖 : ", response)
