from .models import CustomUser
from django import forms


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        if len(self.cleaned_data["password"]) < 16:
            user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
