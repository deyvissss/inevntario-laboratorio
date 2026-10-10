# Evidencia de validación

**Proyecto:** inventario-laboratorio

## 1. Resumen

Se validaron las funciones del sistema de inventario según las reglas de
[README.md]
y [AGENTS.md].
Los datos se guardan en JSON (`data/equipos.json`), sin librerías externas
ni interfaz gráfica.

## 2. Validación del contexto con Antigravity

Se pidió a la IA analizar `README.md` y `AGENTS.md` sin generar código.
Interpretó bien el objetivo, las funciones, la estructura, las convenciones
y las restricciones. No fue necesario modificar los archivos.

## 3. Funciones validadas

| Función | Archivo | Resultado |
|---|---|---|
| `registrar_equipo()` | `src/inventario.py` | Correcto |
| `listar_equipos()` | `src/inventario.py` | Correcto |
| `buscar_equipo()` | `src/inventario.py` | Correcto |
| `modificar_estado()` | `src/inventario.py` | Correcto |
| `eliminar_equipo()` | `src/inventario.py` | Correcto |
| `registrar_ingreso_mantenimiento()` | `src/mantenimiento.py` | Correcto |
| `listar_en_mantenimiento()` | `src/mantenimiento.py` | Correcto |

*(Ajusta la columna "Archivo" según dónde esté cada función en tu repo.)*

## 4. Criterios verificados

- Nombres en español y en `snake_case`.
- Docstring en cada función.
- Validación de entradas vacías.
- Solo biblioteca estándar de Python.
- Lectura y escritura correcta en `data/equipos.json`.
- Sin interfaz gráfica ni dependencias externas.

## 5. Prueba de la regla de documentación

Se agregó en `AGENTS.md` la regla de docstrings. Al pedir `buscar_equipo()`,
la IA incluyó el docstring sin que se lo pidiera en el prompt.

## 6. Contradicción detectada y corregida

Se cambió temporalmente `AGENTS.md` para pedir SQLite, mientras `README.md`
decía JSON. La IA detectó el conflicto. Se corrigió quitando SQLite y
dejando solo JSON local.

## 7. Resultado

Las funciones cumplen el estándar del proyecto y permiten registrar,
consultar, modificar y eliminar equipos, además de gestionar los que están
en mantenimiento. Guardar las reglas en archivos funcionó mejor que
repetirlas en cada prompt.