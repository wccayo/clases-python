from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse

import uvicorn

app = FastAPI()

# Monta la carpeta 'static' para servir archivos estáticos.
# El nombre "static" es el nombre con el que se accederá a la URL
# En este caso, http://127.0.0.1:8000/static/index.html
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define una ruta raíz para servir el index.html
'''
@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Lee el contenido del archivo y lo devuelve como una respuesta HTML
    with open("static/index.html", "r") as f:
        html_content = f.read()
    return html_content
'''
@app.get("/", response_class=HTMLResponse)
async def root( request: Request ):
    return RedirectResponse("/static/index.html")

uvicorn.run(app, host="0.0.0.0", port=8000)