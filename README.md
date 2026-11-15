# DrainWatch: Autonomous Multi-Agent Urban Drainage & Flood Early-Warning System

[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg?style=flat&logo=Streamlit)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg?style=flat&logo=Python)](https://python.org)
[![Hackathon](https://img.shields.io/badge/Hackathon-Agentic%20AI%202026-0284C7.svg)](https://theamse.org/hackathon/AgenticAIHackathon2026)
[![Track](https://img.shields.io/badge/Track-Smart%20Cities%20%26%20Infrastructure-16A34A.svg)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)]()

> **Shifting municipal flood management from reactive disaster relief to autonomous, predictive prevention.**  
> Built for the **Agentic AI Hackathon 2026** organized by **Ulster University, UK** & **AMSE**.

---

## Executive Summary

Every monsoon season, major metropolitan corridors across India (Mumbai, Delhi NCR, Bengaluru, Chennai, Kolkata, and Hyderabad) experience catastrophic street waterlogging, subterranean drain choking, and urban flash flooding. 

Traditional municipal response is **100% reactive**: citizen hotlines jam, panic ensues, emergency crews deploy *after* vehicles drown, and localized cloudbursts cause millions in infrastructural damages.

**DrainWatch** is an enterprise-grade, cyber-physical **Autonomous Multi-Agent System** that continuously monitors high-risk stormwater chokepoints, ingests crowdsourced vision reports and live Doppler radar data, simulates runoff surge using a hydrological digital twin, and **autonomously formulates and dispatches preventive work-orders 45–60 minutes before cloudbursts hit**.

---

## 4-Tier Multi-Agent System Architecture

DrainWatch operates as a closed-loop cyber-physical autonomous network:

```
[ Tier 1: Multimodal Perception & Edge Telemetry ]
  ├── Citizen Smartphone App (Geo-tagged Photos & Intake)
  ├── IoT Underground Stormdrain Sensors (Ultrasonic Depth & Silt)
  ├── Doppler Weather Radar (Real-Time Precipitation mm/hr)
  └── GIS Digital Elevation Models (Topographical Runoff Gradients)
                         │
                         ▼
[ Tier 2: Streaming Ingestion & Deduplication Gateway ]
  └── Kafka / MQTT Event Broker (Spatial-Temporal Clustering & De-duplication)
                         │
                         ▼
[ Tier 3: Agentic AI Cognitive Core (LangGraph Orchestrator) ]
  ├── Computer Vision Agent (YOLOv8-Sewer: Debris & Inflow Restriction)
  ├── Weather Telemetry Agent (Precipitation Window & Runoff Coefficient)
  ├── Hydrological Digital Twin Simulator (Dynamic Risk Score 0–100)
  └── Dispatch Optimization Agent (Autonomous Work-Order Generation & Routing)
                         │
                         ▼
[ Tier 4: Field Actuation & Closed-Loop Machine Auditing ]
  ├── Mechanized Super-Suckers & Jetting Units (Preemptive Extraction)
  ├── Variable-Speed Storm Pumps & Automated Canal Sluices (SCADA)
  ├── Automated Traffic Police Route Diversion Advisories
  └── Post-Action Verification Node (Field Crews Upload Clean Proof Photo)
```

---

## Key Modules & Live Capabilities

### 1. Real-Time Scenario Simulation
* Interactive parameter controls: Target Urban Hotspot, Rainfall Forecast (Light to Torrential Cloudburst), Drain Blockage State, and Historical Inundation Frequency.
* Autonomous Risk Inference: Hydrological Digital Twin calculates exact risk score (**87/100 CRITICAL HIGH RISK** in demo scenario).
* Direct Work-Order Formulation: Prepares assigned emergency units, targeted interventions, and public notices.
* One-click commitment to the Municipal Dispatch Queue.

### 2. National Urban Vulnerability Map (GIS)
* High-resolution spatial GIS powered by Leaflet & Folium.
* Pre-loaded with **17 high-vulnerability national drainage chokepoints** across **6 major metropolitan regions**:
  * **Mumbai Metropolitan Region:** Hindmata Junction, Milan Subway, Kurla West LBS Marg.
  * **Delhi NCR:** Minto Bridge Underpass, Pul Prahladpur, ITO Junction.
  * **Bengaluru Urban Corridor:** Silk Board Junction, Ecospace Bellandur, Hebbal Flyover.
  * **Chennai Coastal Corridor:** Velachery Main Road, Vyasarpadi GKM Colony, Madipakkam Lake Basin.
  * **Kolkata Riverine Corridor:** Thanthania Kalibari, Camac Street, Ultadanga Underpass.
  * **Hyderabad Deccan Plateau:** Nadeem Colony Tolichowki, Begumpet Rasoolpura Drain.
* Street-level deep zoom, real-time risk color-coding (Critical Red, Moderate Orange, Monitored Green).

### 3. Citizen Intake Portal
* Multimodal citizen reporting interface for choked drains.
* Vision AI feature extraction classifying debris type, constriction ratio, severity classification, and automated geo-spatial clustering to eliminate duplicate reports.

### 4. Operations Command Console
* Executive municipal operations dashboard for municipal commissioners and emergency crews.
* Real-time metrics tracking High Risk Zones, Maintenance Crews En Route, Ingested Reports, and Floods Averted.
* Dynamic, audit-ready database log of all dispatched work-orders.

### 5. Multi-View System Architecture
* **3D Isometric Digital Twin Visualization** (16:9 widescreen presentation-ready).
* **2D Enterprise System Flow** (LangGraph ReAct Loop).
* **Interactive White-Theme Graphviz Architecture Graph** with `-` and `+` zoom controls, mouse wheel zoom, touch pinch-to-zoom, and smooth hand-drag panning.

---

## Tech Stack

| Layer | Technologies |
|---|---|
| **Frontend UI** | Streamlit 1.28+, Custom Responsive Enterprise CSS |
| **GIS & Mapping** | Folium, Leaflet.js, OpenStreetMap |
| **Agentic AI Core** | Python, LangGraph State Machine Architecture, ReAct Loop |
| **Computer Vision** | YOLOv8 Multimodal Feature Extraction (Simulated Inference) |
| **Database** | SQLite3, Pandas |
| **Visualization** | Graphviz DOT, WebAssembly SVG rendering, HTML5 Canvas |
| **Presentation** | Python-PPTX (Automated 13-slide PowerPoint generator) |

---

## Local Installation & Quickstart

### Prerequisites
* Python 3.10, 3.11, or 3.12
* Git

### Step-by-Step Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/drainwatch.git
   cd drainwatch
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the DrainWatch Dashboard:**
   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

---

## Automated Verification Suite

Run the built-in 5-stage pre-deployment system diagnostic:
```bash
python verify_system.py
```
* **Stage 1:** SQLite Database Connectivity & Seed Location Schema.
* **Stage 2:** Multi-Agent Pipeline (Vision, Weather, Risk, Dispatch).
* **Stage 3:** Hackathon Presentation & Screenshot Assets.
* **Stage 4:** Python Codebase Syntax Integrity.
* **Stage 5:** Streamlit HTTP Server Health Status.

---

## Submission Documents

* **Full Presentation PPTX:** [`DrainWatch_Final_Hackathon_Submission.pptx`](DrainWatch_Final_Hackathon_Submission.pptx) (13 slides, official template format, fully populated with diagrams and screenshots).
* **Slide Transcript & Deck Plan:** [`DrainWatch_Hackathon_13_Slides.md`](DrainWatch_Hackathon_13_Slides.md).

---

## Team & Hackathon Details

* **Event:** Agentic AI Hackathon 2026
* **Organizers:** Ulster University, UK & AMSE
* **Track:** Smart Cities & Intelligent Infrastructure / Sustainable AI
* **Submission Deadline:** 16 November 2026, 10:00 PM IST
* **Portal:** [Agentic AI Hackathon 2026 Portal](https://theamse.org/hackathon/AgenticAIHackathon2026)

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.
