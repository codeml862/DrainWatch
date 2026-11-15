# DrainWatch - Hackathon Presentation (Official 13-Slide Deck)
**Event:** Agentic AI Hackathon 2026 (Ulster University, UK & AMSE)  
**Theme:** Smart Cities and Intelligent Infrastructure / Sustainable AI for Environment  
**Project Name:** **DrainWatch: Autonomous Multi-Agent Urban Drainage & Flood Early-Warning System**  

---

## Slide 1: Title Slide (Front Slide)
* **Title:** DrainWatch: Autonomous Multi-Agent Urban Drainage & Flood Early-Warning System
* **Theme:** Smart Cities & Intelligent Infrastructure / Sustainable AI
* **Tagline:** Empowering Autonomous AI Agents for Proactive Urban Flood Prevention & Intelligent Municipal Dispatch
* **Team Name:** Team DrainWatch (or your chosen Team Name)
* **Institute / College Name:** [Your College/University Name]
* **Team Details:**
  * **Team Leader:** [Your Name] | [Email ID] | [Phone Number] | Department & Year
  * **Member 2:** [Name] | [Email ID] | [Role: ML & Computer Vision Engineer]
  * **Member 3:** [Name] | [Email ID] | [Role: Geospatial & Backend Developer]
  * **Member 4:** [Name] | [Email ID] | [Role: Agentic Workflow & Systems Architect]

---

## Slide 2: Background & Context
* **The Urban Reality:** Rapid urbanization and changing rainfall patterns have led to chronic urban waterlogging in major cities worldwide.
* **Economic & Human Impact:**
  * Waterlogged roads cause severe traffic congestion, loss of hundreds of productive commute hours, vehicular breakdowns, and road accidents.
  * Direct structural damage to road surfaces, subterranean utilities, and adjacent residential properties.
* **The Underlying Bottleneck:**
  * 80% of urban flash waterlogging is not solely due to low drainage design capacity, but because roadside storm drains and culvert inlets are **physically blocked by plastic debris, solid waste, and unmanaged silt**.
  * Citizen complaints currently arrive via fragmented channels and flood municipal hotlines with duplicate reports only *after* streets are already submerged.

---

## Slide 3: Problem Statement
* **The Core Gap:**
  * Traditional municipal management operates in an entirely **reactive** paradigm: responding with emergency pumps hours after streets become flooded.
  * Lack of predictive spatial triage: Municipal disaster teams cannot anticipate *which specific street drainage inlet* will overflow before the rain starts.
* **Exact Problem Statement:**
  > *"Develop an Agentic AI-powered urban drainage monitoring and early-warning system that identifies potential waterlogging locations using rainfall information, historical complaints, and drainage-condition reports, prioritizes high-risk areas, and recommends preventive action before flooding occurs."*

---

## Slide 4: Proposed Solution — DrainWatch
* **Virtual Municipal Monitoring Assistant:**
  * DrainWatch is an autonomous, multi-agent AI framework designed to shift municipal flood management from **disaster response to disaster prevention**.
* **Core Capabilities:**
  1. **Multimodal Ingestion:** Ingests crowdsourced citizen photos, street reports, and live Doppler rainfall forecast radar feeds.
  2. **Automated Vision Telemetry:** Computer Vision classifies drain obstructions (plastic accumulation, silt levels, flow constriction) and clusters duplicate citizen complaints.
  3. **Spatial Risk Synthesis:** Cross-correlates terrain elevation, drainage catchment capacity, and historical flooding records to compute dynamic risk scores (0–100).
  4. **Autonomous Action Orchestration:** Automatically formulates proactive municipal maintenance work orders, crew routing, and public advisories *before* downpours begin.

---

## Slide 5: Novelty, Showstopper & Unique Value Proposition (USP)
* **What Makes DrainWatch Unique?**
  * **Proactive Preemption (The Showstopper):** Eliminates the emergency phase by initiating cleaning 1–3 hours before precipitation hits the catchment basin.
  * **Autonomous Multi-Agent Collaboration:** Unlike static dashboards or rule-based alerts, specialized autonomous agents negotiate, verify data, plan interventions, and issue machine-readable work orders.
  * **Closed-Loop Vision Verification:** Maintenance crews upload post-cleaning photos; the Vision Agent re-evaluates the drain condition in real-time, downgrading the risk level and closing the operational ticket.
  * **Smart Deduplication & Noise Rejection:** Semantic geo-clustering prevents redundant dispatches from citizen panic reporting.

---

## Slide 6: System Architecture & Agentic Workflow
* **Four-Tier Autonomous Agentic Architecture:**
  1. **Perception & Ingestion Agent:**
     * Ingests citizen smartphone photos & text.
     * Computer Vision (YOLO/CLIP inference) detects plastic packaging, debris obstruction percentage, and generates geo-cluster tags.
  2. **Environmental & Weather Agent:**
     * Ingests live precipitation intensity (mm/hr), storm duration, and Doppler radar projections.
  3. **Spatial & Hydrological Risk Agent:**
     * Integrates digital elevation models (DEM), culvert flow discharge capacity, and historical incident logs.
     * Computes the Dynamic Waterlogging Risk Score ($0 \rightarrow 100$).
  4. **Action & Dispatch Orchestrator Agent:**
     * Evaluates operational threshold (e.g., Score $\ge 75 \rightarrow$ Critical High Risk).
     * Synthesizes actionable maintenance plans, dispatches mechanized super-sucker trucks, notifies traffic police for diversions, and issues citizen safety advisories.

---

## Slide 7: Tech Stack & Implementation Methodology
* **Frontend:** Streamlit & Streamlit-Folium (Intuitive, responsive GIS command center & citizen portal).
* **Backend & Workflow:** Python 3.12, LangGraph / Multi-Agent Decision Engine.
* **Geospatial & Mapping:** Folium, Leaflet, GeoPandas, OpenStreetMap.
* **AI & Computer Vision:** Scikit-learn (Risk prediction regression), YOLO/Vision LLM (Debris & blockage classification).
* **Data Storage:** SQLite (Spatial tables, incident history, work-order state machine).
* **APIs:** Weather Radar API, Municipal GIS Data Lake.

---

## Slide 8: Feasibility, Budget & Scalability
* **Operational Feasibility:**
  * Zero expensive proprietary hardware required—leverages existing citizen smartphones and standard municipal maintenance trucks.
  * Integrates seamlessly with existing Smart City Integrated Command and Control Centers (ICCC).
* **Budget & Implementation Cost:**
  * **Phase 1 (Pilot Deployment):** Cloud hosting + Open-source models + Free/Open APIs $\approx$ Minimal pilot cost ($0 - $150/month).
  * **Municipal Return on Investment (ROI):** Prevents millions in flood damages, road repair costs, and economic productivity losses.
* **Scalability:**
  * Modular design allows plug-and-play expansion to any smart city worldwide by importing local GIS shapefiles and historical rainfall maps.

---

## Slide 9: Team Member Roles & Responsibilities
* **[Member 1 - Team Lead & Systems Architect]:** Overall architecture, multi-agent state graph orchestration, and municipal workflow alignment.
* **[Member 2 - AI & Vision Engineer]:** Computer vision pipeline for drain obstruction classification, model fine-tuning, and risk scoring logic.
* **[Member 3 - Geospatial & Frontend Developer]:** Streamlit interface, interactive Folium heatmap integration, and citizen portal UX.
* **[Member 4 - Data Engineer & Backend Developer]:** Database schema design, API integrations (Weather Radar, municipal dispatch), and test simulation suite.

---

## Slide 10: Prototype Demonstration — Live Scenario Walkthrough
*(Embed actual screenshots from the running Streamlit prototype)*
* **Scenario Input:**
  * Target Location: **Area A (Central Underpass Junction)**
  * Rainfall Forecast: **Heavy (35–65 mm/hr)**
  * Drain Condition: **Severely Blocked with Plastic Bottles & Trash**
  * Historical Flood Frequency: **3 Previous Incidents**
* **Agentic Execution:**
  * **Perception Agent:** Detects solid waste choke (94% confidence), generates deduplication hash.
  * **Risk Assessment:** Calculates **87 / 100 (CRITICAL HIGH RISK)**; estimated time to inundation: 45 minutes.

---

## Slide 11: Prototype Demonstration — Autonomous Dispatch & Map Visuals
*(Embed interactive Folium Map screenshot and Municipal Dispatch Log)*
* **Folium Interactive Map:**
  * Real-time spatial visualization color-coded by vulnerability (🔴 Red: Area A, 🟠 Orange: Area B, 🟢 Green: Safe zones).
* **Generated Proactive Action Plan (Work Order #WO-8492-DW):**
  1. Inspect the drainage system immediately before downpour commences.
  2. Prioritize rapid plastic debris extraction using mechanized super-sucker unit.
  3. Alert Municipal Quick Response Team (QRT Sector-4) and stage mobile de-watering pump.
  4. Broadcast proactive advisory to Traffic Police for lane diversion.
  5. Dynamically refresh risk scores based on real-time Doppler radar.

---

## Slide 12: References & Academic Foundations
1. *Agentic AI & Multi-Agent Collaboration*: Wu, Q., et al. (2023). AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation.
2. *Urban Flood Prediction*: Henonin, J., et al. (2013). Real-time urban flood forecasting and modeling - A review. *Journal of Hydroinformatics*.
3. *Computer Vision in Municipal Infrastructure*: Al-Sarayreh, M., et al. (2021). Deep learning approaches for sewer pipe defect detection and classification.
4. *Smart City Guidelines*: Ministry of Housing and Urban Affairs (MoHUA) / UK Smart Cities Framework.

---

## Slide 13: Thank You & Contact
* **DrainWatch: Turning Reactive Cities into Proactive Smart Communities.**
* **Contact:**
  * Team DrainWatch
  * Email: [Your Email]
  * GitHub / Demo Repository: [Repository Link]
* **Open for Questions & Panel Discussion!**
