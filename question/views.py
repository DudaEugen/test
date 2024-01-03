
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Question
from .serializers import QuestionDetailsSerializer, QuestionListSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return QuestionListSerializer
        return QuestionDetailsSerializer

    def list(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(self.queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        question = get_object_or_404(self.queryset, pk=pk)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(question)
        return Response(serializer.data)
