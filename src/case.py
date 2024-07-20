from django.test import TestCase as DjangoTestCase

from .mixins import AssertHTMLMixin

__all__ = ["TestCase"]


class TestCase(DjangoTestCase, AssertHTMLMixin):
    pass
