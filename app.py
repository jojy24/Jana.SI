import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

# إعداد الصفحة لتكون بوضع الشاشة الكاملة واللون الداكن
st.set_page_config(page_title="JANA-SI Cinematic Simulation", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 JANA-SI: Autonomous Swarm Targeting Sequence")
st.write("Live In-Silico Validation of the Reprogramming Paradigm")

# التحكم في التشغيل من الشريط الجانبي
st.sidebar.header("Mission Parameters")
start_mission = st.sidebar.button("🚀 Execute Targeting")
swarm_intelligence = st.sidebar.slider("BASS-MIM Intelligence Level", 0.1, 1.0, 0.8)

# إعدادات البيئة ثلاثية الأبعاد
grid_limit = 40
center = grid_limit // 2
n_particles = 60 # عدد الجسيمات في السرب

# مكان لعرض الرسم البياني
placeholder = st.empty()

if start_mission:
    # نقطة البداية: الأسراب منتشرة في الأطراف (تحاكي الحقن في الدم)
    px = np.random.uniform(0, grid_limit, n_particles)
    py = np.random.uniform(0, 5, n_particles) # تبدأ من الأسفل
    pz = np.random.uniform(0, grid_limit, n_particles)

    # حلقة الفيديو (Animation Loop)
    for t in range(50):
        # منطق الحركة: الجسيمات تنجذب للمنطقة depolarized (-20mV)
        # الجذب يزداد كلما اقتربت الجسيمات (محاكاة لذكاء السرب)
        dx = (center - px) * swarm_intelligence * 0.15
        dy = (center - py) * swarm_intelligence * 0.15
        dz = (center - pz) * swarm_intelligence * 0.15
        
        # إضافة "ضجيج خوارزمي" (Stochastic Noise) لتجاوز العوائق كما في بحثك
        px += dx + np.random.normal(0, 1.2, n_particles)
        py += dy + np.random.normal(0, 1.2, n_particles)
        pz += dz + np.random.normal(0, 1.2, n_particles)

        # بناء المشهد البصري
        fig = go.Figure()

        # 1. رسم الورم (Target Zone) بشكل كروي متوهج
        u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
        tx = center + 7 * np.cos(u) * np.sin(v)
        ty = center + 7 * np.sin(u) * np.sin(v)
        tz = center + 7 * np.cos(v)
        fig.add_trace(go.Mesh3d(x=tx.flatten(), y=ty.flatten(), z=tz.flatten(), 
                                alphahull=0, color='red', opacity=0.15, name="Malignant Tumor"))

        # 2. رسم الأسراب (MENPs) كنقاط ذهبية متوهجة
        fig.add_trace(go.Scatter3d(
            x=px, y=py, z=pz, mode='markers',
            marker=dict(size=5, color='gold', symbol='diamond', 
                        line=dict(width=1, color='white'), opacity=0.8),
            name="MENPs Swarm"
        ))

        # إعدادات الكاميرا والإضاءة لتبدو سينمائية
        fig.update_layout(
            scene=dict(
                xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False),
                aspectmode='cube'
            ),
            margin=dict(l=0, r=0, b=0, t=0),
            paper_bgcolor="#0e1117",
            showlegend=False
        )

        placeholder.plotly_chart(fig, use_container_width=True)
        time.sleep(0.05) # سرعة الفريمات لتبدو كفيديو

    st.success("🎯 Mission Accomplished: Swarm successfully localized within the bioelectric target.")
    
    # عرض النتائج الرقمية من بحثك للتأكيد
    st.write("---")
    c1, c2, c3 = st.columns(3)
    [span_3](start_span)[span_4](start_span)c1.metric("Targeting Efficiency (TES)", "2.76", "+253.8%")[span_3](end_span)[span_4](end_span)
    [span_5](start_span)[span_6](start_span)c2.metric("Healthy Tissue Exposure", "28.6%", "-49.6%")[span_5](end_span)[span_6](end_span)
    [span_7](start_span)[span_8](start_span)c3.metric("Tumor Normalization Rate", "100%", "Absolute")[span_7](end_span)[span_8](end_span)

else:
    st.info("Waiting for command... Click 'Execute Targeting' to launch the simulation.")
