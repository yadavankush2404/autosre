<a name="readme-top"></a>

<div align="center">
  <a href="https://github.com/yourusername/autosre">
    <img src="https://img.icons8.com/?size=100&id=lsZBoVE2zMo3&format=png&color=000000" alt="Logo" width="80" height="80">
  </a>

  <h1 align="center">AutoSRE</h1>

  <p align="center">
    <b>Self-Healing Infrastructure through Agentic Intelligence.</b>
    <br />
    An Autonomous Incident Response layer for Distributed Microservices.
    <br />
    <br />
  </p>
</div>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis">
  <img src="https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white" alt="LangChain">
  <img src="https://img.shields.io/badge/ChromaDB-FF4B4B?style=for-the-badge&logo=googlecloud&logoColor=white" alt="ChromaDB">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI">
</div>

<br />

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#system-architecture">System Architecture</a></li>
    <li><a href="#core-workflow">Core Workflow</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#chaos-testing">Chaos Testing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

---

## 🤖 About The Project

**AutoSRE** is a proactive operations layer designed to bridge the gap between "Observability" and "Action." Traditional monitoring tells you *when* a service is down; AutoSRE decides *how* to fix it. 

By leveraging **Agentic RAG**, the system consumes real-time failure events from a Redis stream, retrieves technical remediation steps from a Vector Database, and executes the necessary API calls to restore service health—all without human intervention.

**Key Capabilities:**
* 📡 **Event-Driven Monitoring:** Asynchronous failure detection via Redis Pub/Sub.
* 🧠 **Knowledge-Augmented Reasoning:** Uses ChromaDB to store and query SRE Runbooks (Manuals).
* 🛠️ **Autonomous Tool-Use:** A "Host Agent" that can dynamically call Microservice endpoints to apply patches.
* 📉 **MTTR Reduction:** Slashes Mean Time to Recovery by automating the "Discovery & Investigation" phase of incidents.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🏗️ System Architecture



The architecture is built on the principle of **Separation of Concerns**:
1. **The Victims (Microservices):** Independent Flask services that emit "Heartbeat" or "Failure" signals.
2. **The Backbone (Redis):** Acts as the high-speed message broker for incident streaming.
3. **The Brain (Host Agent):** An LLM-powered controller that uses tools to fetch documentation and execute fixes.
4. **The Library (VectorDB):** Stores unstructured runbooks as high-dimensional embeddings for semantic search.

---

## ⚡ Core Workflow

1. **Signal:** A service encounters an error (e.g., `DB_CONN_LIMIT`) and publishes to the Redis `incidents` channel.
2. **Retrieve:** The Host Agent picks up the alert and queries ChromaDB for the matching Runbook.
3. **Analyze:** The LLM evaluates the Runbook steps against the current service state.
4. **Act:** The Agent invokes the `execute_remediation` tool to hit the `/fix` endpoint on the failing service.
5. **Verify:** The Agent performs a follow-up health check to ensure the remediation was successful.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🚀 Getting Started

### Prerequisites
* Redis Server (Running on `localhost:6379`)
* Python 3.11+
* OpenAI API Key

### Installation



1. Clone the repo:

```bash
git clone https://github.com/yadavankush2404/autosre.git

```

2. Install packages:

```bash
pip install flask redis chromadb langchain langchain-openai python-dotenv

```


3. Initialize the Vector Knowledge Base:
```bash
python data/setup_vectordb.py

```



---

## 🧪 Chaos Testing

To see **AutoSRE** in action, follow this sequence:


1. **Start the Agent** 
```bash
python brain/host_agent.py
```
2. **Start the Service** 
```bash
python services/payment_service.py
```
3. **Inject Chaos** 
```bash
curl http://localhost:5001/chaos/trigger
```



4. **Observe:** Watch the Agent logs as it detects the 500 error, searches the runbook, and automatically calls the `/fix-pool` endpoint.

---

## 📧 Contact

**Ankush Yadav** - Final Year B.Tech CSE @ MMMUT

Project Link: [https://github.com/yadavankush2404/autosre](https://www.google.com/url?sa=E&source=gmail&q=https://github.com/yourusername/autosre)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 📜 License
This project is open-source. Feel free to use it to protect your own data!