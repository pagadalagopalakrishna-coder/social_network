from django.contrib import admin
from api.models import FriendRequest, Friendship, CustomUser
# Register your models here.

admin.site.register(FriendRequest)
admin.site.register(Friendship)
admin.site.register(CustomUser)