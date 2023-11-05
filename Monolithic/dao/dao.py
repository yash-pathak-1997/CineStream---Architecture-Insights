import json
import psycopg2


def get_user_dao(username):
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
    cur.close()
    conn.close()

    print(user_data)
    return user_data[0]


def create_user_dao(username, password, email):
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
    return "added"


def get_contents_dao():
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
    contents = [dict(zip(('name', 'desc', 'rate', 'provider'), row)) for row in filtered_rows]
    cur.close()
    conn.close()

    print(contents)
    return contents


def get_providers_dao():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="CineStreamMonolith",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM provider")
    rows = cur.fetchall()
    filtered_rows = [row for row in rows]
    if len(filtered_rows) == 0:
        return None
    providers = [dict(zip(('name', 'rate'), row)) for row in filtered_rows]
    cur.close()
    conn.close()

    print(providers)
    return providers


def create_provider_dao(provider_name, srate):
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
    return "added"


def create_content_dao(id, name, des, srate, provider):
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
    return "added"


def get_user_content_dao(user_email):
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
    query = "SELECT * FROM content WHERE content_id IN %s"
    cur.execute(query, (tuple(content_ids),))
    rows = cur.fetchall()
    filtered_rows = [row for row in rows]
    contents = [dict(zip(('content_id', 'content_name', 'content_des', 'srate', 'provider'), row)) for row in
                filtered_rows]
    res = {"email": user_email, "subscribed_contents": contents}

    cur.close()
    conn.close()

    print(res)
    return res


def user_subscribe_dao(user_email, content_id):
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="CineStreamMonolith",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM content")
    rows = cur.fetchall()
    filtered_rows = [row for row in rows if row[0] == content_id]
    if len(filtered_rows) == 0:
        return "no such content!"

    # Insert new user into the users table
    sql = "INSERT INTO user_subscription_content (user_email, content_id) VALUES (%s, %s)"
    values = (user_email, content_id)
    cur.execute(sql, values)

    conn.commit()
    cur.close()
    conn.close()
    return "subscription added!"
