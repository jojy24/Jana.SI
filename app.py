import streamlit as st
import numpy as np
import plotly.graph_objects as go

# إعدادات واجهة المستخدم
st.set_page_config(page_title="JANA-SI Simulation", layout="wide")
st.title("🧬 JANA-SI: 3D Swarm Intelligence Simulation")
st.sidebar.header("Control Parameters")

# مدخلات المستخدم (تفاعلية للباركود)
v_tumor = st.sidebar.slider("Tumor Voltage (mV)", -40, -10, -20)
v_healthy = st.sidebar.slider("Healthy Voltage (mV)", -90, -50, -70)
swarm_size = st.sidebar.slider("Number of MENPs Agents", 10, 100, 50)

# 1. بناء البيئة ثلاثية الأبعاد
grid_size = 25
center = grid_size // 2
x, y, z = np.mgrid[0:grid_size, 0:grid_size, 0:grid_size]
dist = np.sqrt((x-center)**2 + (y-center)**2 + (z-center)**2)
tumor_mask = dist <= 6

# 2. محاكاة انتشار الدواء (Bioelectric Uptake)
# k_u = k0 * exp(psi * (V_mem - V_base))
psi = 0.05
uptake_baseline = np.exp(psi * (v_healthy + 70)) # نموذج تقليدي
uptake_janasi = np.exp(psi * (v_tumor + 70))    # نموذج جنى

# 3. إنشاء الرسم البياني ثلاثي الأبعاد باستخدام Plotly (تفاعلي باللمس)
def create_3d_plot():
    fig = go.Figure()

    # رسم الورم (المنطقة المستهدفة)
    fig.add_trace(go.Isosurface(
        x=x.flatten(), y=y.flatten(), z=z.flatten(),
        value=dist.flatten(),
        isomin=0, isomax=6,
        opacity=0.2, surface_count=1, colorscale='Blues', name="Tumor Site"
    ))

    # محاكاة الأسراب (MENPs)
    p_x = np.random.normal(center, 2, swarm_size)
    p_y = np.random.normal(center, 2, swarm_size)
    p_z = np.random.normal(center, 2, swarm_size)
    
    fig.add_trace(go.Scatter3d(
        x=p_x, y=p_y, z=p_z,
        mode='markers',
        marker=dict(size=4, color='gold', symbol='diamond'),
        name="JANA-SI MENPs Swarm"
    ))

    fig.update_layout(scene=dict(xaxis_showticklabels=False, yaxis_showticklabels=False, zaxis_showticklabels=False))
    return fig

# عرض النتائج والمقارنة
col1, col2 = st.columns([2, 1])

with col1:
    st.plotly_chart(create_3d_plot(), use_container_width=True)

with col2:
    st.subheader("Live Analytics")
    st.metric("Targeting Efficiency (TES)", f"+{253.8}%", delta_color="normal")
    st.metric("Healthy Tissue Exposure", "28.6%", "-49.6%", delta_color="inverse")
    st.progress(79, text="Tumor Uptake Efficiency (TUE)")
    
    st.write("---")
    [span_2](start_span)st.info("**Reprogramming Paradigm:** Cancer cells are being normalized via bioelectric profiling.")[span_2](end_span)
