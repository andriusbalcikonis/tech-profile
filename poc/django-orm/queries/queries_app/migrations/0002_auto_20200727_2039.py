# Generated by Django 3.0.8 on 2020-07-27 20:39
# flake8: noqa

from django.db import migrations, models
import django.db.models.deletion
import queries.queries_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('queries_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arena',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('attendance', models.IntegerField()),
                ('final_score_home', models.IntegerField()),
                ('final_score_away', models.IntegerField()),
                ('arena', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                            related_name='games', to='queries_app.Arena')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('position', models.CharField(choices=[(queries.queries_app.models.Positions['CN'], 'Center'), (queries.queries_app.models.Positions['PF'], 'Power forward'), (
                    queries.queries_app.models.Positions['SF'], 'Small forward'), (queries.queries_app.models.Positions['SG'], 'Shooting guard'), (queries.queries_app.models.Positions['PG'], 'Point guard')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='StatLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('rebounds', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='stat_lines', to='queries_app.Game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                             related_name='game_stats', to='queries_app.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AddField(
            model_name='game',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='away_games', to='queries_app.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='home_games', to='queries_app.Team'),
        ),
        migrations.AddField(
            model_name='contract',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='contracts', to='queries_app.Player'),
        ),
        migrations.AddField(
            model_name='contract',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='contracts', to='queries_app.Team'),
        ),
    ]