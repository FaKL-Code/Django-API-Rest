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
        
class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
        
    def get_periodo(self, obj):
        return obj.get_periodo_display()