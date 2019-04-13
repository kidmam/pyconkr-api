# Generated by Django 2.2 on 2019-04-12 14:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20190412_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='pyconkorea',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 4, 12, 14, 36, 7, 462752, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pyconkorea',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='keynote_recommendation_announce_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='keynote_recommendation_finish_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='keynote_recommendation_start_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='lightning_talk_announce_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='lightning_talk_proposal_finish_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='lightning_talk_proposal_start_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='presentation_announce_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='presentation_proposal_finish_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='presentation_proposal_start_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='presentation_review_finish_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='presentation_review_start_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='sponsor_proposal_finish_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='sponsor_proposal_start_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='sprint_proposal_announce_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='sprint_proposal_finish_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='sprint_proposal_start_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='sprint_ticket_finish_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='sprint_ticket_start_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='tutorial_proposal_announce_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='tutorial_proposal_finish_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='tutorial_proposal_start_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='tutorial_ticket_finish_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='tutorial_ticket_start_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='volunteer_announce_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='volunteer_recruiting_finish_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pyconkorea',
            name='volunteer_recruiting_start_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
