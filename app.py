import streamlit as st
import streamlit.components.v1 as components
import folium
from streamlit_folium import st_folium
import pandas as pd
from PIL import Image
import os
import time

# Local modules
import database as db
from agent import DrainWatchAgentSystem
from architecture_view import get_interactive_architecture_html
from white_architecture_view import get_white_interactive_architecture_html

# Page config
st.set_page_config(
    page_title="DrainWatch | Autonomous Urban Flood Prevention",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Responsive Enterprise CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Clean container padding */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        padding-left: clamp(1rem, 3vw, 3rem) !important;
        padding-right: clamp(1rem, 3vw, 3rem) !important;
        max-width: 1400px;
    }

    /* Header Banner */
    .hero-banner {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 50%, #0369A1 100%);
        padding: clamp(1.2rem, 2.5vw, 2rem);
        border-radius: 16px;
        color: white;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.15);
    }
    
    .hero-title {
        font-size: clamp(1.5rem, 3vw, 2.3rem);
        font-weight: 800;
        letter-spacing: -0.02em;
        margin: 0 0 6px 0;
        color: #FFFFFF;
    }
    
    .hero-subtitle {
        font-size: clamp(0.9rem, 1.3vw, 1.1rem);
        color: #93C5FD;
        margin: 0;
        font-weight: 500;
    }

    /* Glass & Card Containers */
    .dw-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: clamp(1rem, 2vw, 1.5rem);
        box-shadow: 0 2px 8px -2px rgba(0, 0, 0, 0.05);
        margin-bottom: 1.2rem;
        transition: all 0.2s ease;
    }

    /* Risk Score Gauge Card */
    .risk-badge-box {
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        background: #FFF1F2;
        border: 2px solid #F43F5E;
    }
    
    .risk-score-text {
        font-size: clamp(2.5rem, 5vw, 3.8rem);
        font-weight: 800;
        color: #E11D48;
        line-height: 1;
        margin: 10px 0;
    }

    /* Action Plan Items - Clean Modern SaaS Card (No Blue Vertical Border) */
    .action-step {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        padding: 11px 14px;
        background: #FFFFFF;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
        margin-bottom: 8px;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03);
    }

    /* Segmented Enterprise Pill Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background-color: #F1F5F9;
        padding: 5px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        overflow-x: auto;
    }

    .stTabs [data-baseweb="tab-highlight"] {
        display: none !important;
    }

    .stTabs [data-baseweb="tab-border"] {
        display: none !important;
    }

    .stTabs [data-baseweb="tab"] {
        height: 38px;
        white-space: nowrap;
        border-radius: 8px;
        padding: 0 18px;
        font-weight: 500;
        font-size: 0.90rem;
        color: #475569;
        border: none !important;
        background: transparent !important;
        transition: all 0.15s ease-in-out;
    }

    .stTabs [data-baseweb="tab"]:hover {
        color: #0F172A;
        background-color: rgba(255, 255, 255, 0.6) !important;
    }

    .stTabs [aria-selected="true"] {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        font-weight: 700;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08), 0 1px 2px rgba(0, 0, 0, 0.04);
    }

    /* Responsive grid flex */
    @media (max-width: 768px) {
        .block-container {
            padding-left: 0.8rem !important;
            padding-right: 0.8rem !important;
        }
        .hero-banner {
            border-radius: 12px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize database & agent
db.init_db()
agent_system = DrainWatchAgentSystem()

# Hero Header
st.markdown("""
<div class="hero-banner">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
        <div>
            <h1 class="hero-title">DrainWatch</h1>
            <p class="hero-subtitle">Autonomous Multi-Agent Urban Drainage & Flood Early-Warning System</p>
        </div>
        <div style="background: rgba(255,255,255,0.15); backdrop-filter: blur(8px); padding: 8px 16px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.2);">
            <span style="color: #6EE7B7; font-weight: 700;">● SYSTEM OPERATIONAL</span><br>
            <span style="font-size: 0.85rem; color: #E2E8F0;">Agentic AI Hackathon 2026 | Ulster University & AMSE</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Main Navigation Tabs (Clean Enterprise Style - Zero Emojis)
tab_demo, tab_map, tab_citizen, tab_command, tab_arch = st.tabs([
    "Scenario Simulation",
    "National Vulnerability Map",
    "Citizen Intake Portal",
    "Operations Command Console",
    "System Architecture"
])

locations = db.get_all_locations()
loc_names = [l["name"] for l in locations]

# ========================================================
# TAB 1: LIVE AGENTIC DEMONSTRATION
# ========================================================
with tab_demo:
    st.markdown("#### **Real-Time Scenario Assessment**")
    st.caption("Configure rainfall, drainage blockage, and historical data to observe how the AI agent calculates risk and autonomously dispatches municipal intervention teams.")

    # Two-column responsive layout
    col_params, col_results = st.columns([1, 1.25], gap="medium")

    with col_params:
        with st.container():
            st.markdown("##### Scenario Parameters")
            
            selected_loc_name = st.selectbox(
                "Target Urban Hotspot",
                loc_names,
                index=0,
                help="Select an area to evaluate storm drainage inundation risk."
            )
            selected_loc = next((l for l in locations if l["name"] == selected_loc_name), locations[0])

            p_col1, p_col2 = st.columns(2)
            with p_col1:
                selected_rain = st.selectbox(
                    "Rainfall Forecast",
                    ["Heavy", "Moderate", "Light", "Torrential"],
                    index=0,
                    help="Live precipitation rate simulated from Doppler radar"
                )
            with p_col2:
                drain_condition = st.selectbox(
                    "Drain Blockage State",
                    ["Blocked", "Partially Clogged", "Clear"],
                    index=0,
                    help="Condition derived from citizen complaints and Vision AI"
                )

            p_col3, p_col4 = st.columns(2)
            with p_col3:
                past_floods = st.number_input(
                    "Past Flooding Frequency",
                    min_value=0, max_value=15, value=3,
                    help="Historical times this location experienced severe waterlogging"
                )
            with p_col4:
                st.metric("Elevation & Capacity", f"{selected_loc['elevation_m']}m", f"Index: {selected_loc['drainage_capacity_index']}")

            rain_map = {
                "Heavy": "Heavy (35-65 mm/hr)",
                "Moderate": "Moderate (15-30 mm/hr)",
                "Light": "Light (5-10 mm/hr)",
                "Torrential": "Torrential / Cloudburst (>70 mm/hr)"
            }

            simulate_photo = st.toggle("Include Citizen Drain Photo Verification", value=True)
            if simulate_photo:
                st.info("Optical Telemetry: Ingesting street camera / mobile capture of drainage inlet.")

            trigger_btn = st.button("Run Multi-Agent Assessment", type="primary", use_container_width=True)

    with col_results:
        # Run the assessment
        result = agent_system.full_agentic_pipeline(
            location_name=selected_loc_name,
            rainfall_forecast=rain_map[selected_rain],
            citizen_desc="Drain blocked with plastic waste and garbage near road inlet.",
            has_image=simulate_photo,
            past_incidents=past_floods,
            elevation=selected_loc["elevation_m"],
            capacity=selected_loc["drainage_capacity_index"]
        )

        r = result["risk"]
        p = result["perception"]
        a = result["action"]

        # 1. Risk Score Card (Responsive Design)
        st.markdown(f"""
        <div class="risk-badge-box" style="border-color: {r['color']}; background: {r['color']}12;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <span style="font-size: 0.95rem; font-weight: 700; color: {r['color']}; letter-spacing: 0.05em;">DRAINWATCH PREDICTIVE RISK</span>
                <span style="background: {r['color']}; color: white; padding: 4px 12px; border-radius: 20px; font-weight: 700; font-size: 0.85rem;">{r['risk_tier']}</span>
            </div>
            <div class="risk-score-text" style="color: {r['color']};">
                {r['risk_score']}<span style="font-size: 1.8rem; font-weight: 600; color: #64748B;">/100</span>
            </div>
            <div style="font-size: 0.88rem; color: #475569; font-weight: 500;">
                Estimated Time to Waterlogging: <b>{r['estimated_time_to_flood']}</b>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        # 2. Perception & Vision Agent Telemetry
        with st.expander("Perception & Computer Vision Telemetry", expanded=True):
            st.markdown(f"""
            * **AI Vision Status:** `{p['status']}` (Confidence: **{int(p['confidence']*100)}%**)
            * **Identified Obstacles:** {', '.join(p['detected_objects'])}
            * **Deduplication Cluster:** `{p['deduplication_tag']}` (Citizen reports unified)
            """)

        # 3. Action Plan Card
        st.markdown(f"""
        <div style="background: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 12px; padding: 16px; margin-top: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; flex-wrap: wrap;">
                <span style="color: #166534; font-weight: 800; font-size: 1.05rem;">PROACTIVE INTERVENTION DIRECTIVES</span>
                <span style="background: #DC2626; color: white; font-weight: 700; font-size: 0.75rem; padding: 3px 8px; border-radius: 6px;">{a['priority']}</span>
            </div>
            {"".join(f'<div class="action-step"><span style="color: #0284C7; font-weight: bold; font-size: 1.1rem;">•</span><span style="font-size: 0.92rem; color: #1E293B;"><b>{rec}</b></span></div>' for rec in a["recommendations"])}
            <div style="margin-top: 12px; padding-top: 10px; border-top: 1px dashed #86EFAC; font-size: 0.88rem; color: #166534;">
                <b>Unit Assignment:</b> {a['assigned_crew']}<br>
                <b>Public Advisory Notice:</b> <i>"{a['citizen_advisory']}"</i>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        if st.button("Commit Work-Order to Municipal Operations Center", type="secondary", use_container_width=True):
            db.add_dispatch(
                location_name=selected_loc_name,
                rainfall=selected_rain,
                risk_score=r["risk_score"],
                priority=a["priority"],
                action_plan="; ".join(a["recommendations"]),
                crew=a["assigned_crew"]
            )
            st.toast("Work order committed to Municipal Dispatch Queue.")

# ========================================================
# TAB 2: NATIONAL VULNERABILITY MAP
# ========================================================
with tab_map:
    st.markdown("#### **National Urban Drainage & Flood Vulnerability Map**")
    st.caption("Interactive spatial GIS monitoring high-risk stormwater infrastructure across major Indian metropolitan corridors.")

    # Top KPI stats
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("National Monitored Nodes", f"{len(locations)} Hotspots", "6 Metros Active")
    with c2:
        st.metric("Critical Red Alerts", "7 Zones", "Immediate Preemptive Action", delta_color="inverse")
    with c3:
        st.metric("Precipitation Alert", "Active Downpours", "High Runoff Risk")
    with c4:
        st.metric("Autonomous Dispatch", "14 Crews Staged", "Pre-event Jetting")

    # Interactive Region / Hotspot Zoom Selector
    zoom_col1, zoom_col2 = st.columns([1.5, 1], gap="medium")
    
    city_presets = {
        "All India Overview": {"center": [21.5, 79.5], "zoom": 5},
        "Mumbai Metropolitan Region": {"center": [19.05, 72.85], "zoom": 12},
        "Delhi National Capital Region": {"center": [28.58, 77.24], "zoom": 12},
        "Bengaluru Urban Corridor": {"center": [12.96, 77.63], "zoom": 12},
        "Chennai Coastal Corridor": {"center": [12.98, 80.20], "zoom": 12},
        "Kolkata Riverine Corridor": {"center": [22.56, 88.36], "zoom": 12},
        "Hyderabad Deccan Plateau": {"center": [17.42, 78.43], "zoom": 12}
    }

    with zoom_col1:
        selected_region = st.selectbox(
            "Filter by Metropolitan Region",
            list(city_presets.keys()),
            index=0,
            help="Choose a metropolitan zone to zoom into its drainage grid, or view all of India."
        )

    with zoom_col2:
        all_spot_options = ["(Select Specific Hotspot...)"] + [l["name"] for l in locations]
        selected_spot = st.selectbox(
            "Focus on Specific Infrastructure Chokepoint",
            all_spot_options,
            index=0
        )

    # Determine center and zoom level dynamically
    if selected_spot != "(Select Specific Hotspot...)":
        spot_obj = next((l for l in locations if l["name"] == selected_spot), locations[0])
        map_center = [spot_obj["latitude"], spot_obj["longitude"]]
        map_zoom = 15  # Street-level deep zoom!
    else:
        map_center = city_presets[selected_region]["center"]
        map_zoom = city_presets[selected_region]["zoom"]

    # Initialize Folium Map with 100% width and height
    m = folium.Map(
        location=map_center,
        zoom_start=map_zoom,
        tiles="OpenStreetMap",
        width="100%",
        height="100%"
    )

    # Plot small, clean circular dots across all India locations
    for loc in locations:
        res = agent_system.run_hydrological_risk_agent(
            rainfall_forecast="Heavy (35-65 mm/hr)",
            drain_condition=loc["current_drain_status"],
            past_incidents=loc["historical_flood_count"],
            elevation_m=loc["elevation_m"],
            drainage_capacity=loc["drainage_capacity_index"]
        )
        score = res["risk_score"]
        color = "#DC2626" if score >= 75 else ("#EA580C" if score >= 50 else "#16A34A")

        popup_html = f"""
        <div style="font-family: 'Plus Jakarta Sans', Arial; width: 230px; padding: 4px;">
            <b style="font-size: 13px; color: #0F172A;">{loc['name']}</b>
            <div style="margin: 5px 0; padding: 6px; background: #F8FAFC; border-radius: 6px; border-left: 3px solid {color};">
                <b>Risk Score:</b> <span style="color:{color}; font-size:15px;"><b>{score}/100</b></span><br>
                <small style="color: {color}; font-weight: bold;">{res['risk_tier']}</small>
            </div>
            <div style="font-size: 11px; color: #475569; line-height: 1.4;">
                <b>City:</b> {loc.get('city', 'Urban')}<br>
                <b>Condition:</b> {loc['current_drain_status']}<br>
                <b>Historical Inundations:</b> {loc['historical_flood_count']} times<br>
                <b>Elevation:</b> {loc['elevation_m']}m MSL
            </div>
        </div>
        """

        folium.CircleMarker(
            location=[loc["latitude"], loc["longitude"]],
            radius=8,  # Small clean dot!
            popup=folium.Popup(popup_html, max_width=280),
            color=color,
            weight=2,
            fill=True,
            fill_color=color,
            fill_opacity=0.85,
            tooltip=f"{loc['name']} ({loc.get('city', '')}) — Risk: {score}/100"
        ).add_to(m)

    # Render map seamlessly with 100% fill (No blank white void on mobile or desktop)
    components.html(m.get_root().render(), height=480)

    # Legend & Fast Links
    st.markdown("""
    <div style="display: flex; gap: 20px; flex-wrap: wrap; margin-top: 10px; font-size: 0.9rem; padding: 12px; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px;">
        <div><b style="color: #DC2626;">[Critical Risk >75]</b> Preemptive Jetting & De-watering Pumps Dispatched</div>
        <div><b style="color: #EA580C;">[Moderate Risk 50-74]</b> Scheduled Manual Desilting Squad</div>
        <div><b style="color: #16A34A;">[Low Risk &lt;50]</b> Monitored Gravity Drainage Flow</div>
    </div>
    """, unsafe_allow_html=True)

# ========================================================
# TAB 3: CITIZEN INTAKE PORTAL
# ========================================================
with tab_citizen:
    st.markdown("#### **Crowdsourced Citizen Drainage Reporting**")
    st.caption("Citizens can report choked street storm drains with photos. Multimodal AI automatically analyzes the severity and clusters duplicate complaints.")

    col_rep1, col_rep2 = st.columns([1, 1], gap="large")

    with col_rep1:
        st.markdown("##### Submit Stormdrain Obstruction Report")
        with st.form("citizen_form"):
            name = st.text_input("Citizen Name", value="Rahul Varma")
            phone = st.text_input("Contact Number", value="+91 98480 12345")
            rep_loc = st.selectbox("Nearest Landmark / Road", loc_names)
            desc = st.text_area("Issue Description", "Plastic garbage and beverage bottles blocking the grating inlet. Water already rising.")
            uploaded_file = st.file_uploader("Upload Drainage Photo", type=["jpg", "png", "jpeg"])
            
            sub = st.form_submit_button("Submit Complaint to DrainWatch", type="primary", use_container_width=True)

        if sub:
            p_res = agent_system.run_perception_agent(
                image_provided=True if uploaded_file else False,
                description=desc,
                reported_location=rep_loc
            )
            db.add_complaint(
                location_name=rep_loc,
                citizen_name=name,
                phone=phone,
                description=desc,
                image_path="sample.jpg",
                blockage_status=p_res["status"],
                confidence=p_res["confidence"]
            )
            st.success("Complaint successfully logged. Vision Agent has classified and clustered this report.")

    with col_rep2:
        st.markdown("##### Optical Inspection Analysis")
        if uploaded_file:
            img = Image.open(uploaded_file)
            st.image(img, caption="Citizen Submitted Image", use_column_width=True)
        else:
            st.markdown("""
            <div style="border: 1px dashed #CBD5E1; border-radius: 12px; padding: 30px; text-align: center; background: #F8FAFC;">
                <p style="color: #64748B; font-weight: 500;">Upload an inspection photograph on the left to review optical feature extraction.</p>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("""
        ```json
        {
          "agent": "Perception & Vision Agent",
          "model": "YOLO-Vision-Sewer v8",
          "detected_blockage": "Plastic Packaging & PET Bottles",
          "flow_constriction_ratio": "85%",
          "severity_classification": "CRITICAL_OBSTRUCTION",
          "confidence_score": 0.94
        }
        ```
        """)

# ========================================================
# TAB 4: MUNICIPAL COMMAND CONSOLE
# ========================================================
with tab_command:
    st.markdown("#### **Municipal Operations Command Console**")
    st.caption("Central executive console for municipal commissioners, disaster squads, and maintenance engineers.")

    dispatches = db.get_all_dispatches()
    complaints = db.get_all_complaints()

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("High Risk Alerts", "2 Zones", "Preemptive Action")
    m2.metric("Maintenance Crews", "5 Teams", "En Route")
    m3.metric("Ingested Complaints", f"{len(complaints)} Reports", "Clustered")
    m4.metric("Potential Floods Averted", "18 Spots", "+3 Today")

    st.markdown("---")
    st.markdown("##### Autonomous Work-Order Dispatch Log")
    if dispatches:
        st.dataframe(pd.DataFrame(dispatches), use_container_width=True, height=220)
    else:
        st.info("No work orders recorded yet. Trigger a proactive assessment in the Simulation tab.")

    st.markdown("##### Active Citizen Reports Database")
    if complaints:
        st.dataframe(pd.DataFrame(complaints), use_container_width=True, height=220)

# ========================================================
# TAB 5: SYSTEM ARCHITECTURE
# ========================================================
with tab_arch:
    st.markdown("#### **DrainWatch Autonomous Multi-Agent System Architecture**")
    st.caption("State-of-the-art Smart City Cyber-Physical Architecture: 3D Digital Twin visualization, 2D Enterprise LangGraph Swarm, and Structured Architecture Graph.")

    # High-resolution image paths
    p_screenshots = os.path.abspath(os.path.join(os.path.dirname(__file__), "screenshots"))
    img_3d_file = os.path.join(p_screenshots, "drainwatch_3d_architecture_diagram.jpg")
    img_flow_file = os.path.join(p_screenshots, "drainwatch_system_architecture_flow.jpg")

    # Segmented View Selector without emojis
    view_selection = st.radio(
        "Architecture View Mode:",
        [
            "3D Isometric Digital Twin",
            "2D Enterprise System Flow (LangGraph Core)",
            "System Architecture Graph (White Theme)"
        ],
        index=0,
        horizontal=True
    )

    st.write("")

    if view_selection == "3D Isometric Digital Twin":
        if os.path.exists(img_3d_file):
            st.image(
                Image.open(img_3d_file),
                caption="DrainWatch - 3D Isometric Cyber-Physical Architecture Diagram (16:9 Presentation Ready)",
                use_column_width=True
            )
            c_dl1, c_dl2 = st.columns([1, 4])
            with c_dl1:
                with open(img_3d_file, "rb") as file:
                    st.download_button(
                        label="Download 3D Architecture Diagram",
                        data=file,
                        file_name="drainwatch_3d_architecture_diagram.jpg",
                        mime="image/jpeg",
                        key="dl_3d_btn_main"
                    )

    elif view_selection == "2D Enterprise System Flow (LangGraph Core)":
        if os.path.exists(img_flow_file):
            st.image(
                Image.open(img_flow_file),
                caption="DrainWatch - 2D Enterprise Multi-Agent Architecture with LangGraph Orchestrator",
                use_column_width=True
            )
            c_dl1, c_dl2 = st.columns([1, 4])
            with c_dl1:
                with open(img_flow_file, "rb") as file:
                    st.download_button(
                        label="Download 2D Architecture Diagram",
                        data=file,
                        file_name="drainwatch_system_architecture_flow.jpg",
                        mime="image/jpeg",
                        key="dl_flow_btn_main"
                    )

    else:
        st.markdown("##### Structured Cyber-Physical Graph Architecture")
        
        # - and + Zoom Controls (Replacing Slider per User Request)
        if "graph_zoom" not in st.session_state:
            st.session_state["graph_zoom"] = 125

        c_z1, c_z2, c_z3, c_z4, c_zspace = st.columns([1.1, 1.2, 1.1, 1.1, 3.5])
        with c_z1:
            if st.button("– Zoom Out", key="btn_z_out", use_container_width=True):
                st.session_state["graph_zoom"] = max(75, st.session_state["graph_zoom"] - 25)
                st.rerun()
        with c_z2:
            st.markdown(f"""
            <div style="display: flex; align-items: center; justify-content: center; height: 38px; background: #F8FAFC; border: 1px solid #CBD5E1; border-radius: 8px; font-weight: 700; color: #0F172A; font-size: 0.95rem;">
                Zoom: {st.session_state['graph_zoom']}%
            </div>
            """, unsafe_allow_html=True)
        with c_z3:
            if st.button("+ Zoom In", key="btn_z_in", use_container_width=True):
                st.session_state["graph_zoom"] = min(225, st.session_state["graph_zoom"] + 25)
                st.rerun()
        with c_z4:
            if st.button("Reset View", key="btn_z_reset", use_container_width=True):
                st.session_state["graph_zoom"] = 125
                st.rerun()

        st.caption("Interactive Pan & Drag: Click and hold or swipe with hand/touch to navigate across the architecture graph.")

        target_width_px = int(850 * (st.session_state["graph_zoom"] / 100))

        st.markdown(f"""
        <style>
        [data-testid*="graphvizchart" i], [data-testid="stGraphVizChart"], [data-testid="stGraphvizChart"] {{
            overflow: auto !important;
            max-height: 640px !important;
            background: #FFFFFF !important;
            padding: 16px !important;
            border-radius: 12px !important;
            border: 1px solid #E2E8F0 !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
            cursor: grab !important;
            user-select: none !important;
            -webkit-user-select: none !important;
            -webkit-overflow-scrolling: touch !important;
            touch-action: pan-x pan-y !important;
        }}
        [data-testid*="graphvizchart" i]:active, [data-testid="stGraphVizChart"]:active {{
            cursor: grabbing !important;
        }}
        [data-testid*="graphvizchart" i] svg, [data-testid="stGraphVizChart"] svg, [data-testid="stGraphvizChart"] svg {{
            width: {target_width_px}px !important;
            min-width: {target_width_px}px !important;
            max-width: none !important;
            height: auto !important;
            transition: width 0.2s ease, min-width 0.2s ease;
        }}
        </style>
        """, unsafe_allow_html=True)

        white_arch_dot = """
        digraph DrainWatchArchitecture {
            rankdir=TB;
            bgcolor="#FFFFFF";
            node [fontname="Helvetica", shape=box, style="filled,rounded", fontsize=10, penwidth=1.5];
            edge [fontname="Helvetica", fontsize=9, color="#0284C7", penwidth=1.3, arrowhead=vee];

            subgraph cluster_layer1 {
                label = "Tier 1: Multimodal Perception & Edge Telemetry";
                fontname="Helvetica-Bold";
                fontsize=11;
                color="#CBD5E1";
                style="filled,rounded";
                fillcolor="#F8FAFC";

                C [label="Citizen Smartphone App\\n(Crowdsourced Photos & Geotag)", fillcolor="#FFFFFF", color="#0284C7"];
                S [label="IoT Stormdrain Sensors\\n(Ultrasonic Level & Silt Depth)", fillcolor="#FFFFFF", color="#0284C7"];
                W [label="Doppler Weather Radar\\n(Real-Time Rain Rate mm/hr)", fillcolor="#FFFFFF", color="#0284C7"];
                G [label="GIS Digital Elevation Model\\n(Catchment Topology & Culverts)", fillcolor="#FFFFFF", color="#0284C7"];
            }

            subgraph cluster_layer2 {
                label = "Tier 2: Streaming Ingestion & Deduplication Gateway";
                fontname="Helvetica-Bold";
                fontsize=11;
                color="#E2E8F0";
                style="filled,rounded";
                fillcolor="#F1F5F9";

                K [label="Kafka / MQTT Event Streaming Broker\\n(Filter, Validate & Semantic Spatial Clustering)", fillcolor="#FFFFFF", color="#7C3AED", penwidth=1.8];
            }

            subgraph cluster_layer3 {
                label = "Tier 3: Agentic AI Cognitive Core (LangGraph Multi-Agent Swarm)";
                fontname="Helvetica-Bold";
                fontsize=11;
                color="#DDD6FE";
                style="filled,rounded";
                fillcolor="#FAF5FF";

                ORCH [label="Central Multi-Agent Orchestrator\\n(LangGraph State Machine & ReAct Loop)", fillcolor="#FFFFFF", color="#6D28D9", penwidth=2.0];
                VIS [label="Computer Vision Agent\\n(YOLOv8 Debris & Silt Classification)", fillcolor="#FFFFFF", color="#2563EB"];
                WEA [label="Weather Telemetry Agent\\n(Precipitation Intensity & Window)", fillcolor="#FFFFFF", color="#2563EB"];
                RISK [label="Hydrological Digital Twin Simulator\\n(Dynamic Risk Score: 0 - 100)", fillcolor="#FEF2F2", color="#DC2626", penwidth=1.8];
                DISP [label="Dispatch Optimization Agent\\n(Work-Order Synthesis & Fleet Routing)", fillcolor="#F0FDF4", color="#16A34A", penwidth=1.8];
            }

            subgraph cluster_layer4 {
                label = "Tier 4: Field Actuation & Closed-Loop Verification";
                fontname="Helvetica-Bold";
                fontsize=11;
                color="#BBF7D0";
                style="filled,rounded";
                fillcolor="#F0FDF4";

                TRUCK [label="Municipal Jetting & Super-Suckers\\n(Preemptive Debris Extraction)", fillcolor="#FFFFFF", color="#16A34A"];
                GATE [label="Automated Canal Sluice Gates\\n(Dynamic SCADA Level Actuation)", fillcolor="#FFFFFF", color="#16A34A"];
                TRAF [label="Traffic Advisory Broadcast\\n(Dynamic Route Diversion Alerts)", fillcolor="#FFFFFF", color="#16A34A"];
                PROOF [label="Post-Action Verification Node\\n(Crews Upload Clean Proof Photo)", fillcolor="#ECFDF5", color="#059669", penwidth=1.8];
            }

            C -> K;
            S -> K;
            W -> K;
            G -> K;

            K -> ORCH [color="#6D28D9", penwidth=1.8];
            ORCH -> VIS;
            ORCH -> WEA;
            VIS -> RISK;
            WEA -> RISK;
            RISK -> DISP;
            DISP -> ORCH;

            ORCH -> TRUCK [color="#16A34A", penwidth=1.5];
            ORCH -> GATE [color="#16A34A", penwidth=1.5];
            ORCH -> TRAF [color="#16A34A", penwidth=1.5];

            TRUCK -> PROOF [style="dashed", color="#059669"];
            PROOF -> VIS [style="dashed", color="#059669", label="Closed-Loop Feedback Proof"];
        }
        """
        st.graphviz_chart(white_arch_dot, use_container_width=True)

        # Real Hand Cursor Click-and-Drag Pan Script (Mouse + Mobile Touch Support)
        components.html("""
        <script>
            try {
                const doc = window.parent.document;
                function setupDraggable() {
                    const containers = doc.querySelectorAll('[data-testid*="graphvizchart" i], [data-testid="stGraphVizChart"], [data-testid="stGraphvizChart"]');
                    containers.forEach(slider => {
                        if (slider.dataset.dragReady) return;
                        slider.dataset.dragReady = "true";

                        // Add floating instant zoom toolbar inside container
                        if (!slider.querySelector('.dw-zoom-floating-bar')) {
                            const bar = doc.createElement('div');
                            bar.className = 'dw-zoom-floating-bar';
                            bar.style.position = 'sticky';
                            bar.style.top = '10px';
                            bar.style.float = 'right';
                            bar.style.zIndex = '20';
                            bar.style.display = 'flex';
                            bar.style.alignItems = 'center';
                            bar.style.gap = '6px';
                            bar.style.background = 'rgba(255, 255, 255, 0.95)';
                            bar.style.backdropFilter = 'blur(6px)';
                            bar.style.padding = '4px 8px';
                            bar.style.borderRadius = '8px';
                            bar.style.border = '1px solid #CBD5E1';
                            bar.style.boxShadow = '0 2px 8px rgba(0,0,0,0.08)';
                            bar.style.marginRight = '8px';

                            bar.innerHTML = `
                                <button id="dw-z-minus" style="width:28px;height:28px;border-radius:6px;border:1px solid #CBD5E1;background:#F8FAFC;font-weight:700;font-size:15px;cursor:pointer;color:#0F172A;display:flex;align-items:center;justify-content:center;">–</button>
                                <span id="dw-z-text" style="font-size:12px;font-weight:700;color:#334155;min-width:44px;text-align:center;">Zoom</span>
                                <button id="dw-z-plus" style="width:28px;height:28px;border-radius:6px;border:1px solid #CBD5E1;background:#F8FAFC;font-weight:700;font-size:15px;cursor:pointer;color:#0F172A;display:flex;align-items:center;justify-content:center;">+</button>
                                <button id="dw-z-reset" style="padding:0 8px;height:28px;border-radius:6px;border:1px solid #CBD5E1;background:#F8FAFC;font-weight:600;font-size:11px;cursor:pointer;color:#475569;">Reset</button>
                            `;

                            slider.insertBefore(bar, slider.firstChild);

                            function updateFloatingZoom(delta) {
                                const svg = slider.querySelector('svg');
                                if (!svg) return;
                                const curW = svg.getBoundingClientRect().width;
                                const newW = delta === 0 ? 850 : Math.max(700, Math.min(2400, Math.round(curW + delta)));
                                svg.style.width = newW + 'px';
                                svg.style.minWidth = newW + 'px';
                                const pct = Math.round((newW / 850) * 100);
                                const txt = bar.querySelector('#dw-z-text');
                                if (txt) txt.innerText = pct + '%';
                            }

                            bar.querySelector('#dw-z-minus').addEventListener('click', (e) => { e.stopPropagation(); updateFloatingZoom(-150); });
                            bar.querySelector('#dw-z-plus').addEventListener('click', (e) => { e.stopPropagation(); updateFloatingZoom(150); });
                            bar.querySelector('#dw-z-reset').addEventListener('click', (e) => { e.stopPropagation(); updateFloatingZoom(0); slider.scrollLeft = 0; slider.scrollTop = 0; });
                        }

                        let isDown = false;
                        let startX, startY, scrollLeft, scrollTop;

                        // Desktop Mouse Drag
                        slider.addEventListener('mousedown', (e) => {
                            isDown = true;
                            slider.style.cursor = 'grabbing';
                            startX = e.pageX - slider.offsetLeft;
                            startY = e.pageY - slider.offsetTop;
                            scrollLeft = slider.scrollLeft;
                            scrollTop = slider.scrollTop;
                        });

                        slider.addEventListener('mouseleave', () => {
                            isDown = false;
                            slider.style.cursor = 'grab';
                        });

                        slider.addEventListener('mouseup', () => {
                            isDown = false;
                            slider.style.cursor = 'grab';
                        });

                        slider.addEventListener('mousemove', (e) => {
                            if (!isDown) return;
                            e.preventDefault();
                            const x = e.pageX - slider.offsetLeft;
                            const y = e.pageY - slider.offsetTop;
                            const walkX = (x - startX) * 1.5;
                            const walkY = (y - startY) * 1.5;
                            slider.scrollLeft = scrollLeft - walkX;
                            slider.scrollTop = scrollTop - walkY;
                        });

                        // Mouse Wheel Smooth Zoom (Ctrl+Wheel or Meta+Wheel)
                        slider.addEventListener('wheel', (e) => {
                            if (e.ctrlKey || e.metaKey) {
                                e.preventDefault();
                                const svg = slider.querySelector('svg');
                                if (svg) {
                                    const curW = svg.getBoundingClientRect().width;
                                    const delta = e.deltaY > 0 ? -75 : 75;
                                    const newW = Math.max(750, Math.min(2400, Math.round(curW + delta)));
                                    svg.style.width = newW + 'px';
                                    svg.style.minWidth = newW + 'px';
                                }
                            }
                        }, { passive: false });

                        // Mobile Touch Drag / Pan
                        let touchStartX = 0, touchStartY = 0;
                        let touchScrollLeft = 0, touchScrollTop = 0;
                        let initialPinchDist = null;
                        let initialSvgWidth = null;

                        slider.addEventListener('touchstart', (e) => {
                            if (e.touches.length === 1) {
                                touchStartX = e.touches[0].pageX - slider.offsetLeft;
                                touchStartY = e.touches[0].pageY - slider.offsetTop;
                                touchScrollLeft = slider.scrollLeft;
                                touchScrollTop = slider.scrollTop;
                            } else if (e.touches.length === 2) {
                                // Pinch-to-zoom start
                                const dx = e.touches[0].pageX - e.touches[1].pageX;
                                const dy = e.touches[0].pageY - e.touches[1].pageY;
                                initialPinchDist = Math.hypot(dx, dy);
                                const svg = slider.querySelector('svg');
                                if (svg) {
                                    initialSvgWidth = svg.getBoundingClientRect().width;
                                }
                            }
                        }, { passive: true });

                        slider.addEventListener('touchmove', (e) => {
                            if (e.touches.length === 1) {
                                const touchX = e.touches[0].pageX - slider.offsetLeft;
                                const touchY = e.touches[0].pageY - slider.offsetTop;
                                const diffX = touchX - touchStartX;
                                const diffY = touchY - touchStartY;
                                slider.scrollLeft = touchScrollLeft - diffX;
                                slider.scrollTop = touchScrollTop - diffY;
                            } else if (e.touches.length === 2 && initialPinchDist && initialSvgWidth) {
                                // Pinch-to-zoom move
                                const dx = e.touches[0].pageX - e.touches[1].pageX;
                                const dy = e.touches[0].pageY - e.touches[1].pageY;
                                const curDist = Math.hypot(dx, dy);
                                const scaleFactor = curDist / initialPinchDist;
                                const newW = Math.max(700, Math.min(2400, Math.round(initialSvgWidth * scaleFactor)));
                                const svg = slider.querySelector('svg');
                                if (svg) {
                                    svg.style.width = newW + 'px';
                                    svg.style.minWidth = newW + 'px';
                                }
                            }
                        }, { passive: true });

                        slider.addEventListener('touchend', () => {
                            initialPinchDist = null;
                            initialSvgWidth = null;
                        });
                    });
                }
                setInterval(setupDraggable, 350);
            } catch(e) {
                console.log(e);
            }
        </script>
        """, height=0)

    st.markdown("---")

    # Detailed Architectural Breakdown
    c_arch1, c_arch2 = st.columns([1, 1], gap="large")

    with c_arch1:
        st.markdown("""
        ### 4-Tier Architectural Pipeline:
        
        * **Tier 1: Multimodal Perception & Edge Telemetry**  
          Integrates high-velocity time series data: crowdsourced geo-tagged citizen photos, underground IoT ultrasonic depth sensors, real-time Doppler radar rainfall vectors, and GIS Digital Elevation Models (DEM).
        
        * **Tier 2: Streaming Fusion & Geo-Clustering Gateway**  
          Kafka/MQTT message streaming normalizes disparate data feeds. Semantic spatial-temporal clustering eliminates duplicate citizen panic reports and aligns hydraulic features.
        
        * **Tier 3: Agentic AI Collaborative Core (The Brain)**  
          Powered by a central LangGraph/ReAct Orchestrator coordinating specialized sub-agents:
          - *Perception & Vision Agent:* YOLOv8-Sewer model classifies plastic waste, silt, and inflow restriction ratio.
          - *Weather Telemetry Agent:* Predicts peak rainfall window and localized runoff surge.
          - *Hydrological Digital Twin Agent:* Simulates street-level inundation and calculates dynamic Risk Score (0–100).
          - *Action & Dispatch Agent:* Formulates machine-readable work-orders and routes municipal emergency fleets.
        
        * **Tier 4: Field Actuation & Closed-Loop Verification**  
          Preemptive deployment of mechanized super-sucker units and variable-speed storm pumps *before* rain commences. Closed-loop verification ensures field crews upload post-action photos to auto-close tickets and reset risk to 0.
        """)

    with c_arch2:
        st.markdown("""
        ### Why DrainWatch is 100% Agentic AI:
        
        * **1. Goal-Directed Autonomy (Not a Chatbot):**  
          DrainWatch does not require human prompts or emergency calls. Its constant operational goal is *Zero Urban Flood Damage*.
        
        * **2. Multi-Agent Specialization & Tool Calling:**  
          Individual agents execute real tools (GIS spatial queries, Doppler Radar APIs, Computer Vision inference, Municipal Work-Order state machines).
        
        * **3. Proactive Decision Horizon:**  
          Shifts municipal governance from reactive disaster relief (pumping water out after roads drown) to predictive prevention (clearing drains 1–3 hours before cloudbursts hit).
        
        * **4. Closed-Loop Machine Auditing:**  
          Verification photos uploaded by field teams close the feedback loop, creating an auditable, transparent digital record for municipal commissioners and citizens alike.
        """)
