# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt en el directorio de trabajo
COPY requirements.txt .

# Instala las dependencias del archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación en el contenedor
COPY . .

# Crear y activar un entorno virtual en el contenedor
RUN python -m venv /app/venv

# Instalar las dependencias dentro del entorno virtual
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Asegura que el script de entrada tenga permisos de ejecución
RUN chmod +x /app/docker/entrypoint.sh

# Define el script de entrada por defecto
ENTRYPOINT ["/app/docker/entrypoint.sh"]
