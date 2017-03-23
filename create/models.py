from __future__ import unicode_literals

from django.db import models

# Create your models here.

class RadioAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    id_question = models.ForeignKey('Question', models.DO_NOTHING, db_column='id_question')
    text = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'Enum_answer'

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    id_test = models.ForeignKey('Test', models.DO_NOTHING, db_column='id_test')
    type = models.CharField(max_length=1)
    text = models.CharField(max_length=250)

    class Meta:
        managed = True
        db_table = 'Question'

class SetAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    id_question = models.ForeignKey(Question, models.DO_NOTHING, db_column='id_question')
    text = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'Set_answer'

class Test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    pub_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'Test'
