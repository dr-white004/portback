from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    bio = models.TextField()
    years_of_experience = models.PositiveIntegerField()
    projects_completed = models.PositiveIntegerField()
    contact_email = models.EmailField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class Portfolio(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolios')
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    hero_image = models.URLField()
    project_type = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    duration = models.CharField(max_length=100)
    tools = models.JSONField()
    role = models.JSONField()
    problem = models.TextField()
    solution = models.TextField()
    images = models.JSONField()
    results = models.TextField()
    project_link = models.URLField()

    def __str__(self):
        return self.title

