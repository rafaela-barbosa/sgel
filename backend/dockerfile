# Imagem oficial do Python (slim -> versão enxuta)
FROM python:3.11-slim

# Define /app como pasta de trabalho dentro do container
WORKDIR /app

# Copia só o requirements primeiro (otimização de cache)
COPY requirements.txt .

# Instala as dependências dentro da imagem
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código
COPY . .

# Comando que roda quando o container sobe
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]