from ckeditor.widgets import CKEditorWidget
from django.forms import CharField, ModelForm, ValidationError

from .models import Answer, Question


class CreateQuestionForm(ModelForm):

    class Meta:
        model = Question
        exclude = [
            'author',
            'created_at',
            'slug',
            'created_at',
            'updated_at',
            'total_votes',
            'total_views',
            'times_shared',
            'is_answered',
            'has_accepted_answer',
            'tags',
            "upvotes",
            "downvotes",
            'category']

    def clean_title(self):
        title = self.cleaned_data['title']

        if len(title) < 8:
            raise ValidationError("Formula tu pregunta para que la comunidad pueda ayudarte")

        if title == '¿Cuál es tu pregunta?':
            raise ValidationError("Formula tu pregunta para que la comunidad pueda ayudarte")
        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 10:
            raise ValidationError("Detalla precisamente tu pregunta para que la comunidad pueda ayudarte.")
        return content


class CreateAnswerForm(ModelForm):
    content = CharField(widget=CKEditorWidget(config_name='writter'))
    class Meta:
        model = Answer
        exclude = [
            'author',
            'created_at',
            'question_related',
            'created_at',
            'is_accepted',
            "upvotes",
            "downvotes",
            'total_votes']
