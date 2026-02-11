Read the `AGENTS.md` and `README.md` to get an understanding of the project.

There are multiple backup scripts:

- docker-volume-backup
- docker-mysql-backup
- docker-odoo-backup
- docker-postgres-backup

These backup scripts create a dump in a docker container. Then they zip the dump and store it in a specific location.

During the backup process a lot of disk space is required. At some point there is the dump files and the already existing zip file. So twice the disk space is used for the backup. 

I want to make simple optimisation to the backup script. Before the dumps are created, the destination file is deleted.

Please update the scripts according to the new requirement.