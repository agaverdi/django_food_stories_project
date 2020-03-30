from rest_framework.routers import DefaultRouter
from .views import ProductViewSet ,QuestionViewSet ,ArticleViewSet ,CommentViewSet ,CommentCloneViewSet, OrderViewSet


router=DefaultRouter()


router.register(r'products', ProductViewSet )
router.register(r'questions', QuestionViewSet )
router.register(r'articles', ArticleViewSet )
router.register(r'comments', CommentViewSet )
router.register(r'comments-clones', CommentCloneViewSet )
router.register(r'orders', OrderViewSet )