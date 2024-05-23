from django import forms

class InputUnico(forms.Form):
    nome_aluno = forms.CharField(required=True, max_length=100, label='Nome do Aluno')
    nome_disciplina = forms.CharField(required=True, max_length=100, label='Nome da Disciplina')
    como_avaliar = forms.CharField(required=True, widget=forms.Textarea(attrs={'cols': 5, 'rows': 4, 'style':'resize:none;'}), label='Como Devo Avaliar ?')
    nota_max = forms.IntegerField(required=True, max_value=100, label='Nota Máxima')
    nota_min = forms.IntegerField(required=True, max_value=100,  label='Nota Mínima')
    trabalho = forms.CharField(required=True, widget=forms.Textarea(attrs={'cols': 5, 'rows': 4, 'style':'resize:none;'}), label='Insira o Trabalho')
    
