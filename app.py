from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flash messages

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    # Retrieve form data
    forename = request.form.get('forename')
    surname = request.form.get('surname')
    email = request.form.get('email')
    phone = request.form.get('phone')
    address = request.form.get('address')

    # Simple validation
    if not forename or not surname or not email:
        flash('Fields with * recquired!')
        return redirect(url_for('index'))

    # Here you can process the form data
    # we'll just flash a message with the input data
    flash(f'Form Submitted! Forename: {forename}, Surname: {surname}, Email: {email}, Phone: {phone}, Address: {address}')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

