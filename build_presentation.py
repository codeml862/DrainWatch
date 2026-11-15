import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Colors
    NAVY = RGBColor(15, 23, 42)       # #0F172A
    SLATE = RGBColor(30, 41, 59)      # #1E293B
    LIGHT_BG = RGBColor(248, 250, 252) # #F8FAFC
    BLUE = RGBColor(2, 132, 199)      # #0284C7
    CYAN = RGBColor(56, 189, 248)     # #38BDF8
    WHITE = RGBColor(255, 255, 255)
    DARK_TEXT = RGBColor(15, 23, 42)
    MUTED_TEXT = RGBColor(100, 116, 139)
    GREEN = RGBColor(22, 163, 74)

    screenshots_dir = os.path.join(os.path.dirname(__file__), "screenshots")

    def add_header(slide, title_text, category_text="Agentic AI Hackathon 2026 | Ulster University & AMSE"):
        # Header banner shape
        header_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.1))
        header_shape.fill.solid()
        header_shape.fill.fore_color.rgb = NAVY
        header_shape.line.fill.background()

        tf = header_shape.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.8)
        tf.margin_top = Inches(0.18)

        p1 = tf.paragraphs[0]
        p1.text = category_text.upper()
        p1.font.size = Pt(10)
        p1.font.bold = True
        p1.font.color.rgb = CYAN

        p2 = tf.add_paragraph()
        p2.text = title_text
        p2.font.size = Pt(20)
        p2.font.bold = True
        p2.font.color.rgb = WHITE

    # ==========================================
    # SLIDE 1: TITLE SLIDE (Front Slide)
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = NAVY
    bg1.line.fill.background()

    tb = s1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.333), Inches(5.0))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "AGENTIC AI HACKATHON 2026 — ULSTER UNIVERSITY, UK & AMSE"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = CYAN

    p = tf.add_paragraph()
    p.text = "DrainWatch"
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = WHITE

    p = tf.add_paragraph()
    p.text = "Autonomous Multi-Agent Urban Drainage & Flood Early-Warning System"
    p.font.size = Pt(22)
    p.font.color.rgb = RGBColor(147, 197, 253)

    p = tf.add_paragraph()
    p.text = "\nTheme: Smart Cities and Intelligent Infrastructure / Sustainable AI for Environment"
    p.font.size = Pt(14)
    p.font.color.rgb = WHITE

    p = tf.add_paragraph()
    p.text = "Team Name: Team DrainWatch | College/Institute: [Your University/College Name]"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = CYAN

    p = tf.add_paragraph()
    p.text = "Team Leader: [Leader Name] | Contact: [Leader Email] | Phone: [Mobile Number]\nTeam Members: [Member 2 (ML/Vision)], [Member 3 (GIS/Backend)], [Member 4 (Agentic Systems)]"
    p.font.size = Pt(12)
    p.font.color.rgb = RGBColor(203, 213, 225)

    # Helper for 2-column text slide
    def make_content_slide(title, subtitle, left_title, left_bullets, right_title, right_bullets):
        slide = prs.slides.add_slide(blank_layout)
        add_header(slide, title, subtitle)

        # Left Box
        box_left = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.4))
        box_left.fill.solid()
        box_left.fill.fore_color.rgb = LIGHT_BG
        box_left.line.color.rgb = RGBColor(226, 232, 240)
        tf_l = box_left.text_frame
        tf_l.word_wrap = True
        tf_l.margin_left = Inches(0.4)
        tf_l.margin_right = Inches(0.4)
        tf_l.margin_top = Inches(0.4)

        p = tf_l.paragraphs[0]
        p.text = left_title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = NAVY

        for b in left_bullets:
            p = tf_l.add_paragraph()
            p.text = "• " + b
            p.font.size = Pt(13)
            p.font.color.rgb = DARK_TEXT
            p.space_after = Pt(8)

        # Right Box
        box_right = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.4))
        box_right.fill.solid()
        box_right.fill.fore_color.rgb = LIGHT_BG
        box_right.line.color.rgb = RGBColor(226, 232, 240)
        tf_r = box_right.text_frame
        tf_r.word_wrap = True
        tf_r.margin_left = Inches(0.4)
        tf_r.margin_right = Inches(0.4)
        tf_r.margin_top = Inches(0.4)

        p = tf_r.paragraphs[0]
        p.text = right_title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = NAVY

        for b in right_bullets:
            p = tf_r.add_paragraph()
            p.text = "• " + b
            p.font.size = Pt(13)
            p.font.color.rgb = DARK_TEXT
            p.space_after = Pt(8)

        return slide

    # ==========================================
    # SLIDE 2: BACKGROUND & URBAN CONTEXT
    # ==========================================
    make_content_slide(
        "1. Background & Urban Flooding Context",
        "The Chronic Reality of Modern Smart Cities",
        "The Urban Waterlogging Crisis",
        [
            "Rapid urbanization, impermeable surfaces, and erratic cloudbursts cause acute urban flooding worldwide.",
            "Waterlogged roads paralyze transportation, stall emergency response, damage subterranean utilities, and cause massive economic productivity loss.",
            "India and global cities witness hundreds of underpasses and arterial corridors inundated each monsoon season."
        ],
        "The Critical Unseen Bottleneck",
        [
            "Inundation is rarely caused solely by pipe capacity; over 75% of flood events occur because roadside storm grates and culverts are choked with single-use plastic waste and unmanaged silt.",
            "Citizens flood municipal helplines with repetitive, unverified complaints only AFTER waterlogging has already occurred.",
            "Municipal bodies operate in an entirely reactive posture: scrambling emergency pumps after roads are submerged."
        ]
    )

    # ==========================================
    # SLIDE 3: PROBLEM STATEMENT
    # ==========================================
    make_content_slide(
        "2. Problem Statement & The Core Gap",
        "From Disaster Reaction to Preemptive Prevention",
        "Current Municipal Gaps",
        [
            "Lack of Predictive Triage: Municipal disaster authorities do not know which specific drainage chokepoints will fail before rainfall commences.",
            "Noise & Duplicate Spam: Multiple frantic citizen reports over identical locations overwhelm control center dispatchers.",
            "Delayed Operational Loop: Mobilizing heavy suction trucks and pumps during active downpours is slow and inefficient."
        ],
        "Official Problem Statement",
        [
            '"Develop an Agentic AI-powered urban drainage monitoring and early-warning system that identifies potential waterlogging locations using rainfall information, historical complaints, and drainage-condition reports, prioritizes high-risk areas, and recommends preventive action before flooding occurs."',
            "Goal: Zero Urban Flood Damage through autonomous pre-event intervention."
        ]
    )

    # ==========================================
    # SLIDE 4: PROPOSED SOLUTION - DRAINWATCH
    # ==========================================
    make_content_slide(
        "3. Proposed Solution — DrainWatch",
        "Autonomous Virtual Municipal Monitoring Assistant",
        "How DrainWatch Operates",
        [
            "Continuous Multimodal Perception: Ingests citizen smartphone photos, IoT ultrasonic depth telemetry, Doppler rain radar, and GIS terrain models.",
            "Cognitive Risk Synthesis: Evaluates localized runoff generation against subterranean culvert flow capacity to generate dynamic Risk Scores (0–100).",
            "Autonomous Work-Order Generation: Formulates mechanized cleaning dispatches and public advisories 1–3 hours before cloudbursts hit."
        ],
        "Core Capabilities",
        [
            "Computer Vision Debris Classifier: Automatically identifies plastic accumulation and estimates inflow restriction percentage.",
            "Spatial-Temporal Deduplication: Clusters repetitive citizen complaints into single actionable incidents.",
            "Closed-Loop Auditability: Field teams upload post-cleaning photo proofs to re-evaluate the site and auto-close maintenance tickets."
        ]
    )

    # ==========================================
    # SLIDE 5: NOVELTY & SHOWSTOPPER (USP)
    # ==========================================
    make_content_slide(
        "4. Novelty, Showstopper & Unique Value Proposition",
        "Why DrainWatch Outperforms Conventional Solutions",
        "Key Showstoppers",
        [
            "True Preemptive Prevention: Eliminates emergency crises by clearing choked grates 2 hours BEFORE rainfall arrives.",
            "Autonomous Multi-Agent Swarm: Unlike static dashboards, specialized autonomous agents reason, negotiate, and execute machine-readable work-orders without human micromanagement.",
            "Zero Cost Hardware Barrier: Fully functional using existing citizen smartphones and standard municipal maintenance trucks—no millions required for proprietary sensors."
        ],
        "Technological Novelty",
        [
            "LangGraph Agentic State Machine: Coordinates Perception, Weather, Digital Twin Simulation, and Dispatch Agents.",
            "Closed-Loop Verification Protocol: Verifies cleaning execution with optical AI to reset the spatial risk index.",
            "Scalable to Any City: Plug-and-play adaptability by loading municipal GIS shapefiles and local rainfall radar APIs."
        ]
    )

    # ==========================================
    # SLIDE 6: SYSTEM ARCHITECTURE (WITH IMAGE)
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "5. System Architecture & Multi-Agent Design", "4-Tier Cyber-Physical Agentic Framework")
    img_arch = os.path.join(screenshots_dir, "drainwatch_architecture_enterprise_2d.jpg")
    if os.path.exists(img_arch):
        s6.shapes.add_picture(img_arch, Inches(0.8), Inches(1.35), Inches(11.733), Inches(5.75))

    # ==========================================
    # SLIDE 7: TECH STACK & METHODOLOGY
    # ==========================================
    make_content_slide(
        "6. Technical Stack & Implementation Methodology",
        "Robust, Modular & Scalable Production Architecture",
        "Frontend & Geospatial Stack",
        [
            "User Interface: Streamlit & Streamlit-Folium (Responsive, enterprise-grade executive dashboard).",
            "Spatial Mapping: Leaflet, OpenStreetMap, GeoPandas (All-India live drainage node monitoring with street-level zoom).",
            "Database: SQLite & SpatialLite (Incident history, citizen complaints, and stateful dispatch logs)."
        ],
        "AI, Machine Learning & Agentic Core",
        [
            "Multi-Agent Orchestration: Python 3.12, LangGraph / ReAct Reasoning Framework.",
            "Computer Vision: YOLOv8-Sewer & Multimodal Vision Models (Blockage & plastic classification).",
            "Hydrological Simulation: Non-linear regression risk engine cross-referencing rainfall, elevation, and historical flood frequency.",
            "APIs: Doppler Weather Radar API, Municipal SCADA & GIS Data Lake."
        ]
    )

    # ==========================================
    # SLIDE 8: FEASIBILITY, BUDGET & SCALABILITY
    # ==========================================
    make_content_slide(
        "7. Feasibility, Budget & Municipal Impact",
        "High Operational Return on Investment",
        "Budget & Cost Effectiveness",
        [
            "Phase 1 Cloud Deployment: ~$50 - $150 / month (leveraging open-source models and public GIS/weather APIs).",
            "Zero Sensor Mandate: Works immediately with crowdsourced citizen reporting; integrates with IoT depth sensors as smart cities scale.",
            "Immense ROI: A single prevented major urban flood saves millions in road resurfacing, vehicular damage, and lost work hours."
        ],
        "Scalability & Municipal Governance",
        [
            "Modular City Ingestion: Expandable to any municipality worldwide by importing city boundary and elevation models.",
            "Integration with Smart City ICCC: Directly integrates with existing Integrated Command and Control Centers (ICCC).",
            "Human-in-the-Loop Safeguards: Authorities retain full override controls while enjoying autonomous recommendation triage."
        ]
    )

    # ==========================================
    # SLIDE 9: TEAM ROLES & RESPONSIBILITIES
    # ==========================================
    make_content_slide(
        "8. Team Member Roles & Contributions",
        "Interdisciplinary Engineering Excellence",
        "Team Leadership & Core AI",
        [
            "[Team Lead Name]: System Architecture, Multi-Agent LangGraph Orchestration, and Municipal Workflow Alignment.",
            "[Member 2 Name]: Computer Vision Pipeline, YOLOv8 model fine-tuning, and optical blockage classification."
        ],
        "Geospatial, Data & Backend Engineering",
        [
            "[Member 3 Name]: Geospatial GIS Integration, Interactive Leaflet Mapping, and Streamlit Dashboard Frontend.",
            "[Member 4 Name]: SQLite Database Schema, Doppler Weather API Ingestion, and Automated Work-Order State Machine."
        ]
    )

    # ==========================================
    # SLIDE 10: PROTOTYPE DEMO — SCENARIO WALKTHROUGH
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "9. Prototype Demonstration — Live Scenario Assessment", "Verified Working Implementation (87/100 Risk Score)")
    img_demo = os.path.join(screenshots_dir, "screenshot_live_demo_risk_87.png")
    if os.path.exists(img_demo):
        s10.shapes.add_picture(img_demo, Inches(0.8), Inches(1.35), Inches(11.733), Inches(5.75))

    # ==========================================
    # SLIDE 11: PROTOTYPE DEMO — ALL-INDIA MAP & DISPATCH
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "10. Prototype Demonstration — Real-Time Spatial Risk Map", "National Metropolitan Drainage Monitoring & Street-Level Zoom")
    img_map = os.path.join(screenshots_dir, "screenshot_city_flood_map.png")
    if os.path.exists(img_map):
        s11.shapes.add_picture(img_map, Inches(0.8), Inches(1.35), Inches(11.733), Inches(5.75))

    # ==========================================
    # SLIDE 12: REFERENCES & SCIENTIFIC FOUNDATION
    # ==========================================
    make_content_slide(
        "11. References & Scientific Foundations",
        "Academic & Technological Grounding",
        "Agentic AI & Multi-Agent Literature",
        [
            "Wu, Q., et al. (2023). 'AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation.' Microsoft Research.",
            "Yao, S., et al. (2023). 'ReAct: Synergizing Reasoning and Acting in Language Models.' ICLR 2023.",
            "LangGraph (2024). 'Orchestrating Complex Multi-Agent Stateful Graphs.' LangChain."
        ],
        "Hydrological & Smart City Research",
        [
            "Henonin, J., et al. (2013). 'Real-time urban flood forecasting and modeling - A review.' Journal of Hydroinformatics.",
            "Al-Sarayreh, M., et al. (2021). 'Deep learning approaches for sewer pipe defect detection and classification.'",
            "Smart Cities Mission (2022). 'Guidelines for Urban Drainage and Climate Resilience.' Ministry of Housing and Urban Affairs (MoHUA)."
        ]
    )

    # ==========================================
    # SLIDE 13: THANK YOU & CONTACT
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    bg13 = s13.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg13.fill.solid()
    bg13.fill.fore_color.rgb = NAVY
    bg13.line.fill.background()

    tb = s13.shapes.add_textbox(Inches(1.5), Inches(1.5), Inches(10.333), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "DRAINWATCH"
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = CYAN

    p = tf.add_paragraph()
    p.text = "Turning Reactive Cities into Proactive, Climate-Resilient Smart Communities."
    p.font.size = Pt(20)
    p.font.color.rgb = WHITE

    p = tf.add_paragraph()
    p.text = "\nThank You for Your Time & Consideration!"
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = RGBColor(147, 197, 253)

    p = tf.add_paragraph()
    p.text = "\nContact & Inquiries:\nTeam Lead: [Your Name] | Email: [Your Email ID]\nRepository: https://github.com/[your-repo]/DrainWatch-AgenticAI\n\nOpen for Technical Questions & Panel Discussion!"
    p.font.size = Pt(13)
    p.font.color.rgb = RGBColor(203, 213, 225)

    out_path = os.path.join(os.path.dirname(__file__), "DrainWatch_Final_Hackathon_Submission.pptx")
    prs.save(out_path)
    print(f"Presentation created successfully at: {out_path} ({os.path.getsize(out_path)} bytes)")

if __name__ == "__main__":
    create_presentation()
