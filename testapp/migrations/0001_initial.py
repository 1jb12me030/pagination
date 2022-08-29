# Generated by Django 4.0.5 on 2022-07-03 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='employes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comp_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.company')),
                ('emp_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.employes')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='emp_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.employes'),
        ),
    ]
