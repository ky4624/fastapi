from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `clas` ADD `addr` VARCHAR(30) NOT NULL COMMENT '班级地址' DEFAULT '';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `clas` DROP COLUMN `addr`;"""


MODELS_STATE = (
    "eJztmVtP2zAUgP8KytMmsSm9l72VbmiMARKwaRKgyEncNGpqF8cZVKj/fbbj1Lk0IaGMBp"
    "SXXo6PE58vx+fiPGpzbEPP/zz2gK992XvUEJhD9iMh39/TwGKhpFxAgekJRSvSMH1KgEWZ"
    "bAI8HzKRDX2LuAvqYsSkKPA8LsQWU3SRo0QBcu8CaFDsQDqFhA1c3zKxi2z4AP3o72JmTF"
    "zo2Ylluja/t5AbdLkQsmNEj4Qiv5tpWNgL5kgpL5Z0itFa20WUSx2IIAEU8stTEvDl89VJ"
    "KyOLwpUqlXCJsTk2nIDAozFzSzKwMOL82GrC5+Dwu3xqt7qD7rDT7w6ZiljJWjJYheYp28"
    "OJgsDZlbYS44CCUENgVNzEd4bceArIZnSRfgoeW3IaXoSqiF4kUPiUyxTy026CQQfa7BOC"
    "wU3Q6+r898FE18pRnYMHw4PIoVP2t6MXIPw9uhh/H1186Ogf+bUxc+3Q38/kSFsMccqKKr"
    "BtUoVqpP96VDXtSaaDjs4/uztkyrf7ZBZzXC4wgTW7B8Q2EiMKvk8DG/JFZR7AoZx5dHIB"
    "PSDMzkKXAe8yvMqrenXpqLCKHCiSysAjgOE2ziOWHZq352kJQMARq+b35neKUgAOiA83Jo"
    "dwpDg9KJ0mQTQJ4hUSxNCcQBbMgG7WL0FQCCzmwEYlr0xOeto76xGrXsJBM3kgQzKL8QgT"
    "6DroBC4FzWO2KICsTb4po9iVulL9KOZFfCYm4H4d71I+woxkpkEa7tnR5Xj09Zu2yk+iW6"
    "aPMjn4FKDlFeafJR/LFon4f8fegociFm+k8mTMFMILEGivNcL0GPLCRNCewWUMpXyi62ch"
    "R8N5cpBOCQ6caXyWSrsbfYHJjXRCWxVWAZENG8qAmHn5dYAfU2oKgZrF2fdZCPQO7E5YAt"
    "Qj+S/uN7hgPkipXgOOptVnRdRQb9WDIwtQFbay1N5x2cQxwkH3JjiYDLslMb7Ixo7lZvhQ"
    "xf2k+u7dr6+3+bFEu20+x/1aZdyvle9+rYz7+QhXcD+pXQP3M/tsF/c6k8Fu3I+fE1fre2"
    "IzmqYncda+ZccTHerXj1/ZdifmGjvrdeKl+3atjjpHe+udjrIk3egkOsNkp5PoZdKNTrIN"
    "2r7TEQiLW53oQGBDqxM7K8hvdWJHE02rU7fout+0Ok2r07Q6TavTtDpPtzrUpV6liLiesH"
    "uWQ71r7frVz7PeY+fWlVVeYz+/pHynb7FHkLjWdFNNJ0cKSzqgdJqK7g1VdH8h8eU+KRvC"
    "YlN2HMTKU0yErnavVyJ2Ma3c4CXGUoUI2xoVIEr1twmwpZdLpEWZNJNK2R2pfP+VhPjj8v"
    "ws5/xLTUmB/IWYgde2a9H9Pc/16W09sRZQ5FbzRc99/86Lw/twOvqT5jr+eX4oKGCfOkRc"
    "RVzgsFqKffn0svoHaenQ0A=="
)
