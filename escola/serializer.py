from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'data_nascimento', 'rg', 'cpf']
        
class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
        
class MatriculasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []