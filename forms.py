from flask_wtf import FlaskForm
from wtforms import StringField, FloatField


class SnackForm(FlaskForm):
    """form for adding snacks"""

    name = StringField("Snack Name")
    price = FloatField("Price in USD")
    
