from app_1.models import Habitat
from django import forms
from datetime import datetime
from django.utils import timezone

class formHabitat(forms.ModelForm):
    class Meta:
        model = Habitat
        fields = '__all__'
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type':'date'}) 
        }

    def clean_fecha_ingreso(self):
        fechaInput = self.cleaned_data['fecha_ingreso']

        formato = ['%d-%m-%Y','%d-%m-%Y', '%m-%Y-%d']

        for fmt in formato:
            try:
                parsed_date = datetime.strptime(str(fechaInput), fmt).date()
                if parsed_date > timezone.now().date():
                    raise forms.ValidationError("fecha futura")
                return parsed_date
            except (ValueError, TypeError):
                continue

        raise forms.ValidationError("dato invalido")