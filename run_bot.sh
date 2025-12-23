#!/bin/bash

# Navega para o diretório onde o script está localizado
cd "$(dirname "$0")"
git pull origin main

# Ativa o ambiente virtual
if [ -d ".venv" ]; then
    source .venv/bin/activate
else
    echo "Erro: Ambiente virtual .venv não encontrado!"
    exit 1
fi

# Executa o bot
nohup python3 bot.py > bot.log 2>&1 &
echo "Leon Bot iniciado em segundo plano."
