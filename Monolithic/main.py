from api import app

if __name__ == "__main__":
    app.run("0.0.0.0", port=8080, debug=True, threaded=True, use_reloader=False)
