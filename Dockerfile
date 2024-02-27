# Use a imagem oficial do Python
FROM python:3.10-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos necessários e instale as dependências
COPY . .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta em que a aplicação estará rodando
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
