import requests

# Replace with your Jenkins server URL and credentials
jenkins_url = 'http://localhost:8080/'
username = 'yugeshbuchipalle'
password = 'Vijaya@238a'

# Jenkins API endpoint to get the build history
api_url = f"{jenkins_url}/api/json?tree=jobs[name,builds[number,result,timestamp,duration]]"
api_url =f"{jenkins_url}/job/s6/api/json"
response = requests.get(api_url, auth=(username, password))
data = response.json()['nextBuildNumber']


print(data)


if response.status_code == 200:
    data = response.json()
    jobs = data.get('jobs', [])

    for job in jobs:
        job_name = job['name']
        builds = job['builds']

        print(f"Job: {job_name}")

        for build in builds:
            build_number = build['number']
            build_result = build['result']
            build_timestamp = build['timestamp']
            build_duration = build['duration']

            print(f"Build Number: {build_number}")
            print(f"Status: {build_result}")
            print(f"Timestamp: {build_timestamp}")
            print(f"Duration: {build_duration} milliseconds")
            print("-" * 50)

else:
    print(f"Failed to fetch build history. Status code: {response.status_code}")
