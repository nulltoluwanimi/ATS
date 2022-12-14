import json

from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import SignupForm
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from .models import Post, Comment, Profile
from .forms import CommentForm, BlogForm


# Create your views here.
def home(request):
    context = {
        "user": request.user
    }
    print(request.user)
    return render(request, "cape/home.html", context)


def blogs(request):
    return render(request, 'cape/blogs.html')


class UserCreate(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UpdateUser(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = '__all__'
    success_url = reverse_lazy('index')


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title', 'content', 'tags', 'image')
    success_url = reverse_lazy('post')


class BlogList(ListView):
    model = Post
    ordering = ["-id"]


class BlogView(DetailView):
    model = Post

    # form_class = CommentForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogView, self).get_context_data()
        context['current_user'] = User.objects.get(username=self.request.user)
        context['blog_owner'] = self.get_object().author
        context[
            'optional_image'] = 'https://images.unsplash.com/photo-1453728013993-6d66e9c9123a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8dmlld3xlbnwwfHwwfHw%3D&w=1000&q=80'
        context['comments'] = Comment.objects.filter(post=self.get_object().id)
        context['archive_comments'] = Comment.archived_comments.all()
        context['comments_form'] = CommentForm()
        print(context["current_user"],
              context["blog_owner"], self.get_object().id)
        return context


@login_required
def SubmitComment(request, slug):

    if request.POST:
        print(request, slug)
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            # return HttpResponseRedirect(reverse("cape", args=[slug]))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        "post": post,
        "comment_form": comment_form,
        "comments": post.comments.all().order_by("-created_at")
    }
    return render(request, "cape/post_detail.html", context)
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def SubmitCommentWithAjax(request):
    if request.method == "POST":
        # print(json.load(request.POST.get('comment_form')))
        print(json.load(request.POST))


class ArchivedPost(LoginRequiredMixin, ListView):
    models = Post
    # permission_required = 'cape:can_check_archived'
    template_name = 'cape/archieved_list.html'

    def get_queryset(self):
        data = super(ArchivedPost, self).get_queryset()
        # print(self.get_object())
        return data.archieved_objects.all()


class Unarchived(View):
    pass
    # def post(self, request, slug):
    # blogs = Post.objects.get(slug=slug)
    # blogs
    # con
    # render


class ArchiveComment(View):
    def post(self, request, pk):
        try:
            comment = Comment.objects.get(id=pk)
        except:
            comment = Comment.archived_comments.get(id=pk)
        if not comment.is_archived:
            comment.archive_comment()
        else:
            comment.unarchive_comment()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        # return HttpResponseRedirect(reverse('post', args=(slug,)))


class BlogEditDetail(View):
    def get(self, request, slug):
        blog = Post.objects.get(slug=slug)
        context = {
            "blog": blog,
            "blog_form": BlogForm(),
            "current_user": self.request.user
            # "comments": blog.comments.all().order_by("-created_at")
        }
        return render(request, "cape/edit_blog.html", context)

    @method_decorator(login_required)
    def post(self, request, slug):
        blog_form = BlogForm(request.POST)
        blog = Post.objects.get(slug=slug)
        if blog_form.is_valid():
            blog = blog_form.save(commit=False)
            blog.blog = blog
            # blog.current_user = self.request.user
            blog.save()
            return HttpResponseRedirect(reverse("cape:post_detail", args=[slug]))
        context = {
            "blog": blog,
            "blog_form": blog_form,
            # "comments": blog.comments.all().order_by("-post_date")
        }
        return render(request, "blog/blog_detail.html", context)


class UserDetails(LoginRequiredMixin, DetailView):
    # model = Profile
    # context_object_name = 'logged_in_user'
    def get(self, request, pk):
        profile = Profile.objects.get(user_id=pk)
        current_user = User.objects.get(id=pk)
        # profile_form = ProfileForm(instance=profile)
        # user_form = UserForm(instance=current_user)

        # comments_for_blogger = Comment.objects.filter(blog__author=self.kwargs['pk']).count()
        context = {
            "user_detail": profile.user,
            # "total_comments": comments_for_blogger,
            # "user_form": user_form,
            "profile": profile,
            'current_user': current_user
            # "profile_form": profile_form,
        }
        return render(request, "cape/profile_detail.html", context)

    # def post(self, request, pk, *args, **kwargs):
    #     user = User.objects.get(id=pk)
    #     user_profile = Profile.objects.get(author_id=pk)
    #
    #     user_form = UserForm(request.POST, instance=user)
    #     profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)
    #
    #     if user_form.is_valid() and profile_form.is_valid():
    #         user_form.save()
    #         profile_form.save()
    #         return HttpResponseRedirect(reverse("blog:author-detail", args=[pk]))
    #
    #     comments_for_blogger = Comment.objects.filter(blog__author=self.kwargs['pk']).count()
    #     context = {
    #         'user_detail': user_profile.author,
    #         'total_comments': comments_for_blogger,
    #         'profile_form': profile_form
    #     }
    #     return render(request, "blog/user_detail.html", context)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user_details'] = User.objects.get(id=self.get_object().pk)
    #     print(1, context['user_details'])
    #     return context

    # def get_context_data(self, **kwargs):
    #     context = super(BlogView, self).get_context_data()
    #     image = Post.author


# Create your views here.
# class IndexPageView(View):
#     def get(self, request):
#         num_blogs = Blog.objects.all().count()
#         num_comments = Comment.objects.all().count()
#         num_bloggers = User.objects.all().count()
#         num_visits = request.session.get('num_visits', 0)
#         request.session['num_visits'] = num_visits + 1
#         user = self.request.user
#         if user != AnonymousUser:
#             current_user = user
#         else:
#             current_user = None
#         context = {
#             "num_blogs": num_blogs,
#             "num_comments": num_comments,
#             "num_bloggers": num_bloggers,
#             "num_visits": num_visits,
#             "current_user": current_user
#         }
#         return render(request, "blog/index.html", context)


# class BlogAuthorDetailView(DetailView):
#     model = User
#     template_name = "blog/user_detail.html"
#     context_object_name = "user_detail"
#
#     def get_context_data(self, **kwargs):
#         context = super(BlogAuthorDetailView, self).get_context_data(**kwargs)
#         comments_for_blogger = Comment.objects.filter(
#             blog__author=self.kwargs['pk']).count()
#         context['total_comments'] = comments_for_blogger
#         return context
#
#
# class BlogPostDetailPage(View):
#     def get(self, request, slug):
#         blog = Post.objects.get(slug=slug)
#         context = {
#             "blog": blog,
#             "comment_form": CommentForm(),
#             "comments": blog.comments.all().order_by("-created_at")
#         }
#         return render(request, "blog/blog_detail.html", context)
#
#     @method_decorator(login_required)
#     def post(self, request, slug):
#         comment_form = CommentForm(request.POST)
#         blog = Post.objects.get(slug=slug)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.blog = blog
#             comment.comment_owner = self.request.user
#             comment.save()
#             return HttpResponseRedirect(reverse("blog:blog-detail", args=[slug]))
#         context = {
#             "blog": blog,
#             "comment_form": comment_form,
#             "comments": blog.comments.all().order_by("-post_date")
#         }
#         return render(request, "blog/blog_detail.html", context)


class BloggersListView(ListView):
    model = User
    # template_name = "blog/user_list.html"
    # ordering = ["first_name"]
# logging in, logging out
# admin siteCollapse
