
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '00001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='timeStamp',
            new_name='dateTime',
        ),
    ]
