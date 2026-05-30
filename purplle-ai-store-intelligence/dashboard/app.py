import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Purplle AI Store Intelligence",
    layout="wide"
)

st.title("🛍️ Purplle AI Store Intelligence")

store_id = st.text_input(
    "Store ID",
    "STORE_001"
)

if st.button("Load Analytics"):

    metrics = requests.get(
        f"http://127.0.0.1:8000/stores/{store_id}/metrics"
    ).json()

    funnel = requests.get(
        f"http://127.0.0.1:8000/stores/{store_id}/funnel"
    ).json()

    heatmap = requests.get(
        f"http://127.0.0.1:8000/stores/{store_id}/heatmap"
    ).json()

    anomalies = requests.get(
        f"http://127.0.0.1:8000/stores/{store_id}/anomalies"
    ).json()

    st.subheader("Store Metrics")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Unique Visitors",
            metrics["unique_visitors"]
        )

    with col2:
        st.metric(
            "Store ID",
            metrics["store_id"]
        )

    st.subheader("Funnel Analytics")

    funnel_df = pd.DataFrame({
        "Stage": [
            "Entry",
            "Zone Visit",
            "Billing Queue",
            "Purchase"
        ],
        "Count": [
            funnel["entry"],
            funnel["zone_visit"],
            funnel["billing_queue"],
            funnel["purchase"]
        ]
    })

    st.bar_chart(
        funnel_df.set_index("Stage")
    )

    st.subheader("Heatmap Analytics")

    if heatmap["zones"]:

        heatmap_df = pd.DataFrame(
            heatmap["zones"]
        )

        st.dataframe(
            heatmap_df,
            use_container_width=True
        )

    st.subheader("Anomalies")

    if anomalies["anomalies"]:
        st.warning(anomalies)
    else:
        st.success(
            "No anomalies detected"
        )