# Reglas para agentes de IA

Antes de trabajar en este proyecto, lee README.md y este archivo.

## 1. Lenguaje
- El código se escribe en Python 3.
- Los nombres de variables, funciones y archivos van en español.
- Los comentarios y los mensajes al usuario van en español.
- No mezclar español e inglés en los nombres.

## 2. Convenciones de nombres
- Variables: `snake_case` (ejemplo: `lista_equipos`).
- Funciones: `snake_case`, con un verbo que indique la acción (ejemplo: `registrar_equipo`).
- Archivos y carpetas: minúsculas, sin espacios.
- Constantes: MAYÚSCULAS (ejemplo: `RUTA_DATOS`).
- Claves del JSON: exactamente `codigo`, `nombre`, `tipo`, `estado`, `ubicacion`.

## 3. Organización del código
- `app.py`: solo contiene el menú principal y la llamada a las funciones.
- `src/inventario.py`: contiene la lógica de gestión de equipos.
- `data/equipos.json`: contiene únicamente los datos.
- No crear carpetas ni archivos nuevos sin que se pida.
- No mezclar la lógica del inventario dentro de `app.py`.

## 4. Funciones
- Cada función realiza una sola tarea.
- Las funciones deben ser cortas y fáciles de leer.
- No duplicar funciones que ya existen; reutilizarlas.
- Nombres exigidos: `registrar_equipo`, `listar_equipos`, `buscar_equipo`, `modificar_estado`, `eliminar_equipo`.
- Validar las entradas del usuario y mostrar un mensaje claro si hay un error.

## 5. Datos
- Cada equipo tiene: `codigo`, `nombre`, `tipo`, `estado`, `ubicacion`.
- El `codigo` es único; no se pueden registrar dos equipos con el mismo código.
- Valores permitidos de `estado`: `disponible`, `en uso`, `en mantenimiento`, `dado de baja`.
- Los datos se guardan en `data/equipos.json`.
- Si el archivo no existe o está vacío, se trabaja con una lista vacía sin que el programa falle.
- No cambiar el formato del JSON sin autorización.

## 6. Restricciones
- Usar solo la biblioteca estándar de Python (por ejemplo, `json` y `os`).
- No instalar ni importar librerías externas.
- No usar bases de datos (SQLite u otras); el almacenamiento es JSON.
- No crear interfaz gráfica; la aplicación es de consola.

## 7. Modificación del código
- Modificar únicamente lo que se solicita.
- No cambiar código que ya funciona.
- No renombrar funciones ni variables existentes sin que se pida.
- No implementar funcionalidades que no fueron solicitadas.
- Mantener el estilo del código existente.

## 8. Procedimiento antes de realizar cambios
1. Leer README.md y AGENTS.md.
2. Indicar qué archivo se va a modificar.
3. Indicar qué reglas de este archivo se van a aplicar.
4. Si una instrucción contradice README.md o AGENTS.md, avisar y no continuar hasta que se aclare.
5. Hacer solo los cambios solicitados y explicar brevemente qué se hizo.
## Documentación
- Todas las funciones deben incluir docstring.
- El docstring debe describir brevemente el propósito de la función.

