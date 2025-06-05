from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Optional: endpoint to receive text from frontend
@app.route('/save_text', methods=['POST'])
def save_text():
    data = request.json
    text = data.get('text', '')
    print("Received text:", text)
    # You can save it to a file or database here
    return jsonify({'status': 'success', 'message': 'Text received!'})

if __name__ == '__main__':
    app.run(debug=True)
