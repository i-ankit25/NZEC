from flask import Flask, jsonify, request
import os
app = Flask(__name__)

# @app.route("/", methods = ['GET', 'POST'])
# def index():
#     if(request.method == 'POST'):
#         some_json = request.get_json()
#         print(some_json)
#         return jsonify ({"you sent" : some_json}), 201
#     else:
#         return jsonify({"about":"hello world!"})

@app.route('/', methods = ['POST'])
def changeEnv():
    some_json = request.get_json()
    value = some_json[u'val']
    if(value == 1):
        while(os.getenv("CURRENT") !=  "0"):
            try:
                os.environ["CURRENT"] = "0"
            except: pass
    else:
        while(os.getenv("CURRENT") != "1"):
            try:
                os.environ["CURRENT"] = "1"
            except: pass
    return jsonify({"status":"changes made"})


if __name__ == '__main__':
    app.run(debug=True)