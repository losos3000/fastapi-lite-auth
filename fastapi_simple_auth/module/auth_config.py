from typing import Literal
from authx import AuthX, AuthXConfig

from fastapi_simple_auth.basics import basic_config


# MODELS CLASSES CONFIG CLASS
class ModelsConfig:
    def __init__(
            self,
            UserModel = basic_config.USER_MODEL,
    ):
        self.UserModel = UserModel


# SCHEMAS CLASSES CONFIG CLASS
class SchemasConfig:
    def __init__(
            self,
            LoginSchema = basic_config.LOGIN_SCHEMA,
            GetUserSchema = basic_config.GET_USER_SCHEMA,
    ):
        self.LoginSchema = LoginSchema
        self.GetUserSchema = GetUserSchema


# LOGIN FIELDS CONFIG CLASS
class LoginConfig:
    def __init__(
            self,
            login_field_name: str = basic_config.LOGIN_FIELD_NAME,
            password_field_name: str = basic_config.PASSWORD_FIELD_NAME,
    ):
        self.login_field_name: str = login_field_name
        self.password_field_name: str = password_field_name


# TOKEN CONFIG CLASS
class TokenConfig:
    def __init__(
            self,
            secret_key: str =basic_config.SECRET_KEY,
            token_location =basic_config.TOKEN_LOCATION,
    ):
        self.secret_key: str = secret_key
        self.token_location = token_location


# COOKIE CONFIG CLASS
class CookieConfig:
    def __init__(
            self,
            cookie_name: str =basic_config.COOKIE_NAME,
            cookie_httponly: bool | None =basic_config.COOKIE_HTTPONLY,
            cookie_secure: bool | None =basic_config.COOKIE_SECURE,
            cookie_samesite: Literal["lax", "strict", "none"] | None | None =basic_config.COOKIE_SAMESITE,
            cookie_max_age: int | None =basic_config.COOKIE_MAX_AGE,
            cookie_path: str | None =basic_config.COOKIE_PATH,
            cookie_domain: str | None =basic_config.COOKIE_DOMAIN,
            cookie_expires: str | int | None =basic_config.COOKIE_EXPIRES,
    ):
        self.cookie_name: str = cookie_name
        self.cookie_httponly: bool | None = cookie_httponly
        self.cookie_secure: bool | None = cookie_secure
        self.cookie_samesite: Literal["lax", "strict", "none"] | None = cookie_samesite
        self.cookie_max_age: int | None = cookie_max_age
        self.cookie_path: str | None = cookie_path
        self.cookie_domain: str | None = cookie_domain
        self.cookie_expires: str | int | None = cookie_expires


# MAIN CONFIG CLASS
class AuthConfig:
    def __init__(
            self,
            UserModel = basic_config.USER_MODEL,
            LoginSchema = basic_config.LOGIN_SCHEMA,
            GetUserSchema = basic_config.GET_USER_SCHEMA,
            secret_key: str = basic_config.SECRET_KEY,
            token_location=basic_config.TOKEN_LOCATION,

            cookie_name: str = basic_config.COOKIE_NAME,
            cookie_httponly: bool | None = basic_config.COOKIE_HTTPONLY,
            cookie_secure: bool | None = basic_config.COOKIE_SECURE,
            cookie_samesite: Literal["lax", "strict", "none"] | None | None = basic_config.COOKIE_SAMESITE,
            cookie_max_age: int | None = basic_config.COOKIE_MAX_AGE,
            cookie_path: str | None = basic_config.COOKIE_PATH,
            cookie_domain: str | None = basic_config.COOKIE_DOMAIN,
            cookie_expires: str | int | None = basic_config.COOKIE_EXPIRES,

            login_field_name: str = basic_config.LOGIN_FIELD_NAME,
            password_field_name: str = basic_config.PASSWORD_FIELD_NAME,
    ):
        self.models_config: ModelsConfig = ModelsConfig(
            UserModel=UserModel,
        )

        self.schemas_config: SchemasConfig = SchemasConfig(
            LoginSchema=LoginSchema,
            GetUserSchema=GetUserSchema,
        )

        self.token_config: TokenConfig = TokenConfig(
            secret_key=secret_key,
            token_location=token_location,
        )

        self.cookie_config: CookieConfig = CookieConfig(
            cookie_name = cookie_name,
            cookie_httponly = cookie_httponly,
            cookie_secure = cookie_secure,
            cookie_samesite = cookie_samesite,
            cookie_max_age = cookie_max_age,
            cookie_path = cookie_path,
            cookie_domain = cookie_domain,
            cookie_expires = cookie_expires,
        )

        self.login_config: LoginConfig = LoginConfig(
            login_field_name=login_field_name,
            password_field_name=password_field_name,
        )

        self.authx_config: AuthXConfig = AuthXConfig(
            JWT_SECRET_KEY=self.token_config.secret_key,
            JWT_TOKEN_LOCATION=self.token_config.token_location,
            JWT_ACCESS_COOKIE_NAME=self.cookie_config.cookie_name,
        )

        self.auth: AuthX = AuthX(config=self.authx_config)


    def authx_ready(self):
        self.authx_config.JWT_SECRET_KEY = self.token_config.secret_key
        self.authx_config.JWT_TOKEN_LOCATION = self.token_config.token_location
        self.authx_config.JWT_ACCESS_COOKIE_NAME = self.cookie_config.cookie_name

        self.auth.load_config(config=self.authx_config)




auth_config = AuthConfig(login_field_name="username")

