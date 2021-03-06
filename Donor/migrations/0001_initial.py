# Generated by Django 2.2.7 on 2022-03-26 10:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('App_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DonationRequestFormQuesitons',
            fields=[
                ('Question_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('HeartDisease', models.TextField()),
                ('Kidney_Lung_Bloodpressure_Diabetes_Epilepsy', models.TextField(blank=True, null=True)),
                ('Liverproblems', models.TextField(blank=True, null=True)),
                ('STD', models.TextField(blank=True, null=True)),
                ('Tattoo_Ear_skin_pierced_lastmonth', models.TextField(blank=True, null=True)),
                ('Slpet_Unsafely_OtherThanPartner', models.TextField(blank=True, null=True)),
                ('SeriousSkinRepair', models.TextField(blank=True, null=True)),
                ('Preagnant', models.TextField(blank=True, null=True)),
                ('Abortion', models.TextField(blank=True, null=True)),
                ('BreastFeeding', models.TextField(blank=True, null=True)),
                ('BloodHealthfulnessInfo', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DonationRequestFormResult',
            fields=[
                ('Result_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('HeartDisease', models.BooleanField(blank=True, max_length=3, null=True)),
                ('Kidney_Lung_Bloodpressure_Diabetes_Epilepsy', models.BooleanField(blank=True, max_length=3, null=True)),
                ('Liverproblems', models.BooleanField(blank=True, max_length=3, null=True)),
                ('STD', models.BooleanField(blank=True, max_length=3, null=True)),
                ('Tattoo_Ear_skin_pierced_lastmonth', models.BooleanField(blank=True, max_length=3, null=True)),
                ('Slpet_Unsafely_OtherThanPartner', models.BooleanField(blank=True, max_length=3, null=True)),
                ('SeriousSkinRepair', models.BooleanField(blank=True, max_length=3, null=True)),
                ('Preagnant', models.BooleanField(blank=True, max_length=3, null=True)),
                ('Abortion', models.BooleanField(blank=True, max_length=3, null=True)),
                ('BreastFeeding', models.BooleanField(blank=True, max_length=3, null=True)),
                ('BloodHealthfulnessInfo', models.BooleanField(blank=True, max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Donorname', models.CharField(blank=True, max_length=20, null=True)),
                ('DateOfBirth', models.DateTimeField(blank=True, max_length=6, null=True)),
                ('Bloodgroup', models.CharField(blank=True, max_length=10, null=True)),
                ('Gender', models.CharField(blank=True, max_length=10, null=True)),
                ('Age', models.IntegerField()),
                ('Nationality', models.CharField(blank=True, max_length=10, null=True)),
                ('Height', models.FloatField(blank=True, max_length=10, null=True)),
                ('Weight', models.FloatField(blank=True, max_length=10, null=True)),
                ('BMS', models.FloatField(blank=True, max_length=10, null=True)),
                ('BloodPressure', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
