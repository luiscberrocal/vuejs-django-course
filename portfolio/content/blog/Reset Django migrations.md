---
creation date: 2022-08-22 17:00
modification date: 2022-08-22 17:00
toc: true
---

# Reset Django migrations

[[Django]] [[migrations]]

https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html



## 1 Keeping the same database

```shell
python manage.py showmigrations
```

```
d-manage migrate --fake felix_pago zero
```

```shell
find . -path "*/felix_pago/migrations/*.py" -not -name "__init__.py" -delete
```


```shell
find . -path "*/migrations/*.pyc"  -delete
```

```shell
d-manage migrate --fake-initial
```
