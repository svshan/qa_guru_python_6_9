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

def test_github():
    with allure.step("Open main page"):
        browser.open("https://github.com")

    with allure.step("Search needed repository"):
        s('[data-target="qbsearch-input.inputButtonText"]').click()
        s('[id = "query-builder-test"]').send_keys("eroshenkoam/allure-example")
        s('[id = "query-builder-test"]').submit()

    with allure.step("Click on the repository link"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Open 'Issue' tab"):
        s("#issues-tab").click()

    with allure.step("Check Issue with 81 number is present"):
        s(by.partial_text("#81")).should(be.visible)