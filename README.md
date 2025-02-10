# Plat Plus Playground

Imagination is more important than knowledge.

## Features

- Real-time chat interface
- Session management for multiple conversations
- Clean and modern UI
- CORS support for development
- Environment variable configuration

## Prerequisites

- Python 3.8 or higher
- OpenAI API key

## Installation

After cloning the repository, run the following commands to install the dependencies and create a virtual environment:

1. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Flask application:
```bash
python completed/app.py
```
3. Open your browser and navigate to `http://127.0.0.1:5000`

## Project Structure

```
.
├── completed/
│   ├── app.py              # Main Flask application
│   ├── templates/          # HTML templates
│   │   └── index.html      # Main chat interface
│   └── static/             # Static files
│       ├── css/
│       │   └── style.css   # Custom styles
│       └── js/
│           └── app.js      # Frontend JavaScript
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (not tracked in git)
└── README.md             # This file
```

## Security Notes

- Never commit your `.env` file or expose your API keys
- This is a development server, not suitable for production use
- For production, use a proper WSGI server like Gunicorn

## License

MIT License - feel free to use this code for your own projects.

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Submit a pull request
