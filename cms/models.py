from django.utils import timezone
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_uploader = models.BooleanField(default=False)
    is_webuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name_plural = 'Users'


class Contests(models.Model):
    # author = models.ForeignKey('auth.User')
    author = models.ForeignKey('cms.MyUser')
    title = models.CharField(max_length=200)
    description = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    publish_duration = models.DateTimeField(blank=True, null=True)
    banner = models.CharField(max_length=200)
    points = models.IntegerField(default=0)

    
    def publish(self):
        self.publish_schedule = timezone.now()
        self.save()

    
    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = 'Contests'



class Answers(models.Model):
    question = models.ForeignKey(Contests)
    answer_text = models.CharField(max_length=200)
    correct_answer = models.BooleanField(verbose_name='This is the correct answer',default=False)


    def __str__(self):
        return self.answer_text


    class Meta:
        verbose_name_plural = 'Answers'


class Locations(models.Model):
    name = models.CharField(max_length=100)
    # schedule = models.TextField()
    schedule = models.CharField(max_length=200)
    # address = models.TextField()
    address = models.CharField(max_length=500)
    timestamp = models.DateTimeField(default=timezone.now)
    # author = models.CharField(max_length=200,default=timezone.now())

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Locations'


class Product(models.Model):
    # location = models.ForeignKey(Locations)
    name = models.CharField(max_length=200)
    info = models.TextField()
    banner = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Promotions(models.Model):
    location = models.ForeignKey(Locations)
    name = models.CharField(max_length=200)
    info = models.TextField()
    banner = models.CharField(max_length=200)
    tag_account = models.ForeignKey('cms.MyUser')
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Promotions'


class Rewards(models.Model):
    REWARD_TYPE_CHOICES = (
        ('r', 'Redeemable'),
        ('p', 'Points'),
    )
    name = models.TextField(max_length=200)
    info = models.TextField()
    reward_type = models.CharField(choices=REWARD_TYPE_CHOICES,default='p',max_length=1)
    reward_value = models.IntegerField(default=0)
    banner = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Rewards'


class Respondents(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contest = models.ForeignKey(Contests)
    answer = models.ForeignKey(Answers)

    class Meta:
        verbose_name_plural = 'Respondents'

