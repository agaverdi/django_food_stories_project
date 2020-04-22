from django.db import models
from django.contrib.auth import get_user_model


User=get_user_model()


class Tags(models.Model):
    title=models.CharField('Tags',max_length=20)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= 'Teq'
        verbose_name_plural= 'Teqler'
        ordering = ('title',)

    def __str__(self):
        return self.title


class Category(models.Model):
    title=models.CharField('Categories',max_length=20)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= 'Kateqori'
        verbose_name_plural= 'Kateqoriler'
        ordering = ('title',)

    def __str__(self):
        return self.title


class Product(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='products')
    category=models.ManyToManyField(Category, related_name='products')
    tags=models.ManyToManyField(Tags,related_name='products')


    product_name=models.CharField('Product name',max_length=40)
    price=models.DecimalField(max_digits = 6, decimal_places = 2)
    discountprice=models.DecimalField(max_digits = 6, decimal_places = 2)
    description=models.TextField('Description')
    author=models.CharField('Author',max_length=40)
    pagecount=models.IntegerField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= 'produkt'
        verbose_name_plural= 'produktlar'
        ordering = ('product_name',)

    def __str__(self):
        return self.product_name



class Order(models.Model):
    owner_order=models.ForeignKey(User , on_delete=models.CASCADE,related_name='orders')
    order_product=models.ForeignKey(Product, on_delete=models.CASCADE,related_name='orders')

    unitprice=models.DecimalField(max_digits = 6, decimal_places = 2)
    quantity=models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= 'Sifaris'
        verbose_name_plural= 'Sifarisler'
        ordering = ('owner_order',)

    def __str__(self):
        return str(self.order_product) if self.order_product else ''

class Question(models.Model):
    owner_question=models.ForeignKey(User, on_delete=models.CASCADE,related_name='questions')
    question_tag=models.ManyToManyField(Tags,related_name='questions')

    title=models.CharField('Title', max_length=35)
    description=models.TextField('Description')
    viewed=models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name= 'Sual'
        verbose_name_plural= 'Suallar'
        ordering = ('title',)

    def __str__(self):
        return self.title




class CommentsClone(models.Model):
    comment_owner=models.ForeignKey(User,on_delete=models.CASCADE ,related_name='commentsclone')
    article=models.ForeignKey('Article', on_delete=models.CASCADE ,related_name='commentsclone')

    comment=models.TextField('Comments') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name= 'komentklon' 
        verbose_name_plural= 'komentklonlar'
        ordering = ('comment',)

    def __str__(self):
        return self.comment




class Article(models.Model):
    article_owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='articles')
    article_tags=models.ManyToManyField(Tags, related_name='articles')



    title=models.CharField('Title', max_length=35)
    description=models.TextField('Description')
    short_description=models.TextField('Short_Description')
    viewer=models.IntegerField()
    image=models.ImageField(upload_to="users/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= 'artikl'
        verbose_name_plural= 'artikllar'
        ordering = ('title',)

    def __str__(self):
        return self.title


class Comments(models.Model):
    usercomment=models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE, )
    reply_comment=models.ForeignKey('self',on_delete=models.CASCADE, null=True, blank=True, related_name='replycomments')
    question=models.ForeignKey(Question,on_delete=models.CASCADE, related_name='comments')
    user_comment_impressions = models.ManyToManyField(User,  blank=True, related_name='user_comment_impressions')

    comment=models.TextField('Comments')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name= 'koment'
        verbose_name_plural= 'komentlar'
        ordering = ('comment',)

    def __str__(self):
        return self.comment


class Messages(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='messages')
    group=models.ForeignKey('Group',on_delete=models.CASCADE,related_name='messages')

    message=models.TextField('Message')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name= 'mesaj'
        verbose_name_plural= 'mesajlar'
        ordering = ('message',)

    def __str__(self):
        return self.sender.username

class Group(models.Model):
    group_users=models.ManyToManyField(User ,related_name='users')

    group_name=models.CharField('Group-name',max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= 'qrup'
        verbose_name_plural= 'qruplar'
        ordering = ('group_name',)

    def __str__(self):
        return self.group_name


