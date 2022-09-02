# Generated by Django 3.2 on 2022-09-01 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adventures', '0004_auto_20220831_1424'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='Publication Date')),
                ('comment', models.TextField(max_length=1024)),
                ('value', models.IntegerField(choices=[(5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1')], default=1)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventures.country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Testimnoial',
                'verbose_name_plural': 'Testimonials',
                'ordering': ['-pub_date'],
            },
        ),
    ]