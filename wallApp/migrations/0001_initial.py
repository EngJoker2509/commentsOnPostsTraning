# Generated by Django 4.1.5 on 2023-01-23 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginAndRegApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('Users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_id', to='loginAndRegApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('Users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_users_id', to='loginAndRegApp.user')),
                ('messages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_id', to='wallApp.messages')),
            ],
        ),
    ]
