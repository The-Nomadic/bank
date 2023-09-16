# Generated by Django 4.2.5 on 2023-09-15 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=250)),
                ('wiki_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=150)),
                ('account_type', models.CharField(max_length=150)),
                ('material', models.CharField(max_length=200)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_app.branch')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_app.district')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_app.district'),
        ),
    ]
