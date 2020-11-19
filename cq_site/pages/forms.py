from django import forms
from threads.models import Thread
from categories.models import Category


class ThreadCreationForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = [
            'thr_title',
            'thr_content',
            'thr_category',
            'thr_author'
        ]
        labels = {
            'thr_title': 'Thread title',
            'thr_content': 'Thread content',
            'thr_category': 'Thread category'
        }
        widgets = {
            'thr_author': forms.HiddenInput(),
        }
