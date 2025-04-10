from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class categorie(models.Model):
    nom = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom
    
class article(models.Model):
    titre = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    date_publication = models.DateTimeField()
    description = models.TextField()
    auteur = models.ForeignKey(User,on_delete=models.CASCADE)
    categorie = models.ForeignKey(categorie, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titre}, {self.description }"
    

class commentaire(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.description}, {self.user.first_name}"