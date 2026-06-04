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

    # Store Metrics
    st.subheader("Store Metrics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Visitors",
            metrics["unique_visitors"]
        )

    with col2:
        st.metric(
            "Staff",
            metrics["staff_count"]
        )

    with col3:
        st.metric(
            "Purchases",
            metrics["purchase_count"]
        )

    with col4:
        st.metric(
            "Conversion %",
            metrics["conversion_rate"]
        )

    # Funnel Analytics
    st.subheader(
        f"Funnel Analytics (Conversion: {funnel['conversion_rate']}%)"
    )

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

    # Heatmap Analytics
    st.subheader("Heatmap Analytics")

    if heatmap["zones"]:

        heatmap_df = pd.DataFrame(
            heatmap["zones"]
        )

        st.bar_chart(
            heatmap_df.set_index("zone_id")
        )

        st.dataframe(
            heatmap_df,
            use_container_width=True
        )

    # Anomalies
    st.subheader("Anomalies")

    if anomalies["anomalies"]:

        for anomaly in anomalies["anomalies"]:

            st.warning(
                f"{anomaly['type']} : {anomaly['message']}"
            )

    else:

        st.success(
            "No anomalies detected"
        )