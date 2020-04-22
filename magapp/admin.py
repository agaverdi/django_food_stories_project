from django.contrib import admin
from .models import Product ,Category,Tags , Comments, Article,CommentsClone,Question,Order ,Messages,Group




admin.site.register([Product,Category,Tags, Comments,Article,Question,Order,CommentsClone ,Messages,Group])
