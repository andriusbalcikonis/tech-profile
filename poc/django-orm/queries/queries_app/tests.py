from datetime import date
from django.db.models import F
from django.test import TestCase
from queries.queries_app.models import Player, Team, Positions, Contract, Arena, Game, StatLine


class QueriesTestCase(TestCase):

    # Setup:

    def setUp(self):

        # Team1

        self.team1 = Team(name="Sakalai")
        self.team1.save()

        self.team1_arena = Arena(name="Sakalai homecourt")
        self.team1_arena.save()

        self.team1_player1 = Player(first_name="Rolandas", last_name="Matulis", height=200,
                                    weight=120, date_of_birth=date(1975, 1, 1),
                                    position=Positions.CN.value)
        self.team1_player1.save()
        Contract(player=self.team1_player1, team=self.team1, start_date=date(2000, 1, 1)).save()

        self.team1_player2 = Player(first_name="Rolandas", last_name="Skaisgirys",
                                    height=190, weight=90, date_of_birth=date(1975, 1, 1),
                                    position=Positions.SG.value)
        self.team1_player2.save()
        Contract(player=self.team1_player2, team=self.team1, start_date=date(2000, 1, 1)).save()

        self.team1_player3 = Player(first_name="Justas", last_name="Sinica",
                                    height=200, weight=120, date_of_birth=date(1980, 1, 1),
                                    position=Positions.SF.value)
        self.team1_player3.save()
        Contract(player=self.team1_player3, team=self.team1, start_date=date(2000, 1, 1)).save()

        # Team2

        self.team2 = Team(name="Lietuvos rinktine")
        self.team2.save()

        self.team2_arena = Arena(name="Zalgirio arena")
        self.team2_arena.save()

        self.team2_player1 = Player(first_name="Sarunas", last_name="Jaikevicius", height=190,
                                    weight=90, date_of_birth=date(1980, 1, 1),
                                    position=Positions.PG.value)
        self.team2_player1.save()
        Contract(player=self.team2_player1, team=self.team2, start_date=date(2000, 1, 1)).save()

        self.team2_player2 = Player(first_name="Arvydas", last_name="Sabonis",
                                    height=220, weight=120, date_of_birth=date(1970, 1, 1),
                                    position=Positions.CN.value)
        self.team2_player2.save()
        Contract(player=self.team2_player2, team=self.team2, start_date=date(2000, 1, 1)).save()

        self.team2_player3 = Player(first_name="Arvydas", last_name="Macijauskas",
                                    height=190, weight=85, date_of_birth=date(1980, 1, 1),
                                    position=Positions.SF.value)
        self.team2_player3.save()
        Contract(player=self.team2_player3, team=self.team2, start_date=date(2000, 1, 1)).save()

        # Game1

        self.game1 = Game(
            date=date(2005, 1, 1),
            arena=self.team2_arena,
            attendance=16000,
            final_score_home=120,
            final_score_away=70,
            home_team=self.team2,
            away_team=self.team1
        )
        self.game1.save()

        StatLine(game=self.game1, player=self.team1_player1, points=10, rebounds=3, assists=0).save()
        StatLine(game=self.game1, player=self.team1_player2, points=20, rebounds=12, assists=3).save()
        StatLine(game=self.game1, player=self.team1_player3, points=0, rebounds=0, assists=0).save()

        StatLine(game=self.game1, player=self.team2_player1, points=10, rebounds=3, assists=10).save()
        StatLine(game=self.game1, player=self.team2_player2, points=20, rebounds=23, assists=3).save()
        StatLine(game=self.game1, player=self.team2_player3, points=30, rebounds=0, assists=4).save()

        # Game2

        self.game2 = Game(
            date=date(2007, 1, 1),
            arena=self.team1_arena,
            attendance=6000,
            final_score_home=39,
            final_score_away=80,
            home_team=self.team1,
            away_team=self.team2
        )
        self.game2.save()

        StatLine(game=self.game2, player=self.team1_player1, points=12, rebounds=3, assists=0).save()
        StatLine(game=self.game2, player=self.team1_player2, points=22, rebounds=12, assists=3).save()
        StatLine(game=self.game2, player=self.team1_player3, points=2, rebounds=0, assists=0).save()

        StatLine(game=self.game2, player=self.team2_player1, points=12, rebounds=3, assists=10).save()
        StatLine(game=self.game2, player=self.team2_player2, points=22, rebounds=23, assists=3).save()
        StatLine(game=self.game2, player=self.team2_player3, points=32, rebounds=0, assists=4).save()

    # Test methods:

    def test_1_get_count(self):
        """
        For a warmup just get the count of players.
        """
        query = Player.objects.all()
        results = list(query)
        self.assertEqual(len(results), 6)

    def test_2_get_by_finding_one_record(self):
        """
        Get can work by finding by params
        """
        result = Player.objects.get(first_name="Arvydas", last_name="Sabonis")
        self.assertEqual(result.id, self.team2_player2.id)

    def test_3_filter_operators(self):
        """
        Filter fields with __ operators
        """
        query = Player.objects.filter(first_name__startswith="A", height__gte=210)
        result = list(query)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].last_name, "Sabonis")

    def test_4_exclude(self):
        """
        .exclude in query excludes things
        """
        query = Player.objects.filter(first_name="Arvydas")
        query = query.exclude(last_name="Sabonis")

        result = list(query)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].last_name, "Macijauskas")

    def test_5_iexact(self):
        """
        __iexact is case insensitive exact
        """
        query = Player.objects.filter(first_name__iexact="ARVYDAS")

        result = list(query)

        self.assertEqual(len(result), 2)

    def test_6_spanning_multiple_relationships(self):
        """
        Filter lookups can span multiple relationships
        """
        query = Team.objects.filter(contracts__player__first_name="Sarunas")

        result = list(query)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Lietuvos rinktine")

    def test_7_two_conditions_in_same_filter_or_in_separate(self):
        """
        Filter conditions in same filter expression or in separate
        https://docs.djangoproject.com/en/3.0/topics/db/queries/#spanning-multi-valued-relationships
        """

        # Should be zero, as there is no player with both these conditions:
        query = Team.objects.filter(
            contracts__player__first_name="Sarunas",
            contracts__player__last_name="Macijauskas",
        )
        result = list(query)
        self.assertEqual(len(result), 0)

        # Should be one team, as there is team with player named Sarunas
        # ...and also with player named Macijauskas
        query = Team.objects.filter(
            contracts__player__first_name="Sarunas"
        ).filter(
            contracts__player__last_name="Macijauskas"
        )
        result = list(query)
        self.assertEqual(len(result), 1)

        self.assertEqual(result[0].name, "Lietuvos rinktine")

    def test_8_f_expressions(self):
        """
        F expression lets to reference other fields (as opposed to providing values)
        """
        query = StatLine.objects.filter(points=F('rebounds'))
        result = list(query)
        self.assertEqual(len(result), 1)

    def test_9_complex_f_expressions(self):
        """
        F expression can be complex
        https://docs.djangoproject.com/en/3.0/topics/db/queries/#filters-can-reference-fields-on-the-model
        """
        query = StatLine.objects.filter(points=F('rebounds') * 4)
        result = list(query)
        self.assertEqual(len(result), 3)
