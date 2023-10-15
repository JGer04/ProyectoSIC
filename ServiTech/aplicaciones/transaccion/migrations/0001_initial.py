# Generated by Django 4.2.1 on 2023-10-15 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuenta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='transaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=100)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cuenta_Debe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transacción_abono', to='cuenta.cuenta')),
                ('cuenta_Haber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transacción_deuda', to='cuenta.cuenta')),
            ],
        ),
    ]