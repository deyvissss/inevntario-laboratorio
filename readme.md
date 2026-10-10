# Sistema de Inventario de Laboratorio

## 1. Descripción
Aplicación de consola para gestionar y administrar los equipos tecnológicos de los laboratorios de Tecsup. Permite llevar un registro ordenado de cada equipo, su estado y su ubicación.

## 2. Objetivo
Permitir el control, registro y seguimiento del estado y la ubicación de los equipos del laboratorio, evitando pérdidas y registros desordenados.

## 3. Usuarios
- Administradores del laboratorio
- Personal técnico de soporte

## 4. Funcionalidades
El programa muestra un menú interactivo en consola con el siguiente diseño y flujo de opciones:

```text
=======================================
   SISTEMA DE INVENTARIO DE LABORATÓRIO
=======================================
1. Registrar equipo
2. Listar equipos
3. Buscar equipo
4. Modificar estado
5. Eliminar equipo
0. Salir
=======================================
Seleccione una opción: 
```
### Estado del Desarrollo (Progreso)
Las funcionalidades se implementan de forma progresiva. El estado actual del repositorio es el siguiente:
- [x] Estructura base de carpetas y archivos definida.
- [x] Función `registrar_equipo()` implementada en `src/inventario.py`.
- [x] Función `buscar_equipo()` implementada en `src/inventario.py`.
- [ ] Implementación del menú principal interactivo en `app.py`.
- [ ] Función `listar_equipos()` en `src/inventario.py`.
- [ ] Función `modificar_estado()` en `src/inventario.py`.
- [ ] Función `eliminar_equipo()` en `src/inventario.py`.

## 5. Información de los equipos
Cada equipo contiene:
- `codigo`: identificador único del equipo
- `nombre`: nombre o descripción corta del equipo
- `tipo`: categoría del equipo (por ejemplo: laptop, router, switch)
- `estado`: situación actual (disponible, en uso, en mantenimiento o dado de baja)
- `ubicacion`: lugar del laboratorio donde se encuentra

## 6. Tecnologías
- Lenguaje: Python 3
- Almacenamiento: archivo JSON local (`data/equipos.json`)
- Dependencias: solo biblioteca estándar de Python, sin librerías externas

## 7. Estructura del proyecto
```
inventario-laboratorio/
│
├── README.md          # Qué hace el proyecto
├── AGENTS.md          # Reglas para agentes de IA
├── app.py             # Punto de entrada y menú principal
│
├── src/
│   └── inventario.py  # Lógica de gestión de equipos
│
└── data/
    └── equipos.json   # Datos almacenados de los equipos
```

## 8. Ejecución
Requisito: Python 3 instalado.

```
git clone URL_DEL_REPOSITORIO
cd inventario-laboratorio
python app.py
```

## 9. Reglas para agentes de IA
Las convenciones y restricciones del proyecto están definidas en [AGENTS.md](AGENTS.md).
