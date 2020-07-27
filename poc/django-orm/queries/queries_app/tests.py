from datetime import date
from django.test import TestCase
from queries.queries_app.models import Player, Team, Positions


class QueriesTestCase(TestCase):

    # Setup:

    def setUp(self):
        self.team1 = Team(name="Sakalai")
        self.team1.save()
        self.team1_player1 = Player(first_name="Rolandas", last_name="Matulis", height=200,
                                    weight=120, date_of_birth=date(1970, 1, 1),
                                    position=Positions.CN)
        self.team1_player1.save()
        self.team1_player2 = Player(first_name="Rolandas", last_name="Skaisgirys",
                                    height=190, weight=90, date_of_birth=date(1970, 1, 1),
                                    position=Positions.SG)
        self.team1_player2.save()
        self.team1_player3 = Player(first_name="Justas", last_name="Sinica",
                                    height=200, weight=120, date_of_birth=date(1970, 1, 1),
                                    position=Positions.SF)
        self.team1_player3.save()

    # Test methods:

    def test_trivial_query(self):

        query = Player.objects.all()
        results = list(query)

        self.assertEqual(len(results), 3)
