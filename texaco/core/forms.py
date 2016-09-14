from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed, FileRequired


class FileForm(Form):
    upload = FileField('File', validators=[
        FileRequired(),
        FileAllowed(['txt', 'csv'], 'Text files only!')
    ])
