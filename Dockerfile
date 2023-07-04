# Imagen de python
FROM python:3-alpine

# Folder
WORKDIR /final

# Instalamos dependencias
COPY requirements.txt ./

# Instalamos librerias
RUN pip install Flask
RUN pip install Flask-Cors
RUN pip install -r requirements.txt

# Copiamos todo
COPY . .

# Exponemos el puerto
EXPOSE 5000
CMD ["flask","run","--host","0.0.0.0","--port","6000"]