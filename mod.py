# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class RadioAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    id_question = models.ForeignKey('Question', models.DO_NOTHING, db_column='id_question')
    text = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Enum_answer'


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    id_test = models.ForeignKey('Test', models.DO_NOTHING, db_column='id_test')
    type = models.CharField(max_length=1)
    text = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'Question'


class SelectedRadioAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    id_session = models.ForeignKey('Session', models.DO_NOTHING, db_column='id_session')
    id_selected_enum = models.ForeignKey(RadioAnswer, models.DO_NOTHING, db_column='id_selected_enum')

    class Meta:
        managed = False
        db_table = 'Selected_enum_answer'


class SelectedSetAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    id_session = models.ForeignKey('Session', models.DO_NOTHING, db_column='id_session')
    id_selected_set = models.ForeignKey('SetAnswer', models.DO_NOTHING, db_column='id_selected_set')

    class Meta:
        managed = False
        db_table = 'Selected_set_answer'


class SelectedTextAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    id_session = models.ForeignKey('Session', models.DO_NOTHING, db_column='id_session')
    id_question = models.ForeignKey(Question, models.DO_NOTHING, db_column='id_question')
    answer = models.TextField()

    class Meta:
        managed = False
        db_table = 'Selected_text_answer'


class Session(models.Model):
    id = models.AutoField(primary_key=True)
    id_test = models.ForeignKey('Test', models.DO_NOTHING, db_column='id_test')

    class Meta:
        managed = False
        db_table = 'Session'


class SetAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    id_question = models.ForeignKey(Question, models.DO_NOTHING, db_column='id_question')
    text = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Set_answer'


class Test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    pub_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'Test'
