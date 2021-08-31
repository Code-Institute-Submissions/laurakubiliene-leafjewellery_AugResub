from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import ReviewForm


def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'Successfully added review!')
            form.save()
            return redirect(reverse('reviews'))
        else:
            messages.error(
                request,
                'Failed to add review. Please ensure the form is valid.')
    else:
        form = ReviewForm()

    template = 'reviews/reviews.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
