import streamlit as st
import pandas as pd
from model_loader import load_model

st.set_page_config(
    page_title="Smart Energy Consumption Prediction",
    page_icon="⚡",
    layout="wide"
)

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500;700&display=swap');

:root {
    --bg-surface: #FFFFFF;
    --bg-surface-2: #EEF1EF;
    --accent-teal: #0F7A5F;
    --accent-teal-soft: #E7F0EC;
    --accent-amber: #B4790A;
    --text-primary: #1C2321;
    --text-muted: #626C68;
    --border-soft: #DCE1DE;
}

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.stApp {
    background-color: #EFF2F0;
    color: var(--text-primary);
}

#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { background: transparent; }
header [data-testid="stToolbar"] { visibility: hidden; }
[data-testid="collapsedControl"] {
    visibility: visible !important;
    display: flex !important;
    opacity: 1 !important;
}
[data-testid="stSidebarCollapseButton"] {
    visibility: visible !important;
    display: flex !important;
}

/* ---------- Hero ---------- */
.hero-wrap {
    padding: 1.8rem 2.2rem 1.6rem 2.2rem;
    border-radius: 10px;
    background-color: #FFFFFF;
    border: 1px solid var(--border-soft);
    border-left: 4px solid var(--accent-teal);
    margin-bottom: 1.5rem;
}
.hero-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    font-size: 0.72rem;
    color: var(--accent-teal);
    margin-bottom: 0.55rem;
}
.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 2.05rem;
    margin: 0 0 0.45rem 0;
    color: var(--text-primary);
}
.hero-sub {
    color: var(--text-muted);
    font-size: 0.97rem;
    max-width: 680px;
    line-height: 1.55;
}

/* ---------- Section cards ---------- */
.section-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-soft);
    border-radius: 10px;
    padding: 1.3rem 1.4rem 0.3rem 1.4rem;
    margin-bottom: 1.1rem;
}
.section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.0rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 0.3rem;
}
.section-caption {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: var(--text-muted);
    letter-spacing: 0.04em;
    margin-bottom: 0.9rem;
}

/* ---------- Inputs ---------- */
div[data-testid="stNumberInput"] label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.76rem;
    color: var(--text-muted);
}
div[data-testid="stNumberInput"] input {
    background-color: var(--bg-surface-2) !important;
    border: 1px solid var(--border-soft) !important;
    color: var(--text-primary) !important;
    border-radius: 8px !important;
}

/* ---------- Tabs ---------- */
button[data-baseweb="tab"] {
    font-family: 'Space Grotesk', sans-serif;
    color: var(--text-muted);
}
button[data-baseweb="tab"][aria-selected="true"] { color: var(--accent-teal) !important; }
div[data-baseweb="tab-highlight"] { background-color: var(--accent-teal) !important; }
div[data-baseweb="tab-border"] { background-color: var(--border-soft) !important; }

/* ---------- Buttons ---------- */
.stButton button {
    background-color: var(--accent-teal);
    color: #FFFFFF;
    font-weight: 600;
    border: none;
    border-radius: 8px;
    padding: 0.55rem 1.5rem;
    transition: background-color 0.15s ease;
}
.stButton button:hover {
    background-color: #0C6B53;
}

/* ---------- Meter readout ---------- */
.meter-card {
    background-color: var(--accent-teal-soft);
    border: 1px solid var(--border-soft);
    border-left: 4px solid var(--accent-teal);
    border-radius: 10px;
    padding: 1.6rem 2rem;
    text-align: center;
    margin-top: 0.9rem;
}
.meter-label {
    font-family: 'JetBrains Mono', monospace;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-size: 0.74rem;
    color: var(--text-muted);
    margin-bottom: 0.5rem;
}
.meter-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2.7rem;
    font-weight: 700;
    color: var(--accent-teal);
    line-height: 1.1;
}
.meter-unit {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.05rem;
    color: var(--text-muted);
}

/* ---------- Misc badges ---------- */
.badge-row { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.8rem; }
.badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: var(--text-muted);
    background: var(--bg-surface-2);
    border: 1px solid var(--border-soft);
    border-radius: 999px;
    padding: 0.28rem 0.7rem;
}

/* ---------- Sidebar ---------- */
section[data-testid="stSidebar"] {
    background-color: #E7EBE8;
    border-right: 1px solid var(--border-soft);
}
section[data-testid="stSidebar"] .block-container { padding-top: 1.6rem; }
.sidebar-title {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 600;
    font-size: 1.0rem;
    color: var(--text-primary);
    margin-bottom: 0.3rem;
}
.sidebar-item {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.76rem;
    color: var(--text-muted);
    display: flex;
    justify-content: space-between;
    padding: 0.35rem 0;
    border-bottom: 1px dashed var(--border-soft);
}
.sidebar-item span:last-child { color: var(--text-primary); font-weight: 600; }

/* Dataframe corners */
div[data-testid="stDataFrame"] { border-radius: 12px; overflow: hidden; }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

model = load_model()

feature_names = [
    "lights",
    "T1", "RH_1", "T2", "RH_2", "T3", "RH_3", "T4", "RH_4",
    "T5", "RH_5", "T6", "RH_6", "T7", "RH_7", "T8", "RH_8", "T9", "RH_9",
    "T_out", "Press_mm_hg", "RH_out", "Windspeed", "Visibility", "Tdewpoint",
    "Year", "Month", "Day", "Hour", "Minute", "DayOfWeek", "IsWeekend"
]

ZONE_LABELS = {
    "T1": "Kitchen", "T2": "Living Room", "T3": "Laundry Room",
    "T4": "Office", "T5": "Bathroom", "T6": "Outside (North)",
    "T7": "Ironing Room", "T8": "Teenager Room", "T9": "Parents Room",
}

with st.sidebar:
    st.markdown('<div class="sidebar-title">About this model</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sidebar-item"><span>Algorithm</span><span>Lasso Regression</span></div>'
        '<div class="sidebar-item"><span>Task</span><span>Regression</span></div>'
        '<div class="sidebar-item"><span>Target</span><span>Appliances (Wh)</span></div>'
        '<div class="sidebar-item"><span>Input features</span><span>32</span></div>'
        '<div class="sidebar-item"><span>Dataset</span><span>Appliance Energy</span></div>',
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.caption(
        "Trained on sensor readings from 9 indoor zones plus outdoor "
        "weather data to estimate whole-home appliance energy draw."
    )

st.markdown(
    """
    <div class="hero-wrap">
        <div class="hero-eyebrow">Household Energy Intelligence</div>
        <div class="hero-title">Smart Energy Consumption Prediction</div>
        <div class="hero-sub">
            Estimate whole-home appliance energy draw from live indoor climate,
            outdoor weather, and time-of-day signals — enter readings manually
            for a single estimate, or upload a batch file to score many records at once.
        </div>
        <div class="badge-row">
            <div class="badge">MODEL: LASSO REGRESSION</div>
            <div class="badge">UNIT: WATT-HOURS (Wh)</div>
            <div class="badge">FEATURES: 32</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

tab_manual, tab_upload = st.tabs(["Manual Input", "Upload CSV / Excel"])

with tab_manual:

    user_input = {}
    st.info(
    "Complete all four sections before making a prediction. "
    "The model uses all 32 features together to predict appliance energy consumption."
)

    sub_lighting, sub_zones, sub_weather, sub_time = st.tabs(
        ["Lighting", "Zone Climate", "Outdoor Weather", "Time"]
    )

    with sub_lighting:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Lighting Load</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-caption">ENERGY USE FROM LIGHT FIXTURES (Wh)</div>', unsafe_allow_html=True)
        user_input["lights"] = st.number_input("lights", value=0.0, key="lights")
        st.markdown('</div>', unsafe_allow_html=True)

    with sub_zones:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Indoor Zone Readings</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-caption">TEMPERATURE (°C) &amp; RELATIVE HUMIDITY (%) PER ZONE</div>', unsafe_allow_html=True)

        for i in range(1, 10):
            t_key, rh_key = f"T{i}", f"RH_{i}"
            zone_name = ZONE_LABELS.get(t_key, f"Zone {i}")
            col_label, col_t, col_rh = st.columns([1.2, 1, 1])
            with col_label:
                st.markdown(f"<div style='padding-top:1.9rem; color:#E8EDF4; font-weight:500;'>{zone_name}</div>", unsafe_allow_html=True)
            with col_t:
                user_input[t_key] = st.number_input(t_key, value=0.0, key=t_key)
            with col_rh:
                user_input[rh_key] = st.number_input(rh_key, value=0.0, key=rh_key)
        st.markdown('</div>', unsafe_allow_html=True)

    with sub_weather:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Outdoor Weather Conditions</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-caption">STATION READINGS AT PREDICTION TIME</div>', unsafe_allow_html=True)
        weather_features = ["T_out", "Press_mm_hg", "RH_out", "Windspeed", "Visibility", "Tdewpoint"]
        cols = st.columns(3)
        for idx, feature in enumerate(weather_features):
            with cols[idx % 3]:
                user_input[feature] = st.number_input(feature, value=0.0, key=feature)
        st.markdown('</div>', unsafe_allow_html=True)

    with sub_time:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Time Context</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-caption">WHEN THE READING WAS TAKEN</div>', unsafe_allow_html=True)
        time_features = ["Year", "Month", "Day", "Hour", "Minute", "DayOfWeek", "IsWeekend"]
        cols = st.columns(4)
        for idx, feature in enumerate(time_features):
            with cols[idx % 4]:
                user_input[feature] = st.number_input(feature, value=0.0, key=feature)
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    predict_col, _ = st.columns([1, 3])
    with predict_col:
        run_prediction = st.button("Predict Energy Consumption", type="primary", use_container_width=True)

    if run_prediction:

        input_df = pd.DataFrame([user_input], columns=feature_names)
        prediction = model.predict(input_df)

        st.markdown(
            f"""
            <div class="meter-card">
                <div class="meter-label">Predicted Appliance Energy Consumption</div>
                <div class="meter-value">{prediction[0]:.2f} <span class="meter-unit">Wh</span></div>
            </div>
            """,
            unsafe_allow_html=True
        )

with tab_upload:

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Batch Prediction</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-caption">UPLOAD A CSV OR EXCEL FILE CONTAINING THE 32 REQUIRED FEATURES</div>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Choose a CSV or Excel file",
        type=["csv", "xlsx"],
        label_visibility="collapsed"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    if uploaded_file is not None:

        try:

            if uploaded_file.name.lower().endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.lower().endswith(".xlsx"):
                df = pd.read_excel(uploaded_file)
            else:
                st.error("Unsupported file format.")
                st.stop()

            st.success(f"File uploaded successfully: {uploaded_file.name}")

            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">Uploaded Data</div>', unsafe_allow_html=True)
            st.dataframe(df, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

            missing_columns = [c for c in feature_names if c not in df.columns]

            if missing_columns:
                st.error("The uploaded file is missing the following required columns:")
                st.write(missing_columns)

            else:
                st.success("All 32 required features are present.")

                input_data = df[feature_names]

                st.divider()

                predict_col, _ = st.columns([1, 3])
                with predict_col:
                    run_batch = st.button("Generate Predictions", type="primary", use_container_width=True)

                if run_batch:

                    predictions = model.predict(input_data)

                    result_df = df.copy()
                    result_df["Predicted_Appliances"] = predictions

                    st.markdown(
                        f"""
                        <div class="meter-card">
                            <div class="meter-label">Batch Predictions Generated</div>
                            <div class="meter-value">{len(predictions)} <span class="meter-unit">records</span></div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.markdown('<div class="section-card">', unsafe_allow_html=True)
                    st.markdown('<div class="section-title">Prediction Results</div>', unsafe_allow_html=True)
                    st.dataframe(result_df, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                    csv_data = result_df.to_csv(index=False).encode("utf-8")

                    st.download_button(
                        label="⬇Download Predictions",
                        data=csv_data,
                        file_name="energy_predictions.csv",
                        mime="text/csv"
                    )

        except Exception as e:
            st.error(f"An error occurred while processing the file: {e}")