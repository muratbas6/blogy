from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    header = models.CharField(max_length=30)
    text = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False,
                            max_length=50, default="ops")

    def __str__(self):
        return self.header

    def get_unique_slug(self):
        slug = slugify(self.header)
        unique_slug = slug
        counter = 1

        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = slug + "-" + str(counter)
            counter += 1

        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()

        return super(Post, self).save(*args, **kwargs)
