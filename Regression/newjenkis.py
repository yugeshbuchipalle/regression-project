import jenkins
JENKINS_URL = "http://localhost:8080/"
JENKINS_USERNAME = "yugeshbuchipalle"
JENKINS_PASSWORD = "Vijaya@238a"
server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)
job_name = 'katalon_automation1'
job_config = """<?xml version='1.1' encoding='UTF-8'?>
<project>
  <actions/>
  <description></description>
  <keepDependencies>false</keepDependencies>
  <properties/>
  <scm class="hudson.scm.NullSCM"/>
  <canRoam>true</canRoam>
  <disabled>false</disabled>
  <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
  <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
  <authToken>1234</authToken>
  <triggers/>
  <concurrentBuild>false</concurrentBuild>
  <builders>
    <com.katalon.jenkins.plugin.ExecuteKatalonStudioTask plugin="katalon@1.0.34">
      <version>8.6.6</version>
      <location></location>
      <executeArgs>-projectPath=&quot;C:\\Users\\yuges\\Katalon Studio\\inception\\inception.prj&quot; -retry=0 -testSuitePath=&quot;Test Suites/FT1&quot; -browserType=&quot;Chrome&quot; -executionProfile=&quot;default&quot; -apiKey=&quot;5f791d0c-405a-4379-9031-05160a22f82e&quot; --config -proxy.auth.option=NO_PROXY -proxy.system.option=NO_PROXY -proxy.system.applyToDesiredCapabilities=true</executeArgs>
      <x11Display></x11Display>
      <xvfbConfiguration></xvfbConfiguration>
    </com.katalon.jenkins.plugin.ExecuteKatalonStudioTask>
  </builders>
  <publishers/>
  <buildWrappers/>
</project>"""

# Create the Jenkins job
# server.create_job(job_name, job_config)
PARAMETERS = {}
TOKEN_NAME = "1234"
job_name = "s6"
# server.build_job(job_name,PARAMETERS,TOKEN_NAME)
print(server.get_job_config(job_name))