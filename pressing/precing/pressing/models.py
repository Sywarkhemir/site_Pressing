from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail

class Client(models.Model):
    user = models.OneToOneField(User, related_name='user_client',blank=True, null=True,on_delete=models.CASCADE)
    phone = models.CharField(max_length=8,blank=True,default='')
    adress = models.CharField(max_length=255,blank=True,default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Lenge(models.Model):
    choix =(
    ('4',('Delivered')),
    ('3',('Ready')),
    ('2',('In progress')),
    ('1',('Waiting'))
    )
    author = models.ForeignKey(User,null=True, blank=True, related_name='client_lenge',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    typeoflenge = models.CharField(max_length=255)
    quantityoflenge = models.IntegerField(default=0)
    caseoflenge = models.CharField(default='1',choices=choix,max_length=255)
    weight=models.DecimalField(max_digits=10, decimal_places=2)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    dateofreceive = models.DateTimeField(auto_now_add=True)
    dateoftake= models.DateField()

    def __str__(self):
        return self.author.username

class ClientComment(models.Model):

    client = models.ForeignKey(User,null=True, blank=True, related_name='client_comment',on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client.username

    class Meta:
        ordering = ('-created_at',)

    @property
    def stars(self):
        return '<i class="fas fa-star filled"></i>'*int(self.rating)



class NotifierClient(models.Model):
    client = models.ForeignKey(User, related_name='notif',on_delete=models.CASCADE,blank=True)
    content = models.CharField(max_length=255,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.client.username
