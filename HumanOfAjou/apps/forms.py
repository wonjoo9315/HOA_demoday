# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import (
    StringField,
    PasswordField,
    TextAreaField,
    FileField
)
from wtforms import validators
from wtforms.fields.html5 import EmailField


class HumansForm(Form):
    text = TextAreaField(
        u'내용',
        [validators.data_required(u'내용을 입력하시기 바랍니다.')],
        description={'placeholder': u'내용을 입력하세요.'}
    )
    q_month = TextAreaField(
        u'질문',
        [validators.data_required(u'질문을 입력하시기 바랍니다.')],
        description={'placeholder': u'질문을 입력하세요.'}
    )

    photo = FileField(
        u'사진'
    )
class AjouForm(Form):
    title = StringField(
        u'제목',
        [validators.data_required(u'제목을 입력하시기 바랍니다.')],
        description={'placeholder': u'제목을 입력하세요.'}
    )
    photographer = StringField(
        u'작성자',
        [validators.data_required(u'이름을 입력하시기 바랍니다.')],
        description={'placeholder': u'이름을 입력하세요.'}
    )

    text = TextAreaField(
        u'내용',
        [validators.data_required(u'내용을 입력하시기 바랍니다.')],
        description={'placeholder': u'내용을 입력하세요.'}
    )