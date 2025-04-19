#!/usr/bin/env python3
import os
import sys


def create_files(entidade):
    print(f'Criando e abrindo arquivos para {entidade}...')

    files_to_create = [
        f'garagem\\models\\{entidade}.py',
        f'garagem\\serializers\\{entidade}.py',
        f'garagem\\views\\{entidade}.py',
    ]

    for file_path in files_to_create:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            pass  


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Uso: python {sys.argv[0]} <entidade>')
        sys.exit(1)

    parametro = sys.argv[1]
    create_files(parametro)
