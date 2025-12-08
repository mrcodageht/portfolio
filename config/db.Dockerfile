FROM mysql:8.0


COPY /config/scripts/init.sql /docker-entrypoint-initdb.d/00-init.sql
COPY /config/scripts/seed.sql /docker-entrypoint-initdb.d/01-seed.sql
