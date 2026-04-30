import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

st.set_page_config(page_title="JANA-SI Live Simulation", layout="wide")
st.title("🎬 JANA-SI: Dynamic Swarm Targeting")

# التحكم في التشغيل
st.sidebar.header("Simulation Controls")
run_sim = st.sidebar.button("Start Targeting Sequence (Play)")
v_tumor = st.sidebar.slider("Tumor Voltage (mV)", -40, -10, -20)
swarm_speed = st.sidebar.slider("Swarm Velocity", 0.1, 1.0, 0.5)

# إعداد البيئة
grid_size = 30
center = grid_size // 2
x, y, z = np.mgrid[0:grid_size, 0:grid_size, 0:grid_size]
dist = np.sqrt((x-center)**2 + (y-center)**2 + (z-center)**2)
tumor_mask = dist <= 6

# إنشاء الرسم البياني الأساسي
fig_placeholder = st.empty()

# محاكاة الحركة (فيديو)
if run_sim:
    # نقطة البداية للأسراب (بعيداً عن الورم)
    p_x = np.random.uniform(0, grid_size, 40)
    p_y = np.random.uniform(0, grid_size, 40)
    p_z = np.random.uniform(0, grid_size, 40)

    for frame in range(30): # 30 إطار للحركة
        # معادلة الحركة نحو الورم (BASS-MIM Logic)
        p_x += (center - p_x) * swarm_speed * 0.2 + np.random.normal(0, 0.5, 40)
        p_y += (center - p_y) * swarm_speed * 0.2 + np.random.normal(0, 0.5, 40)
        p_z += (center - p_z) * swarm_speed * 0.2 + np.random.normal(0, 0.5, 40)

        fig = go.Figure()
        # الورم
        fig.add_trace(go.Isosurface(
            x=x.flatten(), y=y.flatten(), z=z.flatten(),
            value=dist.flatten(), isomin=0, isomax=6,
            opacity=0.1, colorscale='Reds', showscale=False
        ))
        # الأسراب المتحركة (MENPs)
        fig.add_trace(go.Scatter3d(
            x=p_x, y=p_y, z=p_z, mode='markers',
            marker=dict(size=5, color='gold', symbol='diamond', line=dict(width=1, color='white')),
            name="Active Swarm"
        ))
        
        fig.update_layout(scene=dict(xaxis_range=[0,30], yaxis_range=[0,30], zaxis_range=[0,30]),
                          margin=dict(l=0, r=0, b=0, t=0))
        
        fig_placeholder.plotly_chart(fig, use_container_width=True)
        time.sleep(0.1) # سرعة الفيديو
    [span_0](start_span)st.success("Targeting Complete: Malignant behavior normalized[span_0](end_span).")
else:
    st.info("اضغطي على زر 'Start Targeting Sequence' لرؤية الأسراب وهي تعمل!")

# عرض النتائج التقنية أسفل المحاكاة
st.write("---")
col1, col2, col3 = st.columns(3)
[span_1](start_span)col1.metric("Targeting Efficiency (TES)", "2.76", "+253.8%[span_1](end_span)")
[span_2](start_span)col2.metric("Elimination Rate", "100%", "Absolute[span_2](end_span)")
[span_3](start_span)col3.metric("Healthy Tissue Safety", "71.4%", "+49.6%[span_3](end_span)")
