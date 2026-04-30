import cv2
import os
import math

video_path = '/Users/Kevin/Documents/supercamp/recortado.mov'
output_dir = '/Users/Kevin/CD/8vo Semestre/Sport Analytics/scroll_story/imagenes_scroll'

# Crear el directorio si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Limpiar directorio previo si tuviera algo
for f in os.listdir(output_dir):
    os.remove(os.path.join(output_dir, f))

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error al abrir el video.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = total_frames / fps

print(f"FPS original: {fps}, Total frames: {total_frames}, Duración: {duration:.2f}s")

target_fps = 12
interval = 1.0 / target_fps
current_time = 0.0
saved_count = 0

while True:
    # Set the time position
    cap.set(cv2.CAP_PROP_POS_MSEC, current_time * 1000)
    ret, frame = cap.read()
    
    if not ret:
        break
        
    # Resize frame para que no pese tanto (ej: 1280px de ancho)
    height, width = frame.shape[:2]
    new_width = 1280
    new_height = int(height * (new_width / width))
    frame_resized = cv2.resize(frame, (new_width, new_height))
    
    filename = f"frame_{saved_count + 1:04d}.jpg"
    filepath = os.path.join(output_dir, filename)
    
    cv2.imwrite(filepath, frame_resized, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
    saved_count += 1
    
    current_time += interval
    
    if current_time > duration:
        break

cap.release()
print(f"Extracción completa. Se guardaron {saved_count} imágenes.")
