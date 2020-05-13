# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bug(models.Model):
    bug_id = models.AutoField(primary_key=True)
    bug_name = models.TextField()
    bug_value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Bug'

        verbose_name = "Bug"
        verbose_name_plural = "Bugs"

    def __str__(self):
        return self.bug_name





