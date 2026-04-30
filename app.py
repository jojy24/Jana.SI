import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

# 1. إعدادات المسرح المظلم (High-End Laboratory UI)
st.set_page_config(page_title="JANA-SI | Digital Twin", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #000000; color: #00ffcc; }
    .stMetric { background-color: #0a0e14; border: 1px solid #00ffcc; border-radius: 15px; padding: 10px; }
    .stButton>button { width: 100%; border-radius: 50px; background: linear-gradient(90deg, #00ffcc, #0099ff); color: black; font-weight: bold; height: 3em; border: none; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ JANA-SI: Sovereign Digital Twin")
st.sidebar.title("🎮 Command Center")

# متغيرات تفاعلية
swarm_size = st.sidebar.slider("MENPs Swarm Density", 40, 150, 80)
intensity_val = st.sidebar.slider("Bioelectric Field Strength", 0.5, 2.0, 1.2)

# حاويات العرض الحية
view_port = st.empty()
status_msg = st.empty()

# دالة رسم المشهد السينمائي
def render_cinematic_frame(p_x, p_y, p_z, tumor_color, tumor_opac, stage_text):
    fig = go.Figure()

    # رسم الورم ككتلة بيولوجية متوهجة (Mesh3d Optimized)
    u, v = np.mgrid[0:2*np.pi:25j, 0:np.pi:15j]
    tx = 20 + 7 * np.cos(u) * np.sin(v)
    ty = 20 + 7 * np.sin(u) * np.sin(v)
    tz = 20 + 7 * np.cos(v)
    
    fig.add_trace(go.Mesh3d(
        x=tx.flatten(), y=ty.flatten(), z=tz.flatten(), 
        alphahull=0, color=tumor_color, opacity=tumor_opac,
        lighting=dict(ambient=0.5, diffuse=0.8, specular=1, roughness=0.1),
        name="Target Site"
    ))

    # رسم الأسراب (MENPs) كنقاط نيون ذهبية
    fig.add_trace(go.Scatter3d(
        x=p_x, y=p_y, p_z, mode='markers',
        marker=dict(size=4, color='#FFD700', symbol='diamond', 
                    line=dict(width=1, color='white'), opacity=0.8),
        name="BASS-MIM Swarm"
    ))

    fig.update_layout(
        scene=dict(
            xaxis_visible=False, yaxis_visible=False, zaxis_visible=False,
            bgcolor="black", camera=dict(eye=dict(x=1.5, y=1.5, z=1.2))
        ),
        margin=dict(l=0, r=0, b=0, t=0), paper_bgcolor="black", showlegend=False
    )
    return fig

# بدء الرحلة العلاجية (Full Clinical Sequence)
if st.sidebar.button("🚀 EXECUTE FULL SEQUENCE"):
    # المرحلة 1: الانتشار (Searching Phase)
    status_msg.info("📡 PHASE 1: Deploying MENPs... Scanning for $V_{mem} \\approx -20mV$")
    px, py, pz = np.random.uniform(0, 40, swarm_size), np.random.uniform(0, 5, swarm_size), np.random.uniform(0, 40, swarm_size)
    
    for i in range(12):
        py += 2.0 # حركة صعودية لمحاكاة الحقن
        view_port.plotly_chart(render_cinematic_frame(px, py, pz, 'red', 0.1, "Scanning"), use_container_width=True)
        time.sleep(0.05)

    # المرحلة 2: الهجوم (Swarm Convergence)
    status_msg.warning("🎯 PHASE 2: BASS-MIM Logic Engaged. Swarm converging on bioelectric signature.")
    for i in range(20):
        px += (20 - px) * 0.2 + np.random.normal(0, 0.7, swarm_size)
        py += (20 - py) * 0.2 + np.random.normal(0, 0.7, swarm_size)
        pz += (20 - pz) * 0.2 + np.random.normal(0, 0.7, swarm_size)
        view_port.plotly_chart(render_cinematic_frame(px, py, pz, '#ff4d4d', 0.3, "Targeting"), use_container_width=True)
        time.sleep(0.04)

    # المرحلة 3: الشفاء (The Miracle of Reprogramming)
    status_msg.success("✨ PHASE 3: Normalizing Cell Polarity. Reprogramming Paradigm Successful!")
    for i in range(8):
        # يتحول الورم تدريجياً للأخضر المضيء (دليل الشفاء)
        view_port.plotly_chart(render_cinematic_frame(px, py, pz, '#00ffcc', 0.6, "Healing"), use_container_width=True)
        time.sleep(0.1)
    
    st.balloons()

    # عرض الأرقام القوية من بحثك
    st.write("---")
    c1, c2, c3 = st.columns(3)
    c1.metric("Targeting Efficiency (TES)", "2.76", "+253.8%")
    c2.metric("Normalization Rate", "100%", "Absolute")
    c3.metric("Healthy Tissue Safety", "71.4%", "+49.6%")
    
    st.markdown("> **REPROGRAM. RESTORE. [span_5](start_span)[span_6](start_span)HEAL.** - JANA-SI Final Validation[span_5](end_span)[span_6](end_span).")

else:
    st.markdown("### 🖥️ System Ready. Waiting for Command...")
    st.write("اضغطي على الزر في القائمة الجانبية لتري 'مستقبل الطب' في عرض سينمائي كامل.")
