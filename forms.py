from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
# from wtforms import FileField
from wtforms.widgets import TextArea
from wtforms.validators import InputRequired, Length


class DealForm(FlaskForm):
    projectName = StringField(
        'Project Name',
        validators=[InputRequired(), Length(min=1, max=10)]
    )
    projectScore = SelectField(
        'Project Score',
        choices=[('', ''), ('A', 'A'), ('A-', 'A-'), ('B+', 'B+'),
                 ('B', 'B'), ('B-', 'B-'), ('C+', 'C+'), ('D', 'D')]
    )
    teamScore = SelectField(
        'Team Score',
        choices=[('', ''), ('A', 'A'), ('A-', 'A-'), ('B+', 'B+'),
                 ('B', 'B'), ('B-', 'B-'), ('C+', 'C+'), ('D', 'D')]
    )
    projectStatus = SelectField(
        'Project Status',
        choices=[('', ''), ('passed', 'Passed'), ('follow-up', 'Followed Up'),
                 ('in-dd', 'In Due Diligence'), ('ic-pending', 'Waiting \
                 for IC'), ('ic-aye', 'IC Accepted'), ('ic-nay', 'IC \
                 Rejected'), ('in-portfolio', 'In Portfolio')]
    )
    industry = StringField(
        'Industry',
        validators=[InputRequired()]
    )
    memo = StringField(
        'Memo',
        widget=TextArea()
    )
    # fileUpload = FileField(
    #     'BP Upload'
    # )


class ContactForm(FlaskForm):
    contactName = StringField(
        'Contact Name',
        validators=[InputRequired(), Length(min=1, max=10)]
    )
    contactMethod = StringField(
        'Contact Method',
        validators=[InputRequired(), Length(min=1, max=10)]
    )
    contactNote = StringField(
        'Notes',
        widget=TextArea()
    )
