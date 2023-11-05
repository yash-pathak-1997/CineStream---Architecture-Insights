from flask import Flask, render_template, redirect, url_for
import content_dao
import sqlalchemy as sa
import sys
import json


with open('./config.json') as con_file:
    config_dict = json.load(con_file)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = sa.engine.URL.create(
    drivername="postgresql",
    username=config_dict['username'],
    password=config_dict['password'],
    host=config_dict['host'],
    database=config_dict['database'],
)

content_dao.db.init_app(app)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/netflix')
def netflix():
    content = content_dao.query_platform('netflix')
    content['platform'] = 'Netflix'
    return render_template('platform.html', content=content)


@app.route('/prime')
def prime():
    content = content_dao.query_platform('prime')
    content['platform'] = 'Amazon Prime Video'
    return render_template('platform.html', content=content)


@app.route('/hotstar')
def hotstar():
    content = content_dao.query_platform('hotstar')
    content['platform'] = 'Disney+ Hotstar'
    return render_template('platform.html', content=content)


@app.route('/stream_video/<int:item_id>')
def stream_video(item_id):
    has_access = content_dao.check_access(item_id)
    if has_access:
        content = content_dao.query_id(item_id)
        return render_template('stream.html', content=content)
    return redirect(url_for('payment', item_id=item_id, paid=0))


@app.route('/payment/<int:item_id>/<int:paid>')
def payment(item_id, paid):
    if paid == 1:
        content_dao.grant_access(item_id)
        return redirect(url_for('stream_video', item_id=item_id))
    content = content_dao.query_id(item_id)
    return render_template('payment.html', content=content)


@app.route('/loadbalancer')
def loadbalancer():
    return "Response from server: " + sys.argv[1]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid arguments: python <filename> <port no>")
        sys.exit()

    app.run(host='localhost', port=int(sys.argv[1]), debug=True)
