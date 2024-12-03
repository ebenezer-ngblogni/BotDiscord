# Étape 1 : Utilisation d'une image de base appropriée
FROM python:3.9-slim

# Étape 2 : Mise à jour et installation des dépendances nécessaires
RUN apt-get update && apt-get install -y \
    git \
    && apt-get clean

# Étape 3 : Création des répertoires pour les volumes
WORKDIR /app
RUN mkdir -p /app/har_and_cookies /app/generated_images

# Étape 4 : Téléchargement de l'image hlohaus789/g4f
RUN docker pull hlohaus789/g4f:latest

# Étape 5 : Premier conteneur avec les ports mappés et volumes montés
CMD ["docker", "run", \
     "-p", "8080:8080", "-p", "1337:1337", "-p", "7900:7900", \
     "--shm-size=2g", \
     "-v", "/app/har_and_cookies:/app/har_and_cookies", \
     "-v", "/app/generated_images:/app/generated_images", \
     "hlohaus789/g4f:latest"]

# Étape 6 : Deuxième conteneur avec les ports et volumes
CMD ["docker", "run", \
     "-p", "1337:1337", \
     "-v", "/app/har_and_cookies:/app/har_and_cookies", \
     "-v", "/app/generated_images:/app/generated_images", \
     "hlohaus789/g4f:latest-slim", \
     "rm", "-r", "-f", "/app/g4f/", \
     "&&", "pip", "install", "-U", "g4f[slim]", \
     "&&", "python", "-m", "g4f.cli", "api", "--gui", "--debug"]

# Étape 7 : Clonage du projet GitHub et récupération du fichier main.py
RUN git clone https://github.com/ebenezer-ngblogni/BotDiscord.git 
WORKDIR /app
CMD ["python", "main.py"]

