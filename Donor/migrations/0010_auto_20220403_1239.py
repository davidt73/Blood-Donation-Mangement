# Generated by Django 2.2.7 on 2022-04-03 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0009_auto_20220403_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationrequestformquesitons',
            name='Abortion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformquesitons',
            name='BloodHealthfulnessInfo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformquesitons',
            name='BreastFeeding',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformquesitons',
            name='Kidney_Lung_Bloodpressure_Diabetes_Epilepsy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformquesitons',
            name='Liverproblems',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformquesitons',
            name='Preagnant',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformquesitons',
            name='STD',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformquesitons',
            name='SeriousSkinRepair',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformquesitons',
            name='Slpet_Unsafely_OtherThanPartner',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformquesitons',
            name='Tattoo_Ear_skin_pierced_lastmonth',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformresult',
            name='Abortion',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformresult',
            name='BloodHealthfulnessInfo',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformresult',
            name='BreastFeeding',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformresult',
            name='HeartDisease',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformresult',
            name='Kidney_Lung_Bloodpressure_Diabetes_Epilepsy',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformresult',
            name='Liverproblems',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformresult',
            name='Preagnant',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformresult',
            name='STD',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformresult',
            name='SeriousSkinRepair',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformresult',
            name='Slpet_Unsafely_OtherThanPartner',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformresult',
            name='Tattoo_Ear_skin_pierced_lastmonth',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=3, null=True),
        ),
    ]