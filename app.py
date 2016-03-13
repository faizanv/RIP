from flask import Flask, render_template, request
import rip

app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ripit", methods=["POST"])
def ripit():
    content = request.get_json(silent=True)
    param = {}
    param["startTime"] = content.get('startTime')
    param["duration"] = content.get('duration')
    param["filename"] = content.get('filename')
    param["url"] = content.get('link')
    return rip.rip(param)

if __name__ == "__main__":
    app.run(debug=True)
