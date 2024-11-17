from .models import Record
from django import forms


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "date_of_birth",
            "date_of_death",
            "content",
            "author"
        ]