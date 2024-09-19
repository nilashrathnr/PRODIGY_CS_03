from flask import Flask, render_template, request

app = Flask(__name__)

# Function to assess password strength
def check_password_strength(password):
    strength = 0
    feedback = ""

    if len(password) >= 8:
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in "!@#$%^&*()-_+=" for char in password):
        strength += 1

    if strength <= 1:
        feedback = "Very Weak"
    elif strength == 2:
        feedback = "Weak"
    elif strength == 3:
        feedback = "Moderate"
    elif strength == 4:
        feedback = "Strong"
    else:
        feedback = "Very Strong"

    return feedback

@app.route("/", methods=["GET", "POST"])
def index():
    strength = None
    if request.method == "POST":
        password = request.form["password"]
        strength = check_password_strength(password)
    return render_template("index.html", strength=strength)

if __name__ == "__main__":
    app.run(debug=True)
