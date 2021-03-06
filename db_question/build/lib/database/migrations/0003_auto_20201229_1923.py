# Generated by Django 3.1.4 on 2020-12-29 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0002_auto_20201229_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='candidate',
        ),
        migrations.RemoveField(
            model_name='answertext',
            name='candidate',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Answer_question', to='database.question'),
        ),
        migrations.AddField(
            model_name='answertext',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AnswerText_question', to='database.question'),
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField(default=0)),
                ('answer', models.ManyToManyField(related_name='answers_many_to_many', to='database.Answer')),
                ('answer_text', models.ManyToManyField(related_name='answers_text_many_to_many', to='database.AnswerText')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
