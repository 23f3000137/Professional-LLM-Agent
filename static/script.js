// static/script.js

document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chat-form');
    const messageInput = document.getElementById('message-input');
    const chatWindow = document.getElementById('chat-window');
    const errorAlert = document.getElementById('error-alert');
    const sendButton = document.getElementById('send-button');
    const spinner = document.getElementById('spinner');
    const sendIcon = sendButton.querySelector('.fa-paper-plane');

    // Add initial welcome message
    addMessageToChat('agent', "Hello! I am a professional LLM Agent. Ask me about IBM to see me use my tools.");

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const message = messageInput.value.trim();
        if (!message) return;

        addMessageToChat('user', message);
        messageInput.value = '';
        toggleLoading(true);

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: message }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || 'Server error');
            }

            const data = await response.json();
            addMessageToChat('agent', data.reply);
            hideError();

        } catch (error) {
            console.error('Error:', error);
            showError(`Error: ${error.message}`);
        } finally {
            toggleLoading(false);
        }
    });

    /**
     * Creates and appends a new message bubble to the chat window.
     * @param {'user' | 'agent'} sender - The sender of the message.
     * @param {string} text - The message content.
     */
    function addMessageToChat(sender, text) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', `message-${sender}`);

        const avatarIcon = sender === 'user' ? 'fa-user' : 'fa-robot';
        
        // Using template literal for cleaner HTML structure
        messageElement.innerHTML = `
            <div class="avatar">
                <i class="fa-solid ${avatarIcon}"></i>
            </div>
            <div class="message-content">
                ${text}
            </div>
        `;

        chatWindow.appendChild(messageElement);
        chatWindow.scrollTop = chatWindow.scrollHeight; // Auto-scroll to the latest message
    }

    function showError(message) {
        errorAlert.textContent = message;
        errorAlert.classList.remove('d-none');
    }

    function hideError() {
        if (!errorAlert.classList.contains('d-none')) {
            errorAlert.classList.add('d-none');
        }
    }
    
    function toggleLoading(isLoading) {
        messageInput.disabled = isLoading;
        sendButton.disabled = isLoading;

        if (isLoading) {
            spinner.style.display = 'inline-block';
            sendIcon.style.display = 'none';
        } else {
            spinner.style.display = 'none';
            sendIcon.style.display = 'inline-block';
            messageInput.focus();
        }
    }
});