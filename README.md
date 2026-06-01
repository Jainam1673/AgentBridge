# AgentBridge

Enterprise GenAI Deployment Platform.

## Architecture

- **Backend:** FastAPI, Python 3.14+, LangGraph, OpenTelemetry, SQLAlchemy 2.0, PyTorch, XGBoost.
- **Frontend:** Next.js 16+, TypeScript, Bun, Tailwind CSS, shadcn/ui, TanStack Query, Zustand.
- **Infrastructure:** Google Cloud (Vertex AI, BigQuery, Cloud Run, Cloud SQL, Redis).

## Project Structure

- `backend/`: FastAPI backend with domain-driven design.
- `frontend/`: Next.js dashboard application.
- `infra/`: Terraform configurations for GCP.
- `data/`: Seed data and tenant simulations.
- `docs/`: Design documents and ADRs.

## Getting Started

### Backend
1. Install `uv`.
2. `cd backend && uv sync`
3. `uv run uvicorn src.main:app --reload`

### Frontend
1. Install `bun`.
2. `cd frontend && bun install`
3. `bun dev`

### Infrastructure
1. Install `terraform`.
2. `cd infra && terraform init`
3. `terraform plan -var="project_id=YOUR_PROJECT_ID"`
