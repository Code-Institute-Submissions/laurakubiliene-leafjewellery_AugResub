from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .forms import ReviewForm


def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('reviews'))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')
    else:
        form = ReviewForm()

    template = 'reviews/reviews.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
