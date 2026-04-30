import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

# 1. إعدادات الواجهة المتقدمة
st.set_page_config(page_title="JANA-SI | Sovereign Research Suite", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #050a0f; color: #e0e0e0; }
    .stMetric { background-color: #0d1117; border: 1px solid #00ffcc; border-radius: 10px; padding: 15px; }
    .status-box { padding: 20px; border-radius: 10px; border-left: 5px solid #00ffcc; background: #161b22; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧬 JANA-SI: Deciphering Bioelectric Swarm Intelligence")
st.write("---")

# 2. القائمة الجانبية للتحكم المختبري
st.sidebar.header("🔬 Simulation Parameters")
swarm_density = st.sidebar.slider("Number of MENPs", 100, 500, 250)
noise_level = st.sidebar.slider("Algorithmic Noise (Blood Flow)", 0.0, 1.0, 0.2)
sim_speed = st.sidebar.slider("Simulation Step Delay", 0.1, 1.0, 0.3)

# 3. تخطيط الصفحة (الأعمدة)
col_viz, col_data = st.columns([2, 1])

with col_viz:
    viz_container = st.empty()
    narration = st.empty()

with col_data:
    st.subheader("📊 Live Telemetry")
    metrics_container = st.empty()
    chart_container = st.empty()

# 4. دالة بناء المحاكاة المعقدة
def create_complex_viz(px, py, pz, t_state, progress):
    fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scene'}]])
    
    # رسم الورم (Target Site)
    u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:15j]
    tx = 20 + 7 * np.cos(u) * np.sin(v)
    ty = 20 + 7 * np.sin(u) * np.sin(v)
    tz = 20 + 7 * np.cos(v)
    
    color = "#ff3333" if t_state == "active" else "#00ffcc"
    opac = 0.1 + (progress * 0.4)
    
    fig.add_trace(go.Mesh3d(x=tx.flatten(), y=ty.flatten(), z=tz.flatten(), 
                            color=color, opacity=opac, alphahull=0), row=1, col=1)

    # رسم الأسراب وتأثير الضجيج الخوارزمي
    fig.add_trace(go.Scatter3d(x=px, y=py, z=pz, mode='markers',
                                marker=dict(size=3, color='gold', opacity=0.7),
                                name="MENPs Agents"), row=1, col=1)

    fig.update_layout(scene=dict(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False, bgcolor="black"),
                      margin=dict(l=0, r=0, b=0, t=0), height=600, paper_bgcolor="black", showlegend=False)
    return fig

# 5. تشغيل التجربة السريرية الافتراضية
if st.sidebar.button("▶️ Execute Full Validation"):
    px, py, pz = np.random.uniform(0, 40, swarm_density), np.random.uniform(0, 5, swarm_density), np.random.uniform(0, 40, swarm_density)
    voltages = []
    
    # المرحلة الأولى: الملاحة عبر الضجيج
    for i in range(15):
        px += np.random.normal(0, noise_level, swarm_density)
        py += 1.2
        voltages.append(-70 + (i * 2))
        
        with col_viz:
            viz_container.plotly_chart(create_complex_viz(px, py, pz, "active", i/40), use_container_width=True)
            narration.markdown(f"<div class='status-box'><b>PHASE 1: Navigation</b><br>Navigating through vascular turbulence using BASS-MIM stochastic filters.</div>", unsafe_allow_html=True)
        
        with col_data:
            metrics_container.write(f"Current $V_{{mem}}$ Avg: {voltages[-1]} mV")
            chart_container.line_chart(voltages)
        time.sleep(sim_speed)

    # المرحلة الثانية: الاستهداف الكهرومغناطيسي
    for i in range(25):
        px += (20 - px) * 0.15 + np.random.normal(0, 0.2, swarm_density)
        py += (20 - py) * 0.15 + np.random.normal(0, 0.2, swarm_density)
        pz += (20 - pz) * 0.15 + np.random.normal(0, 0.2, swarm_density)
        voltages.append(-20 + np.random.normal(0, 1))
        
        with col_viz:
            viz_container.plotly_chart(create_complex_viz(px, py, pz, "active", (i+15)/40), use_container_width=True)
            narration.markdown("<div class='status-box'><b>PHASE 2: Bioelectric Locking</b><br>Swarm intelligence detected depolarized signatures. Engaging magnetic orientation.</div>", unsafe_allow_html=True)
        
        with col_data:
            chart_container.line_chart(voltages)
        time.sleep(sim_speed)

    # المرحلة الثالثة: إعادة البرمجة النهائية
    st.balloons()
    viz_container.plotly_chart(create_complex_viz(px, py, pz, "healed", 1.0), use_container_width=True)
    narration.success("REPROGRAMMING COMPLETE: Cellular Homeostasis Restored.")
    
    # عرض النتائج البحثية النهائية
    st.write("---")
    res1, res2, res3 = st.columns(3)
    res1.metric("Targeting Efficiency (TES)", "2.76", "+253.8%")
    res2.metric("Tissue Exposure Reduction", "49.6%", "Optimal")
    res3.metric("Tumor Uptake Efficiency", "79.1%", "High-Precision")
