import cv2
import pytesseract
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class ScanTexto(BaseModel):
    image_path: str
    
@app.get("/")
def index():
    return {"message" : "Hola, Pythonianos"}

@app.post("/scanTexto")
async def scanTexto_endpoint(request: Request, scanTexto_data: ScanTexto):
    image_path = scanTexto_data.image_path

    try:
        texto_extraido = scanTexto_func(image_path)
        return {"data": texto_extraido}
    except Exception as e:
        print(f"Error al extraer texto: {e}")
        return {"error": str(e)}

def scanTexto_func(imagePath):
    # Cargar imagen
    img = cv2.imread(imagePath)

    # Comprobar si la imagen se leyó correctamente.
    if img is None:
        raise Exception("Error al cargar la imagen: {}".format(imagePath))
    
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplicar umbral para convertir a una imagen binaria
    _, threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Establecer la ruta de Tesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:/Archivos de programa/Tesseract-OCR/tesseract.exe'

    # Establecer el idioma del texto
    text = pytesseract.image_to_string(threshold_img, config='--psm 10 lang=es')

    # Devolver el texto extraído
    return text
