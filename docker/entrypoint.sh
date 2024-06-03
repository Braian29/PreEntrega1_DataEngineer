#!/bin/bash

# Activar el entorno virtual
source /app/venv/bin/activate

# Ejecutar el script principal
python /app/logic-etl/main.py

# Mantén el contenedor corriendo (opcional)
tail -f /dev/null
