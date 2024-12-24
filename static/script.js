document.addEventListener("DOMContentLoaded", () => {
    const chatMessages = document.getElementById("chat-messages");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-btn");
    const emotionWidget = document.getElementById("emotion-widget");
    const emotionIcon = document.getElementById("emotion-icon");
    const typingIndicator = document.getElementById("typing-indicator");

    // Append messages to the chat
    const appendMessage = (message, type) => {
        const messageBubble = document.createElement("div");
        messageBubble.className = `message ${type}`;
        messageBubble.textContent = message;
        chatMessages.appendChild(messageBubble);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    };

    // Show/Hide Typing Indicator
    const showTypingIndicator = () => {
        typingIndicator.classList.remove("hidden");
    };

    const hideTypingIndicator = () => {
        typingIndicator.classList.add("hidden");
    };

    // Update emotion widget
    const updateEmotion = (emotion) => {
        const currentEmotion = document.getElementById("current-emotion");
        emotionWidget.className = "emotion-widget"; // Reset classes
        switch (emotion) {
            case "happy":
                emotionWidget.classList.add("positive");
                emotionIcon.textContent = "😊";
                currentEmotion.textContent = "Happy";
                break;
            case "excited":
                emotionWidget.classList.add("positive");
                emotionIcon.textContent = "🤩";
                currentEmotion.textContent = "Excited";
                break;
            case "sad":
                emotionWidget.classList.add("negative");
                emotionIcon.textContent = "😢";
                currentEmotion.textContent = "Sad";
                break;
            case "lonely":
                emotionWidget.classList.add("negative");
                emotionIcon.textContent = "🥺";
                currentEmotion.textContent = "Lonely";
                break;
            case "frustrated":
                emotionWidget.classList.add("negative");
                emotionIcon.textContent = "😤";
                currentEmotion.textContent = "Frustrated";
                break;
            case "angry":
                emotionWidget.classList.add("negative");
                emotionIcon.textContent = "😡";
                currentEmotion.textContent = "Angry";
                break;
            case "bored":
                emotionWidget.classList.add("neutral");
                emotionIcon.textContent = "😑";
                currentEmotion.textContent = "Bored";
                break;
            case "anxious":
                emotionWidget.classList.add("negative");
                emotionIcon.textContent = "😰";
                currentEmotion.textContent = "Anxious";
                break;
            case "depressed":
                emotionWidget.classList.add("negative");
                emotionIcon.textContent = "😞";
                currentEmotion.textContent = "Depressed";
                break;
            default:
                emotionWidget.classList.add("neutral");
                emotionIcon.textContent = "😐";
                currentEmotion.textContent = "Neutral";
                break;
        }
    };

    // Handle user input
    const sendMessage = async () => {
        const message = userInput.value.trim();
        if (!message) return;

        // Show user message
        appendMessage(message, "user");
        userInput.value = "";

        // Show typing indicator
        showTypingIndicator();

        try {
            const response = await fetch("http://127.0.0.1:5000/get_response", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message }),
            });

            const data = await response.json();
            hideTypingIndicator(); // Hide typing indicator
            appendMessage(data.response, "assistant");
            updateEmotion(data.emotion); // Update emotion dynamically
        } catch (error) {
            hideTypingIndicator(); // Hide typing indicator
            appendMessage("Error: Unable to connect to the server.", "assistant");
            console.error(error); // Logs detailed error info to the console
        }
    };

    // Event listeners for send button and Enter key
    sendButton.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") sendMessage();
    });
});
