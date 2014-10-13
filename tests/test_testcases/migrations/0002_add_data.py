# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def add_person(apps, schema_editor):
    apps.get_model("test_testcases", "Person").objects.using(
        schema_editor.connection.alias,
    ).create(
        first_name="John",
        last_name="Doe",
    )


class Migration(migrations.Migration):

    dependencies = [("test_testcases", "0001_initial")]

    operations = [
        migrations.RunPython(
            add_person,
        ),
    ]
