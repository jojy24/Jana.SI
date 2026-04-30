import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

# 1. إعدادات المسرح (Cinematic Dark UI)
st.set_page_config(page_title="JANA-SI | Digital Twin", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #000000; color: #00ffcc; }
    .stMetric { background-color: #0a0e14; border: 1px solid #00ffcc; border-radius: 15px; padding: 10px; }
    .stButton>button { width: 100%; border-radius: 50px; background: linear-gradient(90deg, #00ffcc, #0099ff); color: black; font-weight: bold; height: 3.5em; border: none; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ JANA-SI: The Bioelectric Reprogramming Journey")
st.sidebar.title("🎮 Command Center")

# متغيرات تحكم
swarm_density = st.sidebar.slider("MENPs Swarm Density", 50, 200, 100)

# حاويات العرض
view_port = st.empty()
status_msg = st.empty()

# دالة رسم المشهد (Corrected Order)
def render_frame(px, py, pz, tumor_color, tumor_opac, glow_size):
    fig = go.Figure()

    # رسم الورم (Target Site)
    u, v = np.mgrid[0:2*np.pi:25j, 0:np.pi:15j]
    tx = 20 + 7 * np.cos(u) * np.sin(v)
    ty = 20 + 7 * np.sin(u) * np.sin(v)
    tz = 20 + 7 * np.cos(v)
    
    fig.add_trace(go.Mesh3d(
        x=tx.flatten(), y=ty.flatten(), z=tz.flatten(), 
        color=tumor_color, 
        opacity=tumor_opac,
        alphahull=0,
        name="Malignant Core"
    ))

    # رسم الأسراب (MENPs)
    fig.add_trace(go.Scatter3d(
        x=px, y=py, z=pz,
        mode='markers',
        marker=dict(
            size=glow_size, 
            color='#FFD700', 
            symbol='diamond', 
            opacity=0.9,
            line=dict(width=1, color='white')
        ),
        name="Swarm Agents"
    ))

    fig.update_layout(
        scene=dict(
            xaxis_visible=False, yaxis_visible=False, zaxis_visible=False,
            bgcolor="black", camera=dict(eye=dict(x=1.6, y=1.6, z=1.2))
        ),
        margin=dict(l=0, r=0, b=0, t=0), paper_bgcolor="black", showlegend=False
    )
    return fig

# تسلسل العرض الكامل
if st.sidebar.button("🚀 INITIATE CLINICAL SEQUENCE"):
    # المرحلة 1: الانتشار والبحث
    status_msg.info("📡 PHASE 1: Deploying MENPs... Scanning for V_mem ≈ -20mV")
    px, py, pz = np.random.uniform(0, 40, swarm_density), np.random.uniform(0, 5, swarm_density), np.random.uniform(0, 40, swarm_density)
    for i in range(10):
        py += 2.0
        view_port.plotly_chart(render_frame(px, py, pz, 'red', 0.1, 3), use_container_width=True)
        time.sleep(0.05)

    # المرحلة 2: هجوم الأسراب (BASS-MIM)
    status_msg.warning("🎯 PHASE 2: BASS-MIM Logic Engaged. Locking onto Malignant Signatures...")
    for i in range(20):
        px += (20 - px) * 0.2 + np.random.normal(0, 0.8, swarm_density)
        py += (20 - py) * 0.2 + np.random.normal(0, 0.8, swarm_density)
        pz += (20 - pz) * 0.2 + np.random.normal(0, 0.8, swarm_density)
        view_port.plotly_chart(render_frame(px, py, pz, '#ff4d4d', 0.3, 5), use_container_width=True)
        time.sleep(0.04)

    # المرحلة 3: الشفاء (إعادة البرمجة)
    status_msg.success("✨ PHASE 3: Homeostasis Restored. Reprogramming Paradigm Successful!")
    for i in range(8):
        view_port.plotly_chart(render_frame(px, py, pz, '#00ffcc', 0.7, 7), use_container_width=True)
        time.sleep(0.1)
    
    st.balloons()
    
    # عرض النتائج من بحثك
    st.write("---")
    c1, c2, c3 = st.columns(3)
    c1.metric("Targeting Efficiency (TES)", "2.76", "+253.8%")
    c2.metric("Normalization Rate", "100%", "Absolute")
    c3.metric("Healthy Tissue Safety", "71.4%", "+49.6%")
    st.info("Results validated against Digital Cell Twins (A549 Model).")

else:
    st.markdown("### 🖥️ Waiting for Command...")
    st.write("اضغطي على الزر لبدء المحاكاة الكاملة.")
