import requests
import json
from requests.auth import HTTPBasicAuth
# Jenkins URL and job name
jenkins_url = 'http://192.168.1.9:8080/'
job_name = 's6'

# Jenkins API token
api_token = '11bdf5756a87b138187ecc70a45e6e04fa'
username = 'yugeshbuchipalle'
password = 'Vijaya@238a'
# Construct the API URL for the job
job_api_url = f'{jenkins_url}/job/{job_name}/api/json'
# job_api_url ='http://192.168.1.9:8080/builds'
print(job_api_url)
# Define headers for authentication
headers = {
    'Authorization': f'Bearer {api_token}'
}

# Send a GET request to the Jenkins API
# response = requests.get(job_api_url, headers=headers)
response = requests.get(job_api_url, auth=HTTPBasicAuth(username, password),headers=headers)

if response.status_code == 200:
    job_info = response.json()
    # Print build history
    for build in job_info['builds']:
        build_number = build['number']
        print(f'Build #{build_number}')
        print(build)
else:
    print(f'Error: {response.status_code} - {response.text}')