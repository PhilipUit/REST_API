class StubAirflow():
    @staticmethod
    def PushJob(args=None):
        return("I pushed a job")

    @staticmethod
    def JobStatus(args=None):
        print('I am in Airflow with job {}'.format(args['ID']))
        return("Job {} completed successfully".format(args["ID"]))
        
