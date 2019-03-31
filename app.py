import flask
from flask import request, jsonify, make_response, abort

# import imp
from sklearn.externals import joblib

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.testing = True


@app.route('/', methods=['GET'])
def home():
    return make_response(jsonify({'test': 'Test'}), 200)

@app.errorhandler(404)
def page_not_found(e):
    return make_response(jsonify({'error': 'Not found'}), 404)

# @app.route('/predictDylexia', methods=['POST'])
# def create_task():
    
#     # print(request.json)
#     if request.json['type'] == 1:
#          knn = joblib.load('model47.joblib')
#     elif request.json['type'] == 2:
#          knn = joblib.load('model89.joblib')
#     knn = joblib.load('model47.joblib')
#     resultArr = knn.predict([[request.json['GenBackground'],request.json['FRBackground'],request.json['DSMT1'],request.json['DSMT2'],request.json['DSMT3'],request.json['DSMT4'],request.json['BGT'],request.json['DMWT']]])
#     result = str(resultArr[0])


#     print("sucess")
#     return jsonify({'isDylexia': result}), 200



app.run()