# app.py

import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
# Set up the Flask app
app = Flask(__name__)

# Configure the Gemini API key
# Create a .env file in your project root and add: GOOGLE_API_KEY="your_api_key"
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file.")
genai.configure(api_key=api_key)

# --- Tool Definitions ---
def google_search(query: str) -> str:
    """
    A mock function to simulate searching Google and returning snippets.
    In a real application, this would use a real search API.
    """
    print(f"--- Executing Tool: google_search with query '{query}' ---")
    if "ibm" in query.lower():
        return "IBM (International Business Machines Corporation) is a major American multinational technology company headquartered in Armonk, New York. It was founded in 1911."
    elif "llm agent" in query.lower():
        return "An LLM Agent is an AI system that uses a large language model (LLM) as its core reasoning engine to autonomously perform tasks by using a set of available tools."
    else:
        return f"No specific information found for '{query}'. Try searching for 'IBM' or 'LLM agent'."

# --- Gemini Model and Tool Configuration ---
tools = [
    {
        "function_declarations": [
            {
                "name": "google_search",
                "description": "Gets snippets from a Google search for a given query.",
                "parameters": {
                    "type": "OBJECT",
                    "properties": {
                        "query": {"type": "STRING", "description": "The search query."}
                    },
                    "required": ["query"],
                },
            }
        ]
    }
]

model = genai.GenerativeModel(model_name="gemini-1.5-flash", tools=tools)

# --- Flask Routes ---
@app.route("/")
def index():
    """Render the main chat page."""
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """Main chat endpoint that follows the agent logic loop."""
    data = request.json
    user_message = data.get("message")
    chat_session = model.start_chat() 

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Send user message to the model
        response = chat_session.send_message(user_message)
        
        # Safely check if the model requested a tool call
        if hasattr(response, 'function_calls') and response.function_calls:
            function_call = response.function_calls[0]
            tool_name = function_call.name
            tool_args = function_call.args

            if tool_name == "google_search":
                # Execute the tool
                tool_result = google_search(query=tool_args['query'])

                # Send the tool's result back to the model
                response = chat_session.send_message(
                    genai.Part(
                        function_response={
                            "name": tool_name,
                            "response": {"result": tool_result},
                        }
                    )
                )

        # Return the final text response from the agent
        return jsonify({"reply": response.text})

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

if __name__ == "__main__":
    app.run(debug=True)