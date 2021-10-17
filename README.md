# REST_API
REST API using Flask, triggering workflow DAGs in Apache Airflow upon request; while CouchDB allows end user application to query the state of request via API and the scripts in Airflow update their status triggered by REST calls in the workflow with Dockers 

- Please see README.pdf for more details & images to better explain process (attached)

#### 1. jobs_airflow.py
- Lines 3-12 demonstrate a stubbed class to be able run static method used in PushJob & JobStatus. This will populate in the terminal as we run them, shown below in this documentation.
- Lines 15-22 create a class, Airflow, and establishes how to enter host, port, user, and password required.
- Currently lines 24-27 are not passing through to an active endpoint
- Using the Apache Airflow documentation:https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-apiref.html -- we see in Lines 29-37 that we are able to connect endpoints using “/api/v1/dags/{}” & “/api/v1/dags/{}/dagRuns”. We will demonstrate how to connect to these endpoints using the browser below. 
#### 2. jobs_api.py
- We start by importing packages in lines 1-3
- Lines 6-7 are setting up flask
- Lines 10-21 are the active endpoints. Note some are for testing purposes.
- Lines 24-45 show the error codes that should populate given the status of running the endpoints. They are still commented out and not implemented.
- Lines 47-61 demonstrate the different tests of endpoints using the ID and various status/connections.
- Lines 63-66 demonstrate a Dag Run w/ ID calling ‘GetDag’. This is a successful endpoint connecting to ApacheAirflow.
- Lines 68-72 demonstrate Triggering a Dag Run calling ‘PostDag’. This is a successful endpoint connecting to Apache Airflow.
- Line 74 runs the application.
#### 3. jobs_dummy.py
- this script is used to pass static methods for ‘status1’ and ‘status2’ through to the other scripts. This is used to demonstrate our test endpoints and to verify things work during testing.
#### 4. jobs_core.py
- we start by importing the jobs_dummy.py and jobs_airflow.py scripts (demonstrated above) in lines 1 & 2
- using the static Factory method we generate to make calls to connect to in lines 6-29
- Lines 11-14 connect to jobs_dummy.py and link to Status1 & Status2
- Line 15-17 passes the CouchDB, but is not implemented yet
- Lines 19-29 connect to the jobs_airlfow.py file passing through calls for ‘Submit Job’ ‘Job Status’ ‘GetDag’ and ‘PostDag’ --- please note that the ‘GetDag’ and ‘PostDag’ are able to connect to Apache Airflow endpoints.
#### How to stand-up Deployment Docker 
- locate correct filepath ex) >C:\AirFlow\ak-docker-transform\deployment 
- > RUN >> docker-compose-up -d
- Please see README.pdf (attached for more details)
#### How to test endpoints
Make sure you are in the REST API folder of Philip-Branch-2 using cd:
- Then run >> python3 jobs_api.py 
- Clicking on the url: http://127.0.0.1:5000/ brings us to our endpoints:
- Please see README.pdf (attached for more details)
#### Connecting Endpoint to Airflow 
- This endpoint allows us to connect to Airflow. Due to Airflow being complicated, it shows as ‘unauthorized’, but we are connected to it.
- http://127.0.0.1:5000/api/v1/dags/ID/dagRuns
#### Problem:
• This is not unauthorized due to Airflow being difficult
• it works but is not connected
#### Solution:
• Airflow can be tricky and challenging here
• Download updated deployment folder over current one if not updated
• Create new entrypoint.sh file with the line >> cp scripts/airflow.cfg airflow.cfg and the
new airflow.cfg file in the scripts folder
