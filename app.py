import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

# 1. تهيئة البيئة السينمائية (The Dark Theater)
st.set_page_config(page_title="JANA-SI | Digital Twin", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #000000; color: #00ffcc; }
    .stButton>button { width: 100%; border-radius: 20px; background: linear-gradient(45deg, #FFD700, #FF8C00); color: black; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ JANA-SI: The Reprogramming Journey")
st.sidebar.markdown("### 🛠️ Lab Console")

# متغيرات تحكم تفاعلية
swarm_density = st.sidebar.slider("MENPs Density", 50, 200, 120)
auto_rotate = st.sidebar.checkbox("Auto-Rotate Camera", True)

# حاويات العرض
view_port = st.empty()
status_text = st.empty()

# دالة بناء العالم (The 3D World)
def render_frame(p_coords, tumor_color, tumor_opac, glow_size, stage_name):
    fig = go.Figure()

    # رسم الورم ككتلة حيوية معقدة (Voxel-based)
    u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:20j]
    tx = 20 + 8 * np.cos(u) * np.sin(v)
    ty = 20 + 8 * np.sin(u) * np.sin(v)
    tz = 20 + 8 * np.cos(v)
    
    fig.add_trace(go.Mesh3d(x=tx.flatten(), y=ty.flatten(), z=tz.flatten(), 
                            alphahull=0, color=tumor_color, opacity=tumor_opac, 
                            name="Malignant Core", intensity=10))

    # رسم الأسراب الذهبية بتأثير النيون
    fig.add_trace(go.Scatter3d(
        x=p_coords[0], y=p_coords[1], z=p_coords[2],
        mode='markers',
        marker=dict(size=glow_size, color='#FFD700', symbol='diamond', 
                    line=dict(width=1, color='white'), opacity=0.9),
        name="MENPs Swarm"
    ))

    # إعدادات الإضاءة والكاميرا الاحترافية
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False),
            bgcolor="black",
            camera=dict(eye=dict(x=1.6, y=1.6, z=1.2)),
            aspectmode='cube'
        ),
        margin=dict(l=0, r=0, b=0, t=0),
        paper_bgcolor="black",
        showlegend=False
    )
    return fig

# بدء "الفيلم" التعليمي
if st.sidebar.button("🚀 Start Full Clinical Sequence"):
    # المرحلة 1: الحقن والانتشار (Scanning)
    status_text.warning("📡 PHASE 1: Systemic Injection & Bioelectric Mapping...")
    px, py, pz = np.random.uniform(0, 40, swarm_density), np.random.uniform(0, 5, swarm_density), np.random.uniform(0, 40, swarm_density)
    
    for i in range(15):
        px += np.random.normal(0, 1, swarm_density)
        py += 1.5 + np.random.normal(0, 0.5, swarm_density)
        view_port.plotly_chart(render_frame([px, py, pz], 'red', 0.1, 3, "Scanning"), use_container_width=True)
        time.sleep(0.05)

    # المرحلة 2: هجوم الأسراب (BASS-MIM Locking)
    status_text.error("🎯 PHASE 2: BASS-MIM Algorithm Engaged. Targeting Depolarized Cells (-20mV)...")
    for i in range(25):
        px += (20 - px) * 0.2 + np.random.normal(0, 0.8, swarm_density)
        py += (20 - py) * 0.2 + np.random.normal(0, 0.8, swarm_density)
        pz += (20 - pz) * 0.2 + np.random.normal(0, 0.8, swarm_density)
        view_port.plotly_chart(render_frame([px, py, pz], '#ff4b4b', 0.3, 5, "Targeting"), use_container_width=True)
        time.sleep(0.04)

    # المرحلة 3: إعادة البرمجة (Reprogramming Miracle)
    status_text.success("✨ PHASE 3: Normalizing Bioelectric Potential. Cellular Homeostasis Restored.")
    for i in range(10):
        # تأثير توهج أخضر عند الشفاء
        view_port.plotly_chart(render_frame([px, py, pz], '#00ff00', 0.6, 7, "Healing"), use_container_width=True)
        time.sleep(0.1)
    
    st.balloons()
    
    # عرض النتائج النهائية بشكل مبهر
    st.write("---")
    cols = st.columns(3)
    cols[0].metric("Targeting Efficiency", "2.76", "+253.8%")
    cols[1].metric("Healthy Tissue Safety", "71.4%", "+49.6%")
    cols[2].metric("Elimination Rate", "100%", "Absolute")
    
    st.markdown("### 📝 Researcher's Note:")
    st.info("JANA-SI successfully restored the 'Cognitive Glue' of the cell collective, moving from the Destruction Paradigm to the Reprogramming Paradigm.")

else:
    st.markdown("### ⬅️ Waiting for Execution Command")
    st.image("https://img.icons8.com/nolan/512/microscope.png", width=100)
    st.write("Click the button in the sidebar to run the full simulation sequence.")
