from rest_framework.viewsets import ModelViewSet
from magapp.models import Product , Question , Article ,Comments
from .serializers import *
from rest_framework import permissions


class ProductViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Product.objects.all()
    serializer_class = ProductReadSerializer
    serializer_classes = {
        'list': ProductReadSerializer,
        'retrieve': ProductReadSerializer,
        'default': ProductCreateSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,self.serializer_classes.get('default'))


class QuestionViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Question.objects.all()
    serializer_class = QuestionReadSerializer
    serializer_classes = {
        'list': QuestionReadSerializer,
        'retrieve': QuestionReadSerializer,
        'default': QuestionCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,self.serializer_classes.get('default'))


class ArticleViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Article.objects.all()
    serializer_class = ArticleReadSerializer
    serializer_classes = {
        'list': ArticleReadSerializer,
        'retrieve': ArticleReadSerializer,
        'default': ArticleCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,self.serializer_classes.get('default'))


class CommentViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Comments.objects.all()
    serializer_class = CommentsReadSerializer
    serializer_classes = {
        'list': CommentsReadSerializer,
        'retrieve': CommentsReadSerializer,
        'default': CommentsCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,self.serializer_classes.get('default'))

class CommentCloneViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = CommentsClone.objects.all()
    serializer_class = CommentsCloneReadSerializer
    serializer_classes = {
        'list': CommentsCloneReadSerializer,
        'retrieve': CommentsCloneReadSerializer,
        'default': CommentsCloneCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,self.serializer_classes.get('default'))

class OrderViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Order.objects.all()
    serializer_class = OrderReadSerializer
    serializer_classes = {
        'list': OrderReadSerializer,
        'retrieve': OrderReadSerializer,
        'default': OrderCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,self.serializer_classes.get('default'))