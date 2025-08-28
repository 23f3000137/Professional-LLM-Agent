# Professional-LLM-Agent Chatbot
This project is a sophisticated, web-based LLM (Large Language Model) Agent built with a Python Flask backend and a modern JavaScript frontend. The agent features a professional chat interface and is capable of using external tools to provide more accurate and context-aware responses, demonstrating a core concept in advanced AI systems [1].


*(Replace the link above with a screenshot of your running application)*

## Features

*   **Professional UI:** A clean, modern chat interface inside a distinct "grid box" with a pleasant background gradient.
*   **LLM Agent Logic:** The chatbot can reason and decide when to use external tools to answer a user's query [1].
*   **Tool Integration:** Includes a sample `google_search` tool that the LLM can call upon to fetch information [1].
*   **Live Typing Indicator:** Provides real-time feedback to the user while the agent is processing a response.
*   **Markdown Rendering:** The agent's responses are beautifully formatted with support for lists, code blocks, bold text, and more.
*   **Error Handling:** Gracefully displays errors to the user using Bootstrap alerts [1].

## Tech Stack

*   **Backend:** Python 3, Flask
*   **AI/LLM:** Google Gemini API (`gemini-1.5-flash`)
*   **Frontend:** HTML5, CSS3, JavaScript (ES6)
*   **UI Libraries:**
    *   Bootstrap 5 for styling and layout.
    *   Font Awesome for icons.
    *   Marked.js for client-side Markdown rendering.

## Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

*   Python 3.8 or newer
*   `pip` (Python package installer)

### 2. Set Up Project Files

Create the project structure as described or use the provided single-file `app.py` script.

### 3. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

*   **On macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
*   **On Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

### 4. Install Dependencies

Install the required Python packages using pip:

```bash
pip install Flask google-generativeai python-dotenv
