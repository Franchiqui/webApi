# Usa la imagen base de tiangolo/uvicorn-gunicorn-fastapi para Python 3.12
FROM python:3.11-slim

# Instalar las dependencias
RUN pip install -r requirements.txt

# Copiar todo el contenido del directorio actual al directorio de trabajo del contenedor
COPY . .

# Exponer el puerto 8000 en el contenedor
EXPOSE 4500

# Comando para ejecutar la aplicación utilizando uvicorn
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "4500"]
