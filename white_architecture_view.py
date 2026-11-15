def get_white_interactive_architecture_html():
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
        background: #FFFFFF;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 12px -2px rgba(0, 0, 0, 0.05);
        cursor: grab;
        user-select: none;
    }
    
    #viewport-container:active {
        cursor: grabbing;
    }
    
    /* Subtle dot grid pattern on white bg */
    .grid-bg {
        background-color: #FFFFFF;
        background-image: radial-gradient(#CBD5E1 1px, transparent 1px);
        background-size: 24px 24px;
    }
    
    .toolbar {
        position: absolute;
        top: 14px;
        right: 14px;
        z-index: 100;
        display: flex;
        gap: 6px;
        background: rgba(255, 255, 255, 0.92);
        backdrop-filter: blur(8px);
        padding: 5px 8px;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }
    
    .tool-btn {
        background: #F8FAFC;
        color: #0F172A;
        border: 1px solid #CBD5E1;
        padding: 5px 12px;
        border-radius: 6px;
        font-weight: 600;
        cursor: pointer;
        font-size: 12px;
        transition: all 0.15s ease;
    }
    
    .tool-btn:hover {
        background: #0284C7;
        color: white;
        border-color: #0284C7;
    }
    
    .status-pill {
        position: absolute;
        bottom: 14px;
        left: 14px;
        z-index: 100;
        background: rgba(255, 255, 255, 0.95);
        padding: 5px 12px;
        border-radius: 20px;
        border: 1px solid #E2E8F0;
        color: #475569;
        font-size: 11px;
        font-weight: 600;
        box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }

    #transform-wrapper {
        position: absolute;
        top: 0;
        left: 0;
        transform-origin: 0 0;
        transition: transform 0.05s ease-out;
    }

    #svg-canvas {
        width: 1180px;
        height: 800px;
    }
</style>
</head>
<body class="grid-bg">

<div id="viewport-container" class="grid-bg">
    <!-- Controls Toolbar (Zero Emojis, Clean Professional Style) -->
    <div class="toolbar">
        <button class="tool-btn" onclick="zoom(1.2)"><b>Zoom In (+)</b></button>
        <button class="tool-btn" onclick="zoom(0.8)"><b>Zoom Out (-)</b></button>
        <button class="tool-btn" onclick="resetView()"><b>Reset View</b></button>
        <span style="color: #64748B; font-size: 11px; align-self: center; margin-left: 6px;">Drag to Pan • Mouse Wheel to Zoom</span>
    </div>

    <div class="status-pill">
        <span>DrainWatch System Architecture Graph • Interactive Pan & Zoom</span>
    </div>

    <!-- Canvas -->
    <div id="transform-wrapper">
        <svg id="svg-canvas" viewBox="0 0 1180 800" fill="none" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <marker id="arrowBlue" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#0284C7" />
                </marker>
                <marker id="arrowPurple" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#7C3AED" />
                </marker>
                <marker id="arrowGreen" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#16A34A" />
                </marker>
                <marker id="arrowRed" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#DC2626" />
                </marker>
            </defs>

            <!-- ============================================================== -->
            <!-- TIER 1: MULTIMODAL PERCEPTION & EDGE TELEMETRY -->
            <!-- ============================================================== -->
            <rect x="25" y="25" width="1130" height="145" rx="12" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
            <text x="45" y="55" fill="#0284C7" font-size="13" font-weight="800" letter-spacing="0.05em">TIER 1: MULTIMODAL PERCEPTION & EDGE TELEMETRY LAYER</text>
            <text x="45" y="73" fill="#64748B" font-size="11">Real-time edge ingestion: Crowdsourced mobile photos, subterranean depth sensors, and radar nowcasts</text>

            <!-- Node 1.1 -->
            <rect x="45" y="90" width="250" height="62" rx="8" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
            <text x="65" y="115" fill="#0F172A" font-size="12" font-weight="700">Citizen Smartphone Ingestion</text>
            <text x="65" y="135" fill="#64748B" font-size="11">Geo-tagged Photos & Blockage Reports</text>

            <!-- Node 1.2 -->
            <rect x="325" y="90" width="250" height="62" rx="8" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
            <text x="345" y="115" fill="#0F172A" font-size="12" font-weight="700">IoT Stormdrain Sensors</text>
            <text x="345" y="135" fill="#64748B" font-size="11">Ultrasonic Level & Silt Accumulation</text>

            <!-- Node 1.3 -->
            <rect x="605" y="90" width="250" height="62" rx="8" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
            <text x="625" y="115" fill="#0F172A" font-size="12" font-weight="700">Doppler Weather Radar</text>
            <text x="625" y="135" fill="#64748B" font-size="11">Real-Time Rain Rate (mm/hr) Forecast</text>

            <!-- Node 1.4 -->
            <rect x="885" y="90" width="250" height="62" rx="8" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
            <text x="905" y="115" fill="#0F172A" font-size="12" font-weight="700">GIS Elevation Model (DEM)</text>
            <text x="905" y="135" fill="#64748B" font-size="11">Catchment Topology & Culvert Specs</text>

            <!-- Flow Arrows to Tier 2 -->
            <line x1="170" y1="152" x2="170" y2="200" stroke="#0284C7" stroke-width="1.5" marker-end="url(#arrowBlue)"/>
            <line x1="450" y1="152" x2="450" y2="200" stroke="#0284C7" stroke-width="1.5" marker-end="url(#arrowBlue)"/>
            <line x1="730" y1="152" x2="730" y2="200" stroke="#0284C7" stroke-width="1.5" marker-end="url(#arrowBlue)"/>
            <line x1="1010" y1="152" x2="1010" y2="200" stroke="#0284C7" stroke-width="1.5" marker-end="url(#arrowBlue)"/>

            <!-- ============================================================== -->
            <!-- TIER 2: STREAMING INGESTION & DEDUPLICATION GATEWAY -->
            <!-- ============================================================== -->
            <rect x="25" y="200" width="1130" height="65" rx="10" fill="#F1F5F9" stroke="#94A3B8" stroke-width="1.5"/>
            <text x="45" y="228" fill="#7C3AED" font-size="13" font-weight="800">TIER 2: KAFKA / MQTT REAL-TIME EVENT STREAMING GATEWAY</text>
            <text x="45" y="248" fill="#475569" font-size="11">Data Normalization • Semantic Spatial-Temporal Deduplication • Inflow Feature Fusion</text>

            <!-- Flow Arrow to Tier 3 -->
            <line x1="590" y1="265" x2="590" y2="300" stroke="#7C3AED" stroke-width="2" marker-end="url(#arrowPurple)"/>

            <!-- ============================================================== -->
            <!-- TIER 3: AGENTIC AI COGNITIVE CORE (THE BRAIN) -->
            <!-- ============================================================== -->
            <rect x="25" y="300" width="1130" height="280" rx="12" fill="#FAF5FF" stroke="#C084FC" stroke-width="1.8"/>
            <text x="45" y="330" fill="#6B21A8" font-size="13" font-weight="800" letter-spacing="0.05em">TIER 3: AGENTIC AI COGNITIVE CORE (LANGGRAPH MULTI-AGENT SWARM)</text>
            <text x="45" y="348" fill="#64748B" font-size="11">Coordinated multi-agent reasoning, digital twin hydraulic simulation, and dynamic risk synthesis</text>

            <!-- Central Multi-Agent Orchestrator -->
            <rect x="400" y="370" width="380" height="85" rx="10" fill="#FFFFFF" stroke="#7C3AED" stroke-width="2"/>
            <text x="430" y="402" fill="#4C1D95" font-size="14" font-weight="800">Central Multi-Agent Orchestrator</text>
            <text x="430" y="422" fill="#6D28D9" font-size="11">LangGraph State Machine • ReAct Reasoning Loop</text>
            <text x="430" y="440" fill="#0284C7" font-size="11" font-weight="600">Fixed Objective: Zero Urban Flood Damage</text>

            <!-- Sub-Agent 1: Vision -->
            <rect x="45" y="380" width="310" height="75" rx="8" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
            <text x="65" y="408" fill="#0284C7" font-size="12" font-weight="700">Computer Vision Agent</text>
            <text x="65" y="428" fill="#334155" font-size="11">YOLOv8-Sewer: Plastic Waste & Silt</text>
            <text x="65" y="443" fill="#64748B" font-size="10">Cross-Sectional Inflow Loss Calculation</text>

            <!-- Sub-Agent 2: Weather -->
            <rect x="45" y="475" width="310" height="75" rx="8" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
            <text x="65" y="503" fill="#0284C7" font-size="12" font-weight="700">Weather Telemetry Agent</text>
            <text x="65" y="523" fill="#334155" font-size="11">Precipitation Vectors & Intensity Forecast</text>
            <text x="65" y="538" fill="#64748B" font-size="10">Peak Rainfall Arrival Window Estimation</text>

            <!-- Sub-Agent 3: Risk Simulator -->
            <rect x="825" y="380" width="310" height="75" rx="8" fill="#FEF2F2" stroke="#DC2626" stroke-width="1.8"/>
            <text x="845" y="408" fill="#B91C1C" font-size="12" font-weight="700">Hydrological Digital Twin Simulator</text>
            <text x="845" y="428" fill="#334155" font-size="11">Localized Inundation Modeling (Runoff vs Sump)</text>
            <text x="845" y="443" fill="#DC2626" font-size="11" font-weight="700">Dynamic Risk Score Output: 0 - 100</text>

            <!-- Sub-Agent 4: Dispatcher -->
            <rect x="825" y="475" width="310" height="75" rx="8" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.8"/>
            <text x="845" y="503" fill="#15803D" font-size="12" font-weight="700">Dispatch Optimization Agent</text>
            <text x="845" y="523" fill="#334155" font-size="11">Automated Preventive Work-Order Generation</text>
            <text x="845" y="538" fill="#64748B" font-size="10">Preemptive Fleet Routing & Pump Staging</text>

            <!-- Core Inter-Agent Connectors -->
            <line x1="355" y1="417" x2="400" y2="412" stroke="#0284C7" stroke-width="1.5" marker-end="url(#arrowBlue)"/>
            <line x1="355" y1="512" x2="430" y2="455" stroke="#0284C7" stroke-width="1.5" marker-end="url(#arrowBlue)"/>
            <line x1="780" y1="412" x2="825" y2="417" stroke="#DC2626" stroke-width="1.5" marker-end="url(#arrowRed)"/>
            <line x1="740" y1="455" x2="825" y2="512" stroke="#16A34A" stroke-width="1.5" marker-end="url(#arrowGreen)"/>

            <!-- ============================================================== -->
            <!-- TIER 4: FIELD ACTUATION & CLOSED-LOOP GOVERNANCE -->
            <!-- ============================================================== -->
            <rect x="25" y="615" width="1130" height="150" rx="12" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5"/>
            <text x="45" y="645" fill="#166534" font-size="13" font-weight="800" letter-spacing="0.05em">TIER 4: FIELD ACTUATION & CLOSED-LOOP VERIFICATION LAYER</text>
            <text x="45" y="663" fill="#475569" font-size="11">Preemptive execution before downpours commence • Auditable closed-loop verification</text>

            <!-- Actuation 4.1 -->
            <rect x="45" y="680" width="250" height="65" rx="8" fill="#FFFFFF" stroke="#16A34A" stroke-width="1.5"/>
            <text x="65" y="707" fill="#0F172A" font-size="12" font-weight="700">Municipal Jetting Units</text>
            <text x="65" y="727" fill="#475569" font-size="11">Mechanized Super-Sucker Trucks</text>

            <!-- Actuation 4.2 -->
            <rect x="325" y="680" width="250" height="65" rx="8" fill="#FFFFFF" stroke="#16A34A" stroke-width="1.5"/>
            <text x="345" y="707" fill="#0F172A" font-size="12" font-weight="700">Smart Sluice Gates (SCADA)</text>
            <text x="345" y="727" fill="#475569" font-size="11">Automated Basin Discharge Control</text>

            <!-- Actuation 4.3 -->
            <rect x="605" y="680" width="250" height="65" rx="8" fill="#FFFFFF" stroke="#16A34A" stroke-width="1.5"/>
            <text x="625" y="707" fill="#0F172A" font-size="12" font-weight="700">Traffic Safety Broadcast</text>
            <text x="625" y="727" fill="#475569" font-size="11">Dynamic Early Lane Diversion Alerts</text>

            <!-- Actuation 4.4 Verification -->
            <rect x="885" y="680" width="250" height="65" rx="8" fill="#ECFDF5" stroke="#059669" stroke-width="2"/>
            <text x="905" y="707" fill="#065F46" font-size="12" font-weight="800">Post-Action Verification</text>
            <text x="905" y="727" fill="#047857" font-size="11">Field photo upload verifies clearance</text>

            <!-- Downward Action Arrow -->
            <line x1="980" y1="550" x2="980" y2="680" stroke="#16A34A" stroke-width="2" marker-end="url(#arrowGreen)"/>

            <!-- CLOSED LOOP FEEDBACK DASHED PATH (White Theme) -->
            <path d="M 1030 680 C 1030 580, 1160 480, 1160 280 C 1160 140, 600 15, 170 85" fill="none" stroke="#059669" stroke-width="2" stroke-dasharray="6,4" marker-end="url(#arrowGreen)"/>
            <text x="1100" y="270" fill="#059669" font-size="11" font-weight="700" transform="rotate(90 1100 270)">Closed-Loop Feedback Proof</text>
        </svg>
    </div>
</div>

<script>
    const container = document.getElementById('viewport-container');
    const wrapper = document.getElementById('transform-wrapper');

    let scale = 0.85;
    let pointX = 20;
    let pointY = 10;
    let startX = 0;
    let startY = 0;
    let isPanning = false;

    function updateTransform() {
        wrapper.style.transform = `translate(${pointX}px, ${pointY}px) scale(${scale})`;
    }

    updateTransform();

    function zoom(factor) {
        const newScale = scale * factor;
        if (newScale >= 0.4 && newScale <= 3.0) {
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

    // Touch Support
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
