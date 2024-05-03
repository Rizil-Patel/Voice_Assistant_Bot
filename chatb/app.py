from flask import Flask, render_template,request,jsonify
from chatbot import process_command

app = Flask(__name__)

app.static_folder = 'static'

# Route to serve the HTML interface
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def handle_command():
    data = request.get_json()
    command = data.get('command')
    response = process_command(command)  # Call the imported function
    return jsonify({'response': response})

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred: {e}")