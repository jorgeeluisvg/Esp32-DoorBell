# 📱 SMS Doorbell API

Este proyecto es un servidor **FastAPI** que recibe peticiones `POST` (por ejemplo, desde un ESP32) y envía un **mensaje de texto (SMS)** a tu celular.

---

## 📦 Requisitos

- Python 3.12 o superior
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- Una cuenta de servicio SMS (como Twilio)

---

## 🔥 Instalación


1. **Crea un entorno virtual**

```bash
python3 -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate     # En Windows
```

2. **Instala las dependencias**

```bash
pip install fastapi uvicorn requests twilio
```

5. **Levanta el servidor**

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

El servidor estará disponible en:

```
http://localhost:8000
```

---

## 📡 Cómo enviar datos (Pruebas)

Puedes probarlo usando **Postman** o **curl**.

### 🧪 Usando Postman:

- **Método:** `POST`
- **URL:** `http://localhost:8000/send-sms`
- **Headers:**

  | Key           | Value             |
  |---------------|-------------------|
  | Content-Type  | application/json   |

- **Body (raw → JSON):**

```json
{
    "message": "Hola desde Postman"
}
```

---

### 🧪 Usando Curl:

```bash
curl -X POST http://localhost:8000/send-sms -H "Content-Type: application/json" -d '{"message":"Hola desde curl"}'
```

---

## 📚 Endpoints disponibles

| Método | URL             | Descripción                       |
|--------|------------------|-----------------------------------|
| POST   | `/send-sms`      | Recibe un mensaje y lo envía como SMS |
