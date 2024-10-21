# Meilisync role

Deploy Meilisync container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/long2ice/meilisync
meilisync_image: long2ice/meilisync:main
meilisync_description: Sync Meilisearch with Postgresql # default: Meilisync
meilisync_hostname: meilisync01
meilisync_data_dir: meilisync_conf01 # default: "/usr/share/{{ meilisync_hostname }}"
meilisync_postgres_host: postgres01
meilisync_postgres_db: example
meilisync_postgres_user: example
meilisync_postgres_password: # default: "{{ vault_meilisync_postgres_password }}"
meilisync_api_url: http://meili.example.com:7700/
meilisync_api_key: # default: "{{ vault_meilisync_api_key }}"
meilisync_config: |
  sync:
    - table: POSTGRES_TABLE_NAME_1
      index: MEILISEARCH_INDEX_NAME_1
      pk: id 
      full: true
    - table: POSTGRES_TABLE_NAME_2
      index: MEILISEARCH_INDEX_NAME_2
      full: true
```

And include it in your playbook.

```yml
- hosts: meilisync
  roles:
  - role: meilisync
```


## Docs

### Setup demo database

Run this SQL in `postgres01`.

``` sql
CREATE TABLE users (
  id int, 
  login varchar(255)
);
```

Insert data.

``` sql
INSERT INTO users (id, login) VALUES (1, 'user1');
INSERT INTO users (id, login) VALUES (2, 'user2');
```

Check search index. 

``` bash
curl \
  -H "Authorization: Bearer test" \
  -X GET 'http://localhost:7700/indexes/users/documents'
```
