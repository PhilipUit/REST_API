import flask 
from flask import jsonify
from jobs_core import API




app = flask.Flask(__name__)
app.config["DEBUG"] = True


#Endpoints
@app.route('/', methods=['GET'])
def home():
    endpoints = {
        "status": "/status",
        "status ID": "/status/ID",
        "DAG": "/dags/ID",
        "connections": "/connections/ID"
    }
    return jsonify(endpoints)


@app.route('/status', methods=['GET'])
def status():

#    x = API.Factory('jobstatus', {"id":id})

#    if(x.errorcode == 200):
#        return(jsonify(x.json()))
#    elif(x.errorcode == 400):
#        abort(400, 'Bad Request')
#    elif(x.errorcode == 401):
#        abort(401, 'Unauthorized')
#    elif(x.errorcode == 403):
#        abort(403, 'Forbidden')
#    elif(x.errorcode == 404):
#        abort(404, 'Not Found')

    return('Status')

@app.route('/status/<id>', methods=['GET'])
def ID(id):
    print('I am in API with job {}'.format(id))
    return(API.Factory(call='Job Status', args={'ID':id}))

@app.route('/dags/<id>', methods=['GET'])
def DAG(id):
    return(API.Factory(call='status2', args={'ID':id}))

@app.route('/connections/<id>', methods=['GET'])
def connections(id):
    return(API.Factory(call='status1', args={'ID':id}))




app.run()