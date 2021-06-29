from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import CommentForm


def comments(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'Successfully added comment!')
            return redirect(reverse('comments'))
        else:
            messages.error(
                request,
                'Failed to add comment. Please ensure the form is valid.')
    else:
        form = CommentForm()

    template = 'comments/comments.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
