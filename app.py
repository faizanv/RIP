from flask import Flask, render_template, request, send_from_directory, send_file
from rip import rip, removeFile

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
    rip(param)
    # retval = send_from_directory('./', param["filename"] + ".wav", mimetype="audio/wav")
    # print "Value of return"
    # print retval
    # return send_file("/Users/faizanv/dev/RIP/static/logo.png", attachement_filename="logo.png")
    # path_to_file = "./dance.wav"
    # return send_file(
    #      path_to_file,
    #      mimetype="audio/wav",
    #      as_attachment=True,
    #      attachment_filename="dance.wav")
    return "/download/" + param["filename"] + ".wav"

@app.route("/download/<file>")
def download(file):
    retval = send_file("./output/" + file, attachment_filename=file, mimetype='application/octet-stream')
    removeFile(file)
    return retval

if __name__ == "__main__":
    app.run(debug=False)
