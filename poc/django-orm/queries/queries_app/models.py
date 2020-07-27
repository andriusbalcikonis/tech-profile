
from django.db import models
from enum import Enum


class Positions(Enum):
    CN = "Center"
    PF = "Power forward"
    SF = "Small forward"
    SG = "Shooting guard"
    PG = "Point guard"


class Player(models.Model):

    first_name = models.TextField()

    last_name = models.TextField()

    height = models.IntegerField()

    weight = models.IntegerField()

    date_of_birth = models.DateField()

    position = models.CharField(
        max_length=5,
        choices=[(pos, pos.value) for pos in Positions]
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Team(models.Model):

    name = models.TextField()

    def __str__(self):
        return self.name


class Contract(models.Model):

    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="contracts")

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="contracts")

    start_date = models.DateField()

    end_date = models.DateField()

    def __str__(self):
        return f'{self.player} in {self.team}'


class Arena(models.Model):

    name = models.TextField()

    def __str__(self):
        return self.name


class Game(models.Model):

    date = models.DateField()

    arena = models.ForeignKey(Arena, on_delete=models.CASCADE, related_name="games")

    attendance = models.IntegerField()

    final_score_home = models.IntegerField()

    final_score_away = models.IntegerField()

    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_games")

    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_games")

    def __str__(self):
        return f'{self.home_team} vs {self.away_team} on {self.date}'


class StatLine(models.Model):

    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="stat_lines")

    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="game_stats")

    points = models.IntegerField()

    rebounds = models.IntegerField()

    assists = models.IntegerField()
