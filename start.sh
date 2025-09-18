#!/bin/bash

# Start the Claude Chat app
echo "Starting Claude Chat..."
echo "Make sure to set your ANTHROPIC_API_KEY environment variable:"
echo "  export ANTHROPIC_API_KEY='your-api-key-here'"
echo ""

# Activate virtual environment and start the app
source claude_chat_env/bin/activate
python app.py
