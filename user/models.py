from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

USER_ROLE = (
    ('CUSTOMER' ,'customer'),
    ('VENDOR' , 'vendor'),
    ('ADMIN' , 'admin'),
)

phone_regex = RegexValidator(
    regex = r'^\+?1?\d{6,15}$',
    message= _('Phone Number should start with +')
)

# Create your models here.
class CustomUser(AbstractUser):
    email=models.EmailField(
        unique=True,
        verbose_name=_('Email Address'),
        help_text=_('A valid email address is required!')
    )

    username= models.CharField(
        unique=True,
        max_length=32,
        verbose_name=_('Username'),
        help_text=_('Unique username is required'),
        blank=True,
        null=False
    )

    role = models.CharField(
        max_length=10,
        choices=USER_ROLE,
        default='CUSTOMER',
        verbose_name=_('User Role')
    )

    # personal information
    first_name = models.CharField(
        max_length=32,
        verbose_name=_('First Name')    
    )

    last_name= models.CharField(
        max_length=32,
        verbose_name=_('Last Name')
    )

    phone = models.CharField(
        validators=[phone_regex],
        max_length=17,
        verbose_name=_('Phone Number')
    )

    # address fields
    address_line_1 = models.CharField(max_length=100, verbose_name=_('Address Line 1'))
    address_line_2 = models.CharField(max_length=100,  blank=True, null=True, verbose_name=_('Address Line 2'))
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('City'))
    state_province = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('State/Province'))
    postal_code = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('Postal/Zip Code'))
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('Country'))
    
    #additional information
    date_of_birth = models.DateField(blank=True, null=True, verbose_name=_('Date of Birth'))
    profile_picture_url = models.URLField(blank=True, null=True, verbose_name=_('Profile Picture URL'))
    is_newsletter_subscribed = models.BooleanField(default=False, verbose_name=_('Newsletter Subscription'))

    #account status
    date_joined = models.DateField(auto_now=True, verbose_name=_('Date Joined'))
    last_login = models.DateField(auto_now=True, verbose_name=_('Last Login'))
    is_verified = models.BooleanField(default=False, verbose_name=_('Verfication'))

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']


    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['-date_joined'] 

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email 
    
    @property
    def is_vendor(self):
        return self.role == 'VENDOR'
    
    @property
    def is_customer(self):
        return self.role == 'CUSTOMER'
    
    @property
    def is_admin(self):
        return self.role == 'ADMIN'