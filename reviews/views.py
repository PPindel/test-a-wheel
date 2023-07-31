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
    form = ReviewForm(request.POST or None, request.FILES or None)
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

# @login_required
# def add_review(request):
#     """ Add a product to the store """
#     # if not request.user.is_superuser:
#     #     messages.error(request, 'Sorry, only store owners can do that.')
#     #     return redirect(reverse('home'))

#     if request.method == 'POST':
#         form = ReviewForm(request.POST, request.FILES)
#         if form.is_valid():
#             review = form.save()
#             messages.success(request, 'Successfully added review!')
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


# @login_required
# def update_review(request, review_id):
#     """ Edit a product in the store """
#     if not request.user.is_superuser:
#         messages.error(request, 'Sorry, only store owners can do that.')
#         return redirect(reverse('home'))

#     product = get_object_or_404(Product, pk=product_id)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Successfully updated product!')
#             return redirect(reverse('product_detail', args=[product.id]))
#         else:
#             messages.error(request, 'Failed to update product. Please ensure the form is valid.')  # noqa E501
#     else:
#         form = ProductForm(instance=product)
#         messages.info(request, f'You are editing {product.name}')

#     template = 'products/edit_product.html'
#     context = {
#         'form': form,
#         'product': product,
#     }

#     return render(request, template, context)


# @login_required
# def delete_review(request, review_id):
#     """ Delete a product from the store """
#     if not request.user.is_superuser:
#         messages.error(request, 'Sorry, only store owners can do that.')
#         return redirect(reverse('home'))

#     product = get_object_or_404(Product, pk=product_id)
#     product.delete()
#     messages.success(request, 'Product deleted!')
#     return redirect(reverse('products'))
