from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Path to the file where the credentials will be saved
credentials_file = "credentials.txt"

# Function to save credentials to a text file
def save_credentials(email,age,username, password):
    with open(credentials_file, "a") as file:
        file.write(f"Email:{email},    Age:{age},    Username:{username},   Password:{password}\n")

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        age = request.form["age"]
        
        save_credentials(email ,age, username, password)
        
        return jsonify({"message": "Registration Successful! Credentials have been saved."})
    
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)