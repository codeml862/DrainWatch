import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "drainwatch.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS locations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        city TEXT,
        category TEXT,
        latitude REAL,
        longitude REAL,
        elevation_m REAL,
        drainage_capacity_index REAL,
        historical_flood_count INTEGER,
        current_drain_status TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS complaints (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location_name TEXT,
        citizen_name TEXT,
        phone TEXT,
        description TEXT,
        image_path TEXT,
        ai_detected_blockage TEXT,
        ai_confidence REAL,
        status TEXT,
        created_at TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dispatches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location_name TEXT,
        rainfall_intensity TEXT,
        risk_score INTEGER,
        priority_level TEXT,
        action_plan TEXT,
        assigned_crew TEXT,
        status TEXT,
        created_at TEXT
    )
    """)

    # Repopulate locations with India-wide major urban drainage hotspots
    cursor.execute("DROP TABLE IF EXISTS locations")
    cursor.execute("""
    CREATE TABLE locations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        city TEXT,
        category TEXT,
        latitude REAL,
        longitude REAL,
        elevation_m REAL,
        drainage_capacity_index REAL,
        historical_flood_count INTEGER,
        current_drain_status TEXT
    )
    """)

    all_india_hotspots = [
        # Mumbai
        ("Mumbai - Hindmata Junction", "Mumbai", "Low-lying Underpass", 19.0116, 72.8427, 4.2, 0.25, 7, "Severely Blocked"),
        ("Mumbai - Milan Subway, Santacruz", "Mumbai", "Subway / Arterial Road", 19.0833, 72.8378, 5.8, 0.30, 6, "Severely Blocked"),
        ("Mumbai - Kurla West LBS Road", "Mumbai", "Catchment Basin", 19.0728, 72.8826, 6.5, 0.35, 5, "Partially Clogged"),
        
        # Delhi NCR
        ("Delhi - Minto Bridge Underpass", "Delhi", "Railway Underpass", 28.6349, 77.2255, 214.0, 0.20, 8, "Severely Blocked"),
        ("Delhi - Pul Prahladpur Underpass", "Delhi", "Underpass", 28.5026, 77.2917, 218.5, 0.30, 5, "Partially Clogged"),
        ("Delhi - ITO Ring Road Intersection", "Delhi", "Major Junction", 28.6297, 77.2435, 210.2, 0.40, 4, "Partially Clogged"),

        # Bengaluru
        ("Bengaluru - Silk Board Junction", "Bengaluru", "Arterial Chokepoint", 12.9176, 77.6238, 910.0, 0.35, 6, "Severely Blocked"),
        ("Bengaluru - Bellandur Outer Ring Road", "Bengaluru", "Lake Basin Road", 12.9304, 77.6784, 885.0, 0.28, 7, "Severely Blocked"),
        ("Bengaluru - Hebbal Lake Inflow Drain", "Bengaluru", "Storm Drain", 13.0358, 77.5970, 920.0, 0.55, 2, "Clear"),

        # Chennai
        ("Chennai - Velachery Main Road", "Chennai", "Lowland Corridor", 12.9759, 80.2212, 6.0, 0.22, 8, "Severely Blocked"),
        ("Chennai - Usman Road, T. Nagar", "Chennai", "Commercial Hub", 13.0405, 80.2337, 9.5, 0.32, 5, "Partially Clogged"),
        ("Chennai - Mudichur Main Road", "Chennai", "Residential Basin", 12.9090, 80.0710, 11.2, 0.40, 4, "Partially Clogged"),

        # Kolkata
        ("Kolkata - Central Avenue (CR Avenue)", "Kolkata", "Commercial Artery", 22.5804, 88.3615, 6.5, 0.28, 6, "Severely Blocked"),
        ("Kolkata - Park Circus 7-Point", "Kolkata", "Major Junction", 22.5437, 88.3664, 7.1, 0.35, 4, "Partially Clogged"),

        # Hyderabad
        ("Hyderabad - Begumpet Rasoolpura Underpass", "Hyderabad", "Underpass", 17.4448, 78.4729, 512.0, 0.30, 5, "Severely Blocked"),
        ("Hyderabad - Tolichowki Flyover Junction", "Hyderabad", "Low Basin Road", 17.4022, 78.4116, 520.0, 0.38, 4, "Partially Clogged"),
        ("Hyderabad - Hitec City Mindspace Inflow", "Hyderabad", "Express Corridor", 17.4416, 78.3804, 565.0, 0.80, 1, "Clear")
    ]

    cursor.executemany("""
    INSERT INTO locations (name, city, category, latitude, longitude, elevation_m, drainage_capacity_index, historical_flood_count, current_drain_status)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, all_india_hotspots)

    conn.commit()
    conn.close()

def get_all_locations():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM locations").fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_all_cities():
    conn = get_connection()
    rows = conn.execute("SELECT DISTINCT city FROM locations ORDER BY city ASC").fetchall()
    conn.close()
    return [r["city"] for r in rows]

def get_locations_by_city(city):
    conn = get_connection()
    rows = conn.execute("SELECT * FROM locations WHERE city = ?", (city,)).fetchall()
    conn.close()
    return [dict(r) for r in rows]

def add_complaint(location_name, citizen_name, phone, description, image_path, blockage_status, confidence):
    conn = get_connection()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute("""
    INSERT INTO complaints (location_name, citizen_name, phone, description, image_path, ai_detected_blockage, ai_confidence, status, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, 'Pending', ?)
    """, (location_name, citizen_name, phone, description, image_path, blockage_status, confidence, now))
    conn.execute("UPDATE locations SET current_drain_status = ? WHERE name = ?", (blockage_status, location_name))
    conn.commit()
    conn.close()

def add_dispatch(location_name, rainfall, risk_score, priority, action_plan, crew):
    conn = get_connection()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO dispatches (location_name, rainfall_intensity, risk_score, priority_level, action_plan, assigned_crew, status, created_at)
    VALUES (?, ?, ?, ?, ?, ?, 'Dispatched', ?)
    """, (location_name, rainfall, risk_score, priority, action_plan, crew, now))
    dispatch_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return dispatch_id

def get_all_dispatches():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM dispatches ORDER BY id DESC").fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_all_complaints():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM complaints ORDER BY id DESC").fetchall()
    conn.close()
    return [dict(r) for r in rows]

if __name__ == "__main__":
    init_db()
    print("Database re-initialized with All-India Hotspots successfully.")
