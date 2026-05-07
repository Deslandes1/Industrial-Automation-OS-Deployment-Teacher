import streamlit as st
from datetime import datetime
import random

st.set_page_config(
    page_title="IA OS Deployment | GlobalInternet.py",
    page_icon="🏭",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0a0f1a 0%, #0d1b2a 100%);
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0b1c2c 0%, #07121f 100%);
        border-right: 2px solid #00d4ff;
    }
    [data-testid="stSidebar"] .stMarkdown, 
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] .stCaption {
        color: #e0e0e0 !important;
    }
    .stButton button {
        background-color: #00d4ff !important;
        color: #0a0f1a !important;
        border-radius: 30px !important;
        font-weight: bold !important;
    }
    .stButton button:hover {
        background-color: #ffaa33 !important;
        transform: scale(1.02);
    }
    .step-card {
        background: rgba(0,212,255,0.1);
        border-radius: 15px;
        padding: 1rem;
        margin: 1rem 0;
        border-left: 4px solid #00d4ff;
    }
    .code-block {
        background: #1e1e2e;
        padding: 1rem;
        border-radius: 12px;
        font-family: monospace;
        color: #ffaa66;
        overflow-x: auto;
    }
    .info-banner {
        background: rgba(0,212,255,0.1);
        border-left: 4px solid #00d4ff;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    h1, h2, h3 {
        color: #00d4ff !important;
    }
    p, li {
        color: #d0d0d0 !important;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        border-top: 1px solid #00d4ff;
    }
</style>
""", unsafe_allow_html=True)

# ---------- LOGIN STATE ----------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def logout():
    st.session_state.authenticated = False
    st.rerun()

# ---------- LOGIN PAGE ----------
def show_login():
    st.markdown("""
    <style>
    .login-container { display: flex; justify-content: center; align-items: center; min-height: 80vh; }
    .login-card {
        background: rgba(15,52,96,0.8);
        backdrop-filter: blur(12px);
        border-radius: 30px;
        padding: 2.5rem;
        text-align: center;
        border: 1px solid rgba(0,212,255,0.5);
        width: 100%;
        max-width: 450px;
    }
    .spinning-globe { font-size: 80px; animation: spin 4s linear infinite; display: inline-block; }
    @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    .login-title { color: #00d4ff; font-size: 2rem; margin-bottom: 1rem; }
    </style>
    <div class="login-container">
        <div class="login-card">
            <div class="spinning-globe">🌍</div>
            <div class="login-title">Industrial Automation OS Deployment</div>
            <p style="color:#d0d0d0;">Enter password to access deployment training</p>
    """, unsafe_allow_html=True)
    password = st.text_input("Password", type="password", key="login_pass")
    if st.button("🔐 Enter", use_container_width=True):
        if password == "20082010":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Incorrect password.")
    st.markdown("</div></div>", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
def show_sidebar():
    st.sidebar.markdown("""
    <div style="text-align: center;">
        <div style="font-size:80px; animation:spin 4s linear infinite; display:inline-block;">🌍</div>
    </div>
    <style>@keyframes spin{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}</style>
    """, unsafe_allow_html=True)
    st.sidebar.markdown("## **GlobalInternet.py**")
    st.sidebar.markdown("### IA OS Deployment Training")
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Lead Engineer:** Gesner Deslandes")
    st.sidebar.markdown("📞 (509)-47385663")
    st.sidebar.markdown("✉️ deslandes78@gmail.com")
    st.sidebar.markdown("---")
    st.sidebar.markdown("**🌐 Website:**")
    st.sidebar.markdown("[https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
    st.sidebar.markdown("---")
    
    mode = st.sidebar.radio("📚 Mode", ["🎮 Demo Mode (Simulation)", "🛠️ Real‑Life Practice Mode"])
    
    st.sidebar.markdown("### 💰 Full Deployment Package")
    st.sidebar.markdown("""
    | Plan | Price (USD/year) |
    |------|------------------|
    | **Single Factory** | $4,999 |
    | **Multi‑Site (5 factories)** | $19,999 |
    | **Enterprise (unlimited)** | $49,999 |
    | **Source + OEM License** | $99,999 |
    """)
    st.sidebar.info("✅ Includes OPC UA, MQTT, ROS integration, 24/7 support, and deployment assistance.")
    st.sidebar.markdown("---")
    if st.sidebar.button("🔓 Logout", use_container_width=True):
        logout()
    return mode

# ---------- DEMO MODE (interactive simulation) ----------
def demo_mode():
    st.markdown("<h1 style='text-align:center;'>🏭 IA OS – Deployment Simulator</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Click through the steps to see how the production version would be installed on your server.</p>", unsafe_allow_html=True)
    
    st.markdown("### 🚀 Deployment Steps (Simulated)")
    
    steps = [
        "1️⃣ Prepare a Linux server (Ubuntu 22.04) or Windows Server 2019+",
        "2️⃣ Install Docker and Docker Compose",
        "3️⃣ Download the IA OS package from GlobalInternet.py",
        "4️⃣ Configure `docker-compose.yml` with your hardware IPs",
        "5️⃣ Run `docker-compose up -d` to start the backend",
        "6️⃣ Access dashboard at `http://your-server:8501`",
        "7️⃣ Connect robots via OPC UA / MQTT / ROS"
    ]
    
    # Store step index in session state for simulation
    if "deploy_step" not in st.session_state:
        st.session_state.deploy_step = 0
    
    for i, step in enumerate(steps):
        col_status, col_desc = st.columns([1, 10])
        with col_status:
            if i < st.session_state.deploy_step:
                st.markdown("✅")
            elif i == st.session_state.deploy_step:
                st.markdown("🔄")
            else:
                st.markdown("⏳")
        with col_desc:
            st.markdown(step)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶️ Next Step"):
            if st.session_state.deploy_step < len(steps):
                st.session_state.deploy_step += 1
                st.rerun()
    with col2:
        if st.button("⟳ Reset"):
            st.session_state.deploy_step = 0
            st.rerun()
    
    if st.session_state.deploy_step >= len(steps):
        st.success("🎉 Deployment complete! Dashboard is now running. In production, you would then configure your robots.")
        st.markdown("""
        <div class="info-banner">
        🔌 <strong>In production:</strong> After deployment, you would open the dashboard and enter your robot IPs.  
        The system will automatically discover OPC UA endpoints and start streaming data.
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🖥️ Dashboard Preview (Production)")
    st.image("https://via.placeholder.com/800x400?text=Dashboard+with+Live+Robot+Data", use_container_width=True)
    st.caption("This is what you would see after installation – real metrics from your own equipment.")

# ---------- REAL‑LIFE PRACTICE MODE ----------
def practice_mode():
    st.markdown("<h1 style='text-align:center;'>🛠️ Real‑Life Practice – Deploy IA OS Yourself</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Follow these instructions on your own server to install the production version (after purchasing a license).</p>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-banner">
    📦 <strong>Prerequisites:</strong> A Linux server (Ubuntu 22.04 recommended) with root access, Docker installed, and a stable internet connection.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## 📥 Step 1: Get the Package")
    st.markdown("After purchasing a license, you will receive a download link. The package contains:")
    st.markdown("""
    - `docker-compose.yml` – service definitions
    - `backend/` – Python services for OPC UA, MQTT, ROS
    - `dashboard/` – Streamlit frontend
    - `config/` – example configuration files
    - `install.sh` – one‑click installer script
    """)
    
    st.markdown("## 🐳 Step 2: Run the Installer")
    st.code("""
# Download and unzip the package
unzip ia_os_production.zip
cd ia_os_production

# Make the installer executable and run it
chmod +x install.sh
sudo ./install.sh
    """, language="bash")
    st.markdown("The installer will:")
    st.markdown("- Create a `ia_os` user")
    st.markdown("- Install Python dependencies")
    st.markdown("- Pull Docker images for TimescaleDB, Kafka, and the backend")
    st.markdown("- Generate self‑signed SSL certificates for secure dashboard access")
    
    st.markdown("## ⚙️ Step 3: Configure Hardware Connections")
    st.markdown("Edit the `config/robots.yaml` file:")
    st.code("""
robots:
  - name: "ABB_IRB120"
    protocol: "opcua"
    endpoint: "opc.tcp://192.168.1.10:4840"
    security: "None"
  - name: "Humanoid_ROS"
    protocol: "ros"
    master_uri: "http://10.0.0.5:11311"
  - name: "Conveyor_Belt"
    protocol: "mqtt"
    broker: "mqtt://192.168.1.20:1883"
    topic: "factory/conveyor/status"
    """, language="yaml")
    
    st.markdown("## 🚀 Step 4: Start the System")
    st.code("""
# From the ia_os_production directory
docker-compose up -d

# Check that all services are running
docker-compose ps
    """, language="bash")
    st.markdown("Expected output: `backend`, `dashboard`, `timescaledb`, `kafka` – all `Up`.")
    
    st.markdown("## 🔐 Step 5: Access the Dashboard")
    st.markdown("Open your browser to `https://your-server-ip:8501` (use the self‑signed certificate).")
    st.markdown("Login with the credentials provided in the license email (or set them via `config/auth.yaml`).")
    
    st.markdown("## 📊 Step 6: Verify Data Flow")
    st.markdown("""
    - The dashboard should show live robot speed, conveyor status, and AI inspection results.
    - Use the **Test Connection** button in the dashboard to ping each robot.
    - If any robot is offline, check the event log for specific errors.
    """)
    
    st.markdown("---")
    st.markdown("## 🔧 Troubleshooting Common Issues")
    st.markdown("""
    | Problem | Solution |
    |---------|----------|
    | Docker containers won't start | Run `docker-compose logs` to see error messages. Ensure ports 8501, 5432, 9092 are free. |
    | Cannot connect to OPC UA server | Verify the endpoint URL and that the robot’s firewall allows OPC UA (port 4840). |
    | MQTT no data | Check broker address and topic; use `mosquitto_sub` to test. |
    | ROS connection refused | Ensure ROS master is reachable and `ROS_MASTER_URI` is correct. |
    | Dashboard shows simulation instead of real data | Edit `config/mode.yaml` and set `mode: production`. |
    """)
    
    st.info("📘 For a detailed walkthrough with video, [contact us](mailto:deslandes78@gmail.com) to schedule a deployment training session.")
    
    st.markdown("---")
    st.markdown("## 📦 What You Get After Purchase")
    st.markdown("""
    - Complete Docker‑based stack (backend + dashboard + database)
    - Configuration files for OPC UA, MQTT, and ROS
    - One‑hour remote installation assistance
    - 30 days of email support
    - Option for on‑site training (additional cost)
    """)

# ---------- MAIN ----------
if not st.session_state.authenticated:
    show_login()
else:
    selected_mode = show_sidebar()
    if selected_mode == "🎮 Demo Mode (Simulation)":
        demo_mode()
    else:
        practice_mode()
    st.markdown('<div class="footer">© GlobalInternet.py – Deploy Industrial Automation OS on your own infrastructure. Purchase license via sidebar.</div>', unsafe_allow_html=True)
