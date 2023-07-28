from django.db import models

# Create your models here.
class Login(models.Model):
    login = models.CharField("Login",max_length=40)
    password = models.CharField("Password",max_length=40)
    

    def __str__(self):
        return self.login
    
    def get_absolute_url(self):
        return "/"

    class Meta:
        verbose_name = "login"
        verbose_name_plural = "logins"