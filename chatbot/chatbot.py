import os
from openai import OpenAI
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown

# Initialize Rich console for better output
console = Console()

def initialize_openai():
    """Initialize OpenAI client with API key from environment variables."""
    load_dotenv()  # Load environment variables from .env file
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        console.print("[red]Error: OPENAI_API_KEY not found in .env file[/red]")
        console.print("Please create a .env file with your OpenAI API key:")
        console.print("OPENAI_API_KEY=your-api-key-here")
        exit(1)
    
    return OpenAI(api_key=api_key)

def create_chat_completion(client, user_input, conversation_history):
    """Create a chat completion using OpenAI's API."""
    # Add user's message to conversation history
    conversation_history.append({"role": "user", "content": user_input})
    
    try:
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            temperature=0.7,
            max_tokens=150
        )
        
        # Get the assistant's message
        assistant_message = response.choices[0].message.content
        
        # Add assistant's response to conversation history
        conversation_history.append({"role": "assistant", "content": assistant_message})
        
        return assistant_message
    
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        return None

def main():
    """Main function to run the chatbot."""
    # Initialize OpenAI client
    client = initialize_openai()
    
    # Initialize conversation history with a system message
    conversation_history = [
        {
            "role": "system",
            "content": "You are a helpful and friendly AI assistant. Keep your responses concise and engaging."
        }
    ]
    
    # Welcome message
    console.print("[bold blue]Welcome to the AI Chatbot![/bold blue]")
    console.print("Type 'quit' to exit the chat.")
    console.print("----------------------------------------")
    
    # Main chat loop
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        # Check if user wants to quit
        if user_input.lower() in ['quit', 'exit', 'bye']:
            console.print("\n[bold blue]Goodbye! Thanks for chatting![/bold blue]")
            break
        
        # Skip empty inputs
        if not user_input:
            continue
        
        # Get response from OpenAI
        response = create_chat_completion(client, user_input, conversation_history)
        
        if response:
            # Display the response using Rich's Markdown rendering
            console.print("\n[bold green]Assistant:[/bold green]")
            console.print(Markdown(response))

if __name__ == "__main__":
    main() 