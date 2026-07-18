# 🛡 Credentia

> **Privacy-Preserving Eligibility Verification**
>
> **Prove What Matters. Reveal Nothing Else.**
>
> **AI-powered verification. Privacy by design.**

Built for the **Midnight Network Hackathon 2026**

AI-assisted verification using **Qwen**

---

## 🌐 Live Demo

**Application**

https://credentia.gotihub.com

**API Documentation**

https://credentia.gotihub.com/docs

---

## 📸 Product Walkthrough

![Credentia Product Walkthrough](docs/screenshots/credentia-overview.png)

The walkthrough highlights the complete privacy-preserving verification journey:

- 🏠 Hero Experience
- 📄 Financial Document Upload
- 🤖 AI Verification Pipeline
- 📜 Privacy-Preserving Verification Certificate

---

# 🚀 Platform Vision

Credentia is a configurable **privacy-preserving verification platform** designed to verify eligibility without exposing sensitive personal information.

While this demonstration focuses on **Accredited Investor Verification**, the underlying architecture is reusable across multiple verification domains by combining AI-assisted document understanding with privacy-first verification principles inspired by Midnight.

Future verification policies include:

- 🪪 Identity Verification
- 🏢 Employment Verification
- 💰 Proof of Funds
- 🌍 Residency Verification
- 🎓 Education Verification
- 💼 Professional Certification

Each verification policy leverages the same selective disclosure engine while minimizing unnecessary exposure of sensitive data.

---

# 🌙 Why Midnight

Traditional verification workflows often require users to disclose complete financial documents containing sensitive personal information.

Credentia demonstrates a privacy-first approach inspired by Midnight's philosophy by verifying eligibility while minimizing disclosure of confidential data.

Instead of sharing the underlying financial document, users receive a **privacy-preserving verification certificate** that organizations can trust while sensitive financial information remains protected.

---

# 🔐 Privacy Proof Layer

Credentia separates eligibility verification from proof generation through a dedicated **Privacy Proof Service**.

After eligibility is evaluated, a deterministic proof commitment is generated from the verification outcome without embedding sensitive financial information.

The proof generation process is encapsulated behind a **Midnight Network Adapter**, allowing the current demonstration to simulate a privacy-preserving verification workflow while remaining ready for future native Midnight integrations.

This architecture keeps business logic independent from the underlying proof provider and supports future evolution without requiring application redesign.

---

# 🏗 Architecture

```text
          Financial Document
                  │
                  ▼
         Identity Extraction Agent
                  │
                  ▼
        Eligibility Verification Agent
                  │
                  ▼
        Certificate Generation Agent
                  │
                  ▼
         Privacy Proof Service
                  │
                  ▼
        Midnight Network Adapter
          (Simulation Layer)
                  │
                  ▼
      Proof Commitment Generation
                  │
                  ▼
 Privacy-Preserving Verification Certificate
```

---

# ⚙️ Verification Workflow

```text
Upload Financial Document
            │
            ▼
AI Document Understanding
            │
            ▼
Identity Extraction
            │
            ▼
Eligibility Evaluation
            │
            ▼
Privacy Proof Generation
            │
            ▼
Proof Commitment
            │
            ▼
Verification Certificate
```

---

# ✨ Features

- 🔐 Privacy-Preserving Verification
- 🤖 AI-Assisted Document Understanding
- 📄 Financial Document Processing
- 👤 Identity Extraction
- ✅ Eligibility Verification
- 🔐 Privacy Proof Generation
- 📜 Verification Certificate Generation
- 🌙 Midnight Adapter Architecture
- 🔒 Selective Disclosure
- ⚡ FastAPI Backend
- 🎨 Streamlit User Interface
- 📊 Downloadable Verification Reports

---

# 🛠 Technology Stack

### Backend

- FastAPI
- Pydantic
- PyMuPDF
- pdfplumber

### Frontend

- Streamlit

### AI

- Qwen (AI-assisted extraction)
- Multi-Agent Verification Pipeline

### Platform

- Midnight Network Hackathon

---

# 📋 Supported Verification Policies

## Current Demonstration

- ✅ Accredited Investor Verification

## Planned Policies

- 🪪 Identity Verification
- 🏢 Employment Verification
- 💰 Proof of Funds
- 🌍 Residency Verification
- 🎓 Education Verification
- 💼 Professional Certification

---

# 📂 Repository Structure

```text
src/
├── agents/
│   ├── identity_agent.py
│   ├── eligibility_agent.py
│   └── certificate_agent.py
│
├── services/
│   ├── privacy_proof.py
│   └── midnight/
│       └── adapter.py
│
├── api/
│   ├── app.py
│   └── routes.py
│
├── ui/
│   ├── app.py
│   ├── components.py
│   ├── theme.py
│   └── pages/
│       ├── upload.py
│       └── result.py
│
└── core/
```

---

# 🚀 Getting Started

```bash
git clone https://github.com/apurba-labs/credentia.git

cd credentia

uv sync

# Start the FastAPI backend
uv run uvicorn main:app --reload

# In another terminal, start the Streamlit UI
uv run streamlit run src/ui/app.py
```

---

# 📄 License

MIT License

---

# ❤️ Built For

**Midnight Network Hackathon 2026**

Privacy-Preserving Eligibility Verification

🤖 AI-assisted verification using Qwen

🌙 Privacy-first architecture inspired by Midnight

🔐 Selective Disclosure by Design

Open Source by **Gotihub**

© 2026 Gotihub