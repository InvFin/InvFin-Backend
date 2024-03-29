from django.forms import ModelForm, models

from src.general.forms import BaseEscritoForm

from .models import Term, TermContent, TermCorrection


class CreateCorrectionForm(ModelForm):
    class Meta:
        model = TermCorrection
        fields = ["title", "content", "term_content_related"]


class TermAndTermContentForm(BaseEscritoForm):
    class Meta(BaseEscritoForm.Meta):
        model = Term

    def save(self, *args, **kwrags):
        if kwrags.pop("modify_checking"):
            self.instance.modify_checking("information_clean", True)
            self.instance.modify_checking("request_improvement", True)
        return super().save(*args, **kwrags)


term_content_formset = models.inlineformset_factory(
    Term,
    TermContent,
    fields=["title", "order", "content"],
    extra=0,
    can_delete=False,
)
