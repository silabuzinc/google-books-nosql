from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField, DateField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    pages = IntegerField('Pages', validators=[DataRequired()])
    publish_date = DateField('Publish Date', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    isbn = StringField('ISBN', validators=[DataRequired()])
    submit = SubmitField('Create book')
