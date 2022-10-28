from rest_framework import viewsets
from escola.models import Aluno, Curso
from serializer import AlunosSerializer, CursosSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunosSerializer
    
class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursosSerializer
