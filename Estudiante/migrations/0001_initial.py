# Generated by Django 2.2.1 on 2019-06-03 02:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profesor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('enrollment', models.IntegerField()),
                ('subject', models.CharField(max_length=100)),
                ('phoneNumber', models.IntegerField()),
                ('birthday', models.DateField(default=django.utils.timezone.now)),
                ('delete', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('edited', models.DateTimeField(blank=True, default=None, null=True)),
                ('profesorId', models.ForeignKey(on_delete=models.SET(-1), to='Profesor.Profesor')),
            ],
            options={
                'db_table': 'Estudiante',
            },
        ),
    ]