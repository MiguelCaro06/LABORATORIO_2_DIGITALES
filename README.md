# Laboratorio 2 - Robot Pepper 🤖

Este laboratorio documenta la primera interacción con el robot **Pepper** en el salón de robótica.  
Incluye la investigación de librerías, desarrollo de coreografías en **Choregraphe** y por **consola SSH**, además de un informe en **Overleaf**.

---

## 📚 1. Investigación de Librerías
### qi
- Comunicación con NAOqi, servicios del robot (movimiento, postura, voz).
- Se activa con `import qi`.

### argparse
- Manejo de argumentos de consola.
- Se activa con `import argparse`.

### sys
- Control de rutas y funciones del intérprete.
- Se activa con `import sys`.

### os
- Acceso al sistema de archivos.
- Se activa con `import os`.

### almath
- Librería matemática para control de movimientos.
- Se activa con `import almath`.

### math
- Funciones matemáticas estándar.
- Se activa con `import math`.

### motion
- Control de movimientos del robot.
- Se accede vía:
  ```python
  motion_service = session.service("ALMotion")
