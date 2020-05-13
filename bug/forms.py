from django import forms
from .models import Bug


class CaughtForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = [
            'bug_id', 'bug_value'
        ]

