# Generated by Django 4.2.6 on 2024-01-06 14:01

from django.db import migrations, models
import uuid


def generate_aliases_uuids(apps, schema_editor):
    """Generate new UUIDs for each alias"""

    Alias = apps.get_model("exercises", "Alias")
    for alias in Alias.objects.all():
        alias.uuid = uuid.uuid4()
        alias.save(update_fields=["uuid"])


def generate_comments_uuids(apps, schema_editor):
    """Generate new UUIDs for each comment"""

    Comment = apps.get_model("exercises", "ExerciseComment")
    for comment in Comment.objects.all():
        comment.uuid = uuid.uuid4()
        comment.save(update_fields=["uuid"])


class Migration(migrations.Migration):
    dependencies = [
        ("exercises", "0027_alter_deletionlog_replaced_by_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="exercisecomment",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                unique=False,
                verbose_name="UUID",
            ),
        ),
        migrations.AddField(
            model_name="historicalexercisecomment",
            name="uuid",
            field=models.UUIDField(
                db_index=True,
                default=uuid.uuid4,
                editable=False,
                verbose_name="UUID",
            ),
        ),
        migrations.AddField(
            model_name="alias",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                unique=False,
                verbose_name="UUID",
            ),
        ),
        migrations.AddField(
            model_name="historicalalias",
            name="uuid",
            field=models.UUIDField(
                db_index=True,
                default=uuid.uuid4,
                editable=False,
                verbose_name="UUID",
            ),
        ),
        migrations.RunPython(
            generate_aliases_uuids,
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.RunPython(
            generate_comments_uuids,
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="exercisecomment",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                unique=True,
                verbose_name="UUID",
            ),
        ),
        migrations.AlterField(
            model_name="alias",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                unique=True,
                verbose_name="UUID",
            ),
        )
    ]
