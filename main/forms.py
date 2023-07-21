from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User ### у чела в видосе был был какой то собственный Buyer, а не User

