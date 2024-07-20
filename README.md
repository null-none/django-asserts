# django-asserts

## Overview
Test HTML with Context Managers

### Example

```python

from django.test import TestCase
from with_asserts import AssertHTMLMixin

class MyTest(TestCase, AssertHTMLMixin):

    def test_view(self):
        with self.assertHTML(resp, 'input[name="email"]') as (elem,):
            self.assertEqual(elem.value, 'bob@example.com')
```


