from flask import Flask, render_template, request, jsonify, make_response
from chatgui import chatbot_response
app=Flask(__name__)
@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)
@app.get("/")
def index_get():
    return make_response(render_template("base.html"))
@app.post("/predict")
def predict():
    text=request.get_json().get("message")
    response=chatbot_response(text)
    message={"answer": response}
    return jsonify(message)
if __name__=="__main__":
    app.run(debug=True)
