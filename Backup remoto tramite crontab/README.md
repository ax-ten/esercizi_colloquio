# Backup Script e Configurazione Crontab
Questa cartella contiene uno script di backup in Bash e la configurazione di crontab per eseguire automaticamente il backup ogni domenica notte.


- `/backup.sh`: Script che crea un backup della directory /home/user, lo comprime in un archivio ZIP, lo trasferisce su un server remoto, e rimuove il backup locale.
- `/crontab`: La stringa di crontab che esegue il backup tramite backup.sh ogni domenica alle 2 di notte.
- `/crontab_complete`: Il file di configurazione crontab completo inseribile direttamente nella configurazione crontab.


## Configurazione dell'autenticazione SSH
genera una chiave ssh pubblica e poi aggiungila al server remoto
```
ssh-keygen -t rsa
ssh-copy-id user@192.168.1.100
```

## Traccia
Scrivi una stringa crontab che ogni domenica notte crea un backup della cartella /home/user e lo invia ad un server remoto raggiungibile tramite ssh con user@192.168.1.100 (indicaci quale configurazione potrebbe essere necessaria per gestire l'autenticazione sul server remoto).​
