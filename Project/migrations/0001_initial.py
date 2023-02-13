# Generated by Django 3.2.13 on 2022-10-03 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AngularProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('videos', models.FileField(upload_to='Project_videos')),
            ],
        ),
        migrations.CreateModel(
            name='C_pluseProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('videos', models.FileField(upload_to='Project_videos')),
            ],
        ),
        migrations.CreateModel(
            name='CProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('videos', models.FileField(upload_to='Project_videos')),
            ],
        ),
        migrations.CreateModel(
            name='CsharpProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('videos', models.FileField(upload_to='Project_videos')),
            ],
        ),
        migrations.CreateModel(
            name='DjangoProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('videos', models.FileField(upload_to='Project_videos')),
            ],
        ),
        migrations.CreateModel(
            name='ElixirProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('videos', models.FileField(upload_to='Project_videos')),
            ],
        ),
        migrations.CreateModel(
            name='GoProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('videos', models.FileField(upload_to='Project_videos')),
            ],
        ),
        migrations.CreateModel(
            name='JavaProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('videos', models.FileField(upload_to='Project_videos')),
            ],
        ),
        migrations.CreateModel(
            name='JavascriptProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('videos', models.FileField(upload_to='Project_videos')),
            ],
        ),
        migrations.CreateModel(
            name='NodeProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('videos', models.FileField(upload_to='Project_videos')),
            ],
        ),
        migrations.CreateModel(
            name='PythonProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('videos', models.FileField(upload_to='Project_videos')),
            ],
        ),
        migrations.CreateModel(
            name='ReactProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('videos', models.FileField(upload_to='Project_videos')),
            ],
        ),
        migrations.CreateModel(
            name='RubyProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('videos', models.FileField(upload_to='Project_videos')),
            ],
        ),
        migrations.CreateModel(
            name='RubyrailProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('videos', models.FileField(upload_to='Project_videos')),
            ],
        ),
    ]
