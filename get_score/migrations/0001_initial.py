# Generated by Django 4.1.2 on 2022-10-23 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('input_one', models.DecimalField(decimal_places=2, max_digits=15)),
                ('result', models.DecimalField(decimal_places=2, max_digits=15, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
