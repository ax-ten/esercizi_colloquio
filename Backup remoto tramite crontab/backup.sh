#!/bin/bash

DATE=$(date +\%Y\%m\%d)
BACKUP_FILE="/tmp/backup_$DATE.zip"
REMOTE_DIR="/path/to/backup/directory"
REMOTE_USER="user"
REMOTE_HOST="192.168.1.100"

# Creazione
echo "Creo il backup: $BACKUP_FILE"
zip -r "$BACKUP_FILE" /home/user
if [ $? -ne 0 ]; then
    echo "Errore nella creazione del backup."
    exit 1
fi

# Trasferimento
scp "$BACKUP_FILE" "$REMOTE_USER"@"$REMOTE_HOST":"$REMOTE_DIR"
if [ $? -ne 0 ]; then
    echo "Errore nel trasferimento del backup al server remoto."
    exit 1
fi

# Rimozione locale
echo "Backup trasferito con successo."
rm "$BACKUP_FILE"


