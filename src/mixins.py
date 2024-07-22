from .context_manager import AssertHTMLContext, HTMLNotPresent


__all__ = ["AssertHTMLMixin"]


class AssertHTMLMixin(object):
    def assertHTML(
        self,
        response,
        selector=None,
        element_id=None,
        expected=None,
        status_code=200,
        msg=None,
    ):
        context = AssertHTMLContext(
            response,
            test_case=self,
            selector=selector,
            element_id=element_id,
            status_code=status_code,
            msg=msg,
        )
        return context

    def assertNotHTML(self, *args, **kwargs):
        try:
            with self.assertHTML(*args, **kwargs) as html:
                raise self.failureException(
                    "Found unexpected content: {0}".format(html)
                )
        except HTMLNotPresent:
            pass
