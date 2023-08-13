from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from .models import Review
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReviewForm, AddReviewForm


class ReviewList(generic.ListView):
    """
    Class to show existing reviews
    """

    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'reviews/reviews.html'
    paginate_by = 6


# @login_required
# def add_review(request):
#     """
#     Allows to create a review
#     """
#     form = ReviewForm(request.POST, request.FILES)
#     if request.method == 'POST':
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.author = request.user
#             review.save()
#             form = ReviewForm()
#             messages.success(request, 'Your review was successfully created and now is waiting for approval by the administrator.')  # noqa E501
#             return redirect(reverse('reviews'))
#         else:
#             messages.error(request, 'Failed to add review. Please ensure the form is valid.')  # noqa E501
#     else:
#         form = ReviewForm()

#     template = 'reviews/add_review.html'
#     context = {
#         'form': form,
#     }

#     return render(request, template, context)

class ReviewCreateView(LoginRequiredMixin, CreateView):
    """
    VIEW TO CREATE A REVIEW
    """

    form_class = AddReviewForm
    template_name = 'reviews/add_review.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        from checkout.models import Order, OrderLineItem
        from products.models import Product
        order = Order.objects.get(order_number=self.kwargs['order_number'])  # noqa E501
        form.instance.order = order
        service = OrderLineItem.objects.get(order=order)
        form.instance.service_id = service.product.pk
        super().form_valid(form)
        messages.success(self.request, "Added a new Review! Please wait for our admin to accept and publish.")  # noqa E501
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(ReviewCreateView, self).get_context_data(**kwargs)
        context['order_number'] = self.kwargs['order_number']
        return context

    def get_success_url(self):
        return reverse('reviews')


@login_required
def update_review(request, review_id):
    """ Update a review in the store """

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
        messages.info(request, f'You are updating {review.title}')

    template = 'reviews/update_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


class DeleteReview(LoginRequiredMixin, generic.DeleteView):
    """
    View that allows logged in users to delete a review.
    The user us prompted with a warning.
    """
    model = Review
    template_name = 'reviews/delete_review.html'

    def delete(self, request, *args, **kwargs):
        """
        Method to validate owner against logged in user.
        """
        review = self.get_object()
        if review.author != request.user:
            return PermissionDenied()
        return super(DeleteReview, self).delete(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        messages.success(self.request, 'You have deleted a review!')
        return reverse_lazy('reviews')
