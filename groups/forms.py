import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Group


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = "__all__"

    def clean_group_name(self):
        group_name = self.cleaned_data['group_name']
        # Validate group_name length
        if len(group_name) < 2:
            raise ValidationError("Group name should be at least 2 characters long.")
        # Validate group_name contains only letters
        if not re.match(r'^[a-zA-Z]*$', group_name):
            raise ValidationError("Group name should only contain letters.")

        return group_name
