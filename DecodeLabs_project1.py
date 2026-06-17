import json
from flask import Flask, render_template_string

app = Flask(__name__)

# Deeper Knowledge Base for a more comprehensive rule-based conversation
KNOWLEDGE_BASE = {
    # Greetings & Essentials
    'hello': "Hello! I am your rule-based assistant. How can I help you today?",
    'hi': "Hello! How can I assist you today?",
    'hey': "Hey! Ready to process your commands.",
    'good morning': "Good morning! How may I help you today?",
    'good afternoon': "Good afternoon! What can I do for you?",
    'good evening': "Good evening! I'm online and ready to assist.",
    
    # Identity & Core Specs
    'how are you': "I am a rule-based AI, so I don't have feelings, but my performance metrics are optimal! How are you?",
    'who are you': "I am the DecodeLabs Rule-Based Logic Engine, built to process discrete text instructions natively.",
    'help': "I am a white-box logic engine. I map exact intents to explicit responses without hallucination. Try commands like 'status', 'about', or 'features'.",
    'status': "All systems nominal. The deterministic guardrail is performing perfectly.",
    'about': "Project 1 Foundation Phase: Built for DecodeLabs Industrial Training 2026.",
    'version': "System version: v2.4.0 (Deterministic Release - June 2026).",
    
    # Fine-grained Small Talk & Long-form Fillers
    'fine': "Glad to hear that! What commands or project details would you like to explore next?",
    'good': "Excellent! Let's keep moving. Type a command to interact with my logic blocks.",
    'i am good': "Great! Ready when you are. Enter any supported keyword to continue.",
    'thank you': "You're very welcome! It's my deterministic duty to assist.",
    'thanks': "No problem at all! Let me know if you need anything else.",
    'great': "Fantastic! What else can I pull up from the DecodeLabs framework for you?",
    'awesome': "Agreed! My rule-based indexing ensures 100% predictable accuracy.",
    
    # Capabilities & Platform Questions
    'features': "Features include: Zero hallucination, dark mode UI, sub-300ms response time, and a structural white-box backend.",
    'capabilities': "I can process predefined intent vectors, map system statuses, and display project schemas efficiently.",
    'ai': "Unlike LLMs, I don't use weights or probabilities. I use an atomic dictionary lookup for perfect consistency.",
    'llm': "Large Language Models are creative but can hallucinate. I am a rule-based engine designed for predictable guardrails.",
    'decodelabs': "DecodeLabs provides cutting-edge industrial training and software engineering modules for next-gen developers.",
    
    # System & Troubleshooting Commands
    'reset': "Session tracking cleared. Input pipeline is fresh and ready.",
    'clear': "To clear your screen visually, you can refresh the browser window!",
    'debug': "LOG: Intent map length = 25 keys | Collision state = 0 | Runtime environment = Flask/Python3",
    'contact': "For support regarding DecodeLabs Training 2026, please contact your program administrator or mentor."
}

# Single UI Template combining HTML, CSS, and JS
COMBINED_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DecodeLabs AI Assistant</title>
    <style>
        /* Base layout styles */
        body {
            background-color: #f5f7fb;
            margin: 0;
            padding: 0;
        }
        #chat-container {
            max-width: 500px;
            margin: 50px auto;
            border: 1px solid #dcdcdc;
            border-radius: 8px;
            font-family: Arial, sans-serif;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
        }

        /* Header styles */
        #chat-container .header {
            background-color: #1A237E;
            color: white;
            padding: 14px 16px;
            border-top-left-radius: 7px;
            border-top-right-radius: 7px;
            font-weight: bold;
            display: flex;
            align-items: center;
        }

        /* Dialogue Screen window */
        #chat-window {
            height: 350px;
            overflow-y: auto;
            padding: 16px;
            display: flex;
            flex-direction: column;
            gap: 12px;
            transition: background-color 0.3s ease;
        }

        /* Chat bubbles */
        .message-bubble {
            padding: 10px 14px;
            border-radius: 14px;
            max-width: 80%;
            font-size: 14px;
            line-height: 1.4;
            word-break: break-word;
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        /* Message input panel */
        #chat-container .input-area {
            display: flex;
            border-top: 1px solid #dcdcdc;
            padding: 10px;
        }

        #user-msg {
            flex-grow: 1;
            border-radius: 4px;
            padding: 10px;
            outline: none;
            font-size: 14px;
            transition: border-color 0.3s ease, background-color 0.3s ease, color 0.3s ease;
        }

        #send-btn {
            border: none;
            padding: 0 20px;
            margin-left: 8px;
            border-radius: 20px;
            cursor: pointer;
            font-weight: bold;
            font-size: 14px;
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        /* Theme customization: Light Mode */
        .light-mode {
            background-color: #ffffff;
            border-color: #dcdcdc;
        }
        .light-mode #chat-window {
            background-color: #A7D7EF;
        }
        .light-mode .user-message {
            align-self: flex-end;
            background-color: #42A5F5;
            color: white;
            border-bottom-right-radius: 2px;
        }
        .light-mode .bot-message {
            align-self: flex-start;
            background-color: #e8eaed;
            color: #202124;
            border-bottom-left-radius: 2px;
        }
        .light-mode #user-msg {
            border: 1px solid #42A5F5;
            background-color: white;
            color: #202124;
        }
        .light-mode #send-btn {
            background-color: #42A5F5;
            color: white;
        }

        /* Theme customization: Dark Mode */
        .dark-mode {
            background-color: #2C3E50;
            border-color: #4A5B6C;
        }
        .dark-mode #chat-window {
            background-color: #34495E;
        }
        .dark-mode .user-message {
            align-self: flex-end;
            background-color: #64B5F6;
            color: white;
            border-bottom-right-radius: 2px;
        }
        .dark-mode .bot-message {
            align-self: flex-start;
            background-color: #5D6D7E;
            color: #ECF0F1;
            border-bottom-left-radius: 2px;
        }
        .dark-mode #user-msg {
            border: 1px solid #64B5F6;
            background-color: #4A5B6C;
            color: #ECF0F1;
        }
        .dark-mode #send-btn {
            background-color: #64B5F6;
            color: white;
        }

        #darkModeToggle {
            margin-left: auto;
            background: none;
            border: none;
            color: white;
            cursor: pointer;
            font-size: 1.3em;
            outline: none;
        }
    </style>
</head>
<body>

<div id="chat-container" class="light-mode">
    <div class="header">
        <span style="margin-right: 10px;">🤖</span>
        <span>DecodeLabs AI Assistant</span>
        <button id="darkModeToggle" onclick="toggleDarkMode()"></button>
    </div>

    <div id="chat-window">
        <div class="message-bubble bot-message">
            Hello! Type a command below to begin (e.g., <b>hello</b>, <b>features</b>, <b>status</b>, or <b>help</b>).
        </div>
    </div>

    <div class="input-area">
        <input type="text" id="user-msg" placeholder="Type a command..." onkeydown="if(event.key === 'Enter') sendCommand()">
        <button id="send-btn" onclick="sendCommand()">Send</button>
    </div>
</div>

<script>
    // Grab dynamically loaded JSON dictionary from backend environment
    const knowledgeBase = {{ knowledge_base | safe }};

    function appendMessage(text, isUser) {
        const chatWindow = document.getElementById('chat-window');
        const msgDiv = document.createElement('div');
        msgDiv.classList.add('message-bubble');

        if (isUser) {
            msgDiv.classList.add('user-message');
        } else {
            msgDiv.classList.add('bot-message');
        }

        msgDiv.innerText = text;
        chatWindow.appendChild(msgDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    function sendCommand() {
        const inputField = document.getElementById('user-msg');
        const rawInput = inputField.value;
        const cleanInput = rawInput.toLowerCase().trim();

        if (!cleanInput) return;

        appendMessage(rawInput, true);
        inputField.value = '';

        setTimeout(() => {
            if (['exit', 'quit', 'bye', 'goodbye'].includes(cleanInput)) {
                appendMessage("System received an exit command. Goodbye!", false);
            } else {
                const reply = knowledgeBase[cleanInput] || "Command not recognized. Try 'features', 'help', 'about', or 'capabilities'.";
                appendMessage(reply, false);
            }
        }, 250);
    }

    function toggleDarkMode() {
        const chatContainer = document.getElementById('chat-container');
        const darkModeToggle = document.getElementById('darkModeToggle');
        const isDarkMode = chatContainer.classList.toggle('dark-mode');

        if (isDarkMode) {
            localStorage.setItem('theme', 'dark');
            chatContainer.classList.remove('light-mode');
            darkModeToggle.innerText = '☀️';
        } else {
            localStorage.setItem('theme', 'light');
            chatContainer.classList.add('light-mode');
            darkModeToggle.innerText = '🌙';
        }
    }

    (() => {
        const savedTheme = localStorage.getItem('theme');
        const chatContainer = document.getElementById('chat-container');
        const darkModeToggle = document.getElementById('darkModeToggle');

        if (savedTheme === 'dark') {
            chatContainer.classList.remove('light-mode');
            chatContainer.classList.add('dark-mode');
            darkModeToggle.innerText = '☀️';
        } else {
            chatContainer.classList.remove('dark-mode');
            chatContainer.classList.add('light-mode');
            darkModeToggle.innerText = '🌙';
        }
    })();
</script>

</body>
</html>
"""

@app.route('/')
def home():
    # Direct serialization of dictionary map into HTML context
    kb_json = json.dumps(KNOWLEDGE_BASE)
    return render_template_string(COMBINED_TEMPLATE, knowledge_base=kb_json)

if __name__ == '__main__':
    app.run(debug=True)