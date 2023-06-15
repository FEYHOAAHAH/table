from django.contrib import admin

from .models import Products
from .models import Orders
from .models import Users
from .models import Mouses
from .models import Keyboards
from .models import Headphones
from .models import Gamepads
from .models import Notebooks

# Register your models here.


# Register your models here.

admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(Users)
admin.site.register(Mouses)
admin.site.register(Keyboards)
admin.site.register(Headphones)
admin.site.register(Gamepads)
admin.site.register(Notebooks)
