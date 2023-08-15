# Import necessary modules from Django
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


class PostList(generic.ListView):
    """
    View class for listing blog posts
    """

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')  # Fetch published posts, ordered by creation date # noqa E501
    template_name = 'blog/blog.html'  # Template used to render the list of posts # noqa E501
    paginate_by = 6  # Number of posts per page


class PostDetail(View):
    """
    View class for displaying a single blog post
    """

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


class PostLike(View):
    """
    View class for handling post likes
    """

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)  # Get the specific post with the provided slug # noqa E501

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)  # If user has already liked, remove their like # noqa E501
        else:
            post.likes.add(request.user)  # If user hasn't liked, add their like # noqa E501

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))  # Redirect to the post detail page # noqa E501


@login_required
def add_post(request):
    """
    Allows to create a post
    """
    form = PostForm(request.POST, request.FILES)

    if request.method == 'POST':

        if form.is_valid():

            post = form.save(commit=False)
            post.save()
            form = PostForm()
            messages.success(request, 'Successfully created post')
            return redirect('post_detail', post.slug)
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')  # noqa E501

    template = 'blog/post_add.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def update_post(request, slug):
    """ Update a post in the blog """

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to update the post. Please ensure the form is valid.')  # noqa E501
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are updating {post.title}')

    template = 'blog/post_edit.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, slug):
    """ Delete a post from the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog'))
