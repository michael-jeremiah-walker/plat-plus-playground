// Generate a random session ID
const sessionId = Math.random().toString(36).substring(2);

// DOM elements
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const chatMessages = document.getElementById('chat-messages');

// Function to create a message element
function createMessageElement(content, isUser) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user-message' : 'assistant-message'}`;
    messageDiv.textContent = content;
    return messageDiv;
}

// Function to scroll to bottom of messages
function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Function to handle form submission
async function handleSubmit(e) {
    e.preventDefault();
    
    const message = userInput.value.trim();
    if (!message) return;
    
    // Clear input
    userInput.value = '';
    
    // Add user message to chat
    chatMessages.appendChild(createMessageElement(message, true));
    scrollToBottom();
    
    try {
        // Disable input while waiting for response
        userInput.disabled = true;
        
        // Send message to backend
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: message,
                session_id: sessionId
            }),
        });
        
        const data = await response.json();
        
        if (data.error) {
            throw new Error(data.error);
        }
        
        // Add assistant's response to chat
        chatMessages.appendChild(createMessageElement(data.response, false));
        scrollToBottom();
        
    } catch (error) {
        // Handle error
        const errorMessage = createMessageElement(
            `Error: ${error.message}. Please try again.`,
            false
        );
        errorMessage.style.backgroundColor = '#dc3545';
        errorMessage.style.color = 'white';
        chatMessages.appendChild(errorMessage);
        scrollToBottom();
        
    } finally {
        // Re-enable input
        userInput.disabled = false;
        userInput.focus();
    }
}

// Event listeners
chatForm.addEventListener('submit', handleSubmit);

// Focus input on page load
userInput.focus(); 