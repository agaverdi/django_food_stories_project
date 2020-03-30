from rest_framework.serializers import ModelSerializer, SerializerMethodField 
from magapp.models import *
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import ValidationError


User=get_user_model()

class UserProfileSerializer(ModelSerializer):

    class Meta:
        model=User
        fields=[
            'id',
            'first_name',
            'last_name',
            
        ]

class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields=[
            'id',
            'title',
        ]

class TagSerializer(ModelSerializer):
    class Meta:
        model=Tags
        fields=[
            'id',
            'title',
        ]

class CommentsCloneSerializer(ModelSerializer):
    class Meta:
        model=CommentsClone
        fields=[
            'id',
            'comment',
        ]

class CommentsSerializer(ModelSerializer):
    class Meta:
        model=Comments
        fields=[
            'id',
            'comment',
        ]

class OrderSerializer(ModelSerializer):
    class Meta:
        model=Order
        fields=[
            'id',
            'unitprice',
        ]
##############################################################


##################    COMMENTS      ##########################

class CommentsReadSerializer(ModelSerializer):
    usercomment=UserProfileSerializer()
    reply_comment=CommentsSerializer(source="replycomments", many=True)
    

    class Meta:
        model = Comments
        fields = [ 
            'id',
            'usercomment',
            'reply_comment',
            'user_comment_impressions',
            'comment',
            'created_at',
        ]

class CommentsCreateSerializer(ModelSerializer):
    usercomment = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    class Meta:
        model = Comments
        fields = [ 
            'id',
            'usercomment',
            'reply_comment',
            'question',
            'comment',
            'created_at',
        ]
    
    def validate(self, data):
        request = self.context.get('request')
        data['usercomment'] = request.user
        return super().validate(data)

##################    COMMENTSCLONE      ##########################

class CommentsCloneReadSerializer(ModelSerializer):
    comment_owner=UserProfileSerializer()
    
    
    class Meta:
        model = CommentsClone
        fields = [ 
            'id',
            'comment_owner',
            'comment',
            'article',
            'created_at',
        ]

class CommentsCloneCreateSerializer(ModelSerializer):
    comment_owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = CommentsClone
        fields = [ 
            'id',
            'comment_owner',
            'article',
            'comment',
            'created_at',
        ]
    def validate(self, data):
        request = self.context.get('request')
        data['comment_owner'] = request.user
        return super().validate(data)

###################       ORDER      ########################## 

class OrderReadSerializer(ModelSerializer):
    owner_order=UserProfileSerializer()

    class Meta:
        model=Order
        fields=[
            'owner_order',
            'order_product',
            'unitprice',
            'quantity',
            'created_at',
        ]

class OrderCreateSerializer(ModelSerializer):
    owner_order = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)


    class Meta:
        model=Order
        fields=[
            'owner_order',
            'order_product',
            'unitprice',
            'quantity',
            'created_at',
        ]
    def validate(self, data):
        request = self.context.get('request')
        data['owner_order'] = request.user
        return super().validate(data)

##################    PRODUCT      ##########################

class ProductReadSerializer(ModelSerializer):
    category=CategorySerializer(many=True)
    tags=TagSerializer(many=True)
    owner=UserProfileSerializer()
    orders=SerializerMethodField()
    class Meta:
        model=Product
        fields=[
            'id',
            'owner',
            'category',
            'tags',
            'orders',
            'product_name',
            'price',
            'discountprice',
            'description',
            'author',
            'pagecount',
            'created_at',
        ]

    def get_orders(self, product):
        return OrderReadSerializer(product.orders.all(), many=True).data

class ProductCreateSerializer(ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    
    class Meta:
        model = Product
        fields = [ 
            'id',
            'owner',
            'category',
            'tags',
            'product_name',
            'price',
            'discountprice',
            'description',
            'author',
            'pagecount',
            'created_at',
        ]

    def validate(self, data):
        request = self.context.get('request')
        data['owner'] = request.user
        attrs = super().validate(data)
        if data['discountprice'] and float(data['discountprice']) > float(data['price']):
            raise ValidationError("Discount price must be small than price")
        return attrs

##################    QUESTION      ##########################

class QuestionReadSerializer(ModelSerializer):
    owner_question=UserProfileSerializer()
    question_tag=TagSerializer(many=True)
    comments = SerializerMethodField()
    class Meta:
        model = Question
        fields = [ 
            'id',
            'owner_question',
            'question_tag',
            'comments',
            'title',
            'description',
            'viewed',
            'created_at',
        ]
    
    def get_comments(self, question):
        return CommentsReadSerializer(question.comments.all(), many=True).data

class QuestionCreateSerializer(ModelSerializer):
    owner_question = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)


    class Meta:
        model = Question
        fields = [ 
            'id',
            'owner_question',
            'question_tag',
            'title',
            'description',
            'viewed',
            'created_at',
        ]
    def validate(self, data):
        request = self.context.get('request')
        data['owner_question'] = request.user
        return super().validate(data)

##################    ARTICLE      ##########################

class ArticleReadSerializer(ModelSerializer):
    article_owner=UserProfileSerializer()
    article_tags=TagSerializer(many=True)
    comments=SerializerMethodField()
    
    # article_comments=CommentsCloneSerializer(many=True)
    class Meta:
        model = Article
        fields = [ 
            'id',
            'article_owner',
            'article_tags',
            'comments',
            'title',
            'description',
            'short_description',
            'viewer',
            'image',
            'created_at',
        ]

    def get_comments(self, article):
        return CommentsCloneReadSerializer(article.commentsclone.all(),many=True).data

class ArticleCreateSerializer(ModelSerializer):
    article_owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)


    class Meta:
        model = Article
        fields = [ 
            'id',
            'article_tags',
            'article_owner',
            'title',
            'description',
            'short_description',
            'viewer',
            'image',
            'created_at',
        ]
    def validate(self, data):
        request = self.context.get('request')
        data['article_owner'] = request.user
        return super().validate(data)


