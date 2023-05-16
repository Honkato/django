from django.shortcuts import render
from rest_framework.response import responses
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import viewsets
from .models import *
from .serializer import *

class ClienteList(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    def list(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION','').split(' ')[1]
        print(token)
        print("")
        dados = AccessToken(token)
        usuario = dados['user_id']
        print(usuario)
        listaContatos = Contato.objects.filter(pk = usuario)

        return super().list(request, *args, **kwargs)
    def create(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION','').split(' ')[1]
        print(token)

class ClienteDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
    # dados = request.data
    # criar = Contato.objects.create(telefone=dados['telefone'], ramarl = dados['ramal'])

# class ClientePFList(ListCreateAPIView):
#     queryset = ClientePF.objects.all()
#     serializer_class = ClientePFSerializer
# class ClientePFDetail(RetrieveUpdateDestroyAPIView):
#     queryset = ClientePF.objects.all()
#     serializer_class = ClientePFSerializer



# class ClientePJList(ListCreateAPIView):
#     queryset = ClientePJ.objects.all()
#     serializer_class = ClientePJSerializer
# class ClientePJDetail(RetrieveUpdateDestroyAPIView):
#     queryset = ClientePJ.objects.all()
#     serializer_class = ClientePJSerializer

    

# class EnderecoList(ListCreateAPIView):
#     queryset = Endereco.objects.all()
#     serializer_class = EnderecoSerializer
# class EnderecoDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Endereco.objects.all()
#     serializer_class = EnderecoSerializer



# class ContatoList(ListCreateAPIView):
#     queryset = Contato.objects.all()
#     serializer_class = ContatoSerializer
# class ContatoDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Contato.objects.all()
#     serializer_class = ContatoSerializer



class ContaList(ListCreateAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
class ContaDetail(RetrieveUpdateDestroyAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer



class MovimentacaoList(ListCreateAPIView):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer
class MovimentacaoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer



class InvestimentoList(ListCreateAPIView):
    queryset = Investimento.objects.all()
    serializer_class = MovimentacaoSerializer
class InvestimentoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Investimento.objects.all()
    serializer_class = InvestimentoSerializer

class ModelUpdateView(UpdateAPIView):
    model = UsuarioSerializer
    template_name = ".html"


class UsuarioViews(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    def get_queryset(self):
        queryset = Usuario.objects.all()
        return queryset
    
    # def create(self, request, *args, **kwargs):
    #     dados =request.data
        
    #     criar = Usuario.objects.create(email=dados['email'])
    #     return super().create(request, *args, **kwargs)

class EmprestimoList(ListCreateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
class EmprestimoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer



class ParcelasList(ListCreateAPIView):
    queryset = Parcelas.objects.all()
    serializer_class = ParcelasSerializer
class ParcelasDetail(RetrieveUpdateDestroyAPIView):
    queryset = Parcelas.objects.all()
    serializer_class = ParcelasSerializer


