from django.forms import ModelForm
from dados.models import Dados


class DadosForm(ModelForm):
    class Meta:
        model = Dados
        fields = ['nome', 'sobrenome', 'cpf', 'telefone', 'endereco']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})
        self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})
        