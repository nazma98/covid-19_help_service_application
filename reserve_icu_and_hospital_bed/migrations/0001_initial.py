# Generated by Django 3.1.1 on 2020-09-27 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableHospitalBed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=30)),
                ('bed_number', models.CharField(max_length=30)),
                ('price_per_day', models.CharField(max_length=5)),
                ('available_ac', models.CharField(max_length=5)),
                ('address', models.CharField(max_length=30)),
                ('is_available', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='AvailableICU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=30)),
                ('icu_type', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=5)),
                ('address', models.CharField(max_length=30)),
                ('is_available', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='BookingHospitalBed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('hospital_name', models.CharField(max_length=30)),
                ('price_per_day', models.CharField(max_length=5)),
                ('bed_number', models.CharField(max_length=30)),
                ('available_ac', models.CharField(max_length=5)),
                ('patient_name', models.CharField(max_length=30)),
                ('patient_blood_group', models.CharField(max_length=5)),
                ('patient_age', models.CharField(max_length=5)),
                ('contact_number', models.CharField(max_length=15)),
                ('bkash_number', models.CharField(max_length=15)),
                ('bkash_transaction_id', models.CharField(max_length=20)),
                ('is_available', models.CharField(max_length=5)),
                ('previous_id', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='BookingICU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('hospital_name', models.CharField(max_length=30)),
                ('icu_type', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=5)),
                ('patient_name', models.CharField(max_length=30)),
                ('patient_blood_group', models.CharField(max_length=5)),
                ('patient_age', models.CharField(max_length=5)),
                ('contact_number', models.CharField(max_length=15)),
                ('bkash_number', models.CharField(max_length=15)),
                ('bkash_transaction_id', models.CharField(max_length=20)),
                ('is_available', models.CharField(max_length=5)),
                ('previous_id', models.CharField(max_length=5)),
            ],
        ),
    ]