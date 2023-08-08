# Import necessary modules from Django
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post


# View class for listing blog posts
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')  # Fetch published posts, ordered by creation date # noqa E501
    template_name = 'blog/blog.html'  # Template used to render the list of posts # noqa E501
    paginate_by = 6  # Number of posts per page


# View class for displaying a single blog post
class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)  # Fetch published posts
        post = get_object_or_404(queryset, slug=slug)  # Get the specific post with the provided slug # noqa E501
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True  # Check if the current user has liked the post

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "liked": liked,
            },
        )  # Render the post detail template with the post and liked status

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)  # Fetch published posts
        post = get_object_or_404(queryset, slug=slug)  # Get the specific post with the provided slug # noqa E501
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True  # Check if the current user has liked the post

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "liked": liked,
            },
        )  # Render the post detail template with the post and liked status


# View class for handling post likes
class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)  # Get the specific post with the provided slug # noqa E501

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)  # If user has already liked, remove their like # noqa E501
        else:
            post.likes.add(request.user)  # If user hasn't liked, add their like # noqa E501

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))  # Redirect to the post detail page # noqa E501
