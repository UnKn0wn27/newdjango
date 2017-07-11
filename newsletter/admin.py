from django.contrib import admin
from .models import SignUp
from .forms import SignUpForm

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "updated"]

    form = SignUpForm
    # class Meta:
    #     model = SignUp

admin.site.register(SignUp, SignUpAdmin)