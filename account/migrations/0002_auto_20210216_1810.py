# Generated by Django 2.2.5 on 2021-02-16 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_link',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='group_name',
            field=models.ForeignKey(blank=True, db_column='group_name', null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Group'),
        ),
        migrations.AlterField(
            model_name='member',
            name='user_status',
            field=models.BooleanField(default=False),
        ),
    ]