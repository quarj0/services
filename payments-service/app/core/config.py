from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Hive Academy Payments Service"
    app_version: str = "0.1.0"

    model_config = SettingsConfigDict(
        env_prefix="PAYMENTS_",
        extra="ignore",
    )


settings = Settings()
