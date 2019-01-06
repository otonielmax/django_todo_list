from django import forms

class TodoForm(forms.Form):
    description = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Ingresa aqui tu tarea nueva',
            'aria-label' : 'Ingresa aqui tu tarea nueva',
            'aria-describedby' : 'basic-addon2'
        })
    )