from django.test import TestCase
from queries.queries_app.models import Person


class QueriesTestCase(TestCase):

    # Test methods:

    def test_trivial_query(self):

        p = Person(first_name="A", last_name="B")
        p.save()

        query = Person.objects.all()
        results = list(query)

        self.assertEqual(len(results), 1)
