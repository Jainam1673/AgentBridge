from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from src.api.routes import health, auth
from src.observability.setup import setup_opentelemetry

app = FastAPI(
    title="AgentBridge API",
    description="Enterprise GenAI Deployment Platform API",
    version="0.1.0",
)

# Set up OpenTelemetry
setup_opentelemetry(app)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
async def root():
    return {"message": "Welcome to AgentBridge API"}

FastAPIInstrumentor.instrument_app(app)
