from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group', 'image')
        labels = {
            'text': 'Текст поста',
            'group': 'Группа',
            'image': 'Картинка',
        }
        help_texts = {
            'text': 'Поле не должно быть пустым!',
            'group': 'Группа, к которой относиться пост.',
            'image': 'Изображение, относящееся к посту.',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
        labels = {
            'text': 'Текст комментария',
        }
        help_text = {
            'text': 'Введите текст комментария.',
        }
