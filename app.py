import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

# 1. إعدادات المسرح (Cinematic Stage)
st.set_page_config(page_title="JANA-SI: Virtual Lab", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #05070a; color: #e0e0e0; }
    .stMetric { background-color: #161b22; border-radius: 10px; padding: 15px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧬 JANA-SI: Full In-Silico Sequence")
st.write("---")

# القائمة الجانبية للتحكم الإبداعي
st.sidebar.header("🕹️ Simulation Engine")
mode = st.sidebar.radio("Select Phase:", ["1. Bioelectric Mapping", "2. Swarm Deployment", "3. Final Reprogramming"])
intensity = st.sidebar.slider("Bioelectric Signal Intensity", 0.0, 2.0, 1.2)

# مكان العرض الرئيسي
view_port = st.empty()

# دالة لرسم الورم بشكل "حقيقي" و "مبهر"
def draw_scene(px, py, pz, phase_color, tumor_opac, glow=False):
    fig = go.Figure()
    
    # رسم "الورم" بشكل خلية معقدة (Mesh3d)
    u = np.linspace(0, 2*np.pi, 30)
    v = np.linspace(0, np.pi, 30)
    tx = 20 + 7 * np.outer(np.cos(u), np.sin(v))
    ty = 20 + 7 * np.outer(np.sin(u), np.sin(v))
    tz = 20 + 7 * np.outer(np.ones(np.size(u)), np.cos(v))
    
    fig.add_trace(go.Surface(x=tx, y=ty, z=tz, colorscale='Reds', opacity=tumor_opac, showscale=False, name="Malignant Site"))

    # رسم الأسراب (الجسيمات) بألوان نيون متوهجة
    fig.add_trace(go.Scatter3d(
        x=px, y=py, z=pz, mode='markers',
        marker=dict(size=5, color=phase_color, symbol='diamond', 
                    line=dict(width=1, color='white'), opacity=0.9),
        name="JANA-SI MENPs"
    ))

    # إعدادات الكاميرا والبيئة السوداء
    fig.update_layout(
        scene=dict(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False,
                   bgcolor="#05070a", camera=dict(eye=dict(x=1.5, y=1.5, z=1.5))),
        margin=dict(l=0, r=0, b=0, t=0), paper_bgcolor="#05070a"
    )
    return fig

# تنفيذ المراحل الثلاث
if mode == "1. Bioelectric Mapping":
    st.subheader("🔍 Phase 1: Detecting Malignant Signatures")
    st.info("Searching for cells with V_mem ≈ -20mV...")
    # جسيمات تستكشف المكان بشكل عشوائي
    px, py, pz = np.random.uniform(0, 40, 60), np.random.uniform(0, 40, 60), np.random.uniform(0, 40, 60)
    view_port.plotly_chart(draw_scene(px, py, pz, 'cyan', 0.1), use_container_width=True)

elif mode == "2. Swarm Deployment":
    st.subheader("🚀 Phase 2: BASS-MIM Navigation Sequence")
    if st.button("Execute Swarm Jump"):
        px, py, pz = np.random.uniform(0, 10, 80), np.random.uniform(0, 10, 80), np.random.uniform(0, 10, 80)
        for i in range(25):
            px += (20 - px) * 0.15 + np.random.normal(0, 1, 80)
            py += (20 - py) * 0.15 + np.random.normal(0, 1, 80)
            pz += (20 - pz) * 0.15 + np.random.normal(0, 1, 80)
            view_port.plotly_chart(draw_scene(px, py, pz, 'gold', 0.2), use_container_width=True)
            time.sleep(0.05)
        st.success("Target Locked: Swarm localized at tumor site.")

elif mode == "3. Final Reprogramming":
    st.subheader("✨ Phase 3: Cellular Normalization (The Miracle)")
    # الجسيمات داخل الورم واللون يتحول للأخضر (دليل الشفاء)
    px, py, pz = np.random.normal(20, 3, 100), np.random.normal(20, 3, 100), np.random.normal(20, 3, 100)
    view_port.plotly_chart(draw_scene(px, py, pz, '#00ff00', 0.5), use_container_width=True)
    st.balloons()
    st.write("---")
    # عرض الأرقام القوية من بحثك
    col1, col2, col3 = st.columns(3)
    col1.metric("Targeting Score (TES)", "2.76", "+253.8%")
    col2.metric("Elimination Rate", "100%", "Absolute")
    col3.metric("Healthy Tissue Safety", "71.4%", "+49.6%")
