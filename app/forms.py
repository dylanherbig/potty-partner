from django import forms
from app.models import Feature


class ToiletForm(forms.Form):
    longitude = forms.DecimalField(max_digits=9, decimal_places=6)
    latitude = forms.DecimalField(max_digits=9, decimal_places=6)
    title = forms.CharField(label='Enter a title', max_length=200)
    feature = forms.ModelMultipleChoiceField(
        required = False,
        queryset = Feature.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
