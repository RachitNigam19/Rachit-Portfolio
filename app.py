from flask import Flask, render_template, request, jsonify
from chatbot_logic import Rulebot # Import your chatbot class

app = Flask(__name__)

# Instantiate your chatbot (Loaded from the file of app.py)
chatbot = Rulebot()

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')  # Load your webpage (index.html)

# Route for processing chatbot conversation
@app.route('/chat', methods=['POST'])
def chat():
    # Correct placement of .lower()
    user_input = request.form['message'].lower()  # Convert user input to lowercase
    response = chatbot.match_reply(user_input)  # Get chatbot response
    return jsonify({'response': response})  # Return response as JSON

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
