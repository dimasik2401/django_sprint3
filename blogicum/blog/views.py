from django.shortcuts import get_object_or_404, render

from blog.constans import NUMBER_POSTS
from .models import Category, Post


def index(request):
    """Представление главной страницы блога."""
    post_list = Post.objects.published()[:NUMBER_POSTS]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Представление станицы поста."""
    return render(request, 'blog/detail.html', {'post': get_object_or_404(
        Post.objects.published(), pk=post_id)})


def category_posts(request, category_slug):
    """Представление страницы категории постов."""
    category_list = get_object_or_404(
        Category, is_published=True, slug=category_slug
    )
    post_list = category_list.post_set.published(category=None)
    context = {
        'category': category_list,
        'post_list': post_list
    }
    return render(request, 'blog/category.html', context)
