from django import forms
from .models import Post, Category

#choices = [('Musica', 'Musica'),('Pelicula', 'Pelicula')]
choices = Category.objects.all().values_list('nombre', 'nombre')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'titulo_tag', 'autor', 'categoria','header_image', 'body')

        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'titulo_tag': forms.TextInput(attrs={'class':'form-control'}),
            'autor': forms.Select(attrs={'class':'form-control'}),
            'categoria': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),


        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'titulo_tag', 'body')

        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'titulo_tag': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),


        }