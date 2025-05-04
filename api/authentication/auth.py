from authx import AuthX, AuthXConfig
import configurations.auth_config as auth_config


config = AuthXConfig(
    JWT_SECRET_KEY = auth_config.SECRET_KEY,
    JWT_ACCESS_COOKIE_NAME = auth_config.COOKIE_NAME,
    JWT_TOKEN_LOCATION = auth_config.TOKEN_LOCATION,
)

auth = AuthX(config=config)
