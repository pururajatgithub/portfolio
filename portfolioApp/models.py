from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    category_image = models.ImageField(upload_to='images/category/', blank=False, null=False)

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_category_list():
        return Category.objects.all()



class Images(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/Images', null=False, blank=False)
    

    def __str__(self):
        return self.category.name + ' - ' + self.image.name

    @staticmethod
    def get_images_by_id(id):
        return Images.objects.filter(id__in = ids)
    
    @staticmethod
    def get_images_list():
        return Images.objects.all()

    @staticmethod
    def get_images_list_by_category(category_id):

        if category_id:
            return Images.objects.filter(category=category_id) 
        else:
            return get_images_list() 



    