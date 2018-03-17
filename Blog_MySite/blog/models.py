from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # since only one person is using the blog
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)  # may not be published; can leave empty

    #  update publish date
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        # the comments refer to related_name in Comment class
        # approved_comment has to match from that of Comment class property
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        # may wanna review CBV
        # when Post is created take me to detail page where pk matches
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        # could return to the post detail page; try later
        return reverse('post_list')

    def __str__(self):
        return self.text

