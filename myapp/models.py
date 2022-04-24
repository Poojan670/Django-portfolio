from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    name = models.CharField(max_length=20, blank=True, null=True)

    score = models.IntegerField(default=80, blank=True, null=True)

    image = models.FileField(blank=True, null=True, upload_to='skills')

    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = ' User Profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to="avatar", blank=True, null=True)

    title = models.CharField(max_length=100, blank=True, null=True)

    bio = models.TextField(blank=False, null=True)

    skills = models.ManyToManyField(Skill, blank=True)

    cv = models.FileField(blank=True, null=True, upload_to="cv")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class ContactProfile(models.Model):

    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)

    name = models.CharField(verbose_name="Name",
                            help_text="Please enter your name:", max_length=50)

    email = models.EmailField(verbose_name="Email", unique=True, blank=False)

    message = models.TextField(verbose_name="Message", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Testimonials(models.Model):

    class Meta:
        verbose_name_plural = "Testimonials"
        verbose_name = 'Testimonial'
        ordering = ['name']

    thumbnail = models.ImageField(blank=False, upload_to='testimonials')

    name = models.CharField(max_length=30, blank=False, null=False)

    role = models.CharField(max_length=20, blank=False, null=False)

    quote = models.CharField(max_length=40, blank=False, null=False)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Media(models.Model):

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]

    image = models.ImageField(blank=True, null=True, upload_to="media")

    url = models.URLField(blank=True, null=True)

    name = models.CharField(blank=False, null=False, max_length=30)

    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False

        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Portfolio(models.Model):

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'

    date = models.DateTimeField(blank=True, null=True)

    name = models.CharField(max_length=40, blank=False, null=False)

    description = models.CharField(max_length=500, blank=True, null=True)

    body = RichTextField(blank=True, null=True)

    image = models.ImageField(blank=True, null=True, upload_to="portfolio")

    slug = models.SlugField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"


class Blog(models.Model):

    class Meta:
        verbose_name = 'Blog '
        verbose_name_plural = 'Blog Profiles'
        ordering = ['timestamp']

    timestamp = models.DateTimeField(auto_now_add=True)

    author = models.CharField(max_length=30, blank=False, null=False)

    description = models.CharField(max_length=500, blank=True, null=True)

    name = models.CharField(max_length=40, blank=False, null=False)

    body = RichTextField(blank=True, null=True)

    image = models.ImageField(blank=True, null=True, upload_to="blog")

    slug = models.SlugField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"


class Certificate(models.Model):
    class Meta:
        verbose_name = 'Certificate '
        verbose_name_plural = 'Certificates'

    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=40, blank=False, null=False)
    title = models.CharField(max_length=30, blank=False, null=False)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
