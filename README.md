# Costruisce l'immagine del servizio
docker compose build

# Avvia il container in background
docker compose up -d

# Mostra i log
docker compose logs -f

# Ferma il container
docker compose stop

# Riavvia il container
docker compose restart

# Elimina container e rete
docker compose down