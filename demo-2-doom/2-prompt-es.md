Construye el escenario 2 de BUNKER, un juego estilo shooter clásico de los 90: el laberinto en pseudo-3D con minimapa del escenario 1, más enemigos que te persiguen, vida y game over.

No hagas preguntas: si algo no está definido, elige lo más simple y sigue. Ve rápido, esto es una demo de pocos minutos. La única excepción es el límite de trabajo de abajo.

## Límite de trabajo (obligatorio)
Tu única carpeta autorizada es:
`/Users/robece/Workspace/projects/learning-agents/demo-2-doom/game`

- Antes de hacer nada, ejecuta `pwd`. Si no es exactamente esa ruta, detente y avísame.
- Solo puedes leer, crear y editar archivos dentro de esa ruta, con rutas relativas.
- Nunca salgas de ella: nada de `cd ..`, `~`, `/tmp`, `sudo` ni `rm -r`. No toques la carpeta de arriba.
- No instales nada ni uses internet.
- Nunca modifiques ni borres el archivo de otro escenario: solo crea el de este.

## Punto de partida
- Si existe `escenario-1.html` en esta carpeta, cópialo a `escenario-2.html` y extiéndelo. No reescribas lo que ya funciona ni modifiques el original.
- Si no existe, crea `escenario-2.html` desde cero, incluyendo también todo lo del escenario 1 (lista abajo).

## Entregable
- Un archivo nuevo: `escenario-2.html` (HTML + CSS + JavaScript en el mismo archivo). Sin librerías, imágenes ni audio externos.
- Máximo unas 270 líneas en total.
- Al inicio del archivo, un comentario con: la idea del juego (2 líneas), "Escenario 2 de 3", los controles y la estructura del código (lista de secciones: mapa, jugador, enemigos, render, minimapa, bucle).
- En pantalla: el título "BUNKER · Escenario 2" y una línea con los controles.

## Escenario 1 (base)
1. Raycasting sobre un mapa de cuadrícula de 12x12 con forma de laberinto (pasillos, esquinas y callejones), definido en el código.
2. Paredes de 3 colores, más oscuras en las caras laterales y con la distancia. Cielo y piso de colores distintos.
3. Movimiento con W y S (o flechas arriba y abajo), giro con A y D (o flechas izquierda y derecha), con colisión contra las paredes.
4. Bucle con `requestAnimationFrame` y movimiento independiente de los cuadros por segundo.
5. Un minimapa 2D en la parte inferior de la pantalla (unos 150x150 px, en la esquina inferior izquierda): dibuja el mapa completo con las paredes en color y muestra al jugador como un punto con una línea que indica hacia dónde mira. Se actualiza en cada cuadro.

## Novedades del escenario 2 (solo esto)
1. 4 enemigos colocados en el mapa, dibujados como sprites simples en rojo (formas del canvas, sin imágenes).
2. Los sprites escalan con la distancia y quedan tapados por las paredes (usa un z-buffer).
3. Los enemigos avanzan despacio hacia el jugador. Si lo tocan, le quitan vida.
4. Una barra de vida simple en la esquina inferior derecha (el minimapa ocupa la izquierda).
5. Con la vida en 0: texto "GAME OVER". La tecla R reinicia.

## Proceso
1. Plan de máximo 3 líneas y continúa sin esperar respuesta.
2. Escribe `escenario-2.html`.
3. **Verifica:** extrae el contenido de `<script>` a `.check.js` dentro de esta carpeta, valida con `node --check`, corrige cualquier error y borra `.check.js` al terminar.
4. Abre el juego con `open escenario-2.html`.

## Terminado cuando
Se puede caminar sin atravesar paredes, se ven los enemigos, te persiguen, te quitan vida y aparece GAME OVER.

## Formato de respuesta
Breve. Un resumen de máximo 2 líneas.
