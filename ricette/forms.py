from django import forms
from .models import Ricetta, Commento

class FormNuovaRicetta(forms.ModelForm):
    class Meta:
        model = Ricetta
        fields = ('titolo', 'categoria', 'difficolta', 'tempo_svolgimento', 'numero_persone', 'ingredienti', 'istruzioni',)

    def clean_titolo(self):
        titolo=self.cleaned_data.get('titolo')
        if not titolo:
            self.add_error('titolo', 'Il campo titolo è obbligatorio!')
        return titolo


class FormCommento(forms.ModelForm):

    class Meta:
        model = Commento
        fields =('Testo',)

        widgets={
            'Testo': forms.Textarea(attrs={'cols': 160, 'rows': 6,})
        }
        labels = {
            'Testo': ''
        }

