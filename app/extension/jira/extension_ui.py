import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS


"""def view_cloud_report(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_specific_report_view")
    def measure():
        def app_specific_user_login(username='admin', password='admin'):
            login_page = Login(webdriver)
            login_page.delete_all_cookies()
            login_page.go_to()
            login_page.set_credentials(username=username, password=password)
            if login_page.is_first_login():
                login_page.first_login_setup()
            if login_page.is_first_login_second_page():
                login_page.first_login_second_page_setup()
            login_page.wait_for_page_loaded()
        app_specific_user_login(username='admin', password='admin')
        page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/HealthCheckUIAction!Report.jspa")
        page.wait_until_visible((By.ID, "mainReport"))  # Wait for report to load up 
    measure()


def view_report_config(webdriver, datasets):
    page = BasePage(webdriver)
    
    @print_timing("selenium_app_specific_config_view")
    def measure():
        def app_specific_user_login(username='admin', password='admin'):
            login_page = Login(webdriver)
            login_page.delete_all_cookies()
            login_page.go_to()
            login_page.set_credentials(username=username, password=password)
            if login_page.is_first_login():
                login_page.first_login_setup()
            if login_page.is_first_login_second_page():
                login_page.first_login_second_page_setup()
            login_page.wait_for_page_loaded()
        app_specific_user_login(username='admin', password='admin')
        page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/HealthCheckUIAction.jspa")
        page.wait_until_visible((By.ID, "report-config-form")) 
    measure()


def view_refresh_report(webdriver, datasets):
    page = BasePage(webdriver)
    
    @print_timing("selenium_app_specific_view_refresh_report")
    def measure():
        def app_specific_user_login(username='admin', password='admin'):
            login_page = Login(webdriver)
            login_page.delete_all_cookies()
            login_page.go_to()
            login_page.set_credentials(username=username, password=password)
            if login_page.is_first_login():
                login_page.first_login_setup()
            if login_page.is_first_login_second_page():
                login_page.first_login_second_page_setup()
            login_page.wait_for_page_loaded()
        app_specific_user_login(username='admin', password='admin')
        page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/HealthCheckUIAction!Report.jspa")
        page.wait_until_visible((By.ID, "mainReport"))
        webdriver.find_element_by_id("refreshReport").click()
        page.wait_until_visible((By.ID, "generate")) 
    measure()"""

