"""Main application for the Caeloq Studios AI Phone Automation Platform."""

from fastapi import FastAPI

app = FastAPI(
    title="AI Phone Automation Platform",
    description=(
        "Backend services for Caeloq Studios' conversational AI "
        "and business automation platform."
    ),
    version="0.1.0",
)


@app.get("/", tags=["System"])
def root() -> dict[str, str]:
    """Return basic information about the service."""
    return {
        "service": "AI Phone Automation Platform",
        "company": "Caeloq Studios",
        "version": "0.1.0",
        "status": "online",
    }


@app.get("/health", tags=["System"])
def health_check() -> dict[str, str]:
    """Return the current health status of the application."""
    return {"status": "healthy"}