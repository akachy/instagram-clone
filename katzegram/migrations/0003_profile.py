# Generated by Django 4.1.4 on 2023-07-01 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('katzegram', '0002_alter_post_caption'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='p_images/')),
                ('profile_bio', models.CharField(blank=True, max_length=500, null=True)),
                ('follows', models.ManyToManyField(blank=True, related_name='followed_by', to='katzegram.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
