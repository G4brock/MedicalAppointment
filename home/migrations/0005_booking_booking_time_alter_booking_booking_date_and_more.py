# Generated by Django 4.2.5 on 2023-09-16 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='p_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='p_phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='dep_desc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='dep_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='dep_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.department'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doc_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doc_spec',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
