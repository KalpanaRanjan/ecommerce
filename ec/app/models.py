from django.db import models

# Create your models here.
CATEGORY_CHOICES=(
    ('CR','Curd'),
    ('MI','Milk'),
    ('LS','Lassi'),
    ('MS','Milkshake'),
    ('PN', 'Paneer'),
    ('GH','Ghee'),
    ('CZ','Cheese'),
    ('IC','Ice-Creams'),
    ('KL','Kulfi'),
)
class Product(models.Model):
    tittle=models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price= models.FloatField()
    description= models.TextField()
    composition=models.TextField(default='')
    prodapp=models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image= models.ImageField(upload_to="product")

    def __str__(self):
        return self.tittle
    

class Users(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    contact=models.CharField(max_length=12)
    address=models.CharField(max_length=100 , default=True)
    password=models.CharField(max_length=30)

class Cart(models.Model):
    user=models.ForeignKey(Users,on_delete=models.CASCADE)  
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def total_cost(self):
        return self.quantity* self.product.discounted_price