from django.shortcuts import redirect, render

from .forms import GroupForm
from .models import Group


def group_create(request):
    """Group page."""
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("get_groups_list")
    else:
        form = GroupForm()
    return render(request, "group.html", {"title": "Group", "form": form})


def get_groups_list(request):
    """Get all groups."""
    groups = Group.objects.all().values()
    return render(
        request, "all_groups.html", {"groups": groups, "title": "All Groups"}
    )

