from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Define home route
@app.route('/', methods=['GET', 'POST'])
def home():
    recommendation = ""
    if request.method == 'POST':
        symptom = request.form['symptom']
        X_input = vectorizer.transform([symptom])
        recommendation = model.predict(X_input)[0]
    
    return render_template('index.html', recommendation=recommendation)

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
