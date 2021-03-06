# Generated by Django 3.0.2 on 2020-01-02 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airlinecompany',
            fields=[
                ('airlinecompanyid', models.AutoField(primary_key=True, serialize=False)),
                ('airlinecompanyname', models.CharField(max_length=200)),
                ('airlinecompanyno', models.CharField(max_length=8)),
                ('airlinecompanyaddress', models.CharField(max_length=200)),
                ('airlinecompanyemail', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'airlinecompany',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('airplaneid', models.AutoField(primary_key=True, serialize=False)),
                ('checkinport', models.CharField(max_length=3)),
                ('meal', models.IntegerField()),
            ],
            options={
                'db_table': 'airplane',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Airplaneticket',
            fields=[
                ('airplaneticketid', models.AutoField(primary_key=True, serialize=False)),
                ('destination', models.CharField(max_length=100)),
                ('starttime', models.DateTimeField()),
                ('scheduledtime', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('seat', models.CharField(max_length=3)),
                ('seatingplace', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'airplaneticket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('attractionid', models.AutoField(primary_key=True, serialize=False)),
                ('attractionname', models.CharField(max_length=200)),
                ('attractionaddress', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'attraction',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Attractioncompany',
            fields=[
                ('attractioncompanyid', models.AutoField(primary_key=True, serialize=False)),
                ('attractioncompanyname', models.CharField(max_length=200)),
                ('attractioncompanyno', models.CharField(max_length=8)),
                ('attractioncompanyaddress', models.CharField(max_length=200)),
                ('attractioncompanyemail', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'attractioncompany',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Attractionticket',
            fields=[
                ('attractionticketid', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
            options={
                'db_table': 'attractionticket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('foodid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('foodname', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'food',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Foodcompany',
            fields=[
                ('foodcompanyid', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('foodcompanyname', models.CharField(max_length=200)),
                ('foodcompanyno', models.CharField(max_length=8)),
                ('foodcompanyaddress', models.CharField(max_length=200)),
                ('foodcompanyemail', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'foodcompany',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fooddelivered',
            fields=[
                ('fooddeliveredid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('calltime', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
            options={
                'db_table': 'fooddelivered',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('hotelid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('hotelname', models.CharField(max_length=50)),
                ('hoteladdress', models.CharField(max_length=200)),
                ('hotelno', models.CharField(max_length=8)),
                ('hotelemail', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'hotel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hotelticket',
            fields=[
                ('hotelticketid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('hotelroom', models.CharField(max_length=5)),
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
            ],
            options={
                'db_table': 'hotelticket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('mealid', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('mealname', models.CharField(max_length=50)),
                ('apid', models.CharField(max_length=7)),
            ],
            options={
                'db_table': 'meal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mealvendor',
            fields=[
                ('mealvendorid', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('mealvendorname', models.CharField(max_length=50)),
                ('mealvendoraddress', models.CharField(max_length=200)),
                ('mealvendorno', models.CharField(max_length=8)),
                ('mealvendoremail', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'mealvendor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movieid', models.AutoField(primary_key=True, serialize=False)),
                ('moviename', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'movie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Moviecompany',
            fields=[
                ('moviecompanyid', models.AutoField(primary_key=True, serialize=False)),
                ('moviecompanyname', models.CharField(max_length=200)),
                ('moviecompanyno', models.CharField(max_length=8)),
                ('moviecompanyaddress', models.CharField(max_length=200)),
                ('moviecompanyemail', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'moviecompany',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movietheater',
            fields=[
                ('theaterid', models.AutoField(primary_key=True, serialize=False)),
                ('theatername', models.CharField(max_length=50)),
                ('theateraddress', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'movietheater',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movieticket',
            fields=[
                ('movieticketid', models.AutoField(primary_key=True, serialize=False)),
                ('moviedate', models.DateField()),
                ('moviestarttime', models.DateTimeField()),
                ('movieendtime', models.DateTimeField()),
                ('movieroom', models.CharField(max_length=2)),
                ('movieseat', models.CharField(max_length=3)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
            options={
                'db_table': 'movieticket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paymentid',
            fields=[
                ('paymentid', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.PositiveIntegerField()),
                ('paymentdate', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
            options={
                'db_table': 'paymentid',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Showcompany',
            fields=[
                ('showcompanyid', models.AutoField(primary_key=True, serialize=False)),
                ('showcompanyname', models.CharField(max_length=200)),
                ('showcompanyno', models.CharField(max_length=8)),
                ('showcompanyaddress', models.CharField(max_length=200)),
                ('showcompanyemail', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'showcompany',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shows',
            fields=[
                ('showid', models.AutoField(primary_key=True, serialize=False)),
                ('showname', models.CharField(max_length=100)),
                ('showperformer', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'shows',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Showticket',
            fields=[
                ('showticketid', models.AutoField(primary_key=True, serialize=False)),
                ('showdate', models.DateField()),
                ('showstarttime', models.DateTimeField()),
                ('showendtime', models.DateTimeField()),
                ('showplace', models.CharField(max_length=200)),
                ('showseat', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
            options={
                'db_table': 'showticket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Themepark',
            fields=[
                ('themeparkid', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('themeparkname', models.CharField(max_length=50)),
                ('themeparkcompanyaddress', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'themepark',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Themeparkcompany',
            fields=[
                ('themeparkcompanyid', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('themeparkcompanyname', models.CharField(max_length=200)),
                ('themeparkcompanyaddress', models.CharField(max_length=200)),
                ('themeparkcompanyemail', models.CharField(max_length=200)),
                ('themeparkcompanyno', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'themeparkcompany',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Themeparkticket',
            fields=[
                ('themeparkticketid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('effectivedate', models.DateField()),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('vip', models.IntegerField()),
            ],
            options={
                'db_table': 'themeparkticket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticketid', models.AutoField(primary_key=True, serialize=False)),
                ('ticktype', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'ticket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tourgroup',
            fields=[
                ('tourgroupid', models.AutoField(primary_key=True, serialize=False)),
                ('tourgroupname', models.CharField(max_length=100)),
                ('tourgroupdestination', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tourgroup',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tourgroupticket',
            fields=[
                ('tourgroupticketid', models.AutoField(primary_key=True, serialize=False)),
                ('tourgroupstartdate', models.DateTimeField()),
                ('tourgroupenddate', models.DateTimeField()),
            ],
            options={
                'db_table': 'tourgroupticket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('transportationid', models.AutoField(primary_key=True, serialize=False)),
                ('transportationdriver', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'transportation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transportationcompany',
            fields=[
                ('transportationcompanyid', models.AutoField(primary_key=True, serialize=False)),
                ('transportationcompanyname', models.CharField(max_length=100)),
                ('transportationcompanyaddress', models.CharField(max_length=200)),
                ('transportationcompanyno', models.CharField(max_length=8)),
                ('transportationcompanyemail', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'transportationcompany',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transportticket',
            fields=[
                ('transportticketid', models.AutoField(primary_key=True, serialize=False)),
                ('transportticketstarttime', models.DateTimeField()),
                ('transportticketendtime', models.DateTimeField()),
                ('transporttype', models.CharField(max_length=20)),
                ('transportlocationfrom', models.CharField(max_length=200)),
                ('transportlocationto', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'transportticket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Travelagency',
            fields=[
                ('travelagencyid', models.AutoField(primary_key=True, serialize=False)),
                ('travelagencyname', models.CharField(max_length=50)),
                ('travelagencyaddress', models.CharField(max_length=200)),
                ('travelagencyemail', models.CharField(max_length=100)),
                ('travelagencyno', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'travelagency',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('passwords', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('birth', models.DateField()),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
