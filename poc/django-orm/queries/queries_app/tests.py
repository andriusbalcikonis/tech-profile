from datetime import date
from django.conf import settings
from django.db import connection, reset_queries
from django.db.models import Avg, Case, Count, F, Q, Subquery, OuterRef, When
from django.test import TestCase
from queries.queries_app.models import Player, Team, Positions, Contract, Arena, Game, StatLine


class QueriesTestCase(TestCase):

    # Setup:

    def setUp(self):

        # Tests set DEBUG to False by default. Need to be True for query profiling
        # https://docs.djangoproject.com/en/3.0/faq/models/#how-can-i-see-the-raw-sql-queries-django-is-running

        settings.DEBUG = True

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

    def test_10_q_objects(self):
        """
        Q objects to have logical operators in filter
        https://docs.djangoproject.com/en/3.0/topics/db/queries/#complex-lookups-with-q-objects
        """
        query = Player.objects.filter(Q(first_name="Arvydas") | Q(last_name="Jasikevicius"))
        result = list(query)
        self.assertEqual(len(result), 2)

    def test_11_profile_db_queries(self):
        """
        Profiling what exact queries were executed
        """
        reset_queries()
        self.assertEqual(len(connection.queries), 0)
        Player.objects.get(first_name="Arvydas", last_name="Sabonis")
        self.assertEqual(len(connection.queries), 1)

    def test_12_select_related(self):
        """
        "selct_related" will prefetch all related foreign key fields
        """

        # Two queries without "select_related":

        reset_queries()
        self.assertEqual(len(connection.queries), 0)

        stats = list(StatLine.objects.filter(game__arena__name="Zalgirio arena"))
        self.assertEqual(len(connection.queries), 1)

        self.assertEqual(stats[0].player.first_name, "Rolandas")
        self.assertEqual(len(connection.queries), 2)

        # One query with "select_related":

        reset_queries()
        self.assertEqual(len(connection.queries), 0)

        stats = list(StatLine.objects.select_related().filter(game__arena__name="Zalgirio arena"))
        self.assertEqual(len(connection.queries), 1)

        self.assertEqual(stats[0].player.first_name, "Rolandas")
        self.assertEqual(len(connection.queries), 1)

    def test_13_explicit_naming_of_backward_relation(self):
        """
        Field name "game_stats" was explicitly given in the model StatLine field player
        """
        stat_line_count = self.team1_player1.game_stats.count()
        self.assertEqual(stat_line_count, 2)

    def test_14_default_naming_of_backward_relation(self):
        """
        See https://docs.djangoproject.com/en/3.0/topics/db/queries/#following-relationships-backward
        """
        stat_line_count = self.game1.statline_set.count()
        self.assertEqual(stat_line_count, 6)

    def test_15_simple_aggregation(self):
        """
        Simple aggregation
        """
        stats = Player.objects.aggregate(avg=Avg('height'))
        self.assertEqual(round(stats['avg']), 198.0)

    def test_16_simple_annotation(self):
        """
        Simple annotation
        """
        team_heights = Team.objects.annotate(avg=Avg('contracts__player__height'))
        self.assertEqual(round(team_heights[0].avg), 197.0)

    def test_17_never_combine_agregates_in_annotations(self):
        """
        https://docs.djangoproject.com/en/3.0/topics/db/aggregation/#combining-multiple-aggregations
        """
        correct_hg_counts = Team.objects.annotate(count=Count('home_games'))
        incorrect_counts = Team.objects.annotate(
            count=Count('contracts'),
            count_home_games=Count('home_games')
        )
        # Not the same:
        self.assertNotEqual(correct_hg_counts[0].count, incorrect_counts[0].count_home_games)

    def test_18_inner_filter_on_annotation_fields(self):
        """
        ..
        """
        team_count = Team.objects.annotate(player_count=Count(
            'contracts__player')).filter(player_count__gt=1).count()
        # Not the same:
        self.assertEqual(team_count, 2)

    def test_19_probably_pk_is_used_for_annotation_grouping_by_default(self):
        """
        ...
        """
        # If we check game stats per player the default way...
        player_stats = Player.objects.annotate(count=Count('game_stats'))

        # ...it will be 6 players
        self.assertEqual(len(player_stats), 6)

        # ..and each of them will have 2 games played
        self.assertEqual(player_stats[0].count, 2)
        self.assertEqual(player_stats[1].count, 2)
        self.assertEqual(player_stats[2].count, 2)
        self.assertEqual(player_stats[3].count, 2)
        self.assertEqual(player_stats[4].count, 2)
        self.assertEqual(player_stats[5].count, 2)

    def test_20_values_are_used_for_annotation_grouping(self):
        """
        Values are used for annotation grouping
        https://docs.djangoproject.com/en/3.0/topics/db/aggregation/#values
        """

        # If we check game stats while getting values('first_name')...
        player_stats = Player.objects.values('first_name').annotate(count=Count('game_stats'))

        # ...it will be 4 player names
        self.assertEqual(len(player_stats), 4)

        # ..then we'll get stats grouped by name
        # and also we get a dict, not a model
        self.assertEqual(player_stats[0].get('count'), 4)
        self.assertEqual(player_stats[1].get('count'), 2)
        self.assertEqual(player_stats[2].get('count'), 4)
        self.assertEqual(player_stats[3].get('count'), 2)

    def test_21_if_values_go_after_annotation_then_grouping_by_pk_again(self):
        """
        https://docs.djangoproject.com/en/3.0/topics/db/aggregation/#order-of-annotate-and-values-clauses
        """

        # If we check game stats per player the default way...
        player_stats = Player.objects.annotate(count=Count('game_stats')).values('first_name', 'count').all()

        # ...it will be 6 players
        self.assertEqual(len(player_stats), 6)

        # ..and each of them will have 2 games played
        self.assertEqual(player_stats[0].get('count'), 2)
        self.assertEqual(player_stats[1].get('count'), 2)
        self.assertEqual(player_stats[2].get('count'), 2)
        self.assertEqual(player_stats[3].get('count'), 2)
        self.assertEqual(player_stats[4].get('count'), 2)
        self.assertEqual(player_stats[5].get('count'), 2)

    def test_22_q_objects_not_operator(self):
        """
        https://books.agiliq.com/projects/django-orm-cookbook/en/latest/notequal_query.html
        """
        query = Player.objects.filter(Q(first_name="Arvydas") & ~Q(last_name="Sabonis"))
        result = list(query)
        self.assertEqual(len(result), 1)

    def test_23_queryset_union(self):
        """
        https://books.agiliq.com/projects/django-orm-cookbook/en/latest/union.html
        """
        query1 = Player.objects.filter(first_name="Arvydas")
        query2 = Player.objects.filter(last_name="Sinica")
        result = list(query1.union(query2))
        self.assertEqual(len(result), 3)

    def test_24_subquery(self):
        """
        Subqueries
        https://books.agiliq.com/projects/django-orm-cookbook/en/latest/subquery.html
        """

        # Lets get teams with their tallest player

        tallest_player_qs = Player.objects.filter(
            contracts__team_id=OuterRef("pk")
        ).order_by("-height")

        qs = Team.objects.all().annotate(
            tallest_player_last_name=Subquery(
                tallest_player_qs.values('last_name')[:1]
            )
        )

        teams = qs.all()

        self.assertEqual(teams[0].name, "Sakalai")
        self.assertEqual(teams[0].tallest_player_last_name, "Matulis")
        self.assertEqual(teams[1].name, "Lietuvos rinktine")
        self.assertEqual(teams[1].tallest_player_last_name, "Sabonis")

    def test_25_slicing(self):
        """
        Taking first, taking Nth
        https://books.agiliq.com/projects/django-orm-cookbook/en/latest/second_largest.html
        """

        # Try [0]
        reset_queries()
        tallest = Player.objects.order_by('-height')[0]
        self.assertEqual(tallest.last_name, "Sabonis")
        self.assertTrue('LIMIT 1' in connection.queries[0]['sql'])

        # Try .first()
        reset_queries()
        tallest = Player.objects.order_by('-height').first()
        self.assertEqual(tallest.last_name, "Sabonis")
        self.assertTrue('LIMIT 1' in connection.queries[0]['sql'])

        # Try .last()
        reset_queries()
        tallest = Player.objects.order_by('-height').last()
        self.assertEqual(tallest.last_name, "Skaisgirys")
        self.assertTrue('LIMIT 1' in connection.queries[0]['sql'])

        # Try [2]
        reset_queries()
        tallest = Player.objects.order_by('-height')[2]
        self.assertEqual(tallest.last_name, "Sinica")
        self.assertTrue('LIMIT 1 OFFSET 2' in connection.queries[0]['sql'])

    def test_26_find_duplicates(self):
        """
        https://books.agiliq.com/projects/django-orm-cookbook/en/latest/duplicate.html
        """

        reset_queries()
        duplicates = Player.objects.values(
            'first_name'
        ).annotate(
            name_count=Count('first_name')
        ).filter(name_count__gt=1).all()

        self.assertEqual(duplicates[0]['first_name'], "Arvydas")
        self.assertEqual(duplicates[0]['name_count'], 2)
        self.assertEqual(duplicates[1]['first_name'], "Rolandas")
        self.assertEqual(duplicates[1]['name_count'], 2)

    def test_26_get_and_order_by_list_of_ids(self):
        """
        https://stackoverflow.com/a/37648265
        """

        list_of_ids = [
            5, 1, 3, 2, 4
        ]

        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(list_of_ids)])
        results = Player.objects.filter(pk__in=list_of_ids).order_by(preserved)

        self.assertEqual(results[0].id, list_of_ids[0])
        self.assertEqual(results[1].id, list_of_ids[1])
        self.assertEqual(results[2].id, list_of_ids[2])
        self.assertEqual(results[3].id, list_of_ids[3])
        self.assertEqual(results[4].id, list_of_ids[4])
