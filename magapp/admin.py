from django.contrib import admin
from .models import Product ,Category,Tags , Comments


admin.site.register([Product,Category,Tags, Comments])
