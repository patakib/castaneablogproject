from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse

class Post(models.Model):
    STATUS_CHOICES = (
            ('draft', 'Draft'),
            ('published', 'Published'),
        )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
            unique_for_date='publish')
    body = RichTextField(blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, 
            choices=STATUS_CHOICES,
            default='draft')

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                args=[self.publish.year,
                    self.publish.month,
                    self.publish.day, self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
        

