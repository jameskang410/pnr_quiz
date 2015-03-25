# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Genres(models.Model):
    genre_id = models.IntegerField(blank=True, null=True)
    genre = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'genres'


class MovieGenres(models.Model):
    title_id = models.CharField(max_length=50, blank=True)
    genre_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_genres'


class NetflixMovies(models.Model):
    title = models.CharField(max_length=200, blank=True)
    title_id = models.CharField(max_length=50, blank=True)
    url = models.CharField(max_length=100, blank=True)
    box_art_link = models.CharField(max_length=100, blank=True)
    audience_score = models.IntegerField(blank=True, null=True)
    critic_score = models.IntegerField(blank=True, null=True)
    synopsis = models.TextField(blank=True)
    year = models.CharField(max_length=10, blank=True)
    duration = models.CharField(max_length=30, blank=True)
    cert_rating = models.CharField(max_length=10, blank=True)
    netflix_rating = models.CharField(max_length=10, blank=True)
    tv_show = models.CharField(max_length=1, blank=True)
    rotten_tomatoes_url = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=100, blank=True)
    small_box_art_link = models.CharField(max_length=100, blank=True)
    genre_no = models.IntegerField(blank=True, null=True)
    rt_id = models.CharField(max_length=50, blank=True)
    actors = models.TextField(blank=True)
    movie_pk = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'netflix_movies'


class PnrQuotes(models.Model):
    person = models.CharField(max_length=50, blank=True)
    quote = models.TextField(blank=True)
    quotes_key = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pnr_quotes'


class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'south_migrationhistory'


class Top25(models.Model):
    title = models.CharField(max_length=200, blank=True)
    title_id = models.CharField(max_length=50, blank=True)
    url = models.CharField(max_length=100, blank=True)
    box_art_link = models.CharField(max_length=100, blank=True)
    audience_score = models.IntegerField(blank=True, null=True)
    critic_score = models.IntegerField(blank=True, null=True)
    synopsis = models.TextField(blank=True)
    year = models.CharField(max_length=10, blank=True)
    duration = models.CharField(max_length=30, blank=True)
    cert_rating = models.CharField(max_length=10, blank=True)
    netflix_rating = models.CharField(max_length=10, blank=True)
    tv_show = models.CharField(max_length=1, blank=True)
    rotten_tomatoes_url = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=100, blank=True)
    small_box_art_link = models.CharField(max_length=100, blank=True)
    genre_no = models.IntegerField(blank=True, null=True)
    general_genre = models.CharField(max_length=50, blank=True)
    rank = models.IntegerField(blank=True, null=True)
    movie_pk = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'top_25'


class UpdatedNetflixMovies(models.Model):
    title = models.CharField(max_length=200, blank=True)
    title_id = models.CharField(max_length=50, blank=True)
    url = models.CharField(max_length=100, blank=True)
    box_art_link = models.CharField(max_length=100, blank=True)
    audience_score = models.IntegerField(blank=True, null=True)
    critic_score = models.IntegerField(blank=True, null=True)
    synopsis = models.TextField(blank=True)
    year = models.CharField(max_length=10, blank=True)
    duration = models.CharField(max_length=30, blank=True)
    cert_rating = models.CharField(max_length=10, blank=True)
    netflix_rating = models.CharField(max_length=10, blank=True)
    tv_show = models.CharField(max_length=1, blank=True)
    rotten_tomatoes_url = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=100, blank=True)
    small_box_art_link = models.CharField(max_length=100, blank=True)
    genre_no = models.IntegerField(blank=True, null=True)
    movie_pk = models.BigIntegerField(primary_key=True)
    general_genre = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'updated_netflix_movies'
