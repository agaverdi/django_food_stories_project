from rest_framework.serializers import ModelSerializer, SerializerMethodField
from magapp.models import Product ,Category ,Tags , Question ,Article ,CommentsClone, Comments
from django.contrib.auth import get_user_model

User=get_user_model()


class UserProfileSerializer(ModelSerializer):
    # def full_username(self, id):
    #     user = User.objects.get(id=id)
    #     name = user.first_name + " " + user.last_name
    #     return name
    class Meta:
        model=User
        fields=[
            'id',
            'first_name',
            'last_name',
            
        ]

# class QuestionSerializer(ModelSerializer):
#     class Meta:
#         model=Question
#         fields=[
#             'id',
#             'title',
#         ]


#{{{{{{{{{{{{{{{{{


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


#}}}}}}}}}}}}}}}}}

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

#many to many olmalidi userde? comment
#question qaldi onnan neleri getirmek lazimdi

class CommentsCreateSerializer(ModelSerializer):

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



##################    PRODUCT      ##########################

class ProductReadSerializer(ModelSerializer):
    category=CategorySerializer(many=True)
    tags=TagSerializer(many=True)
    owner=UserProfileSerializer()
    class Meta:
        model=Product
        fields=[
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

class ProductCreateSerializer(ModelSerializer):

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


##################    ARTICLE      ##########################

class ArticleReadSerializer(ModelSerializer):
    article_tags=UserProfileSerializer()
    article_comments=CommentsCloneSerializer(many=True)
    class Meta:
        model = Article
        fields = [ 
            'id',
            'article_tags',
            'article_comments',
            'title',
            'description',
            'short_description',
            'viewer',
            'image',
            'created_at',
        ]

class ArticleCreateSerializer(ModelSerializer):

    class Meta:
        model = Article
        fields = [ 
            'id',
            'article_tags',
            'article_comments',
            'title',
            'description',
            'short_description',
            'viewer',
            'image',
            'created_at',
        ]


