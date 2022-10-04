from flask import Flask, jsonify, request

import json

app = Flask(__name__)

glucose = [
    {
        "glucose_id": 1,
        "date" : "October/12/2022",
        "glucose" : "100mg"
    },

    {
        "glucose_id": 2,
        "date" : "October/12/2022",
        "glucose" : "92mg"
    }
]
@app.route('/glucose', methods=['POST'])
def addGlucose():
    glu = request.get_json()
    glucose.append(glu)
    return {'id':len(glucose)}, 200

@app.route('/glucose', methods=['GET'])
def displayGlucose():
    return jsonify(glucose)

@app.route('/glucose/<int:index>', methods=['GET'])
def getGlucose(index):
    if index < len(glucose):
        return jsonify(glucose[index]), 200
    else:
        return "Glucose id not found", 404

@app.route('/glucose/<int:index>', methods=['POST'])
def updateGlucose(index):
    glu = request.get_json()
    glucose.pop(index)
    glucose.append(glu)
    return f"Successfully updated glucose_id {index}", 200

@app.route('/glucose/<int:index>', methods=['DELETE'])
def deleteGlucose(index):
    glucose.pop(index)
    return "Glucose successfully deleted", 200

if __name__== '__main__':
    app.run()