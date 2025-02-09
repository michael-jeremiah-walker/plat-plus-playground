import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load environment variables and initialize OpenAI client
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("No OpenAI API key found in environment variables")
client = OpenAI(
    base_url="https://api.openai.com/v1",
    api_key=api_key,
    timeout=30.0
)

# Store conversation histories for different sessions
conversations = {}

@app.route('/')
def home():
    """Serve the main chat interface."""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat API requests."""
    try:
        data = request.json
        user_message = data.get('message')
        session_id = data.get('session_id', 'default')

        # Initialize conversation history for new sessions
        if session_id not in conversations:
            conversations[session_id] = [
                {
                    "role": "system",
                    "content": "You are a helpful and friendly AI assistant. Keep your responses concise and engaging."
                }
            ]

        # Add user message to conversation history
        conversations[session_id].append({"role": "user", "content": user_message})

        # Get response from OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversations[session_id],
            temperature=0.7,
            max_tokens=150
        )

        # Extract and store assistant's response
        assistant_message = response.choices[0].message.content
        conversations[session_id].append({"role": "assistant", "content": assistant_message})

        return jsonify({
            "response": assistant_message,
            "session_id": session_id
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 