# Generated by Django 3.0.7 on 2020-06-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('date_n', models.DateField()),
                ('sex', models.CharField(choices=[('H', 'Homme'), ('F', 'Femme')], default='', max_length=1)),
                ('status', models.CharField(max_length=10)),
                ('nationalite', models.CharField(max_length=20)),
                ('pays', models.CharField(max_length=20)),
                ('ville', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=20)),
                ('addresse', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=255)),
                ('linkdin', models.URLField(blank=True, null=True)),
            ],
        ),
    ]