# Generated by Django 2.1.15 on 2019-12-20 02:14

from django.db import migrations, models


def set_frequency(apps, schema_editor):
    M = apps.get_model('eemeter', 'baselinemodel')
    for model in M.objects.all().iterator():
        if 'daily' in model.model_class.lower():
            model.frequency = 'daily'
        else:
            model.frequency = 'hourly'
        model.save()


class Migration(migrations.Migration):

    dependencies = [
        ('eemeter', '0002_baselinemodel_meter'),
    ]

    operations = [
        migrations.AddField(
            model_name='baselinemodel',
            name='frequency',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.RunPython(set_frequency, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='baselinemodel',
            name='frequency',
            field=models.CharField(blank=False, null=False, max_length=255),
        ),
    ]
