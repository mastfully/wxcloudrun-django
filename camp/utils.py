from django.db import models,connection

from .models import BaseSignUpListModel


def create_sign_up_list_model(table_name, app_label='', model='', options=None):
    class Meta:
        db_table = table_name

    if app_label:
        setattr(Meta, 'app_label', app_label)

    if options is not None:
        for key,value in options.items():
            setattr(Meta, key, value)
    attrs = {'__module__': model, 'Meta': Meta}

    return type(table_name,(models.Model,BaseSignUpListModel), attrs)


def create_db_table(sign_up_list_model):
    with connection.schema_editor() as schema_editor:
        schema_editor.create_model(sign_up_list_model)
