import time

import requests

import jenkins
import io
# def app_homepage(request):
#     return render(request, 'project.html')
JENKINS_URL = "http://localhost:8080/"
JENKINS_USERNAME = "yugeshbuchipalle"
JENKINS_PASSWORD = "Vijaya@238a"
# Jenkins API endpoint to get the build history
api_url = "http://localhost:8080/builds"

# Send a GET request to the Jenkins API
server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)
PARAMETERS = {}
TOKEN_NAME = "1234"
# job_name = "FT1 full testsuite"
# latest_build_info = server.get_job_info(job_name)['nextBuildNumber']
# print(latest_build_info)
job_name = "pytestpassinggit"
latest_build_info = server.get_job_info(job_name)

latest_build_info=server.get_job_config(job_name)
print(latest_build_info)
# server.build_job("s6",PARAMETERS,TOKEN_NAME)
# time.sleep(20)
# print("Latest build")


# job_name = "pytestpassinggit"
# latest_build_info = server.get_job_info(job_name)['lastBuild']['number']
# print(latest_build_info)
progress = server.get_build_info(job_name,latest_build_info)["inProgress"]
print(progress)
while(progress==True):
  progress = server.get_build_info(job_name,latest_build_info)["inProgress"]
  print(progress)
  print(server.get_build_info(job_name,latest_build_info)["id"])
#
#
# result = server.get_build_test_report(job_name,latest_build_info)
# print(result)
# print(result['passCount'])
# print(result['failCount'])
# percentage = (result['passCount']/(result['passCount']+result['failCount']))*100
# print(percentage)
# l= []
# for i in result['suites'][0]['cases']:
#     l.append([i['name'],i['status']])
# print(l)






# Extract build details
# build_number = latest_build_info['number']
# build_result = latest_build_info['result']
# build_timestamp = latest_build_info['timestamp']
#
# print(build_number)
# print(build_result)
# print(build_timestamp)







# for build in builds_data:
#     build_number = build['number']
#     build_status = build['result']
#     build_url = build['url']
#
#     print(f"Build Number: {build_number}")
#     print(f"Status: {build_status}")
#     print(f"Build URL: {build_url}")
#     print("-" * 50)
# print(server.get_running_builds())
# a = server.build_job("s6", PARAMETERS, TOKEN_NAME)
# print(a)
# print(server.build_job("s6"))
# if response.status_code == 200:
#     data = response.json()
#     print(data)
#     jobs = data.get('jobs', [])
#
#
# else:
#     print(f"Failed to fetch build history. Status code: {response.status_code}")
a= [['test_add_positive_numbers', 'PASSED'], ['test_add_negative_numbers', 'PASSED'], ['test_add_mixed_numbers', 'PASSED'], ['test_new', 'PASSED'], ['test_fail', 'FAILED']]
d = {}
for i in a:
  print(i)
