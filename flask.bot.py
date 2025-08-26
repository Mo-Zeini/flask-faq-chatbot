import os
from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# FAQ Database
FAQ_RESPONSES = {
    'hours': "We're open Monday-Friday 9 AM to 6 PM, Saturday 10 AM to 4 PM, closed Sunday.",
    'returns': "You can return items within 30 days. Go to My Account > Returns or contact customer service.",
    'tracking': "Use your order number on our tracking page or check your email confirmation.",
    'payment': "We accept all major credit cards, PayPal, and bank transfers.",
    'contact': "Email us at support@company.com or use our live chat feature."
}

# Keywords mapping
KEYWORDS = {
    'hours': ['hours', 'open', 'close', 'time'],
    'returns': ['return', 'refund', 'exchange'],
    'tracking': ['track', 'order', 'shipping'],
    'payment': ['payment', 'pay', 'card', 'paypal'],
    'contact': ['contact', 'support', 'help', 'phone']
}

def get_response(user_input):
    user_input = user_input.lower()
    
    for intent, keywords in KEYWORDS.items():
        if any(keyword in user_input for keyword in keywords):
            return FAQ_RESPONSES[intent]
    
    return "I didn't understand that. Can you rephrase your question?"

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    bot_response = get_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)