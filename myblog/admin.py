from django.contrib import admin
from .models import Post

# Register your models here.


class adminPost(admin.ModelAdmin):
    list_display = ["header", "date", "slug"]
    list_display_links = ["date"]
    list_filter = ["date"]
    search_fields = ["header", "text"]
    list_editable = ["header"]

    class Meta:
        model = Post


admin.site.register(Post, adminPost)
