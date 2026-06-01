# AgentBridge: Enterprise GenAI Deployment Platform

[![GCP Native](https://img.shields.io/badge/GCP-Native-4285F4?logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![Multi-Agent](https://img.shields.io/badge/Agentic-LangGraph-FF6F61?logo=langchain)](https://langchain-ai.github.io/langgraph/)
[![Python 3.13+](https://img.shields.io/badge/Python-3.13+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Next.js 16](https://img.shields.io/badge/Next.js-16-000000?logo=next.js&logoColor=white)](https://nextjs.org/)

AgentBridge is a production-grade, Google Cloud-native platform designed to bridge the gap between disconnected enterprise infrastructure (Google Drive, GitHub, Jira, PostgreSQL) and multi-agent AI systems.

**Inspired by the role of a Google Cloud Forward Deployed Engineer (GenAI)**, this platform demonstrates how organizations can deploy, evaluate, secure, and observe agentic workflows at enterprise scale.

---

## 🚀 Key Value Propositions

- **Multi-Agent Orchestration:** Specialized agents (Planner, Knowledge, Data, Action, Critic) coordinated via **LangGraph** to handle complex, non-linear workflows.
- **Enterprise Connectivity:** Native MCP (Model Context Protocol) servers for secure, tool-based access to corporate data silos.
- **AI Readiness Assessment:** A proprietary ML engine (XGBoost/Pandas) that evaluates data freshness, completeness, and metadata quality to score tenant readiness.
- **Production-Grade ML:** Real-world classification models (PyTorch) for ticket routing and escalation priority prediction—not just wrappers.
- **Observability & Tracing:** Full request lifecycle tracing using **OpenTelemetry**, exported to Google Cloud Trace/Logging.

---

## 🏛 Architecture Overview

AgentBridge follows a **Clean Architecture** pattern, separating domain logic from infrastructure and presentation.

### High-Level Stack
| Layer | Technologies |
| :--- | :--- |
| **Backend** | Python 3.13+, FastAPI, SQLAlchemy 2.0 (Async), Pydantic v2, `uv` |
| **Orchestration** | LangGraph, LangChain, Redis (State/Checkpointing) |
| **Frontend** | Next.js 16 (App Router), TypeScript, Bun, Tailwind CSS, shadcn/ui |
| **Machine Learning** | PyTorch (Neural Networks), XGBoost (Classification), Vertex AI |
| **GCP Services** | BigQuery (DW), Cloud Run, Cloud SQL (Postgres), Vertex AI, Secret Manager |
| **Infrastructure** | Terraform, Docker, GitHub Actions |

---

## 🛠 Core Components

### 1. Multi-Agent System (LangGraph)
We implement a **Hierarchical Planner-Executor** pattern:
- **Planner:** Decomposes complex user queries into atomic steps.
- **Knowledge Agent:** Performs multi-hop retrieval across Vector Stores and BigQuery.
- **Action Agent:** Executes workflows (e.g., Jira ticket creation) via MCP tools.
- **Critic:** Evaluates groundedness and safety before returning the final response.

### 2. Data Ingestion & Warehouse
- **ETL Pipeline:** Handles incremental sync from Google Drive and GitHub.
- **Embedding Pipeline:** Utilizes Vertex AI `text-embedding-004` with chunk versioning.
- **BigQuery Warehouse:** Stores long-term traces, evaluations, and structured analytics for tenant-wide reporting.

### 3. Evaluation Framework
AgentBridge doesn't just "talk"—it measures. We track:
- **Groundedness:** Percentage of claims backed by retrieved context.
- **Hallucination Rate:** Measured via LLM-as-a-judge comparison.
- **Safety:** Content filtering and prompt injection detection.

---

## 📋 Getting Started

### Prerequisites
- Google Cloud Project with Billing Enabled
- Python 3.13+ & `uv`
- Bun 1.1+
- Terraform 1.5+

### Local Development (Simulated)
1. **Clone the Repo:**
   ```bash
   git clone https://github.com/Jainam1673/AgentBridge.git
   cd AgentBridge
   ```

2. **Backend Setup:**
   ```bash
   cd backend
   uv sync
   uv run uvicorn src.main:app --reload
   ```

3. **Frontend Setup:**
   ```bash
   cd frontend
   bun install
   bun dev
   ```

4. **Seed Multi-Tenant Data:**
   ```bash
   cd backend
   uv run python src/seed.py
   ```

---

## 📂 Project Structure

```text
AgentBridge/
├── backend/            # FastAPI & LangGraph core
│   ├── src/agents/     # Multi-agent node definitions
│   ├── src/ml/         # PyTorch/XGBoost models & pipelines
│   └── src/mcp/        # Model Context Protocol servers
├── frontend/           # Next.js 16 Dashboard
│   ├── src/app/        # Dashboard pages (Overview, Readiness, Traces)
│   └── src/components/ # Reusable shadcn/ui components
├── infra/              # Terraform (HCL) modules for GCP
├── data/               # Simulation data for Acme, Globex, & HealthCorp
└── docs/               # Architecture Decision Records (ADRs)
```

---

## 🛡 Security & Compliance
- **OAuth 2.0:** Integrated with Google Identity for secure user access.
- **RBAC:** Fine-grained permissions (Admin, Manager, User) enforced at the API and Tool levels.
- **Audit Logging:** Every agent action and tool execution is logged with user context for compliance.

---

## 📈 Roadmap
- [ ] GKE Deployment for high-availability agent clusters.
- [ ] Support for fine-tuned Gemini models on tenant-specific datasets.
- [ ] Real-time cost-per-session tracking in the dashboard.

---

## 👨‍💻 Author
**Jainam** - [GitHub](https://github.com/Jainam1673)

*Note: This project was built to demonstrate proficiency in architecting enterprise-grade GenAI systems on Google Cloud.*
