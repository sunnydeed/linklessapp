from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms.widgets import DateTimeInput

from .models import ShortenedLink


class ShortenedLinkForm(forms.ModelForm):
    class Meta:
        model = ShortenedLink
        fields = ["original_url", "expiry_date"]
        widgets = {
            "expiry_date": DateTimeInput(attrs={"type": "datetime-local"}),
        }

    def __init__(self, *args, **kwargs):
        super(ShortenedLinkForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Shorten", css_class="btn btn-primary"))
