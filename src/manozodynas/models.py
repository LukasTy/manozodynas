import re
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core import validators
from django.db import models
from django.utils import timezone
from random import sample


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=30, unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, numbers and '
                    '@/./+/-/_ characters'),
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), 'invalid')
        ])
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    email = models.EmailField(_('Email address'), max_length=254, unique=True)
    email_approved = models.BooleanField(_('Was email approved'), default=False)

    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=False,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    organization = models.TextField(_('Organization'), null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

class Word(models.Model):
    word = models.CharField(max_length=255)


    def __str__(self):
        return self.word

    @classmethod
    def get_random_word(cls):
        # Get all table contents
        all_words = Word.objects.all()
        # Get random word from existing ones
        random_word = sample(all_words,1)
        return random_word[0]
    @classmethod
    def get_random_words(cls, count):
        #Get all table contents
        all_words = Word.objects.all()
        #Get random words from existing ones
        random_words = sample(all_words, int(count))
        return random_words
