from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    input_text = TextAreaField("Input", validators=[DataRequired()])
    submit = SubmitField("CONVERT")
    output_text = TextAreaField("Output")