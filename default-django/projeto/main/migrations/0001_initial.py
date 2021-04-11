# Generated by Django 3.1.4 on 2021-01-29 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('title', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('plan', models.CharField(choices=[('indefinido', 'Indefinido'), ('ouro', 'Ouro'), ('platina', 'Platina'), ('diamante', 'Diamante')], default='indefinido', max_length=50)),
                ('type_site', models.CharField(choices=[('indefinido', 'Indefinido'), ('one_page', 'One Page'), ('institucional', 'Institucional'), ('blog', 'Blog'), ('portal', 'Portal'), ('e_commerce', 'E-commerce'), ('dinamico', 'Dinâmico')], default='indefinido', max_length=50)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainDocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('intro', models.TextField()),
                ('update', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_title', models.CharField(max_length=200)),
                ('topic_texts', models.TextField()),
                ('topics', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.maindocuments')),
            ],
        ),
    ]
