from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from .constants import LINK_REG

STRING_FIELD_NAME_ORIGINAL_LINK = 'Длинная ссылка'
STRING_ORIGINAL_LINK_DATAREQUIRED = 'Обязательное поле'
STRING_ORIGINAL_LINK_URL = 'Некорректная ссылка'
STRING_FIELD_NAME_CUSTOM_ID = 'Ваш вариант короткой ссылки'
STRING_CUSTOM_ID_REGEXP = 'Допустимы только цифры и буквы "a-Z"'
STRING_FIELD_NAME_SUBMIT = 'Создать'


class URLMapForm(FlaskForm):
    original_link = URLField(
        STRING_FIELD_NAME_ORIGINAL_LINK,
        validators=[
            DataRequired(message=STRING_ORIGINAL_LINK_DATAREQUIRED),
            URL(message=STRING_ORIGINAL_LINK_URL)]
    )
    custom_id = StringField(
        STRING_FIELD_NAME_CUSTOM_ID,
        validators=[
            Optional(),
            Length(1, 16),
            Regexp(
                regex=LINK_REG,
                message=STRING_CUSTOM_ID_REGEXP)]
    )
    submit = SubmitField(STRING_FIELD_NAME_SUBMIT)
