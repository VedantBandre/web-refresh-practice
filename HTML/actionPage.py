from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        return f"Received: First Name = {fname}, Last Name = {lname}"
    return "Form not Submitted"

if __name__ == '__main__':
    app.run(debug=True)