from django.shortcuts import render, get_object_or_404


def comments(request):
    template = 'comments/comments.html'

    return render(request, template)
