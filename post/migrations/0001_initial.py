# Generated by Django 4.0.4 on 2022-06-02 13:29

from django.db import migrations, models
import post.models.post


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=post.models.post.get_file_path)),
                ('time_to_read', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
