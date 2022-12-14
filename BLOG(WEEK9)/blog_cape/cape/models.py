from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class ArchievedPost(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_archived=True)


class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_archived=False)


class CommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_archived=False)


class ArchievedComments(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_archived=True)


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="media", null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag)
    is_archived = models.BooleanField(default=False)

    objects = PostManager()
    archived_objects = ArchievedPost()

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('cape:blog-details', args=(str(self.id)))

    def save(self):
        print(self.author)
        self.slug = slugify(self.title)
        self.excerpt = self.content[:100]
        return super().save()

    def unarchive(self):
        self.is_archived = False
        return super().save()

    @property
    def post_tags(self):
        return self.tags.all()

    class Meta:
        permissions = (('can_check_archived', 'can checked archived'),)


# @receiver(pre_save, sender=Post)
# def my_callback(sender, instance, *args, **kwargs):
#     blogs = Post.objects.filter(slug__exact=instance.slug).count()
#     instance.excerpt = instance.content[:100] if len(instance.content) > 100 else None
#     print(blogs)
#     if blogs > 0:
#         instance.slug = slugify((instance.title + str(blogs)))
#     else:
#         instance.slug = slugify(instance.slug)

class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='comments')
    text = models.TextField(max_length=400)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    is_archived = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = CommentManager()
    archived_comments = ArchievedComments()

    def __str__(self):
        return f"{self.user} {self.text}"

    def archive_comment(self):
        self.is_archived = True
        return super().save()

    def unarchive_comment(self):
        self.is_archived = False
        return super().save(update_fields=self.is_archived)


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, related_name='user')
    image = models.ImageField(upload_to="posts", null=True)
    organization = models.CharField(max_length=100, null=True, default='')


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()
