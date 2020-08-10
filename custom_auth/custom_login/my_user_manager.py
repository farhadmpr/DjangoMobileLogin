from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, mobile, password=None, **other_fields):
        if not mobile:
            raise ValueError('mobile is required')
        user = self.model(mobile=mobile, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, mobile, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser')

        return self.create_user(mobile, password, **other_fields)
