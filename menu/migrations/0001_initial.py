# Generated by Django 5.1.3 on 2024-12-05 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.CharField(choices=[('APPETIZER', 'Appetizer'), ('MAIN', 'Main Course'), ('DESSERT', 'Dessert'), ('BEVERAGE', 'Beverage')], max_length=20)),
                ('dietary_preference', models.CharField(choices=[('NONE', 'None'), ('VEGETARIAN', 'Vegetarian'), ('VEGAN', 'Vegan'), ('GLUTEN_FREE', 'Gluten-Free'), ('DAIRY_FREE', 'Dairy-Free')], default='NONE', max_length=20)),
                ('is_available', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='menu_images/')),
            ],
        ),
    ]
