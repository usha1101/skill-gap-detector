# 🚀 Smart Multi-Branch Career Skill Gap Detector

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Architecture](https://img.shields.io/badge/Architecture-Standard_Library_HTTP-brightgreen)](https://docs.python.org/3/library/http.server.html)
[![Zero-Dependencies](https://img.shields.io/badge/Dependencies-Zero_External-success)](https://pypi.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A web-based engineering career advising application built with pure Python that compares a student's current skill profile against industry role requirements, computes a role readiness match score, and generates a tailored learning roadmap.

---

## 🌟 Key Features

- **Multi-Branch Coverage:** Supports 6 engineering disciplines:
  - Computer Science & Engineering (CS)
  - Mechanical Engineering
  - Electronics & Communication (ECE)
  - Electrical & Electronics (EEE)
  - VLSI Design & Embedded Systems
  - Civil Engineering
- **Automated Skill Deficit Analysis:** Identifies precise missing technical competencies.
- **Match Readiness Score:** Computes real-time percentage readiness.
- **Dynamic Learning Roadmap:** Generates structured step-by-step roadmaps to close identified skill gaps.
- **Zero External Dependencies:** Built entirely with Python's standard library (`http.server`, `urllib.parse`, `json`).

---

## 🏗️ Architecture & Data Flow

```mermaid
flowchart LR
    A[Student Input:<br>Branch, Role, Skills] --> B[POST /analyze<br>server.py]
    B --> C[(roles.json<br>Industry Benchmarks)]
    C --> D[Gap Comparison &<br>Percentage Calculator]
    D --> E[Rendered Report Card<br>result.html]
```

---

## 🛠️ Tech Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Backend** | Python (`http.server`) | HTTP request routing and score computation |
| **Data Store** | JSON (`roles.json`) | Engineering branch skill taxonomies & roadmaps |
| **Frontend** | HTML5 & CSS3 | User input interface & visual dashboard |

---

## ⚙️ How It Works

1. **Select Branch:** Choose your engineering domain.
2. **Select Target Role:** Choose desired career specializations.
3. **Enter Skills:** Input acquired technical skills (comma-separated).
4. **Instant Diagnostic:** Receive readiness percentage, missing prerequisites, and customized curriculum roadmap.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+ (No `pip install` required!)

### 1. Clone the Repository
```bash
git clone https://github.com/usha1101/skill-gap-detector.git
cd skill-gap-detector
```

### 2. Run the Local Server
```bash
python server.py
```

### 3. Open in Browser
Navigate to:  
`http://localhost:8000`

---

## 📸 Application Screenshots

<p align="center">
  <img width="850" alt="Career Skill Gap Detector Form" src="https://github.com/user-attachments/assets/33f39d44-0684-4fda-b2d9-3fa88f6e442c" />
</p>

<p align="center">
  <img width="600" alt="Analysis Report and Match Score" src="https://github.com/user-attachments/assets/147fe8bb-0f00-48b5-92f0-ddb97ccc5f03" />
</p>

<p align="center">
  <img width="850" alt="Personalized Learning Roadmap" src="https://github.com/user-attachments/assets/473dff9d-f301-42ba-9fc8-05896d55e4b8" />
</p>

---

## 📂 Repository Structure

```text
skill-gap-detector/
├── .gitignore       # Python cache rules
├── README.md        # Project guide and architecture documentation
├── index.html       # Student input form
├── result.html      # Analysis results and roadmap template
├── roles.json       # Industry role skills taxonomy and roadmap dictionary
├── server.py        # Lightweight HTTP server & analytical engine
└── style.css        # Clean UI styling
```

---

## 👩‍💻 Author

**Ushashree M**  
- B.Tech Artificial Intelligence & Data Science, Reva University  
- GitHub: [@usha1101](https://github.com/usha1101)  

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
