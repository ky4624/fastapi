config_orm = {
        "connections": {
            "default": {
                "engine": "tortoise.backends.mysql",
                "credentials": {
                    "host": "localhost",
                    "port": 3306,
                    "user": "root",
                    "password": "Aa147258369",
                    "database": "orm",
                },
            },
        },
        "apps": {
            "models": {
                "models": ["models", "aerich.models"],
                "default_connection": "default",
            },
        },
    }