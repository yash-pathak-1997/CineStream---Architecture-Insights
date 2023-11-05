import json
import psycopg2
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/subscribe-contents', methods=['GET'])
def subscribe_contents():
    user_email = request.args.get('user_email')
    content_id = request.args.get('content_id')
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="CineStreamMonolith",
        user="postgres",
        password="postgres"
    )

    # Checking if content present
    cur = conn.cursor()
    rows = requests.get("http://127.0.0.1:9010/get-all-contents")
    rows = json.loads(rows.text)
    filtered_rows = [row for row in rows if row["content_id"] == content_id]
    if len(filtered_rows) == 0:
        return "No such content!"

    # Checking if content present
    cur = conn.cursor()
    rows = requests.get("http://127.0.0.1:9010/get-all-contents")
    rows = json.loads(rows.text)
    filtered_rows = [row for row in rows if row["content_id"] == content_id]
    if len(filtered_rows) == 0:
        return "No such content!"

    # Checking if content already subscribed
    params = {"user_email": user_email}
    rows = requests.get("http://127.0.0.1:9010/get-user-contents", params=params)
    print(rows.text)
    rows = json.loads(rows.text)
    filtered_rows = [row for row in rows["subscribed_contents"] if row["content_id"] == content_id]
    if len(filtered_rows) != 0:
        return "Content Already Subscribed!"

    # Checking if content already subscribed
    params = {"user_email": user_email}
    rows = requests.get("http://127.0.0.1:9010/get-user-contents", params=params)
    print(rows.text)
    rows = json.loads(rows.text)
    filtered_rows = [row for row in rows["subscribed_contents"] if row["content_id"] == content_id]
    if len(filtered_rows) != 0:
        return "Content Already Subscribed!"

    # Insert new user into the users table
    sql = "INSERT INTO user_subscription_content (user_email, content_id) VALUES (%s, %s)"
    values = (user_email, content_id)
    cur.execute(sql, values)

    conn.commit()
    cur.close()
    conn.close()
    return jsonify("subscription added!")


if __name__ == "__main__":
    app.run("0.0.0.0", port=9020, debug=True, threaded=True, use_reloader=False)
