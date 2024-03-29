from django.forms import ModelForm, ValidationError

from .models import Question


class CreateQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = [
            "title",
            "content",
        ]

    def clean_title(self):
        title = self.cleaned_data["title"]

        if len(title) < 8:
            raise ValidationError("Formula tu pregunta para que la comunidad pueda ayudarte")

        if title == "¿Cuál es tu pregunta?":
            raise ValidationError("Formula tu pregunta para que la comunidad pueda ayudarte")
        return title

    def clean_content(self):
        content = self.cleaned_data["content"]
        if len(content) < 10:
            raise ValidationError(
                "Detalla precisamente tu pregunta para que la comunidad pueda ayudarte."
            )
        return content
