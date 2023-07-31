from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Review
from .forms import ReviewForm


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'reviews/reviews.html'
    paginate_by = 6


@login_required
def add_review(request):
    """
    Allows to create a new ad
    """
    form = ReviewForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            form = ReviewForm()
            messages.success(request, 'Successfully created')
            return redirect(reverse('reviews'))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')  # noqa E501
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def update_review(request, review_id):
    """ Edit a product in the store """

    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('reviews'))
        else:
            messages.error(request, 'Failed to update review. Please ensure the form is valid.')  # noqa E501
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing {review.title}')

    template = 'reviews/update_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a product from the store """

    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('reviews'))
