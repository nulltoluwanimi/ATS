from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Comment, Post


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        def clean_username(self):
            print(self.cleaned_data)
            data = self.cleaned_data['username']
            if '@' in data:
                raise ValidationError("you can not use @ in a user name!")

            # Always return a value to use as the new cleaned data, even if
            # this method didn't change it.
            return data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        # exclude = ('user', 'is_archived')
        initial = {
            "text": "your comment"
        }


class BlogForm(forms.Form):
    model = Post
    exclude = ('created_at', 'updated_at')
    # class Meta:
    #     ini
