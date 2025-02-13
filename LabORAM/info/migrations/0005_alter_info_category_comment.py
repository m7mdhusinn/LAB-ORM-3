# Generated by Django 4.2.7 on 2023-11-28 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_alter_info_category_alter_info_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='category',
            field=models.CharField(choices=[('Photo', 'Photo'), ('Video', 'Video'), ('Other', 'Other')], default='Comment', max_length=64),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('like_it', models.BooleanField()),
                ('Comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.info')),
            ],
        ),
    ]
