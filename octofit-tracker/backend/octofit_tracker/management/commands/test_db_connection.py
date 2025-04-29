from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Testa a conexão com o banco de dados'

    def handle(self, *args, **kwargs):
        try:
            connection.ensure_connection()
            self.stdout.write(self.style.SUCCESS('Conexão com o banco de dados bem-sucedida!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro ao conectar ao banco de dados: {e}'))
