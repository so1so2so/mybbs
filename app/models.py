#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Article(models.Model):
    """
    帖子
    """
    pass
class Commont(models.Model):
    """
    评论
    """
    pass
class module(models.Model):
    """
    板块
    """
    pass

class Userinfo(models.Model):
    """
    用户
    """
    pass
