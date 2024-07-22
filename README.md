# django-asserts

## Overview
Test HTML with Context Managers

### Example

```python

from django.test import TestCase
from django_asserts import AssertHTMLMixin

class MyTest(TestCase, AssertHTMLMixin):

    def test_view(self):
        self.assertHTML(response, "#id-element"):
```


