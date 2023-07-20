import allure
from allure_commons.types import Severity
from selene import browser
from selene.support import by
from selene.support.conditions import be
from selene.support.shared.jquery_style import s


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'shandrokha')
@allure.story('Repository search')
@allure.link('https://github.com', name='Testing')
def test_decorator_steps():
    open_main_page()
    search_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    issue_with_number_visibile("#81")
    close_browser()


@allure.step("Open main page")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Search needed {repo}")
def search_repository(repo):
    s('[data-target="qbsearch-input.inputButtonText"]').click()
    s('[id = "query-builder-test"]').send_keys(repo)
    s('[id = "query-builder-test"]').submit()


@allure.step("Click on the {repo} link")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Open 'Issue' tab")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Check Issue with {number} is present")
def issue_with_number_visibile(number):
    s(by.partial_text(number)).should(be.visible)


@allure.step("Close browser")
def close_browser():
    browser.quit()
