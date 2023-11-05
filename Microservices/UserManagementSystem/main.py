import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('user_name')
    password = request.args.get('user_pass')
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="CineStreamMonolith",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    filtered_rows = [row for row in rows if row[0] == username]
    if len(filtered_rows) == 0:
        return None
    user_data = [dict(zip(('username', 'password', 'email'), row)) for row in filtered_rows]
    user_data = user_data[0]
    cur.close()
    conn.close()

    if user_data and user_data['password'] == password:
        return jsonify(True)
    return jsonify(False)


@app.route('/signup', methods=['GET'])
def signup():
    username = request.args.get('user_name')
    password = request.args.get('user_pass')
    email = request.args.get('user_email')
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="CineStreamMonolith",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()

    # Insert new user into the users table
    sql = "INSERT INTO users (user_name, user_pass, user_email) VALUES (%s, %s, %s)"
    values = (username, password, email)
    cur.execute(sql, values)

    conn.commit()
    cur.close()
    conn.close()
    return jsonify("added")


if __name__ == "__main__":
    app.run("0.0.0.0", port=9030, debug=True, threaded=True, use_reloader=False)
