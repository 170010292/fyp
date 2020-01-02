# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Airlinecompany(models.Model):
    airlinecompanyid = models.AutoField(primary_key=True)
    airlinecompanyname = models.CharField(max_length=200)
    airlinecompanyno = models.CharField(max_length=8)
    airlinecompanyaddress = models.CharField(max_length=200)
    airlinecompanyemail = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'airlinecompany'


class Airplane(models.Model):
    airplaneid = models.AutoField(primary_key=True)
    airlinecompanyid = models.ForeignKey(Airlinecompany, models.DO_NOTHING, db_column='airlinecompanyid')
    checkinport = models.CharField(max_length=3)
    meal = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'airplane'


class Airplaneticket(models.Model):
    airplaneticketid = models.AutoField(primary_key=True)
    destination = models.CharField(max_length=100)
    starttime = models.DateTimeField()
    scheduledtime = models.DateTimeField()
    airplaneid = models.ForeignKey(Airplane, models.DO_NOTHING, db_column='airplaneid')
    price = models.DecimalField(max_digits=10, decimal_places=0)
    seat = models.CharField(max_length=3)
    seatingplace = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'airplaneticket'


class Attraction(models.Model):
    attractionid = models.AutoField(primary_key=True)
    attractioncompanyid = models.ForeignKey('Attractioncompany', models.DO_NOTHING, db_column='attractioncompanyid')
    attractionname = models.CharField(max_length=200)
    attractionaddress = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'attraction'


class Attractioncompany(models.Model):
    attractioncompanyid = models.AutoField(primary_key=True)
    attractioncompanyname = models.CharField(max_length=200)
    attractioncompanyno = models.CharField(max_length=8)
    attractioncompanyaddress = models.CharField(max_length=200)
    attractioncompanyemail = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'attractioncompany'


class Attractionticket(models.Model):
    attractionticketid = models.AutoField(primary_key=True)
    attractionid = models.ForeignKey(Attraction, models.DO_NOTHING, db_column='attractionid')
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'attractionticket'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
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


class Food(models.Model):
    foodid = models.CharField(primary_key=True, max_length=10)
    foodcompanyid = models.ForeignKey('Foodcompany', models.DO_NOTHING, db_column='foodcompanyid')
    foodname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'food'


class Foodcompany(models.Model):
    foodcompanyid = models.CharField(primary_key=True, max_length=3)
    foodcompanyname = models.CharField(max_length=200)
    foodcompanyno = models.CharField(max_length=8)
    foodcompanyaddress = models.CharField(max_length=200)
    foodcompanyemail = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'foodcompany'


class Fooddelivered(models.Model):
    foodid = models.ForeignKey(Food, models.DO_NOTHING, db_column='foodid')
    fooddeliveredid = models.CharField(primary_key=True, max_length=10)
    calltime = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'fooddelivered'


class Hotel(models.Model):
    hotelid = models.CharField(primary_key=True, max_length=10)
    hotelname = models.CharField(max_length=50)
    hoteladdress = models.CharField(max_length=200)
    hotelno = models.CharField(max_length=8)
    hotelemail = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'hotel'


class Hotelticket(models.Model):
    hotelticketid = models.CharField(primary_key=True, max_length=10)
    hotelid = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='hotelid')
    hotelroom = models.CharField(max_length=5)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hotelticket'


class Meal(models.Model):
    mealid = models.CharField(primary_key=True, max_length=3)
    mealname = models.CharField(max_length=50)
    apid = models.CharField(max_length=7)
    mealvendorid = models.ForeignKey('Mealvendor', models.DO_NOTHING, db_column='mealvendorid')

    class Meta:
        managed = False
        db_table = 'meal'


class Mealvendor(models.Model):
    mealvendorid = models.CharField(primary_key=True, max_length=5)
    mealvendorname = models.CharField(max_length=50)
    mealvendoraddress = models.CharField(max_length=200)
    mealvendorno = models.CharField(max_length=8)
    mealvendoremail = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'mealvendor'


class Movie(models.Model):
    movieid = models.AutoField(primary_key=True)
    moviename = models.CharField(max_length=50)
    moviecompanyid = models.ForeignKey('Moviecompany', models.DO_NOTHING, db_column='moviecompanyid')

    class Meta:
        managed = False
        db_table = 'movie'


class Moviecompany(models.Model):
    moviecompanyid = models.AutoField(primary_key=True)
    moviecompanyname = models.CharField(max_length=200)
    moviecompanyno = models.CharField(max_length=8)
    moviecompanyaddress = models.CharField(max_length=200)
    moviecompanyemail = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'moviecompany'


class Movietheater(models.Model):
    theaterid = models.AutoField(primary_key=True)
    theatername = models.CharField(max_length=50)
    theateraddress = models.CharField(max_length=200)
    moviecompanyid = models.ForeignKey(Moviecompany, models.DO_NOTHING, db_column='moviecompanyid')

    class Meta:
        managed = False
        db_table = 'movietheater'


class Movieticket(models.Model):
    movieticketid = models.AutoField(primary_key=True)
    moviedate = models.DateField()
    moviestarttime = models.DateTimeField()
    movieendtime = models.DateTimeField()
    movieroom = models.CharField(max_length=2)
    movieseat = models.CharField(max_length=3)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    movieid = models.ForeignKey(Movie, models.DO_NOTHING, db_column='movieid')
    theaterid = models.ForeignKey(Movietheater, models.DO_NOTHING, db_column='theaterid')

    class Meta:
        managed = False
        db_table = 'movieticket'


class Payment(models.Model):
    paymentid = models.AutoField(primary_key=True)
    id = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id')
    paymentdate = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    ticketid = models.ForeignKey('Ticket', models.DO_NOTHING, db_column='ticketid')

    class Meta:
        managed = False
        db_table = 'payment'


class Showcompany(models.Model):
    showcompanyid = models.AutoField(primary_key=True)
    showcompanyname = models.CharField(max_length=200)
    showcompanyno = models.CharField(max_length=8)
    showcompanyaddress = models.CharField(max_length=200)
    showcompanyemail = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'showcompany'


class Shows(models.Model):
    showid = models.AutoField(primary_key=True)
    showname = models.CharField(max_length=100)
    showperformer = models.CharField(max_length=50)
    showcompanyid = models.ForeignKey(Showcompany, models.DO_NOTHING, db_column='showcompanyid')

    class Meta:
        managed = False
        db_table = 'shows'


class Showticket(models.Model):
    showticketid = models.AutoField(primary_key=True)
    showdate = models.DateField()
    showstarttime = models.DateTimeField()
    showendtime = models.DateTimeField()
    showplace = models.CharField(max_length=200)
    showseat = models.CharField(max_length=200)
    showid = models.ForeignKey(Shows, models.DO_NOTHING, db_column='showid')
    price = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'showticket'


class Themepark(models.Model):
    themeparkid = models.CharField(primary_key=True, max_length=2)
    themeparkcompanyid = models.ForeignKey('Themeparkcompany', models.DO_NOTHING, db_column='themeparkcompanyid')
    themeparkname = models.CharField(max_length=50)
    themeparkcompanyaddress = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'themepark'


class Themeparkcompany(models.Model):
    themeparkcompanyid = models.CharField(primary_key=True, max_length=2)
    themeparkcompanyname = models.CharField(max_length=200)
    themeparkcompanyaddress = models.CharField(max_length=200)
    themeparkcompanyemail = models.CharField(max_length=200)
    themeparkcompanyno = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'themeparkcompany'


class Themeparkticket(models.Model):
    themeparkid = models.ForeignKey(Themepark, models.DO_NOTHING, db_column='themeparkid')
    themeparkticketid = models.CharField(primary_key=True, max_length=10)
    effectivedate = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    vip = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'themeparkticket'


class Ticket(models.Model):
    ticketid = models.AutoField(primary_key=True)
    ticktype = models.CharField(max_length=20)
    airplaneticketid = models.ForeignKey(Airplaneticket, models.DO_NOTHING, db_column='airplaneticketid')
    movieticketid = models.ForeignKey(Movieticket, models.DO_NOTHING, db_column='movieticketid')
    fooddeliveredid = models.ForeignKey(Fooddelivered, models.DO_NOTHING, db_column='fooddeliveredid')
    transportticketid = models.ForeignKey('Transportticket', models.DO_NOTHING, db_column='transportticketid')
    attractionticketid = models.ForeignKey(Attractionticket, models.DO_NOTHING, db_column='attractionticketid')
    themeparkticketid = models.ForeignKey(Themeparkticket, models.DO_NOTHING, db_column='themeparkticketid')
    tourgroupticketid = models.ForeignKey('Tourgroupticket', models.DO_NOTHING, db_column='tourgroupticketid')
    hotelticketid = models.ForeignKey(Hotelticket, models.DO_NOTHING, db_column='hotelticketid')
    showticketid = models.ForeignKey(Showticket, models.DO_NOTHING, db_column='showticketid')

    class Meta:
        managed = False
        db_table = 'ticket'


class Tourgroup(models.Model):
    tourgroupid = models.AutoField(primary_key=True)
    travelagencyid = models.ForeignKey('Travelagency', models.DO_NOTHING, db_column='travelagencyid')
    tourgroupname = models.CharField(max_length=100)
    tourgroupdestination = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tourgroup'


class Tourgroupticket(models.Model):
    tourgroupticketid = models.AutoField(primary_key=True)
    tourgroupid = models.ForeignKey(Tourgroup, models.DO_NOTHING, db_column='tourgroupid')
    tourgroupstartdate = models.DateTimeField()
    tourgroupenddate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tourgroupticket'


class Transportation(models.Model):
    transportationid = models.AutoField(primary_key=True)
    transportationcompanyid = models.ForeignKey('Transportationcompany', models.DO_NOTHING, db_column='transportationcompanyid')
    transportationdriver = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'transportation'


class Transportationcompany(models.Model):
    transportationcompanyid = models.AutoField(primary_key=True)
    transportationcompanyname = models.CharField(max_length=100)
    transportationcompanyaddress = models.CharField(max_length=200)
    transportationcompanyno = models.CharField(max_length=8)
    transportationcompanyemail = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'transportationcompany'


class Transportticket(models.Model):
    transportticketid = models.AutoField(primary_key=True)
    transportationid = models.ForeignKey(Transportation, models.DO_NOTHING, db_column='transportationid')
    transportticketstarttime = models.DateTimeField()
    transportticketendtime = models.DateTimeField()
    transporttype = models.CharField(max_length=20)
    transportlocationfrom = models.CharField(max_length=200)
    transportlocationto = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'transportticket'


class Travelagency(models.Model):
    travelagencyid = models.AutoField(primary_key=True)
    travelagencyname = models.CharField(max_length=50)
    travelagencyaddress = models.CharField(max_length=200)
    travelagencyemail = models.CharField(max_length=100)
    travelagencyno = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'travelagency'
