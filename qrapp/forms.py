from django import forms


class QrForm(forms.Form):
    url = forms.URLField(label="Url")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['url'].widget.attrs['class'] = 'form-control mb-3'
        self.fields['url'].widget.attrs['placeholder'] = 'Example: https://www.google.com'

