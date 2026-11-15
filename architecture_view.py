def get_interactive_architecture_html():
    return """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; }
    body { background-color: transparent; overflow: hidden; }
    
    #viewport-container {
        width: 100%;
        height: 650px;
        position: relative;
        background: #0B1120;
        border-radius: 14px;
        overflow: hidden;
        border: 1px solid #1E293B;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4);
        cursor: grab;
        user-select: none;
    }
    
    #viewport-container:active {
        cursor: grabbing;
    }
    
    .toolbar {
        position: absolute;
        top: 14px;
        right: 14px;
        z-index: 100;
        display: flex;
        gap: 6px;
        background: rgba(15, 23, 42, 0.88);
        backdrop-filter: blur(10px);
        padding: 6px 10px;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.12);
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    
    .tool-btn {
        background: #1E293B;
        color: #F1F5F9;
        border: 1px solid #334155;
        padding: 6px 12px;
        border-radius: 6px;
        font-weight: 600;
        cursor: pointer;
        font-size: 13px;
        transition: all 0.15s ease;
        display: flex;
        align-items: center;
        gap: 4px;
    }
    
    .tool-btn:hover {
        background: #0284C7;
        color: white;
        border-color: #38BDF8;
    }
    
    .status-pill {
        position: absolute;
        bottom: 14px;
        left: 14px;
        z-index: 100;
        background: rgba(15, 23, 42, 0.88);
        backdrop-filter: blur(8px);
        padding: 6px 14px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.12);
        color: #94A3B8;
        font-size: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .pulse-dot {
        width: 8px;
        height: 8px;
        background: #10B981;
        border-radius: 50%;
        box-shadow: 0 0 8px #10B981;
    }

    #svg-canvas {
        transform-origin: 0 0;
        transition: transform 0.05s ease-out;
        width: 1200px;
        height: 820px;
    }
</style>
</head>
<body>

<div id="viewport-container">
    <!-- Controls Toolbar -->
    <div class="toolbar">
        <button class="tool-btn" onclick="zoom(1.25)">➕ <b>Zoom In</b></button>
        <button class="tool-btn" onclick="zoom(0.8)">➖ <b>Zoom Out</b></button>
        <button class="tool-btn" onclick="resetView()">🔄 <b>Reset View</b></button>
        <span style="color: #64748B; font-size: 12px; align-self: center; margin-left: 6px;">| 🖱️ Drag to Pan • Scroll to Zoom</span>
    </div>

    <!-- Active Telemetry Status -->
    <div class="status-pill">
        <div class="pulse-dot"></div>
        <span><b>DrainWatch Digital Twin Architecture</b> • Full-System Interactive Map</span>
    </div>

    <!-- Interactive Canvas -->
    <div id="transform-wrapper" style="position: absolute; top: 0; left: 0;">
        <svg id="svg-canvas" viewBox="0 0 1200 820" fill="none" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <!-- Gradients -->
                <linearGradient id="layer1Grad" x1="0" y1="0" x2="1" y2="1">
                    <stop offset="0%" stop-color="#1E293B" stop-opacity="0.9"/>
                    <stop offset="100%" stop-color="#0F172A" stop-opacity="0.9"/>
                </linearGradient>
                <linearGradient id="agentCoreGrad" x1="0" y1="0" x2="1" y2="1">
                    <stop offset="0%" stop-color="#1E1B4B" stop-opacity="0.95"/>
                    <stop offset="100%" stop-color="#0F172A" stop-opacity="0.95"/>
                </linearGradient>
                <linearGradient id="actionGrad" x1="0" y1="0" x2="1" y2="1">
                    <stop offset="0%" stop-color="#064E3B" stop-opacity="0.3"/>
                    <stop offset="100%" stop-color="#0F172A" stop-opacity="0.8"/>
                </linearGradient>
                <linearGradient id="cardGrad" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stop-color="#1E293B"/>
                    <stop offset="100%" stop-color="#0F172A"/>
                </linearGradient>
                <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
                    <feGaussianBlur stdDeviation="5" result="blur" />
                    <feComposite in="SourceGraphic" in2="blur" operator="over" />
                </filter>
                <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#38BDF8" />
                </marker>
                <marker id="arrowGreen" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#10B981" />
                </marker>
                <marker id="arrowPurple" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#A855F7" />
                </marker>
            </defs>

            <!-- ============================================================== -->
            <!-- LAYER 1: MULTIMODAL PERCEPTION & EDGE SENSING (Top) -->
            <!-- ============================================================== -->
            <rect x="30" y="30" width="1140" height="150" rx="16" fill="url(#layer1Grad)" stroke="#334155" stroke-width="1.5"/>
            <text x="50" y="60" fill="#38BDF8" font-size="14" font-weight="800" letter-spacing="0.08em">LAYER 1: MULTIMODAL PERCEPTION & EDGE TELEMETRY</text>
            <text x="50" y="78" fill="#94A3B8" font-size="11">Real-time edge ingestion: Crowdsourced citizen inputs, underground IoT sensors, and Doppler meteorological streams</text>

            <!-- Node 1.1 Citizen App -->
            <rect x="50" y="95" width="250" height="65" rx="10" fill="#1E293B" stroke="#0284C7" stroke-width="1.5"/>
            <text x="70" y="122" fill="#F8FAFC" font-size="13" font-weight="700">📱 Citizen Crowdsourced App</text>
            <text x="70" y="142" fill="#94A3B8" font-size="11">Geo-tagged Photos + Blockage Reports</text>

            <!-- Node 1.2 IoT Sensors -->
            <rect x="330" y="95" width="250" height="65" rx="10" fill="#1E293B" stroke="#0284C7" stroke-width="1.5"/>
            <text x="350" y="122" fill="#F8FAFC" font-size="13" font-weight="700">📡 IoT Stormdrain Depth Sensors</text>
            <text x="350" y="142" fill="#94A3B8" font-size="11">Ultrasonic Silt & Water Head Levels</text>

            <!-- Node 1.3 Weather Doppler Radar -->
            <rect x="610" y="95" width="250" height="65" rx="10" fill="#1E293B" stroke="#0284C7" stroke-width="1.5"/>
            <text x="630" y="122" fill="#F8FAFC" font-size="13" font-weight="700">🌦️ Doppler Radar & Rain API</text>
            <text x="630" y="142" fill="#94A3B8" font-size="11">Live Precipitation Rate (mm/hr) Forecast</text>

            <!-- Node 1.4 GIS Elevation Model -->
            <rect x="890" y="95" width="260" height="65" rx="10" fill="#1E293B" stroke="#0284C7" stroke-width="1.5"/>
            <text x="910" y="122" fill="#F8FAFC" font-size="13" font-weight="700">🗺️ Spatial GIS & Elevation (DEM)</text>
            <text x="910" y="142" fill="#94A3B8" font-size="11">Subterranean Culvert Discharge Specs</text>

            <!-- Connecting Data Stream Flow -->
            <line x1="175" y1="160" x2="175" y2="215" stroke="#38BDF8" stroke-width="2" marker-end="url(#arrow)"/>
            <line x1="455" y1="160" x2="455" y2="215" stroke="#38BDF8" stroke-width="2" marker-end="url(#arrow)"/>
            <line x1="735" y1="160" x2="735" y2="215" stroke="#38BDF8" stroke-width="2" marker-end="url(#arrow)"/>
            <line x1="1020" y1="160" x2="1020" y2="215" stroke="#38BDF8" stroke-width="2" marker-end="url(#arrow)"/>

            <!-- ============================================================== -->
            <!-- LAYER 2: INGESTION, FUSION & PREPROCESSING GATEWAY -->
            <!-- ============================================================== -->
            <rect x="30" y="215" width="1140" height="65" rx="12" fill="#1E293B" stroke="#475569" stroke-width="1.5"/>
            <text x="50" y="243" fill="#A855F7" font-size="13" font-weight="800">LAYER 2: KAFKA / MQTT STREAMING FUSION & DEDUPLICATION GATEWAY</text>
            <text x="50" y="263" fill="#CBD5E1" font-size="11">Normalizes telemetry • Semantic Geo-Clustering (filters duplicate panic reports) • Spatial-Temporal Feature Alignment</text>

            <!-- Downward Flow from Gateway into Core -->
            <line x1="600" y1="280" x2="600" y2="320" stroke="#A855F7" stroke-width="2" marker-end="url(#arrowPurple)"/>

            <!-- ============================================================== -->
            <!-- LAYER 3: AGENTIC AI & MULTI-AGENT ORCHESTRATION CORE (THE BRAIN) -->
            <!-- ============================================================== -->
            <rect x="30" y="320" width="1140" height="280" rx="16" fill="url(#agentCoreGrad)" stroke="#6366F1" stroke-width="2"/>
            <text x="50" y="352" fill="#818CF8" font-size="14" font-weight="800" letter-spacing="0.08em">LAYER 3: AGENTIC AI & MULTI-AGENT COLLABORATIVE CORE (THE BRAIN)</text>
            <text x="50" y="370" fill="#94A3B8" font-size="11">Autonomous goal-directed reasoning: Perception, Digital Twin Simulation, Risk Calculation, and Action Orchestration</text>

            <!-- Central Multi-Agent Orchestrator -->
            <rect x="420" y="390" width="360" height="85" rx="12" fill="#312E81" stroke="#818CF8" stroke-width="2" filter="url(#glow)"/>
            <text x="450" y="422" fill="#FFFFFF" font-size="15" font-weight="800">⚡ CENTRAL MULTI-AGENT ORCHESTRATOR</text>
            <text x="460" y="442" fill="#C7D2FE" font-size="11">ReAct Loop • Policy Thresholds • Goal: Zero Flood Damage</text>
            <text x="475" y="460" fill="#38BDF8" font-size="10" font-weight="600">LangGraph State Machine & Tool Caller</text>

            <!-- Sub-Agent 1: Perception & Vision Agent -->
            <rect x="50" y="410" width="330" height="75" rx="10" fill="#1E293B" stroke="#0284C7" stroke-width="1.5"/>
            <text x="70" y="438" fill="#38BDF8" font-size="13" font-weight="700">👁️ Perception & Vision Agent</text>
            <text x="70" y="458" fill="#CBD5E1" font-size="11">YOLOv8-Sewer: Plastic Waste & Silt Detection</text>
            <text x="70" y="473" fill="#94A3B8" font-size="10">Calculates Effective Cross-Sectional Inflow Loss</text>

            <!-- Sub-Agent 2: Environmental & Weather Agent -->
            <rect x="50" y="505" width="330" height="75" rx="10" fill="#1E293B" stroke="#0284C7" stroke-width="1.5"/>
            <text x="70" y="533" fill="#38BDF8" font-size="13" font-weight="700">🌦️ Environmental Telemetry Agent</text>
            <text x="70" y="553" fill="#CBD5E1" font-size="11">Precipitation Vectors, Intensity & Duration</text>
            <text x="70" y="568" fill="#94A3B8" font-size="10">Doppler Peak Storm Arrival Window Estimation</text>

            <!-- Sub-Agent 3: Hydrological Risk Agent (Digital Twin) -->
            <rect x="820" y="410" width="330" height="75" rx="10" fill="#1E293B" stroke="#EF4444" stroke-width="1.5"/>
            <text x="840" y="438" fill="#F87171" font-size="13" font-weight="700">🌊 Hydrological Simulation & Risk Agent</text>
            <text x="840" y="458" fill="#CBD5E1" font-size="11">Cognitive Digital Twin: Runoff vs Infiltration</text>
            <text x="840" y="473" fill="#FCA5A5" font-size="10" font-weight="700">Calculates Dynamic Risk Score: 0 - 100</text>

            <!-- Sub-Agent 4: Autonomous Dispatch & Routing Agent -->
            <rect x="820" y="505" width="330" height="75" rx="10" fill="#1E293B" stroke="#10B981" stroke-width="1.5"/>
            <text x="840" y="533" fill="#34D399" font-size="13" font-weight="700">⚡ Dispatch & Route Optimization Agent</text>
            <text x="840" y="553" fill="#CBD5E1" font-size="11">Automated Work-Orders (Mechanized Super-Suckers)</text>
            <text x="840" y="568" fill="#94A3B8" font-size="10">Fleet Routing & Staging Pumps Preemptively</text>

            <!-- Internal Arrows in Core -->
            <line x1="380" y1="447" x2="420" y2="440" stroke="#38BDF8" stroke-width="1.5" marker-end="url(#arrow)"/>
            <line x1="380" y1="535" x2="480" y2="475" stroke="#38BDF8" stroke-width="1.5" marker-end="url(#arrow)"/>
            <line x1="780" y1="440" x2="820" y2="447" stroke="#EF4444" stroke-width="1.5" marker-end="url(#arrow)"/>
            <line x1="740" y1="475" x2="820" y2="535" stroke="#10B981" stroke-width="1.5" marker-end="url(#arrowGreen)"/>

            <!-- ============================================================== -->
            <!-- LAYER 4: AUTONOMOUS ACTUATION & CLOSED LOOP FEEDBACK (Bottom) -->
            <!-- ============================================================== -->
            <rect x="30" y="630" width="1140" height="150" rx="16" fill="url(#actionGrad)" stroke="#10B981" stroke-width="1.5"/>
            <text x="50" y="660" fill="#34D399" font-size="14" font-weight="800" letter-spacing="0.08em">LAYER 4: AUTONOMOUS FIELD ACTUATION & CLOSED-LOOP GOVERNANCE</text>
            <text x="50" y="678" fill="#A7F3D0" font-size="11">Preemptive municipal execution before heavy rainfall starts • Closed-loop computer vision verification</text>

            <!-- Action 4.1 Municipal Fleet -->
            <rect x="50" y="695" width="260" height="65" rx="10" fill="#064E3B" stroke="#34D399" stroke-width="1.5"/>
            <text x="70" y="722" fill="#FFFFFF" font-size="13" font-weight="700">🚛 Municipal QRT Field Squads</text>
            <text x="70" y="742" fill="#A7F3D0" font-size="11">Mechanized Jetting & Super-Suckers</text>

            <!-- Action 4.2 Automated Pumps / SCADA -->
            <rect x="340" y="695" width="260" height="65" rx="10" fill="#064E3B" stroke="#34D399" stroke-width="1.5"/>
            <text x="360" y="722" fill="#FFFFFF" font-size="13" font-weight="700">🚰 Smart Sluice & SCADA Pumps</text>
            <text x="360" y="742" fill="#A7F3D0" font-size="11">Dynamic Discharge Gate Actuation</text>

            <!-- Action 4.3 Traffic & Public Broadcast -->
            <rect x="630" y="695" width="260" height="65" rx="10" fill="#064E3B" stroke="#34D399" stroke-width="1.5"/>
            <text x="650" y="722" fill="#FFFFFF" font-size="13" font-weight="700">🚦 Traffic Police & Citizen Advisory</text>
            <text x="650" y="742" fill="#A7F3D0" font-size="11">Automated Early Lane Diversion Alerts</text>

            <!-- Action 4.4 Closed Loop Verification Node -->
            <rect x="920" y="695" width="230" height="65" rx="10" fill="#134E4A" stroke="#2DD4BF" stroke-width="2"/>
            <text x="935" y="722" fill="#FFFFFF" font-size="13" font-weight="800">🔄 Post-Clean Proof</text>
            <text x="935" y="742" fill="#99F6E4" font-size="11">Crews upload clean photo</text>

            <!-- Output Flow to Layer 4 -->
            <line x1="985" y1="580" x2="985" y2="695" stroke="#10B981" stroke-width="2" marker-end="url(#arrowGreen)"/>

            <!-- CLOSED LOOP FEEDBACK DASHED PATH -->
            <path d="M 1035 695 C 1035 600, 1180 500, 1180 300 C 1180 150, 600 20, 215 90" fill="none" stroke="#2DD4BF" stroke-width="2" stroke-dasharray="6,4" marker-end="url(#arrow)"/>
            <text x="1100" y="270" fill="#2DD4BF" font-size="11" font-weight="700" transform="rotate(90 1100 270)">🔄 Closed-Loop Feedback Proof</text>
        </svg>
    </div>
</div>

<script>
    const container = document.getElementById('viewport-container');
    const wrapper = document.getElementById('transform-wrapper');
    const svg = document.getElementById('svg-canvas');

    let scale = 0.85;
    let pointX = 20;
    let pointY = 10;
    let startX = 0;
    let startY = 0;
    let isPanning = false;

    function updateTransform() {
        wrapper.style.transform = `translate(${pointX}px, ${pointY}px) scale(${scale})`;
    }

    // Initial position
    updateTransform();

    function zoom(factor) {
        const newScale = scale * factor;
        if (newScale >= 0.4 && newScale <= 3.0) {
            // Zoom towards center of container
            const rect = container.getBoundingClientRect();
            const cx = rect.width / 2;
            const cy = rect.height / 2;
            pointX = cx - (cx - pointX) * factor;
            pointY = cy - (cy - pointY) * factor;
            scale = newScale;
            updateTransform();
        }
    }

    function resetView() {
        scale = 0.85;
        pointX = 20;
        pointY = 10;
        updateTransform();
    }

    // Mouse Wheel Zoom
    container.addEventListener('wheel', function(e) {
        e.preventDefault();
        const xs = (e.clientX - container.getBoundingClientRect().left - pointX) / scale;
        const ys = (e.clientY - container.getBoundingClientRect().top - pointY) / scale;
        const delta = e.deltaY < 0 ? 1.15 : 0.85;
        const newScale = scale * delta;

        if (newScale >= 0.4 && newScale <= 3.0) {
            scale = newScale;
            pointX = e.clientX - container.getBoundingClientRect().left - xs * scale;
            pointY = e.clientY - container.getBoundingClientRect().top - ys * scale;
            updateTransform();
        }
    }, { passive: false });

    // Click and Drag Pan
    container.addEventListener('mousedown', function(e) {
        if (e.target.closest('.toolbar')) return;
        isPanning = true;
        startX = e.clientX - pointX;
        startY = e.clientY - pointY;
    });

    window.addEventListener('mousemove', function(e) {
        if (!isPanning) return;
        pointX = e.clientX - startX;
        pointY = e.clientY - startY;
        updateTransform();
    });

    window.addEventListener('mouseup', function() {
        isPanning = false;
    });

    // Touch Support for mobile
    let initialPinchDistance = null;
    container.addEventListener('touchstart', function(e) {
        if (e.touches.length === 1) {
            isPanning = true;
            startX = e.touches[0].clientX - pointX;
            startY = e.touches[0].clientY - pointY;
        } else if (e.touches.length === 2) {
            initialPinchDistance = Math.hypot(
                e.touches[0].clientX - e.touches[1].clientX,
                e.touches[0].clientY - e.touches[1].clientY
            );
        }
    });

    container.addEventListener('touchmove', function(e) {
        if (isPanning && e.touches.length === 1) {
            pointX = e.touches[0].clientX - startX;
            pointY = e.touches[0].clientY - startY;
            updateTransform();
        } else if (e.touches.length === 2 && initialPinchDistance) {
            const currentDist = Math.hypot(
                e.touches[0].clientX - e.touches[1].clientX,
                e.touches[0].clientY - e.touches[1].clientY
            );
            const factor = currentDist / initialPinchDistance;
            zoom(factor > 1 ? 1.05 : 0.95);
            initialPinchDistance = currentDist;
        }
    });

    container.addEventListener('touchend', function() {
        isPanning = false;
        initialPinchDistance = null;
    });
</script>

</body>
</html>
"""
