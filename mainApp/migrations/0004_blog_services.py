# Generated by Django 4.1.4 on 2023-08-19 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_alter_checkoutproducts_name_alter_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('pic', models.ImageField(blank=True, default='noimagep.jpg', null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('baseprice', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('finalprice', models.IntegerField()),
                ('size', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('stock', models.CharField(default='In Stock', max_length=20)),
                ('pic1', models.ImageField(blank=True, default='noimagep.jpg', null=True, upload_to='images')),
                ('pic2', models.ImageField(blank=True, default='noimagep.jpg', null=True, upload_to='images')),
                ('pic3', models.ImageField(blank=True, default='noimagep.jpg', null=True, upload_to='images')),
            ],
        ),
    ]
