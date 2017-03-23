from .models import Synonym
from django.http import Http404

from restapp.serializer import SynonymSerializer
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

class SynonymList(APIView):

    def get(self, request):
        q=request.GET.get('words', '')
        synonyms = Synonym.objects.values('word').order_by('-'+q)
        serializer = SynonymSerializer(synonyms, many = True)
        return Response(serializer.data)

    def post(self,request, format = None):
        serializer = SynonymSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SynonymDetail(RetrieveAPIView):
   queryset = Synonym.objects.all()
   serializer_class = SynonymSerializer
        
