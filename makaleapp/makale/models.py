from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True  )
    description = models.TextField(blank=True, null=True  )

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    konu = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    
class Bugün(models.Model):
    söz = models.CharField(max_length=200)
    söz_aciklama = models.TextField(default='Varsayılan Değer')
    gün = models.CharField (max_length=200 , null=True, blank=True)
    gün_aciklama=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.söz

class afiş(models.Model):
    afiş_ad = models.CharField (max_length=200 , null=True, blank=True)

    def __str__(self):
        return self.afiş_ad  
    
class daha_sorular(models.Model):
    sorular = models.TextField(default='Çok yakında...')

    def __str__(self):
        return self.sorular
    
class daha_yenilik(models.Model):
      yenilik = models.TextField(max_length=100)

      def __str__(self):
        return self.yenilik
