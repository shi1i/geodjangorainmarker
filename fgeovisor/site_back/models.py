from django.contrib.gis.db import models
from django.contrib.auth.models import User
import uuid


# Модель полигона
class Polygon(models.Model):
    polygon_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    polygon_data = models.PolygonField()
    image_id = models.ForeignKey('Image', verbose_name=("img_id"), on_delete=models.SET_NULL, blank=True, null=True)
    user_id = models.ForeignKey(User, verbose_name=("created by"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Полигон - {self.user_id}, создан - {self.created_at}"

# Модель изображения
class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.ImageField(upload_to='IMAGES') # Ссылка на изображение или путь в хранилище
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url

# Временное хранилище данных сессии пользователя
class SessionStorage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.JSONField()  # Хранение временных данных сессии (например, черновики)
    expires_at = models.DateTimeField()  # Время истечения сессии

    def __str__(self):
        return f"Сессия для {self.user} истекает в {self.expires_at}"

# Модель для отслеживания активности пользователей
class ActivityLog(models.Model):
    ACTION_CHOICES = (
        ('created_polygon', 'Created Polygon'),
        ('updated_polygon', 'Updated Polygon'),
        ('deleted_polygon', 'Deleted Polygon'),
        ('uploaded_image', 'Uploaded Image'),
        ('deleted_image', 'Deleted Image'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activity_logs')
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    details = models.JSONField()  # Дополнительная информация о действии в формате JSON
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} в {self.created_at}"


# Данная структура нужна, если у нас один полигон может иметь много изображений и наоборот
'''
class Polygon_Image_Mapping(models.Model):
    user_id = models.ForeignKey("models.User", verbose_name=("login"), on_delete=models.CASCADE)
    polygons_id = models.ForeignKey("models.Polygon", verbose_name=("poly_id"), on_delete=models.CASCADE)
    images_id = models.ForeignKey("models.Image", verbose_name=("img_id"), on_delete=models.CASCADE)
'''