from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ['text']
        labels = {
            'text': 'Nome do tópico'
        }
        widgets = {
            'text': forms.TextInput(
                attrs={
                    'placeholder': 'Ex.: Python, Django, Matemática...',
                    'autocomplete': 'off'
                }
            )
        }


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ['text']
        labels = {
            'text': 'Conteúdo'
        }
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'placeholder': 'Escreva aqui o que você aprendeu...',
                    'rows': 8
                }
            )
        }