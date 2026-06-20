from app.core.config import settings

def root() -> dict[str, str]:
    return {
        "service": settings.app_name,
        "status": "ok",
    }


def health() -> dict[str, str]:
    return {"status": "healthy"}
