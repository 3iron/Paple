<<<<<<< HEAD
# Generated by Django 2.2.5 on 2021-02-09 04:43
=======
# Generated by Django 2.2.5 on 2021-02-09 04:40
>>>>>>> 6840f220a259a58acb2de6d5729d86ac30b08020

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('q_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('q_content', models.CharField(max_length=200)),
                ('q_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('post_date', models.DateTimeField()),
                ('post_name', models.CharField(max_length=30)),
                ('post_content', models.CharField(max_length=200)),
                ('group_name', models.ForeignKey(db_column='group_name', on_delete=django.db.models.deletion.CASCADE, to='account.Group')),
                ('user_email', models.ForeignKey(db_column='user_email', on_delete=django.db.models.deletion.CASCADE, to='account.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('c_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('c_content', models.CharField(max_length=200)),
                ('group_name', models.ForeignKey(db_column='group_name', on_delete=django.db.models.deletion.CASCADE, to='account.Group')),
                ('user_email', models.ForeignKey(db_column='user_email', on_delete=django.db.models.deletion.CASCADE, to='account.Member')),
            ],
        ),
    ]
