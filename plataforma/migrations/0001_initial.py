# Generated by Django 4.1.5 on 2023-01-31 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Clientes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                ("cpf", models.CharField(max_length=20)),
                (
                    "sexo",
                    models.CharField(
                        choices=[("F", "Feminino"), ("M", "Maculino")], max_length=1
                    ),
                ),
                ("idade", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("telefone", models.CharField(max_length=19)),
                (
                    "id_usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DadosCliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pai", models.CharField(max_length=50)),
                ("mae", models.CharField(max_length=50)),
                ("nacionalidade", models.CharField(max_length=50)),
                ("naturalidade", models.CharField(max_length=50)),
                (
                    "uf",
                    models.CharField(
                        choices=[
                            ("Alagoas", "Alagoas"),
                            ("Amapá", "Amapá"),
                            ("Amazonas", "Amazonas"),
                            ("Bahia", "Bahia"),
                            ("Ceará", "Ceará"),
                            ("Distrito Federal", "Distrito Federal"),
                            ("Espírito Santo", "Espírito Santo"),
                            ("Goiás", "Goiás"),
                            ("Maranhão", "Maranhão"),
                            ("Mato Grosso", "Mato Grosso"),
                            ("Mato Grosso do Sul", "Mato Grosso do Sul"),
                            ("Minas Gerais", "Minas Gerais"),
                            ("Pará", "Pará"),
                            ("Paraíba", "Paraíba"),
                            ("Paraná", "Paraná"),
                            ("Pernambuco", "Pernambuco"),
                            ("Piauí", "Piauí"),
                            ("Rio de Janeiro", "Rio de Janeiro"),
                            ("Rio Grande do Norte", "Rio Grande do Norte"),
                            ("Rio Grande do Sul", "Rio Grande do Sul"),
                            ("Rondônia", "Rondônia"),
                            ("Roraima", "Roraima"),
                            ("Santa Catarina", "Santa Catarina"),
                            ("São Paulo", "São Paulo"),
                            ("Sergipe", "Sergipe"),
                            ("Tocantins", "Tocantins"),
                        ],
                        max_length=50,
                    ),
                ),
                ("cidade", models.CharField(max_length=50)),
                ("bairro", models.CharField(max_length=50)),
                ("numero", models.CharField(max_length=10)),
                ("data", models.DateTimeField()),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="plataforma.clientes",
                    ),
                ),
            ],
        ),
    ]