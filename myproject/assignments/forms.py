from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, Form, validators , TextAreaField, BooleanField, RadioField, SelectField
from myproject.models import Courses

class SolveAssignment(FlaskForm):
    pass


class DescriptionAssignment(FlaskForm):
    pass

class AddAssignment(FlaskForm):
    assignment_name = StringField('Assignment Name:', [ validators.Required() ]) 
    difficulty = SelectField('Select Difficulty:', choices = [('Beginner', 'Beginner'), ('intermediate', 'intermediate'), ('Expert', 'Expert')]) 
    

class DeleteAssignment(FlaskForm):
    submit = SubmitField("Delete Assignment")

class SubmitAssignment(FlaskForm):
    review = StringField('Review: ', [ validators.Required() ])
    rating =  SelectField('Select Rating:', choices = [(1 ,'1-Star'), (2 ,'2-Star'), (3 ,'3-Star'),  (4 ,'4-Star'),  (5 ,'5-Star')]) 
    submit = SubmitField("Submit Review")

