# Generated by Django 2.2.16 on 2022-02-17 15:55

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220217_1442'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='one_following',
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='user_not_author',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='one_following'),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, user=django.db.models.expressions.F('following')), name='user_not_author'),
        ),
    ]
