# Usa la imagen base de tiangolo/uvicorn-gunicorn-fastapi para Python 3.12
FROM python:3.11-slim

# Instalar las dependencias
RUN pip install Hypercorn

# ME VAS A DEJAR TERMINAR O VAS A SEGUIR JUGANDO CONMIGO ?

# Exponer el puerto 4500 en el contenedor
EXPOSE 4500

# Comando para ejecutar la aplicación utilizando uvicorn
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "4500"]
