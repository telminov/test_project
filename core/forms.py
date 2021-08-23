from django import forms

import core.models


class BookEdit(forms.ModelForm):
    class Meta:
        model = core.models.Book
        fields = '__all__'


