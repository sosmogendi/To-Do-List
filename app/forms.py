from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    title = StringField('Task', validators=[DataRequired()])
    is_complete = BooleanField('Completed')
    submit = SubmitField('Add Task')

class UpdateTaskForm(FlaskForm):
    is_complete = BooleanField('Complete')
    submit = SubmitField('Update')
