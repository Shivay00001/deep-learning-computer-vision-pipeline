from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Deep Learning CV Pipeline"
    API_V1_STR: str = "/api/v1"
    
    # Model Settings
    DEFAULT_MODEL: str = "fasterrcnn_resnet50_fpn"
    DEVICE: str = "cpu" # Set to 'cuda' if GPU is available
    
    # Confidence threshold
    SCORE_THRESHOLD: float = 0.5
    
    # Logging
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()
