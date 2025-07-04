from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"Message received from {name} ({email}): {message}")
        return redirect(url_for('thank_you'))
    return render_template('contact.html')

@app.route('/thank-you')
def thank_you():
    return '<h2>Thank you for your message!</h2>'

if __name__ == '__main__':
    app.run(debug=True)
