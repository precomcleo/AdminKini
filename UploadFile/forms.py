from django import forms
from .models import Photo

class UploadModelForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }

class FileForm(forms.Form):
    file = forms.FileField(
        # 支援多檔案上傳
        widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control-file'}),
        label='',
    )