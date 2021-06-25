from django.shortcuts import render, get_object_or_404


def reviews(request):
    template = 'reviews/reviews.html'

    return render(request, template)
