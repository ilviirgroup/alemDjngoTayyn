from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Brand(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    ai = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    # subcategory = models.ForeignKey('Subcategory', related_name='cat', on_delete=models.CASCADE, default='')
    photo = models.ImageField(upload_to='Category/%Y/%m/%d')

    def __str__(self):
        return f'{self.ai} '

    def get_sub(self):
         return Subcategory.objects.filter(category=self)

    class Meta:
        ordering = ('-pk',)



class Color(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name



class Gender(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 6
#class Lastids(models.Model):

    #def __str__(self):
        #return self.name


class Messages(models.Model):
    text = models.TextField()
    answer = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    userphone = models.CharField(max_length=150)
    user = models.ForeignKey('UserAlem', related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('-pk',)

class Orders(models.Model):
    ai = models.CharField(max_length=200)
    # ai = models.ForeignKey('Category', related_name='productss', on_delete=models.CASCADE)
    #color = models.ForeignKey('Color', related_name='productss', on_delete=models.CASCADE)
    color = models.ManyToManyField('Color')
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    username = models.CharField(max_length=250)
    useremail = models.EmailField(max_length=250)
    userphone = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    price = models.FloatField()
    # name = models.ForeignKey('Products', related_name='productss', on_delete=models.CASCADE)
    quantity = models.IntegerField()    
    #size = models.ForeignKey('Size', related_name='productss', on_delete=models.CASCADE)
    size = models.ManyToManyField('Size')
    inprocess = models.BooleanField(default=False)
    photo = models.CharField(max_length=250)
    # photo = models.ImageField(upload_to='Category/%Y/%m/%d', blank=True)

    def get_absolute_url(self):
        return reverse('orders', kwargs={"ai":self.ai, "name":self.name})

    def __str__(self):
        return self.name.name

    def get_color(self):
        return  "\n".join([c.name for c in self.color.all()])

    def get_size(self):
        return  "\n".join([c.name for c in self.size.all()])

    class Meta:
        ordering = ('-pk',)

class Products(models.Model):
    #ai = models.ForeignKey('Category', related_name='alem', on_delete=models.CASCADE)
    ai = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='Products/%Y/%m/%d', blank=True)
    photo1 = models.ImageField(upload_to='Photo1/%Y/%m/%d', blank=True)
    photo2 = models.ImageField(upload_to='Photo2/%Y/%m/%d', blank=True)
    photo3 = models.ImageField(upload_to='Photo3/%Y/%m/%d', blank=True)
    photo4 = models.ImageField(upload_to='Photo4/%Y/%m/%d', blank=True)
    price = models.FloatField()
    brand = models.ForeignKey('Brand', related_name='products', on_delete=models.CASCADE )
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    #color = models.ForeignKey('Color', related_name='products', on_delete=models.CASCADE)
    color = models.ManyToManyField('Color')
    gender = models.ForeignKey('Gender', related_name='products', on_delete=models.CASCADE)
    #size = models.ForeignKey('Size', related_name='products', on_delete=models.CASCADE)
    size = models.ManyToManyField('Size')
    status = models.CharField(max_length=150)
    # status = models.ForeignKey('Status', related_name='products', on_delete=models.CASCADE)
    subcategory = models.ForeignKey('Subcategory', related_name='products', on_delete=models.CASCADE)
    new = models.BooleanField(default=False)
    # new = models.ForeignKey('New', related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('infoProducts', kwargs={"pk": self.pk})

    def get_color(self):
        return  "\n".join([c.name for c in self.color.all()])

    def get_size(self):
        return  "\n".join([c.name for c in self.size.all()])

    class Meta:
        ordering = ('-pk',)

class Favorites(models.Model):

    ai = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    photo = models.CharField(max_length=250, blank=True)
    photo1 = models.CharField(max_length=250, blank=True)
    photo2 = models.CharField(max_length=250, blank=True)
    photo3 = models.CharField(max_length=250, blank=True)
    photo4 = models.CharField(max_length=250, blank=True)

    # photo = models.ImageField(upload_to='Orders/%Y/%m/%d', blank=True)
    # photo1 = models.ImageField(upload_to='Photo1/%Y/%m/%d', blank=True)
    # photo2 = models.ImageField(upload_to='Photo2/%Y/%m/%d', blank=True)
    # photo3 = models.ImageField(upload_to='Photo3/%Y/%m/%d', blank=True)
    # photo4 = models.ImageField(upload_to='Photo4/%Y/%m/%d', blank=True)
    price = models.FloatField()
    brand = models.ForeignKey('Brand', related_name='favorites', on_delete=models.CASCADE )
    category = models.ForeignKey('Category', related_name='favorites', on_delete=models.CASCADE)
    #color = models.ForeignKey('Color', related_name='products', on_delete=models.CASCADE)
    color = models.ManyToManyField('Color')
    gender = models.ForeignKey('Gender', related_name='favorites', on_delete=models.CASCADE)
    #size = models.ForeignKey('Size', related_name='products', on_delete=models.CASCADE)
    size = models.ManyToManyField('Size')
    status = models.CharField(max_length=150)
    # status = models.ForeignKey('Status', related_name='products', on_delete=models.CASCADE)
    subcategory = models.ForeignKey('Subcategory', related_name='favorites', on_delete=models.CASCADE)
    new = models.BooleanField(default=False)
    # new = models.ForeignKey('New', related_name='products', on_delete=models.CASCADE)
    user_number=models.CharField(max_length=250, default='')
    useremail=models.CharField(max_length=250, default='')
    

    def get_absolute_url(self):
        return reverse('favorites', kwargs={"ai": self.ai, "name": self.name})

    def __str__(self):
        return self.name.name

    def get_color(self):
        return  "\n".join([c.name for c in self.color.all()])

    def get_size(self):
        return  "\n".join([c.name for c in self.size.all()])

    class Meta:
        ordering = ('-pk',)


class Size(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey('Subcategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='subcategory', default='')
    name = models.CharField(max_length=150,)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-pk',)


# 13
class New(models.Model):
    new = models.BooleanField(default=True)



# 14
class UserAlem(AbstractUser):
   phone = models.IntegerField(null=True)
   surname = models.TextField(max_length=100, default='')




    #def __str__(self):
       # return self.name

class Update(models.Model):
    update=models.BooleanField(default=False)




