# Generated by Django 5.0 on 2023-12-26 21:41

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_stock_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a1e0dacb-f19d-41fa-86d0-ac24cb8f9b78'), editable=False, primary_key=True, serialize=False),
        ),
    ]
