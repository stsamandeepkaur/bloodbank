from django import forms
from Myapp.models import Donor, Contact
from crispy_forms.helper import FormHelper
class DonorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DonorForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta():
        model = Donor
        widgets = {
            'Date_of_birth': forms.DateInput(attrs={'type':'date','class':'form-control'}),

        }
        fields= '__all__'
        helper = FormHelper()
class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta():
        model = Contact
        fields='__all__'
        helper = FormHelper()
