Construye el escenario 1 de BUNKER, un juego estilo shooter clásico de los 90: un pasillo en pseudo-3D (raycasting) por el que se puede caminar. Es la base; los escenarios 2 y 3 vendrán después.

No hagas preguntas: si algo no está definido, elige lo más simple y sigue. Ve rápido, esto es una demo de pocos minutos. La única excepción es el límite de trabajo de abajo.

## Límite de trabajo (obligatorio)
Tu única carpeta autorizada es:
`/Users/robece/Workspace/projects/learning-agents/demo-2-doom/game`

- Antes de hacer nada, ejecuta `pwd`. Si no es exactamente esa ruta, detente y avísame.
- Solo puedes leer, crear y editar archivos dentro de esa ruta, con rutas relativas.
- Nunca salgas de ella: nada de `cd ..`, `~`, `/tmp`, `sudo` ni `rm -r`. No toques la carpeta de arriba.
- No instales nada ni uses internet.
- Nunca modifiques ni borres el archivo de otro escenario: solo crea el de este.

## Entregable
- Un archivo nuevo: `escenario-1.html` (HTML + CSS + JavaScript en el mismo archivo). Sin librerías, imágenes ni audio externos.
- Máximo unas 150 líneas.
- Al inicio del archivo, un comentario con: la idea del juego (2 líneas), "Escenario 1 de 3", los controles y la estructura del código (lista de secciones: mapa, jugador, render, bucle).
- En pantalla: el título "BUNKER · Escenario 1" y una línea con los controles.

## Qué debe tener (solo esto)
1. Raycasting sobre un mapa de cuadrícula de 12x12 definido en el código.
2. Paredes de 3 colores, más oscuras en las caras laterales y con la distancia. Cielo y piso de colores distintos.
3. Movimiento con W y S (o flechas arriba y abajo), giro con A y D (o flechas izquierda y derecha), con colisión contra las paredes.
4. Bucle con `requestAnimationFrame` y movimiento independiente de los cuadros por segundo.

## Proceso
1. Plan de máximo 3 líneas y continúa sin esperar respuesta.
2. Escribe `escenario-1.html`.
3. **Verifica:** extrae el contenido de `<script>` a `.check.js` dentro de esta carpeta, valida con `node --check`, corrige cualquier error y borra `.check.js` al terminar.
4. Abre el juego con `open escenario-1.html`.

## Terminado cuando
El archivo abre en el navegador, se puede caminar y no se atraviesan las paredes.

## Formato de respuesta
Breve. Al final: los controles en 2 líneas.
