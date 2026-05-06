from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    NEO4J_URL: str
    NEO4J_USER: str
    NEO4J_PASSWORD: str
    AZURE_OPENAI_KEY: str
    AZURE_OPENAI_ENDPOINT: str
    AZURE_DEPLOYMENT: str

    class Config:
        env_file = ".env"

settings = Settings()