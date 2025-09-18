# Claude Chat - Simple LLM Wrapper

A clean, simple chat interface for interacting with Claude 4 Sonnet. Features a modern messaging UI similar to popular chat apps with a beautiful red, grey, and white color scheme.

## Features

- 🎨 Clean, modern chat interface with #A51C30 red color scheme
- 💬 Real-time messaging with Claude 4 Sonnet
- 🎭 Customizable system prompts for different personalities
- 📱 Mobile-responsive design
- ⚡ Fast and lightweight
- 🔒 Secure API integration

## Setup

### Prerequisites

- Python 3.8 or higher
- Anthropic API key (Claude)

### Installation

1. **Clone or download this repository**

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Claude API key**
   
   Get your API key from [Anthropic Console](https://console.anthropic.com/) and set it as an environment variable:
   
   ```bash
   export ANTHROPIC_API_KEY='your-api-key-here'
   ```
   
   Or create a `.env` file in the project directory:
   ```
   ANTHROPIC_API_KEY=your-api-key-here
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   
   Navigate to `http://localhost:5000` to start chatting with Claude!

## Usage

- Type your message in the input field at the bottom
- Press Enter or click the send button to send your message
- Claude will respond in real-time
- The interface supports multi-line messages (use Shift+Enter for new lines)
- Character limit: 4000 characters per message

## 🎭 Customizing Claude's Personality

Your chat app now includes a configurable system prompt! You can easily customize how Claude behaves:

### Quick Setup:
1. **Edit `config.py`** - Change the `SYSTEM_PROMPT` variable
2. **Restart the app** - `python app.py`
3. **Test the new personality!**

### Examples Available:
- **Professional Assistant** - Formal, detailed responses
- **Creative Writing Helper** - Storytelling and creative support  
- **Coding Mentor** - Programming guidance and education
- **Casual Friend** - Relaxed, conversational tone
- **Research Assistant** - Information gathering and analysis
- **And many more!**

Check `prompt_examples.md` for ready-to-use prompts you can copy and paste.

### What You Can Customize:
- **System Prompt** - Claude's personality and behavior
- **App Title** - The header text (currently "Claude Chat")
- **Welcome Message** - The first message users see
- **Model Settings** - Temperature, max tokens, etc.

## API Endpoints

- `GET /` - Main chat interface
- `POST /api/chat` - Send message to Claude
- `GET /api/health` - Health check endpoint

## 🚀 Deployment Options

This app is ready to deploy to the cloud so anyone can access it with just a link:

### Recommended: Railway (Easiest!)
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Deploy from GitHub repo
4. Add environment variable: `ANTHROPIC_API_KEY`
5. Get your live URL!

### Other Options:
- **Vercel** - Fast global deployment
- **Render** - Reliable hosting
- **Heroku** - Classic platform

See deployment files included:
- `Dockerfile` - Docker deployment
- `railway.json` - Railway configuration
- `vercel.json` - Vercel configuration
- `runtime.txt` - Python version specification

## Customization

The app is designed to be simple and easily customizable:

- **Styling**: Edit `style.css` to change colors, fonts, or layout
- **Behavior**: Modify `script.js` to add new features
- **Backend**: Update `app.py` to change Claude settings or add new endpoints
- **Prompts**: Edit `config.py` to change Claude's personality

## Troubleshooting

### Common Issues

1. **"API key not configured" error**
   - Make sure you've set the `ANTHROPIC_API_KEY` environment variable
   - Verify your API key is valid and has credits

2. **"Connection refused" error**
   - Check that the Flask server is running on port 5000
   - Ensure no other application is using port 5000

3. **Slow responses**
   - This is normal for LLM responses, especially for longer messages
   - Check your internet connection

4. **Railway deployment issues**
   - Make sure your `ANTHROPIC_API_KEY` is set in Railway environment variables
   - Check the deployment logs for specific errors

### Development Mode

The app runs in production mode by default. For development:

1. Set `debug=True` in `app.py`
2. Use the virtual environment setup from the original CS79 directory

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.