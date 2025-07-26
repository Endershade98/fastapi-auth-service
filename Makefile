# Nome del servizio Docker Compose (default: auth-service)
SERVICE ?= auth-service

# Build del servizio
build:
	docker compose build $(SERVICE)

# Avvia il servizio in background
up:
	docker compose up -d $(SERVICE)

# Ferma il servizio
stop:
	docker compose stop $(SERVICE)

# Riavvia il servizio
restart:
	docker compose restart $(SERVICE)

# Log del servizio
logs:
	docker compose logs -f $(SERVICE)

# Rimuove i container, i volumi anonimi e la rete
down:
	docker compose down

# Stato dei container
ps:
	docker compose ps

# Esegui una shell nel container del servizio
sh:
	docker compose exec $(SERVICE) /bin/sh
