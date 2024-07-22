from .soupselect import select
from bs4 import BeautifulSoup as Soup


class HTMLNotPresent(AssertionError):
    pass


class SelectorNotFound(HTMLNotPresent):
    pass


class ElementIDNotFound(HTMLNotPresent):
    pass


class AssertHTMLContext(object):
    def __init__(self, response, test_case, selector, element_id, status_code, msg):
        self.response = response
        self.test_case = test_case
        self.status_code = status_code
        self.element_id = element_id
        self.selector = selector
        self.test_case.assertEqual(self.response.status_code, self.status_code)
        html = Soup(self.response.content)
        if self.selector is not None:
            elements = select(html, self.selector)
            if len(elements) == 0:
                raise SelectorNotFound(
                    "No selector matches found for {0}".format(self.selector)
                )
        if self.element_id is not None:
            try:
                return select(html, self.element_id)
            except KeyError:
                raise ElementIDNotFound(
                    "Element with id, {0}, not present".format(self.element_id)
                )

    def __exit__(self, exc_type, exc_value, tb):
        pass
