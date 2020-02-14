# Troubleshooting

## Odoo boot fails

**Behavior**

Odoo starts, but throws internal error.

**Error**

```
2020-02-14 10:44:37,227 1 ERROR odoo odoo.modules.loading: Database odoo not initialized, you can force it with `-i base` 
```

**Reference**

https://github.com/odoo/odoo/issues/27447

*Workaround**

```
docker exec -it odoo01 /bin/bash
odoo -i base -d odoo --stop-after-init --db_host=$HOST -r $USER -w $PASSWORD
```
