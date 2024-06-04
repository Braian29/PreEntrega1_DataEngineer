# Proyecto ETL con Airflow y Redshift

Este proyecto implementa un flujo de trabajo de ETL completo utilizando Airflow y Amazon Redshift para cargar datos desde una API pública a un almacén de datos en la nube. El proyecto está estructurado en varios componentes:

## Contenido del Repositorio:

- **docker/**: Contiene el Dockerfile y el script de entrada para configurar un contenedor de Docker con Airflow.
- **logic-etl/**:
  - **db.py**: Define funciones para establecer conexión con la base de datos Redshift y realizar consultas.
  - **etl.py**: Contiene funciones para extraer datos de una API pública, crear la tabla en Redshift y cargar los datos.
  - **main.py**: Coordina el flujo del programa, llamando a las funciones de extracción, transformación y carga de datos.
- **venv/**: Entorno virtual para instalar las dependencias del proyecto.
- **.dockerignore**: Archivo para especificar qué archivos y carpetas se deben ignorar al construir la imagen de Docker.
- **.env**: Archivo para almacenar variables de entorno sensibles, como credenciales de base de datos.
- **.gitignore**: Archivo para especificar qué archivos y carpetas se deben ignorar en el control de versiones de Git.
- **README.md**: Este archivo, que proporciona una descripción general del proyecto y su uso.
- **requirements.txt**: Archivo que lista todas las dependencias del proyecto para su instalación.

## Instrucciones de Uso:

1. Clona este repositorio en tu máquina local.
2. Configura las variables de entorno en el archivo `.env` con las credenciales de tu base de datos Redshift.

    DATABASE_TYPE=""

    DBAPI=""

    ENDPOINT=""

    USER=""

    PASSWORD=""

    PORT=""

    DATABASE=""

4. Crea un entorno virtual e instala las dependencias ejecutando `pip install -r requirements.txt`.

## Notas Adicionales:

- Asegúrate de revisar y cumplir con las especificaciones y requisitos del proyecto antes de ejecutar el código.
- Para cualquier pregunta o problema, no dudes en abrir un issue en este repositorio.

---
