from __future__ import unicode_literals
from create.models import RadioAnswer, Question, Test, SetAnswer
from reg.models import User
from django.db import models

class Session(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    id_test = models.ForeignKey(Test,  db_column='id_test', null=True)
    id_user = models.ForeignKey(User, db_column='id_user', null=True)

    class Meta:
        managed = True
        db_table = 'Session'

class SelectedRadioAnswer(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    id_session = models.ForeignKey(Session,  db_column='id_session', null=True)
    id_selected_enum = models.ForeignKey(RadioAnswer,  db_column='id_selected_enum', null=True)

    class Meta:
        managed = True
        db_table = 'Selected_enum_answer'
