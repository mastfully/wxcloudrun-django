from django.db import connection

from .models import BaseSignUpListModel


def create_or_get_sign_up_list_model(table_name, app_label='camp', model='camp.models', options=None):
    class Meta:
        db_table = table_name

    if app_label:
        setattr(Meta, 'app_label', app_label)

    if options is not None:
        for key,value in options.items():
            setattr(Meta, key, value)
    attrs = {'__module__': model, 'Meta': Meta}

    return type(table_name, (BaseSignUpListModel, ), attrs)


def create_db_table(table_name):
    sign_up_list_model = create_or_get_sign_up_list_model(table_name)
    with connection.schema_editor() as schema_editor:
        schema_editor.create_model(sign_up_list_model)


def product_table_name(t_type, time, vacation):
    if vacation == '暑假':
        return t_type + '_' + time + 's'
    if vacation == '寒假':
        return t_type + '_' + time + 't'
