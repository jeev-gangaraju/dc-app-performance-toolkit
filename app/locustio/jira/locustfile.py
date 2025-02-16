from locust import HttpUser, task, between
from locustio.jira.http_actions import login_and_view_dashboard, create_issue, search_jql, view_issue, \
    view_project_summary, view_dashboard, edit_issue, add_comment, browse_boards, view_kanban_board, view_scrum_board, \
    view_backlog, browse_projects
from locustio.common_utils import LocustConfig, MyBaseTaskSet
from extension.jira.extension_locust import check_report_status, get_config, check_config_change, post_config
from util.conf import JIRA_SETTINGS

config = LocustConfig(config_yml=JIRA_SETTINGS)


class JiraBehavior(MyBaseTaskSet):

    def on_start(self):
        self.client.verify = config.secure
        login_and_view_dashboard(self)

    @task(config.percentage('create_issue'))
    def create_issue_action(self):
        create_issue(self)

    @task(config.percentage('search_jql'))
    def search_jql_action(self):
        search_jql(self)

    @task(config.percentage('view_issue'))
    def view_issue_action(self):
        view_issue(self)

    @task(config.percentage('view_project_summary'))
    def view_project_summary_action(self):
        view_project_summary(self)

    @task(config.percentage('view_dashboard'))
    def view_dashboard_action(self):
        view_dashboard(self)

    @task(config.percentage('edit_issue'))
    def edit_issue_action(self):
        edit_issue(self)

    @task(config.percentage('add_comment'))
    def add_comment_action(self):
        add_comment(self)

    @task(config.percentage('browse_projects'))
    def browse_projects_action(self):
        browse_projects(self)

    @task(config.percentage('view_kanban_board'))
    def view_kanban_board_action(self):
        view_kanban_board(self)

    @task(config.percentage('view_scrum_board'))
    def view_scrum_board_action(self):
        view_scrum_board(self)

    @task(config.percentage('view_backlog'))
    def view_backlog_action(self):
        view_backlog(self)

    @task(config.percentage('browse_boards'))
    def browse_boards_action(self):
        browse_boards(self)

    """@task(config.percentage('run_report'))
    def run_report_action(self):
        run_report(self)"""

    @task(config.percentage('report_status'))
    def check_report_status_action(self):
        check_report_status(self)

    @task(config.percentage('get_config'))
    def get_config_action(self):
        get_config(self)

    @task(config.percentage('config_changed'))
    def check_config_change_action(self):
        check_config_change(self)

    """@task(config.percentage('get_pdf'))
    def get_pdf_action(self):
        get_pdf(self)"""

    @task(config.percentage('post_config'))
    def post_config_action(self):
        post_config(self)

    
class JiraUser(HttpUser):
    host = JIRA_SETTINGS.server_url
    tasks = [JiraBehavior]
    wait_time = between(0, 0)