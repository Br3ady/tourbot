from flask import Flask, request, jsonify, render_template_string, send_from_directory
import anthropic
import os
from datetime import datetime
import logging
from config import SYSTEM_PROMPT, MODEL_NAME, MAX_TOKENS, TEMPERATURE, APP_TITLE, WELCOME_MESSAGE

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Initialize Anthropic client
client = anthropic.Anthropic(
    api_key=os.getenv('ANTHROPIC_API_KEY')
)

@app.route('/')
def index():
    """Serve the main HTML page"""
    try:
        with open('index.html', 'r') as f:
            html_content = f.read()
            # Replace placeholders with config values
            html_content = html_content.replace('{{APP_TITLE}}', APP_TITLE)
            html_content = html_content.replace('{{WELCOME_MESSAGE}}', WELCOME_MESSAGE)
            return html_content
    except FileNotFoundError:
        return "Error: index.html not found", 404

@app.route('/style.css')
def serve_css():
    """Serve the CSS file"""
    try:
        return send_from_directory('.', 'style.css', mimetype='text/css')
    except FileNotFoundError:
        return "Error: style.css not found", 404

@app.route('/script.js')
def serve_js():
    """Serve the JavaScript file"""
    try:
        return send_from_directory('.', 'script.js', mimetype='application/javascript')
    except FileNotFoundError:
        return "Error: script.js not found", 404

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages and return Claude's response"""
    try:
        # Get the message from the request
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'No message provided'}), 400
        
        user_message = data['message'].strip()
        if not user_message:
            return jsonify({'error': 'Empty message'}), 400
        
        # Log the user message
        logger.info(f"User message: {user_message}")
        
        # Check if API key is configured
        if not os.getenv('ANTHROPIC_API_KEY'):
            return jsonify({
                'response': 'Error: ANTHROPIC_API_KEY environment variable not set. Please configure your Claude API key.'
            }), 200
        
        # Send message to Claude
        try:
            message = client.messages.create(
                model=MODEL_NAME,
                max_tokens=MAX_TOKENS,
                temperature=TEMPERATURE,
                system=SYSTEM_PROMPT,
                messages=[
                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            )
            
            # Extract the response text
            response_text = message.content[0].text
            
            # Log the response
            logger.info(f"Claude response: {response_text[:100]}...")
            
            return jsonify({
                'response': response_text,
                'timestamp': datetime.now().isoformat()
            })
            
        except anthropic.APIError as e:
            logger.error(f"Anthropic API error: {e}")
            return jsonify({
                'response': f'Sorry, I encountered an API error: {str(e)}'
            }), 200
            
        except Exception as e:
            logger.error(f"Unexpected error calling Claude API: {e}")
            return jsonify({
                'response': 'Sorry, I encountered an unexpected error. Please try again.'
            }), 200
    
    except Exception as e:
        logger.error(f"Error in chat endpoint: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'api_key_configured': bool(os.getenv('ANTHROPIC_API_KEY'))
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Internal server error: {error}")
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Check if API key is set
    if not os.getenv('ANTHROPIC_API_KEY'):
        print("WARNING: ANTHROPIC_API_KEY environment variable not set!")
        print("Please set your Claude API key with: export ANTHROPIC_API_KEY='your-api-key-here'")
    
    # Get port from environment variable (for cloud deployment) or default to 5000
    port = int(os.getenv('PORT', 5000))
    
    # Run the app
    app.run(debug=False, host='0.0.0.0', port=port)
