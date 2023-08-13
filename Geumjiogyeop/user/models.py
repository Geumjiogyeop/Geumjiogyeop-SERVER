from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, phonenumber, password, **kwargs):
        if not phonenumber:
            raise ValueError('Users must have an phonenumber')
        user = self.model(
            phonenumber=phonenumber,
            **kwargs # 추가
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phonenumber=None, password=None, **extra_fields):
        superuser = self.create_user(
            phonenumber=phonenumber,
            password=password,
        )
        
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        
        superuser.save(using=self._db)
        return superuser

class User(AbstractBaseUser, PermissionsMixin):
    # user_id -> serialize=False가 문제가 되는 부분일수도 있음
    user_id = models.AutoField(primary_key=True) # id값 따로, 아이디용 고유번호 따로 두는게 나을 듯
    phonenumber = models.CharField(max_length=45, unique=True, null=False, blank=False)
    name = models.CharField(max_length=10, null=False, blank=False)
    birthday = models.CharField(max_length=8, null=False, blank=False) # YYYYMMDD
    gender = models.CharField(max_length=1, null=False, blank=False) # 남(m), 여(f)
    is_foreigner = models.BooleanField(default=False) # 내국인(False), 외국인(True)
    
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

	# 헬퍼 클래스 사용
    objects = UserManager()

	# 이메일로 로그인
    USERNAME_FIELD = 'phonenumber'

    def __str__(self):
        return str(1000 + self.user_id) # 1001부터 시작하는 문자열로 변환