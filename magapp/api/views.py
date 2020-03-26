from rest_framework.viewsets import ModelViewSet
from magapp.models import Product , Question , Article ,Comments
from .serializers import *


class ProductViewSet(ModelViewSet):
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
    queryset = Comments.objects.all()
    serializer_class = CommentsReadSerializer
    serializer_classes = {
        'list': CommentsReadSerializer,
        'retrieve': CommentsReadSerializer,
        'default': CommentsCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,self.serializer_classes.get('default'))