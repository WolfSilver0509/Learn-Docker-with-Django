# Utiliser une image de base python
FROM python:3.9

# Définir un repertoir de travail
WORKDIR /app

#Copiez le contenue du repertoire de votre projet
COPY . .

# Copier le contenue des dossier statics
COPY static /app/static

# Installer les dépendances
RUN pip install -r requirements.txt

# Exécutez les migrations et creée la base de donnée
RUN python manage.py migrate

# Permet de prendre les fichiers statics et les déposer dans staticfiles
RUN python manage.py collectstatic --noinput

# Exposer le port sur lequels l'API django s'éxécute
EXPOSE 8000

#Lancer l'application django
CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]