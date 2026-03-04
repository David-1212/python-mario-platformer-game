# 🎮 Juego de Plataformas Tipo Mario en Python

Un juego de plataformas estilo clásico desarrollado desde cero con **Python** y **Pygame**, donde el jugador debe recolectar monedas, evitar enemigos y llegar hasta la princesa para ganar.

---

## 📸 Vista General

Este proyecto recrea la experiencia clásica de los juegos de plataformas:

- 👨 Personaje principal personalizado (`mario.png`)
- 👾 Enemigos en movimiento (`enemigo.png`)
- 🪙 Monedas coleccionables (`moneda.png`)
- 👑 Princesa en la parte superior (`princesa.png`)
- ❤️ Sistema de 3 vidas
- 🔄 Reinicio automático al perder
- 🏆 Pantalla de victoria al completar el objetivo
- 🧱 Múltiples plataformas distribuidas en el mapa

---

## 🎯 Objetivo del Juego

El jugador debe:

1. Saltar entre plataformas.
2. Evitar enemigos en movimiento.
3. Recolectar todas las monedas del mapa.
4. Llegar hasta la princesa en la parte superior.

### Condiciones:

- Si el jugador es tocado por un enemigo, pierde una vida.
- Al perder 3 vidas → aparece mensaje de **"Perdiste"** y el juego se reinicia.
- Si recolecta todas las monedas y llega a la princesa → aparece **"¡Ganaste!"**.

---

## 🛠 Tecnologías Utilizadas

- Python 3
- Pygame
- Programación orientada a objetos
- Detección de colisiones
- Sistema básico de físicas (gravedad y salto)

---

## 🎮 Controles

| Tecla | Acción |
|-------|--------|
| ⬅️ | Mover a la izquierda |
| ➡️ | Mover a la derecha |
| ⬆️ / Barra Espaciadora | Saltar |

---

## 📂 Estructura del Proyecto

📦 python-mario-platformer-game
┣ 📜 main.py
┣ 🖼 mario.png
┣ 🖼 enemigo.png
┣ 🖼 moneda.png
┣ 🖼 princesa.png
┗ 📜 README.md
---
```bash
## ▶ Cómo Ejecutar el Proyecto

### 1️⃣ Clonar el repositorio


git clone https://github.com/tuusuario/python-mario-platformer-game.git
cd python-mario-platformer-game
```


2️⃣ Instalar dependencias
```bash
pip install pygame
```
3️⃣ Ejecutar el juego
```bash
python main.py
💡 Lo que Aprenderás con Este Proyecto
```

Cómo crear un juego 2D en Python

Manejo de sprites

Detección de colisiones

Sistema de vidas

Lógica de victoria y derrota

Movimiento de enemigos

Organización de código en videojuegos

🚀 Posibles Mejoras Futuras

Animaciones del personaje

Efectos de sonido

Música de fondo

Pantalla de inicio

Sistema de niveles

Guardado de puntaje

👨‍💻 Autor

Proyecto desarrollado con fines educativos para practicar desarrollo de videojuegos en Python.

Si te gustó el proyecto ⭐ dale una estrella al repositorio.
