import json

import psycopg2
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/add-providers', methods=['GET'])
def add_providers():
    provider_name = request.args.get('provider_name')
    srate = request.args.get('srate')
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="CineStreamMonolith",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()

    # Insert new user into the users table
    sql = "INSERT INTO provider (provider_name, srate) VALUES (%s, %s)"
    values = (provider_name, srate)
    cur.execute(sql, values)

    conn.commit()
    cur.close()
    conn.close()
    return jsonify("added")


@app.route('/add-contents', methods=['GET'])
def add_contents():
    id = request.args.get('content_id')
    name = request.args.get('content_name')
    des = request.args.get('content_des')
    srate = request.args.get('srate')
    provider = request.args.get('provider')
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="CineStreamMonolith",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()

    # Insert new user into the users table
    sql = "INSERT INTO content (content_id, content_name, content_des, srate, provider) VALUES (%s, %s, %s, %s, %s)"
    values = (id, name, des, srate, provider)
    cur.execute(sql, values)

    conn.commit()
    cur.close()
    conn.close()
    return jsonify("added")


@app.route('/get-all-contents', methods=['GET'])
def get_all_contents():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="CineStreamMonolith",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM content")
    rows = cur.fetchall()
    filtered_rows = [row for row in rows]
    if len(filtered_rows) == 0:
        return None
    contents = [dict(zip(('content_id', 'content_name', 'content_des', 'srate', 'provider'), row)) for row in filtered_rows]
    cur.close()
    conn.close()
    for content in contents:
        content["srate"] = str(content["srate"])

    print(contents)
    return jsonify(contents)


@app.route('/get-user-contents', methods=['GET'])
def get_user_contents():
    user_email = request.args.get("user_email")
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="CineStreamMonolith",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()

    cur.execute("SELECT * FROM user_subscription_content")
    rows = cur.fetchall()
    filtered_rows = [row for row in rows if row[0] == user_email]
    if len(filtered_rows) == 0:
        return None
    contents = [dict(zip(('email', 'content_id'), row)) for row in filtered_rows]

    content_ids = [content["content_id"] for content in contents]
    res = requests.get("http://127.0.0.1:9010/get-all-contents")
    res = json.loads(res.text)
    contents = []
    for item in res:
        if item["content_id"] in content_ids:
            contents.append(item)

    for content in contents:
        content["srate"] = str(content["srate"])
    res = {"email": user_email, "subscribed_contents": contents}

    cur.close()
    conn.close()

    print(res)
    return jsonify(res)


if __name__ == "__main__":
    app.run("0.0.0.0", port=9010, debug=True, threaded=True, use_reloader=False)
