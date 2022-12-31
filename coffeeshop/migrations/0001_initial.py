# Generated by Django 4.1.4 on 2022-12-31 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('ordered_at', models.DateTimeField(verbose_name='order_timestamp')),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coffeeshop.drink')),
            ],
        ),
        migrations.CreateModel(
            name='DrinkType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coffeeshop.category')),
            ],
        ),
        migrations.AddField(
            model_name='drink',
            name='drink_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coffeeshop.drinktype'),
        ),
        migrations.AddField(
            model_name='drink',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coffeeshop.size'),
        ),
        migrations.AlterUniqueTogether(
            name='drink',
            unique_together={('drink_type', 'size')},
        ),
    ]
