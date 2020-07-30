# Generated by Django 3.0.7 on 2020-07-22 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0004_auto_20200720_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=300)),
                ('send_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('recent_msg', models.BooleanField(default=False)),
                ('real_estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.Real_estate')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]