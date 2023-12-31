# Generated by Django 4.2.4 on 2023-08-10 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("showroom", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="brand",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="demand",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="features",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="mileage",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="my",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="p_pic",
        ),
        migrations.AddField(
            model_name="profile",
            name="addpic",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="profile",
            name="dat",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="id",
            field=models.CharField(
                default="1", max_length=5, primary_key=True, serialize=False
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="pic",
            field=models.ImageField(null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="profile",
            name="engine",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="profile",
            name="insured",
            field=models.CharField(
                choices=[("yes", "INSURED "), ("No", "NOT INSURED ")], max_length=3
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="profile",
            name="variant",
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name="profile",
            name="Mileage",
            field=models.PositiveIntegerField(
                blank=True, help_text="In KMs", null=True
            ),
        ),
    ]
