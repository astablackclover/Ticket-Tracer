from flask import Flask, render_template, request, redirect, url_for, jsonify, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key
tickets = []

# Sample user credentials
users = {
    "user1": "password1",  # User account
    "user2": "password2",  # Another user account
    "admin": "adminpass"   # Admin account
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        session['username'] = username
        if username == 'admin':
            return redirect(url_for('admin_dashboard'))
        else:
            return redirect(url_for('ticket_page'))
    return "Invalid credentials", 401

@app.route('/ticket', methods=['GET', 'POST'])
def ticket_page():
    if request.method == 'POST':
        data = request.get_json()
        tickets.append(data)
        return jsonify({"message": "Ticket submitted successfully!"}), 200
    return render_template('ticket.html')

@app.route('/admin', methods=['GET'])
def admin_dashboard():
    return render_template('admin.html', tickets=tickets)

@app.route('/respond_ticket/<int:ticket_id>', methods=['POST'])
def respond_ticket(ticket_id):
    response = request.get_json()
    if ticket_id < len(tickets):
        tickets[ticket_id]['response'] = response['message']
        return jsonify({"message": "Response added!"}), 200
    return jsonify({"message": "Ticket not found!"}), 404

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
