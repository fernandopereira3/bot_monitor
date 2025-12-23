#!/bin/bash

# Navega para o diretório onde o script está localizado
cd "$(dirname "$0")"

# Ativa o ambiente virtual
if [ -d ".venv" ]; then
    source .venv/bin/activate
else
    echo "Erro: Ambiente virtual .venv não encontrado!"
    exit 1
fi

# Executa o bot
echo "Iniciando o Leon Bot..."
python3 bot.py
