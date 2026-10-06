# inventario-laboratorio
# Sistema de Inventario de Laboratorio

## 1. Descripción
Aplicación de consola para gestionar y administrar los equipos tecnológicos dentro de los laboratorios de Tecsup.

## 2. Objetivo
Permitir el control, registro y seguimiento del estado y ubicación de los equipos del laboratorio.

## 3. Usuarios
Administradores del laboratorio y personal técnico de soporte.

## 4. Funcionalidades
- Registrar equipo
- Listar equipos
- Buscar equipo
- Modificar estado
- Eliminar equipo

## 5. Información de los equipos
Cada equipo contiene los siguientes datos:
- codigo
- nombre
- tipo
- estado
- ubicacion

## 6. Tecnologías
- Lenguaje: Python 3
- Almacenamiento: JSON (archivo local)

## 7. Estructura del proyecto
inventario-laboratorio/
│
├── README.md
├── AGENTS.md
├── app.py
│
├── src/
│   └── inventario.py
│
└── data/
    └── equipos.json

## 8. Ejecución
python app.py
