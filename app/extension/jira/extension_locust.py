import re
from locustio.common_utils import init_logger, jira_measure, run_as_specific_user  # noqa F401
from util.conf import JIRA_SETTINGS

logger = init_logger(app_type='jira')

"""@jira_measure("locust_app_specific_run_report")
@run_as_specific_user(username='admin', password='admin')  # run as specific user
def run_report(locust):
    r = locust.get(f"{JIRA_SETTINGS.server_url}/rest/healthcheckjirareporter/latest/run/start", catch_response=True) 
    content = r.content.decode('utf-8')   # decode response content
    statusCode = r.status_code
    assert (content == "{\"status\":\"RUNNING\"}") or (status_code == 500)"""

@jira_measure("locust_app_specific_check_report_status")
@run_as_specific_user(username='admin', password='admin') 
def check_report_status(locust):
    r = locust.get(f"{JIRA_SETTINGS.server_url}/rest/healthcheckjirareporter/latest/run/status", catch_response=True) 
    statusCode = r.status_code
    assert statusCode == 200

@jira_measure("locust_app_specific_get_config")
@run_as_specific_user(username='admin', password='admin') 
def get_config(locust):
    r = locust.get(f"{JIRA_SETTINGS.server_url}/rest/healthcheckjirareporter/latest/config/get", catch_response=True) 
    statusCode = r.status_code 
    assert statusCode == 200

@jira_measure("locust_app_specific_post_config")
@run_as_specific_user(username='admin', password='admin') 
def post_config(locust):
    body = {"user": "admin", "restCalls": "true"} 
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    r = locust.post(f"{JIRA_SETTINGS.server_url}/rest/healthcheckjirareporter/latest/config/post", body, headers, catch_response=True) 


@jira_measure("locust_app_specific_check_config_change")
@run_as_specific_user(username='admin', password='admin') 
def check_config_change(locust):
    r = locust.get(f"{JIRA_SETTINGS.server_url}/rest/healthcheckjirareporter/latest/config/isChanged", catch_response=True) 
    statusCode = r.status_code 
    assert statusCode == 200

"""@jira_measure("locust_app_specific_get_pdf")
@run_as_specific_user(username='admin', password='admin') 
def get_pdf(locust):
    r = locust.get(f"{JIRA_SETTINGS.server_url}/rest/healthcheckjirareporter/latest/pdf", catch_response=True) 
    statusCode = r.status_code 
    assert statusCode == 200"""