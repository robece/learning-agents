Es la carpeta de Descargas de un estudiante: unos 40 archivos mezclados, sin ningún orden.

## Límite de trabajo (obligatorio)
Tu única carpeta autorizada es:
`/Users/robece/Workspace/projects/learning-agents/demo-1-organize/downloads-demo`

- Antes de hacer nada, ejecuta `pwd`. Si no es exactamente esa ruta, detente y avísame. No continúes.
- Solo puedes leer, crear y mover archivos dentro de esa ruta. Usa rutas relativas.
- Nunca salgas de ella: nada de `cd ..`, rutas absolutas hacia otro lugar, `~`, `sudo` ni `rm`. Tampoco leas ni modifiques la carpeta de arriba (incluye `verify.py` y `manifest.json`).
- Si crees que necesitas salir de esta carpeta, pregúntame antes.

## Objetivo
Ordenar los archivos en subcarpetas por tipo.

## Categorías (usa exactamente estos nombres)
- `Documentos`: pdf, docx, txt, md y archivos de texto sin extensión
- `Hojas de cálculo`: xlsx, csv
- `Presentaciones`: pptx
- `Imágenes`: png, jpg, jpeg (sin importar mayúsculas)
- `Videos`: mp4
- `Comprimidos e instaladores`: zip, dmg, pkg
- `Otros`: cualquier cosa que no encaje. Si un archivo no tiene extensión, usa el comando `file` para decidir.

## Reglas
- No borres nada. No renombres nada. No sobrescribas nada (usa `mv -n`).
- Los duplicados (por ejemplo "archivo (1).pdf") se quedan tal cual, cada uno en su categoría.
- No instales nada ni uses internet.

## Proceso (sigue este orden)
1. **Explora, sin modificar nada.** Cuenta los archivos y revisa los tipos con `ls` y `file`.
2. **Muéstrame el plan** en una tabla con columnas: categoría, cantidad y dos ejemplos. **Detente ahí y espera mi aprobación.** No muevas ningún archivo antes.
3. **Cuando yo apruebe, ejecuta** los movimientos.
4. **Verifica con evidencia:** compara el número total de archivos antes y después, confirma que no queda ninguno suelto en la raíz y que ningún nombre cambió. Enséñame los números.

## Terminado cuando
Hay exactamente los mismos archivos antes y después, todos dentro de una subcarpeta.

## Formato de respuesta
Breve y sin adornos. Al final, un resumen de máximo 3 líneas.
