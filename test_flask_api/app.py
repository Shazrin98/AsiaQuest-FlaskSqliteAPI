from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Optional pagination parameters with offset
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 20))
    offset = (page - 1) * limit
    
    # Retrieve users based on pagination parameters
    users = cursor.execute('SELECT * FROM users LIMIT ? OFFSET ?', (limit, offset)).fetchall()
    
    conn.close()
    
    users_list = [dict(user) for user in users]
    return jsonify(users_list)

# Only run flask in this module
if __name__ == '__main__':
    app.run(debug=True)
