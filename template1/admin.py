from django.contrib import admin
from template1.models import Post,Hobby,Music,NhatKy
# Register  models Post.
class PostAdmin(admin.ModelAdmin):
    list_display:['title','date']
    list_filter:['date']
    search_fields:['title']
admin.site.register(Post,PostAdmin)

class HobbyAdmin(admin.ModelAdmin):
    list_display:['name','thumbnail']
admin.site.register(Hobby,HobbyAdmin)

class MusicAdmin(admin.ModelAdmin):
    list_display :['name']
admin.site.register(Music,MusicAdmin)

class NhatKyAdmin(admin.ModelAdmin):
    list_display:['content']
admin.site.register(NhatKy,NhatKyAdmin) 


