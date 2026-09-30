#!/usr/bin/env python3
"""Create (or reset) the messy 'Downloads' folder used in demo 1.

Deterministic: same 40 files, same content, same dates every run.
Writes downloads-demo/ and manifest.json (used by verify.py) next to this script.
"""
import hashlib
import json
import os
import shutil
import struct
import time
import zipfile
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE / "downloads-demo"
MANIFEST = HERE / "manifest.json"

# (file name, kind, days ago, content group). Same group -> identical bytes (duplicates).
FILES = [
    ("Reporte prácticas - versión final.docx", "docx", 3, None),
    ("reporte-practicas-v2.pdf", "pdf", 9, "dup-reporte"),
    ("reporte-practicas-v2 (1).pdf", "pdf", 9, "dup-reporte"),
    ("Captura de pantalla 2026-08-14 a las 10.22.31.png", "png", 46, None),
    ("Captura de pantalla 2026-08-14 a las 10.24.02.png", "png", 46, None),
    ("Captura de pantalla 2026-09-02 a las 18.05.47.png", "png", 27, None),
    ("IMG_4021.JPG", "jpg", 61, None),
    ("IMG_4022.JPG", "jpg", 61, None),
    ("IMG_4023.jpeg", "jpg", 60, None),
    ("foto-perfil.jpg", "jpg", 88, None),
    ("logo-empresa.png", "png", 75, None),
    ("horario-semestre.pdf", "pdf", 52, None),
    ("calificaciones-parcial1.xlsx", "xlsx", 33, None),
    ("presupuesto-viaje.xlsx", "xlsx", 19, None),
    ("datos-encuesta.csv", "csv", 14, None),
    ("ventas_2025.csv", "csv", 120, None),
    ("exposicion-ia.pptx", "pptx", 6, None),
    ("plantilla-presentacion.pptx", "pptx", 95, None),
    ("apuntes-estadistica.txt", "txt", 21, None),
    ("ideas proyecto final.md", "md", 12, None),
    ("lista-compras.txt", "txt", 2, None),
    ("README", "txt", 101, None),
    ("Zoom_Installer.dmg", "dmg", 70, None),
    ("node-v22-installer.pkg", "pkg", 40, None),
    ("respaldo-tareas.zip", "zip", 30, None),
    ("proyecto-final-src.zip", "zip", 8, None),
    ("clase-redes-grabacion.mp4", "mp4", 17, None),
    ("demo-app.mp4", "mp4", 5, None),
    ("cv-2026.pdf", "pdf", 44, None),
    ("carta-recomendacion.docx", "docx", 37, None),
    ("factura-luz-agosto.pdf", "pdf", 29, None),
    ("recibo-renta.pdf", "pdf", 24, None),
    ("articulo-machine-learning.pdf", "pdf", 15, None),
    ("tarea-3-algoritmos.docx", "docx", 11, "dup-tarea"),
    ("tarea-3-algoritmos (copia).docx", "docx", 11, "dup-tarea"),
    ("diagrama-arquitectura.png", "png", 22, None),
    ("mapa-campus.jpg", "jpg", 110, None),
    ("notas-reunion-asesor.txt", "txt", 4, None),
    ("lecturas-semana4.pdf", "pdf", 18, None),
    ("Book1.xlsx", "xlsx", 82, None),
]


def zip_bytes(members):
    path = HERE / ".tmp.zip"
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in members.items():
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            z.writestr(info, data)
    data = path.read_bytes()
    path.unlink()
    return data


def png_bytes(seed):
    width = height = 16
    r, g, b = (seed * 53) % 256, (seed * 97) % 256, (seed * 29) % 256
    raw = b"".join(b"\x00" + bytes([r, g, b]) * width for _ in range(height))

    def chunk(tag, data):
        body = tag + data
        return struct.pack(">I", len(data)) + body + struct.pack(">I", zlib.crc32(body) & 0xFFFFFFFF)

    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b"")


def content(name, kind, group, seed):
    label = group or name
    if kind == "png":
        return png_bytes(seed)
    if kind == "jpg":
        return b"\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00" + label.encode() + b"\xff\xd9"
    if kind == "pdf":
        return (
            "%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n"
            "2 0 obj<</Type/Pages/Kids[3 0 R]/Count 1>>endobj\n"
            "3 0 obj<</Type/Page/Parent 2 0 R/MediaBox[0 0 612 792]>>endobj\n"
            f"% {label}\ntrailer<</Root 1 0 R/Size 4>>\n%%EOF\n"
        ).encode()
    if kind == "docx":
        return zip_bytes({
            "[Content_Types].xml": '<?xml version="1.0"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"/>',
            "word/document.xml": f"<document>{label}</document>",
        })
    if kind == "xlsx":
        return zip_bytes({
            "[Content_Types].xml": '<?xml version="1.0"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"/>',
            "xl/workbook.xml": f"<workbook>{label}</workbook>",
        })
    if kind == "pptx":
        return zip_bytes({
            "[Content_Types].xml": '<?xml version="1.0"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"/>',
            "ppt/presentation.xml": f"<presentation>{label}</presentation>",
        })
    if kind == "zip":
        return zip_bytes({"contenido.txt": f"contenido de {label}"})
    if kind == "csv":
        return f"id,nombre,valor\n1,{label},10\n2,ejemplo,20\n3,demo,30\n".encode()
    if kind == "mp4":
        return b"\x00\x00\x00\x18ftypmp42\x00\x00\x00\x00mp42isom" + label.encode()
    if kind == "pkg":
        return b"xar!\x00\x1c\x00\x01" + label.encode()
    if kind == "dmg":
        return b"\x00" * 64 + label.encode()
    return f"{label}\n\nContenido de ejemplo para la demo.\n".encode()


def main():
    if TARGET.exists():
        if TARGET.name != "downloads-demo":
            raise SystemExit("Refusing to delete an unexpected folder")
        shutil.rmtree(TARGET)
    TARGET.mkdir()

    assert len(FILES) == 40, len(FILES)
    now = time.time()
    manifest = []
    for i, (name, kind, days, group) in enumerate(FILES, start=1):
        data = content(name, kind, group, seed=i if not group else 1000 + len(group))
        path = TARGET / name
        path.write_bytes(data)
        stamp = now - days * 86400
        os.utime(path, (stamp, stamp))
        manifest.append({"name": name, "sha256": hashlib.sha256(data).hexdigest()})

    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Listo: {len(FILES)} archivos revueltos en {TARGET}")


if __name__ == "__main__":
    main()
