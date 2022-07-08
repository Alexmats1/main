# Generated by Django 4.0.6 on 2022-07-08 18:44

from django.db import migrations, models
import django.db.models.deletion
import orders_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.TextField(verbose_name='Наименование организации')),
                ('customer_address', models.TextField(verbose_name='Адрес')),
                ('customer_city', models.TextField(verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Описание контрагента',
                'verbose_name_plural': 'Описания контрагентов',
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.TextField(verbose_name='Производитель')),
                ('moded', models.TextField(verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Доступное оборудование',
                'verbose_name_plural': 'Доступное оборудование',
                'db_table': 'devices',
            },
        ),
        migrations.CreateModel(
            name='DeviceInField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.TextField(verbose_name='Серийный номер')),
                ('owner_status', models.TextField(verbose_name='Статус принадлежности')),
                ('analyzer_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.device', verbose_name='Идентификатор оборудования')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.customer', verbose_name='Идентификатор пользователя')),
            ],
            options={
                'verbose_name': 'Оборудование в полях',
                'verbose_name_plural': 'Оборудование в полях',
                'db_table': 'devices_in_fields',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_description', models.TextField(verbose_name='Описание')),
                ('created_dt', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated_dt', models.DateTimeField(blank=True, null=True, verbose_name='Последнее изменение')),
                ('order_status', models.TextField(validators=[orders_app.models.status_validator], verbose_name='Статус заявки')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.customer', verbose_name='Конечный пользователь')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.deviceinfield', verbose_name='Оборудование')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'db_table': 'orders',
            },
        ),
    ]
