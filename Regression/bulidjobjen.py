import jenkins
import time
# It comes with pip module python-jenkins
# use pip to install python-jenkins

# Jenkins Authentication URL
JENKINS_URL = "http://localhost:8080/"
JENKINS_USERNAME = "yugeshbuchipalle"
JENKINS_PASSWORD = "Vijaya@238a"


class DevOpsJenkins:
    def __init__(self):
        self.jenkins_server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)
        user = self.jenkins_server.get_whoami()
        version = self.jenkins_server.get_version()
        print ("Jenkins Version: {}".format(version))
        print ("Jenkins User: {}".format(user['id']))

    def build_job(self, name, parameters=None, token=None):
        # next_build_number = self.jenkins_server.get_job_info(name)['nextBuildNumber']
        # self.jenkins_server.build_job(name, parameters=parameters, token=token)
        # time.sleep(10)
        # build_info = self.jenkins_server.get_build_info(name, next_build_number)
        # self.jenkins_server.create_job('firstjenkinsfile', jenkins.EMPTY_CONFIG_XML)
        print(jenkins.BUILD_WITH_PARAMS_JOB)
        # return build_info


if __name__ == "__main__":
    NAME_OF_JOB = "firstjava"
    TOKEN_NAME = "1234"
    # Example Parameter
    # PARAMETERS = {'project': 'devops'}
    PARAMETERS = {}
    jenkins_obj = DevOpsJenkins()
    output = jenkins_obj.build_job(NAME_OF_JOB, PARAMETERS, TOKEN_NAME)
    # print ("Jenkins Build URL: {}".format(output['url']))