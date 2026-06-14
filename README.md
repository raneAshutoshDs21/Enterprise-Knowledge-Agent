# 🚀 Enterprise Knowledge Agent

![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Azure AI Foundry](https://img.shields.io/badge/Azure%20AI%20Foundry-412991?style=for-the-badge&logo=microsoft&logoColor=white)
![Azure OpenAI](https://img.shields.io/badge/Azure%20OpenAI-10A37F?style=for-the-badge&logo=openai&logoColor=white)
![GPT-4.1 Mini](https://img.shields.io/badge/GPT--4.1%20Mini-000000?style=for-the-badge&logo=openai&logoColor=white)
![RAG](https://img.shields.io/badge/RAG-Retrieval%20Augmented%20Generation-blue?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Azure Container Registry](https://img.shields.io/badge/Azure%20Container%20Registry-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Azure App Service](https://img.shields.io/badge/Azure%20App%20Service-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Azure DevOps](https://img.shields.io/badge/Azure%20DevOps-0078D4?style=for-the-badge&logo=azuredevops&logoColor=white)
![Application Insights](https://img.shields.io/badge/Application%20Insights-68217A?style=for-the-badge&logo=microsoft&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CI Pipeline](https://img.shields.io/badge/CI-Automated-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Deployment-Live-brightgreen?style=for-the-badge)

---

# 📖 Overview

Enterprise Knowledge Agent is an AI-powered document intelligence platform built using **Azure AI Foundry**, **Azure OpenAI**, and **Retrieval-Augmented Generation (RAG)** architecture.

The solution allows employees to interact with organizational documents using natural language and receive accurate, context-aware responses grounded strictly in enterprise knowledge sources.

Instead of manually searching through policy documents, reimbursement guidelines, employee handbooks, and operational procedures, users can ask questions conversationally and receive instant answers backed by uploaded documents.

---

# 🎯 Business Problem

Organizations often struggle with:

- Time-consuming document searches
- Scattered enterprise knowledge
- Employee dependency on HR and Operations teams
- Repetitive policy-related questions
- Lack of centralized knowledge retrieval

This project addresses these challenges by creating an AI-powered enterprise assistant capable of answering questions directly from organizational documentation.

---

# 🏗️ Solution Architecture

```text
┌───────────────────────────────┐
│         End Users             │
└──────────────┬────────────────┘
               │
               ▼
┌───────────────────────────────┐
│      Streamlit Frontend       │
│ Enterprise Knowledge UI       │
└──────────────┬────────────────┘
               │
               ▼
┌───────────────────────────────┐
│      Azure App Service        │
│ Containerized Deployment      │
└──────────────┬────────────────┘
               │
               ▼
┌───────────────────────────────┐
│     Azure AI Foundry Agent    │
└──────────────┬────────────────┘
               │
               ▼
┌───────────────────────────────┐
│       GPT-4.1 Mini Model      │
└──────────────┬────────────────┘
               │
               ▼
┌───────────────────────────────┐
│ File Search & Vector Store    │
└──────────────┬────────────────┘
               │
               ▼
┌───────────────────────────────┐
│ Enterprise Knowledge PDFs     │
└───────────────────────────────┘
```

---

# ⚙️ Key Features

## 🔍 Intelligent Document Search

Searches enterprise documents using Azure AI Foundry File Search.

---

## 🧠 Retrieval-Augmented Generation (RAG)

Combines:

- Knowledge Retrieval
- Vector Search
- GPT-4.1 Mini Reasoning

to generate accurate responses.

---

## 📚 Enterprise Knowledge Base

Supports organizational documents such as:

- Leave Policies
- Travel Policies
- Reimbursement Policies
- Employee Guidelines
- Internal SOPs

---

## 🚫 Hallucination Prevention

Agent instructions restrict responses to uploaded documents only.

Example:

```text
User:
Who won FIFA World Cup?

Agent:
The requested information was not found in the available documents.
```

---

## 📊 Monitoring & Observability

Integrated with:

- Azure Monitor
- Application Insights

Track:

- Requests
- Failures
- Response Times
- Application Health

---

## 🐳 Containerized Deployment

Application packaged and deployed using Docker.

---

## ☁️ Cloud Native Architecture

Entire solution deployed on Microsoft Azure.

---

# 🛠️ Technology Stack

| Layer | Technology |
|---------|------------|
| Frontend | Streamlit |
| Backend | Python |
| LLM | GPT-4.1 Mini |
| AI Platform | Azure AI Foundry |
| Retrieval | File Search |
| Knowledge Storage | Vector Store |
| Containerization | Docker |
| Registry | Azure Container Registry |
| Hosting | Azure App Service |
| Monitoring | Azure Monitor |
| Logging | Application Insights |
| DevOps | Azure DevOps |
| Version Control | GitHub |

---

# 📁 Project Structure

```text
Enterprise-Knowledge-Agent
│
├── docs/
│
├── src/
│   ├── services/
│   ├── agents/
│   ├── utils/
│   └── config/
│
├── tests/
│
├── Dockerfile
├── requirements.txt
├── streamlit_app.py
├── azure-pipelines.yml
├── README.md
└── .gitignore
```

---

# 🔐 Environment Variables

Create a `.env` file.

```env
PROJECT_ENDPOINT=

MODEL_DEPLOYMENT_NAME=

AGENT_NAME=

AZURE_CLIENT_ID=

AZURE_TENANT_ID=

AZURE_CLIENT_SECRET=

APPLICATIONINSIGHTS_CONNECTION_STRING=
```

---

# 🚀 Local Setup

## Clone Repository

```bash
git clone https://github.com/yourusername/enterprise-knowledge-agent.git

cd enterprise-knowledge-agent
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create:

```env
.env
```

Add Azure credentials.

---

## Run Application

```bash
streamlit run streamlit_app.py
```

---

# 🐳 Docker Deployment

## Build Image

```bash
docker build -t enterprise-knowledge-agent .
```

---

## Run Container

```bash
docker run -p 8501:8501 enterprise-knowledge-agent
```

---

# ☁️ Azure Deployment Workflow

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
Azure DevOps Pipeline
    │
    ▼
Docker Build
    │
    ▼
Azure Container Registry
    │
    ▼
Azure App Service
    │
    ▼
Enterprise Users
```

---

# 🔄 CI Pipeline

Implemented using Azure DevOps.

Pipeline performs:

- Source Checkout
- Dependency Installation
- Docker Image Build
- Push Image to Azure Container Registry
- Artifact Management

Current Status:

✅ Continuous Integration Implemented

⏳ Continuous Deployment Planned

---

# 📈 Monitoring

Azure Application Insights captures:

- User Requests
- Exceptions
- Latency
- Availability
- Application Performance

---

# 🧪 Sample Questions

### Leave Policy

```text
Tell me about annual leave policy.
```

---

### Reimbursement Policy

```text
Explain hotel reimbursement limits.
```

---

### Approval Process

```text
Who approves leave exceeding three days?
```

---

### Unsupported Question

```text
Who won the FIFA World Cup?
```

Response:

```text
The requested information was not found in the available documents.
```

---

# 📊 Project Outcomes

✅ Successfully deployed AI Agent on Azure

✅ Implemented Retrieval-Augmented Generation

✅ Connected enterprise PDFs through Vector Store

✅ Containerized application using Docker

✅ Published images to Azure Container Registry

✅ Hosted application using Azure App Service

✅ Configured Azure Monitor & Application Insights

✅ Automated CI using Azure DevOps

✅ Achieved enterprise-ready cloud deployment

---

# 🔮 Future Enhancements

## Continuous Deployment (CD)

Automated deployment from Azure DevOps to Azure App Service.

---

## Short-Term Memory

Enable conversational context retention.

Example:

```text
User:
Tell me about leave policy.

User:
What about sick leave?
```

Agent remembers prior context.

---

## Long-Term Memory

Store:

- User preferences
- Frequently accessed policies
- Historical interactions

to enable personalized enterprise assistance.

---

## Multi-Agent Architecture

Future specialized agents:

- HR Agent
- Finance Agent
- IT Support Agent
- Compliance Agent

---

## Azure AI Search

Hybrid Search:

- Semantic Search
- Keyword Search
- Vector Search

---

# 📸 Screenshots

Add screenshots here:

### Azure AI Foundry Agent

![Foundry Agent](images/foundry-agent.png)

### Azure DevOps Pipeline

![Pipeline](images/pipeline.png)

### Azure App Service

![App Service](images/app-service.png)

### Enterprise Knowledge Agent UI

![Application](images/application-ui.png)

---

# 👨‍💻 Author

**Ashutosh Rane**

Azure AI Engineer | Generative AI Enthusiast | Azure AI Foundry | Agentic AI | RAG Systems | Cloud AI Solutions

LinkedIn: https://www.linkedin.com/in/ashutosh-rane-61952018b/

GitHub: https://github.com/yourusername

---

# ⭐ If you found this project useful

Give it a star ⭐ and connect with me on LinkedIn.
