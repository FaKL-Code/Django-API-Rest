from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunosSerializer, CursosSerializer, ListaMatriculasAlunoSerializer, MatriculasSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunosSerializer
    
class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursosSerializer

class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo matrículas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculasSerializer
    
class ListaMatriculasAluno(generics.ListAPIView):
    """Exibindo matrículas de um aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer