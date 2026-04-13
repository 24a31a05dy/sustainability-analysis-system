import matplotlib.pyplot as plt
from flask import jsonify
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# Import your pages (routes)
from pages.login import login_page
from pages.register import register_page
from pages.dashboard import dashboard_page

# Import ML logic from utils
from utils.score import predict_sustainability

app = Flask(__name__)
CORS(app)

# ---------------- PAGE ROUTES ----------------

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# ---------------- API ROUTES ----------------
@app.route('/predict', methods=['POST'])
def predict():
    energy = float(request.form['energy'])
    water = float(request.form['water'])
    waste = float(request.form['waste'])
    carbon = float(request.form['carbon'])

    features = [[energy, water, waste, carbon]]
    prediction = model.predict(features)[0]

    score = int(prediction)

    recommendations = generate_recommendation(energy, water, waste, carbon, score)

    return render_template("result.html",
                           score=score,
                           energy=energy,
                           water=water,
                           waste=waste,
                           carbon=carbon,
                           recommendations=recommendations)
labels = ['Energy', 'Water', 'Waste', 'Carbon']
values = [energy, water, waste, carbon]

plt.figure()
plt.bar(labels, values)
plt.title("Sustainability Breakdown")
plt.savefig("static/chart.png")
plt.close()
# ---------------- MAIN ----------------

if __name__ == '__main__':
    app.run(debug=True)

def generate_recommendation(energy, water, waste, carbon, score):
    tips = []

    if energy > 70:
        tips.append("⚡ Reduce energy usage. Switch to renewable energy.")

    if water > 70:
        tips.append("💧 Optimize water usage with recycling systems.")

    if waste > 70:
        tips.append("♻️ Improve waste management and recycling.")

    if carbon > 70:
        tips.append("🌍 Reduce carbon emissions using green transport.")

    if score < 50:
        tips.append("🚨 Overall sustainability is LOW. Immediate action needed.")

    return tips


@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.json
    
    energy = data.get('energy')
    water = data.get('water')
    waste = data.get('waste')
    carbon = data.get('carbon')

    features = [[energy, water, waste, carbon]]
    prediction = model.predict(features)[0]

    return jsonify({
        "score": int(prediction)
    })