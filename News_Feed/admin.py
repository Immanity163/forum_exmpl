from django.contrib import admin
from .models import Creator,Post,Comment,Category


admin.site.register(Creator)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
