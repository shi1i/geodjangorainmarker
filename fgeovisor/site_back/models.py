import uuid
from django.contrib.gis.db import models
from django.contrib.auth.models import User


# Модель полигона
class Polygon(models.Model):
    polygon_id = models.UUIDField(primary_key=True, default=uuid.uuid4, 
                                    editable=False)
    polygon_data = models.PolygonField()
    login = models.ForeignKey(User, related_name=('polygons'), 
                                verbose_name=("created by"), 
                                on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['login', 'polygon_data']

    def __str__(self):
        return f"Полигон - {self.login}, создан - {self.created_at}"

# Модель изображения
class Image(models.Model):
    polygon = models.ForeignKey(Polygon, related_name=('images'), 
                                    on_delete=models.CASCADE)
    # Ссылка на изображение или путь в хранилище
    url = models.ImageField(upload_to='fgeovisor/site_back/IMAGES')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Временное хранилище данных сессии пользователя
class SessionStorage(models.Model):
    login = models.ForeignKey(User, on_delete=models.CASCADE)
    # Хранение временных данных сессии (например, черновики)
    data = models.JSONField()
    expires_at = models.DateTimeField()  # Время истечения сессии

    def __str__(self):
        return f"Сессия для {self.login} истекает в {self.expires_at}"


# Модель для отслеживания активности пользователей
class ActivityLog(models.Model):
    ACTION_CHOICES = (
        ('created_polygon', 'Created Polygon'),
        ('updated_polygon', 'Updated Polygon'),
        ('deleted_polygon', 'Deleted Polygon'),
        ('uploaded_image', 'Uploaded Image'),
        ('deleted_image', 'Deleted Image'),
    )
    login = models.ForeignKey(User, on_delete=models.CASCADE, 
                                related_name='activity_logs')
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    # Дополнительная информация о действии в формате JSON
    details = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.login.username} - {self.action} в {self.created_at}"