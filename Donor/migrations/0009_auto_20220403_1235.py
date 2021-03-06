# Generated by Django 2.2.7 on 2022-04-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0008_auto_20220403_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationrequestformquesitons',
            name='Abortion',
            field=models.TextField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformquesitons',
            name='BloodHealthfulnessInfo',
            field=models.TextField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformquesitons',
            name='BreastFeeding',
            field=models.TextField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformquesitons',
            name='Kidney_Lung_Bloodpressure_Diabetes_Epilepsy',
            field=models.TextField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformquesitons',
            name='Liverproblems',
            field=models.TextField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformquesitons',
            name='Preagnant',
            field=models.TextField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformquesitons',
            name='STD',
            field=models.TextField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformquesitons',
            name='SeriousSkinRepair',
            field=models.TextField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformquesitons',
            name='Slpet_Unsafely_OtherThanPartner',
            field=models.TextField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestformquesitons',
            name='Tattoo_Ear_skin_pierced_lastmonth',
            field=models.TextField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], null=True),
        ),
    ]
