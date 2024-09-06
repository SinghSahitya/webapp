from django.contrib import admin
from .models import Poem, Gift, Letters
# Register your models here.
admin.site.register(Poem)
admin.site.register(Gift)
admin.site.register(Letters)