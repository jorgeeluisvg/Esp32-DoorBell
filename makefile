# Makefile para instalar dependencias y levantar el servidor FastAPI

# Variables
VENV_DIR=venv
PYTHON=python3
PIP=$(VENV_DIR)/bin/pip
UVICORN=$(VENV_DIR)/bin/uvicorn

# Crear entorno virtual
venv:
	$(PYTHON) -m venv $(VENV_DIR)

# Activar entorno virtual y instalar dependencias
install: venv
	$(PIP) install fastapi uvicorn requests twilio

# Correr el servidor
run:
	$(UVICORN) main:app --reload --host 0.0.0.0 --port 8000

# Limpiar el entorno virtual
clean:
	rm -rf $(VENV_DIR)

.PHONY: venv install run clean
