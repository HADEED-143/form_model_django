from django.shortcuts import render
from base.forms import PostCv

# Create your views here.
def form_view(request):
    form = PostCv()
    if request.method == 'POST':
        form = PostCv(request.POST)
        if form.is_valid():
            form.save()
    context = {"form":form}

    return render(request, "cvform.html", context)