Construye el escenario 3 de BUNKER, un juego estilo shooter clásico de los 90: el laberinto con minimapa y enemigos de los escenarios 1 y 2, más disparo, munición y una condición de victoria.

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
- Si existe `escenario-2.html` en esta carpeta, cópialo a `escenario-3.html` y extiéndelo. No reescribas lo que ya funciona ni modifiques el original.
- Si no existe, crea `escenario-3.html` desde cero, incluyendo también todo lo de los escenarios 1 y 2 (listas abajo).

## Entregable
- Un archivo nuevo: `escenario-3.html` (HTML + CSS + JavaScript en el mismo archivo). Sin librerías, imágenes ni audio externos.
- Máximo unas 360 líneas en total.
- Al inicio del archivo, un comentario con: la idea del juego (2 líneas), "Escenario 3 de 3", los controles y la estructura del código (lista de secciones: mapa, jugador, enemigos, disparo, render, minimapa, bucle).
- En pantalla: el título "BUNKER · Escenario 3" y una línea con los controles.

## Escenario 1 (base)
1. Raycasting sobre un mapa de cuadrícula de 12x12 con forma de laberinto (pasillos, esquinas y callejones), definido en el código.
2. Paredes de 3 colores, más oscuras en las caras laterales y con la distancia. Cielo y piso de colores distintos.
3. Movimiento con W y S (o flechas arriba y abajo), giro con A y D (o flechas izquierda y derecha), con colisión contra las paredes.
4. Bucle con `requestAnimationFrame` y movimiento independiente de los cuadros por segundo.
5. Un minimapa 2D en la parte inferior de la pantalla (unos 150x150 px, en la esquina inferior izquierda): dibuja el mapa completo con las paredes en color y muestra al jugador como un punto con una línea que indica hacia dónde mira. Se actualiza en cada cuadro.

## Escenario 2 (enemigos)
1. 4 enemigos colocados en el mapa, dibujados como sprites simples en rojo (formas del canvas, sin imágenes).
2. Los sprites escalan con la distancia y quedan tapados por las paredes (usa un z-buffer).
3. Los enemigos avanzan despacio hacia el jugador. Si lo tocan, le quitan vida.
4. Una barra de vida simple en la esquina inferior derecha (el minimapa ocupa la izquierda). Con la vida en 0: texto "GAME OVER".

## Novedades del escenario 3 (solo esto)
1. Una mira (cruz) al centro de la pantalla.
2. Disparo con la barra espaciadora o clic: elimina al enemigo que esté al centro de la mira y no esté tapado por una pared.
3. Un arma sencilla en la parte inferior, con un destello breve al disparar.
4. Munición limitada a 20, con un contador en pantalla junto con los enemigos restantes.
5. Al eliminar a todos los enemigos: texto "VICTORIA". La tecla R reinicia (también tras GAME OVER).

## Proceso
1. Plan de máximo 3 líneas y continúa sin esperar respuesta.
2. Escribe `escenario-3.html`.
3. **Verifica:** extrae el contenido de `<script>` a `.check.js` dentro de esta carpeta, valida con `node --check`, corrige cualquier error y borra `.check.js` al terminar.
4. Abre el juego con `open escenario-3.html`.

## Terminado cuando
Se puede caminar, los enemigos persiguen, se puede disparar y eliminarlos, y aparecen GAME OVER o VICTORIA según el caso.

## Formato de respuesta
Breve. Al final: los controles en 2 líneas y 3 ideas para mejorarlo.
