from blogger_service import SERVICE_NAME
from chili import gateway


class Config(gateway.BaseConfig):

    def __init__(self):
        super().__init__(SERVICE_NAME)

    def get_db_config(self):
        return self._get_config('DATABASE')