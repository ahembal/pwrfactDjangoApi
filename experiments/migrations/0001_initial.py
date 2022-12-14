# Generated by Django 4.1.2 on 2022-10-31 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiment_number', models.CharField(max_length=20)),
                ('experiment_date', models.DateField(auto_now_add=True)),
                ('sample_name', models.CharField(max_length=20)),
                ('powder_comp', models.CharField(max_length=20)),
                ('synthesis_method', models.CharField(max_length=20)),
                ('polymer', models.CharField(max_length=20)),
                ('substrate', models.CharField(max_length=20)),
                ('deposition', models.CharField(max_length=20)),
                ('nanoparticle_percentage', models.IntegerField()),
                ('polymer_percentage', models.IntegerField()),
                ('linker_composite', models.CharField(max_length=20)),
                ('linker_percentage', models.IntegerField()),
                ('geometry', models.CharField(max_length=20)),
                ('thickness', models.IntegerField()),
                ('comments', models.TextField(blank=True, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement_order', models.IntegerField()),
                ('resistance', models.FloatField()),
                ('voltage', models.FloatField()),
                ('temp', models.FloatField()),
                ('experiment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='experiments.experiment')),
            ],
            options={
                'ordering': ['measurement_order'],
                'unique_together': {('experiment_id', 'measurement_order')},
            },
        ),
    ]
