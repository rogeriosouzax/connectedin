# Generated by Django 2.2.6 on 2019-10-26 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('convidado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='convites_recebidos', to='perfis.Perfil')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='convites_realizados', to='perfis.Perfil')),
            ],
        ),
    ]
