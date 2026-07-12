# ==========================================================
# SALES FORECASTING DASHBOARD
# Retail Business Intelligence System
# ==========================================================

# -----------------------------
# Import Libraries
# -----------------------------
from streamlit_lottie import st_lottie
import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

/* ===========================================================
   IMPORT FONT
=========================================================== */

            
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

/* ===========================================================
   MAIN BACKGROUND
=========================================================== */

.stApp{

background:linear-gradient(-45deg,#0F172A,#1E293B,#111827,#0B1220);
background-size:400% 400%;
animation:gradientBG 18s ease infinite;

}

@keyframes gradientBG{

0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}

}

/* ===========================================================
   TEXT
=========================================================== */

h1,h2,h3,h4,h5,h6,p,label{

color:white;

}

/* ===========================================================
   FLOATING TITLE
=========================================================== */

@keyframes floatTitle{

0%{transform:translateY(0px);}
50%{transform:translateY(-7px);}
100%{transform:translateY(0px);}

}

.dashboard-title{

animation:floatTitle 4s ease-in-out infinite;

}

/* ===========================================================
   WELCOME CARD
=========================================================== */

.welcome-card{

background:rgba(37,99,235,.15);
padding:25px;
border-radius:18px;
border:1px solid rgba(255,255,255,.12);
backdrop-filter:blur(10px);

animation:fadeUp 1s;

box-shadow:0 8px 30px rgba(0,0,0,.25);

}

@keyframes fadeUp{

0%{
opacity:0;
transform:translateY(25px);
}

100%{
opacity:1;
transform:translateY(0px);
}

}

/* ===========================================================
   KPI CARDS
=========================================================== */

/* KPI Cards */

[data-testid="stMetric"]{

background:rgba(255,255,255,0.08);
backdrop-filter:blur(14px);

padding:18px;

border-radius:20px;

border:1px solid rgba(255,255,255,0.15);

box-shadow:
0 8px 25px rgba(0,0,0,.35),
0 0 18px rgba(59,130,246,.30);

transition:0.3s;

transform:translateY(-4px);
}

[data-testid="stMetric"]:hover{

transform:translateY(-8px) scale(1.02);

box-shadow:
0 10px 35px rgba(59,130,246,.45),
0 0 30px rgba(59,130,246,.45);

}

/* ===========================================================
   BUTTONS
=========================================================== */

.stButton>button{

background:#2563EB;
color:white;
border:none;
border-radius:10px;
padding:.55rem 1.4rem;
transition:.3s;

}

.stButton>button:hover{

background:#1D4ED8;

transform:scale(1.05);

box-shadow:0 0 18px rgba(37,99,235,.5);

}

/* ===========================================================
   SLIDER
=========================================================== */

.stSlider{

padding-top:8px;

}

/* ===========================================================
   SELECT BOX
=========================================================== */

div[data-baseweb="select"] > div{
    background:#1E293B !important;
    border:1px solid #3B82F6 !important;
    border-radius:10px !important;
    color:white !important;
}

div[data-baseweb="select"] span{
    color:white !important;
}

div[data-baseweb="select"] svg{
    fill:white !important;
}

/* Dropdown popup */
div[data-baseweb="popover"]{
    background:#1E293B !important;
}

div[data-baseweb="popover"] ul{
    background:#1E293B !important;
}

/* Dropdown options */
div[data-baseweb="popover"] li{
    background:#1E293B !important;
    color:white !important;
}

/* Hover */
div[data-baseweb="popover"] li:hover{
    background:#2563EB !important;
    color:white !important;
}

/* Selected option */
div[data-baseweb="popover"] li[aria-selected="true"]{
    background:#2563EB !important;
    color:white !important;
}   

/* ==========================================
   DROPDOWN OPTIONS
========================================== */

div[data-baseweb="popover"] ul{
    background:white !important;
}

div[data-baseweb="popover"] li{
    background:white !important;
    color:black !important;
}

div[data-baseweb="popover"] li:hover{
    background:#E5E7EB !important;
    color:black !important;
}

/* ===========================================================
   SIDEBAR
=========================================================== */

section[data-testid="stSidebar"]{

background:#020617;

border-right:1px solid rgba(255,255,255,.08);

}

section[data-testid="stSidebar"] label{

transition:.3s;

}

section[data-testid="stSidebar"] label:hover{

transform:translateX(8px);

}

/* ===========================================================
   DATAFRAME
=========================================================== */

[data-testid="stDataFrame"]{

border-radius:12px;

overflow:hidden;

}

/* ===========================================================
   FOOTER
=========================================================== */

footer{

visibility:hidden;

}

#MainMenu{

visibility:hidden;

}
/* ===========================
   FLOATING GLOW ORBS
=========================== */

.stApp::before{
content:"";
position:fixed;
width:250px;
height:250px;
border-radius:50%;
background:rgba(59,130,246,.18);
filter:blur(90px);
top:5%;
left:10%;
animation:float1 18s ease-in-out infinite;
z-index:-1;
}

.stApp::after{
content:"";
position:fixed;
width:300px;
height:300px;
border-radius:50%;
background:rgba(37,99,235,.15);
filter:blur(120px);
bottom:10%;
right:8%;
animation:float2 22s ease-in-out infinite;
z-index:-1;
}

@keyframes float1{

0%{
transform:translate(0,0);
}

50%{
transform:translate(120px,80px);
}

100%{
transform:translate(0,0);
}

}

@keyframes float2{

0%{
transform:translate(0,0);
}

50%{
transform:translate(-120px,-90px);
}

100%{
transform:translate(0,0);
}

}
            /* ===========================
   HOVER EFFECT
=========================== */

[data-testid="stMetric"]{

transition:0.35s;
border-radius:18px;

}

[data-testid="stMetric"]:hover{

transform:translateY(-8px) scale(1.03);

box-shadow:0 0 30px rgba(59,130,246,.45);

}
            /* ===========================
   PAGE FADE
=========================== */

.main{

animation:fadePage 1s ease;

}

@keyframes fadePage{

from{

opacity:0;

transform:translateY(30px);

}

to{

opacity:1;

transform:translateY(0);

}

}
            /* ==========================================
   KPI VALUE COLOR
========================================== */

[data-testid="stMetricValue"]{
    color: white !important;
    font-weight:700 !important;
}

[data-testid="stMetricLabel"]{
    color:#D1D5DB !important;
}

[data-testid="stMetricDelta"]{
    color:#22C55E !important;
}
/* ==========================================
   STREAMLIT HEADINGS
========================================== */

h1,
h2,
h3,
h4,
h5,
h6,
[data-testid="stHeading"]{
    color:white !important;
}

[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3{
    color:white !important;
}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():

    sales_df = pd.read_csv("processed_sales.csv")
    forecast_df = pd.read_csv("forecast_results.csv")
    segment_df = pd.read_csv("segment_forecast.csv")
    anomaly_df = pd.read_csv("anomaly_results.csv")
    cluster_df = pd.read_csv("cluster_results.csv")

    sales_df["Order Date"] = pd.to_datetime(sales_df["Order Date"])
    sales_df["Ship Date"] = pd.to_datetime(sales_df["Ship Date"])

    anomaly_df["Order Date"] = pd.to_datetime(
        anomaly_df["Order Date"]
    )

    return (
        sales_df,
        forecast_df,
        segment_df,
        anomaly_df,
        cluster_df
    )


(
sales_df,
forecast_df,
segment_df,
anomaly_df,
cluster_df
)=load_data()

# ==========================================================
# SIDEBAR
# ==========================================================

# ===========================
# Sidebar Logo
# ===========================

st.sidebar.image("logo.png", width=400)

st.sidebar.markdown("""
<div style="text-align:center;
font-size:15px;
font-weight:500;
color:white;
margin-top:-10px;
margin-bottom:20px;">
Predict • Analyze • Optimize
</div>
""", unsafe_allow_html=True)

st.sidebar.success(
"👈 Use this menu to navigate between all dashboard pages."
)

page = st.sidebar.radio(

"Navigation",

(

"📊 Sales Overview",

"📈 Forecast Explorer",

"🚨 Anomaly Report",

"📦 Product Demand Segments"

)

)

st.sidebar.markdown("---")

st.sidebar.info("""

### 👩‍💻 Developer

**Dharshiga Shree P**

Internship Project

2026

""")

# ==========================================================
# HEADER
# ==========================================================

st.title("📊 Sales Forecasting Dashboard")
st.caption("Retail Business Intelligence System")


# ==========================================================
# FOOTER FUNCTION
# ==========================================================

def footer():

    st.markdown("---")

    st.markdown("""

<center>

Sales Forecasting Dashboard 

</center>

""", unsafe_allow_html=True)

# ==========================================================
# PAGE 1 : SALES OVERVIEW
# ==========================================================

# ==========================================================
# PAGE 1 : SALES OVERVIEW
# ==========================================================

def sales_overview():

    st.header("📊 Sales Overview Dashboard")

    # ==========================================================
    # WELCOME PANEL
    # ==========================================================

    st.markdown("""
    <div style="
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(14px);
    padding:28px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,0.15);
    box-shadow:
    0 8px 25px rgba(0,0,0,.35),
    0 0 18px rgba(59,130,246,.30);
    margin-bottom:25px;
    ">

    <h2 style="color:white;margin-top:0;">
    👋 Welcome!
    </h2>

    <p style="color:#D1D5DB;font-size:18px;">
    This dashboard provides:
    </p>

    <div style="
    background:rgba(255,255,255,0.05);
    padding:15px;
    border-radius:12px;
    margin-bottom:20px;
    ">

    <ul style="color:white;font-size:17px;line-height:2;">
        <li>📊 Sales Overview</li>
        <li>📈 Sales Forecasting</li>
        <li>🚨 Anomaly Detection</li>
        <li>📦 Product Demand Segmentation</li>
    </ul>

    </div>

    <p style="
    color:#FFD166;
    font-size:17px;
    font-weight:600;
    margin-bottom:0;
    ">
    👉 Use the left sidebar to navigate through the dashboard pages.
    </p>

    </div>
    """, unsafe_allow_html=True)

    # -----------------------
    # KPI CARDS
    # -----------------------

    total_sales = sales_df["Sales"].sum()
    total_orders = sales_df["Order ID"].nunique()
    total_customers = sales_df["Customer ID"].nunique()
    avg_order = sales_df["Sales"].mean()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("💰 Total Sales", f"${total_sales/1_000_000:.2f}M")
    col2.metric("📦 Orders", total_orders)
    col3.metric("👥 Customers", total_customers)
    col4.metric("🛒 Avg Order Value", f"${avg_order:,.2f}")

    st.divider()

    # -----------------------
    # SALES CHARTS
    # -----------------------

    left, right = st.columns(2)

    with left:

        yearly_sales = sales_df.groupby("Year")["Sales"].sum()

        fig, ax = plt.subplots(figsize=(6,4))

        yearly_sales.plot(
            kind="bar",
            ax=ax
        )

        ax.set_title("Total Sales by Year")
        ax.set_xlabel("Year")
        ax.set_ylabel("Sales")

        st.pyplot(fig)
        plt.close(fig)

    with right:

    
        @st.cache_data
        def load_sales():
            df=pd.read_csv("sales.csv")
            df["Order Date"]=pd.to_datetime(df["Order Date"])
            return df

        monthly_sales = (
            sales_df
            .set_index("Order Date")
            .resample("ME")["Sales"]
            .sum()
        )

        fig, ax = plt.subplots(figsize=(6,4))

        ax.plot(
            monthly_sales.index,
            monthly_sales.values,
            linewidth=2
        )

        ax.set_title("Monthly Sales Trend")
        ax.set_xlabel("Date")
        ax.set_ylabel("Sales")

        st.pyplot(fig)
        plt.close(fig)

    st.divider()

    # -----------------------
    # FILTERS
    # -----------------------

    st.subheader("🔍 Interactive Filters")

    f1, f2 = st.columns(2)

    with f1:

        region = st.selectbox(
            "Select Region",
            ["All"] + sorted(sales_df["Region"].unique().tolist())
        )

    with f2:

        category = st.selectbox(
            "Select Category",
            ["All"] + sorted(sales_df["Category"].unique().tolist())
        )

    filtered_df = sales_df.copy()

    if region != "All":
        filtered_df = filtered_df[
            filtered_df["Region"] == region
        ]

    if category != "All":
        filtered_df = filtered_df[
            filtered_df["Category"] == category
        ]

    st.divider()

    # -----------------------
    # FILTERED CHARTS
    # -----------------------

    c1, c2 = st.columns(2)

    with c1:

        category_sales = (
            filtered_df
            .groupby("Category")["Sales"]
            .sum()
            .sort_values(ascending=False)
        )

        fig, ax = plt.subplots(figsize=(6,4))

        category_sales.plot(
            kind="bar",
            ax=ax
        )

        ax.set_title("Sales by Category")

        st.pyplot(fig)
        plt.close(fig)

    with c2:

        region_sales = (
            filtered_df
            .groupby("Region")["Sales"]
            .sum()
            .sort_values(ascending=False)
        )

        fig, ax = plt.subplots(figsize=(6,4))

        region_sales.plot(
            kind="bar",
            ax=ax
        )

        ax.set_title("Sales by Region")

        st.pyplot(fig)
        plt.close(fig)

    st.divider()

    # -----------------------
    # TABLE
    # -----------------------

    st.subheader("📋 Filtered Sales Records")

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

# ==========================================================
# PAGE 2
# Forecast Explorer
# ==========================================================

def forecast_explorer():

    st.title("📈 Forecast Explorer")

    st.markdown("---")

    st.write(
        "Explore future sales forecasts using the best-performing forecasting model (XGBoost)."
    )

    st.markdown("---")

    # ----------------------------
    # Controls
    # ----------------------------

    col1, col2 = st.columns(2)

    with col1:
        forecast_type = st.selectbox(
            "Forecast By",
            ["Overall Sales", "Category", "Region"]
        )

    with col2:
        horizon = st.slider(
            "Forecast Horizon (Months)",
            1,
            3,
            3
        )

    st.markdown("---")

    # =====================================================
    # OVERALL SALES
    # =====================================================

    if forecast_type == "Overall Sales":

        display_df = forecast_df.head(horizon)

        fig, ax = plt.subplots(figsize=(10,4))

        ax.plot(
            display_df["Month"],
            display_df["Forecast"],
            marker="o"
        )

        ax.set_title("Overall Sales Forecast")
        ax.set_xlabel("Forecast Month")
        ax.set_ylabel("Sales")

        st.pyplot(fig)
        plt.close(fig)

        st.dataframe(display_df, use_container_width=True)

        col1, col2 = st.columns(2)

        col1.metric(
            "MAE",
            f"{display_df['MAE'].iloc[0]:,.2f}"
        )

        col2.metric(
            "RMSE",
            f"{display_df['RMSE'].iloc[0]:,.2f}"
        )

    # =====================================================
    # CATEGORY FORECAST
    # =====================================================

    elif forecast_type == "Category":

        category = st.selectbox(
            "Select Category",
            [
                "Furniture",
                "Technology",
                "Office Supplies"
            ]
        )

        chart_df = segment_df[["Month", category]].head(horizon)

        fig, ax = plt.subplots(figsize=(10,4))

        ax.plot(
            chart_df["Month"],
            chart_df[category],
            marker="o"
        )

        ax.set_title(f"{category} Sales Forecast")
        ax.set_xlabel("Forecast Month")
        ax.set_ylabel("Sales")

        st.pyplot(fig)
        plt.close(fig)

        st.dataframe(chart_df, use_container_width=True)

        st.success("Forecast generated using XGBoost model.")

    # =====================================================
    # REGION FORECAST
    # =====================================================

    else:

        region = st.selectbox(
            "Select Region",
            [
                "West",
                "East"
            ]
        )

        chart_df = segment_df[["Month", region]].head(horizon)

        fig, ax = plt.subplots(figsize=(10,4))

        ax.plot(
            chart_df["Month"],
            chart_df[region],
            marker="o"
        )

        ax.set_title(f"{region} Region Forecast")
        ax.set_xlabel("Forecast Month")
        ax.set_ylabel("Sales")

        st.pyplot(fig)
        plt.close(fig)

        st.dataframe(chart_df, use_container_width=True)

        st.success("Forecast generated using XGBoost model.")


# ==========================================================
# PAGE 3
# ==========================================================

# ==========================================================
# PAGE 3
# Anomaly Report
# ==========================================================

def anomaly_report():

    st.title("🚨 Anomaly Detection Report")

    st.markdown("---")

    st.write(
        """
        This report displays anomalous sales periods detected using
        **Isolation Forest** and **Z-Score** techniques.
        """
    )

    # ---------------------------------------
    # Filter anomalies
    # ---------------------------------------

    anomalies = anomaly_df[
        (anomaly_df["Isolation_Anomaly"] == "Anomaly") |
        (anomaly_df["Z_Anomaly"] == "Anomaly")
    ]

    # ---------------------------------------
    # KPI Cards
    # ---------------------------------------

    col1, col2 = st.columns(2)

    isolation_count = (
        anomaly_df["Isolation_Anomaly"] == "Anomaly"
    ).sum()

    zscore_count = (
        anomaly_df["Z_Anomaly"] == "Anomaly"
    ).sum()

    col1.metric(
        "Isolation Forest Anomalies",
        isolation_count
    )

    col2.metric(
        "Z-Score Anomalies",
        zscore_count
    )

    st.markdown("---")

    # ---------------------------------------
    # Sales Trend with Anomalies
    # ---------------------------------------

    st.subheader("📈 Sales Trend with Detected Anomalies")

    fig, ax = plt.subplots(figsize=(12,5))

    # Weekly Sales Line
    ax.plot(
        anomaly_df["Order Date"],
        anomaly_df["Sales"],
        linewidth=2,
        label="Weekly Sales"
    )

    # Isolation Forest Points
    iso = anomaly_df[
        anomaly_df["Isolation_Anomaly"] == "Anomaly"
    ]

    ax.scatter(
        iso["Order Date"],
        iso["Sales"],
        s=80,
        marker="o",
        label="Isolation Forest"
    )

    # Z-Score Points
    z = anomaly_df[
        anomaly_df["Z_Anomaly"] == "Anomaly"
    ]

    ax.scatter(
        z["Order Date"],
        z["Sales"],
        s=90,
        marker="x",
        label="Z-Score"
    )

    ax.set_xlabel("Order Date")
    ax.set_ylabel("Sales")
    ax.set_title("Weekly Sales Anomaly Detection")

    ax.legend()

    st.pyplot(fig)
    plt.close(fig)

    st.markdown("---")

    # ---------------------------------------
    # Detected Anomaly Table
    # ---------------------------------------

    st.subheader("📋 Detected Anomaly Dates")

    st.dataframe(
        anomalies[
            [
                "Order Date",
                "Sales",
                "Isolation_Anomaly",
                "Z_Anomaly"
            ]
        ],
        use_container_width=True
    )

    st.markdown("---")

    # ---------------------------------------
    # Observation
    # ---------------------------------------

    st.subheader("📌 Observation")

    st.success(
        f"""
Isolation Forest detected **{isolation_count} anomalies**, while
Z-Score detected **{zscore_count} anomalies**.

Isolation Forest identifies a larger number of unusual sales patterns,
whereas the Z-Score method focuses on extreme deviations from the rolling mean.
"""
    )
# ==========================================================
# PAGE 4
# ==========================================================

# ==========================================================
# PAGE 4
# Product Demand Segments
# ==========================================================

def product_segments():

    st.title("📦 Product Demand Segmentation")

    st.markdown("---")

    st.write("""
    Products are segmented into demand groups using **K-Means Clustering**
    based on:

    • Total Sales

    • Sales Growth

    • Sales Volatility

    • Average Order Value
    """)

    st.markdown("---")

    # ----------------------------------------
    # Cluster Scatter Plot
    # ----------------------------------------

    st.subheader("📊 Product Demand Clusters")

    fig, ax = plt.subplots(figsize=(10,6))

    clusters = sorted(cluster_df["Cluster"].unique())

    for cluster in clusters:

        temp = cluster_df[
            cluster_df["Cluster"] == cluster
        ]

        ax.scatter(
            temp["PCA1"],
            temp["PCA2"],
            s=100,
            label=f"Cluster {cluster}"
        )

    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")
    ax.set_title("K-Means Product Demand Segmentation")

    ax.legend()

    st.pyplot(fig)
    plt.close(fig)

    st.markdown("---")

    # ----------------------------------------
    # Cluster Table
    # ----------------------------------------

    st.subheader("📋 Product Cluster Details")

    st.dataframe(
        cluster_df[
            [
                "Sub-Category",
                "Cluster",
                "Cluster Label",
                "Total Sales",
                "Sales Growth",
                "Sales Volatility",
                "Average Order Value"
            ]
        ],
        use_container_width=True
    )

    st.markdown("---")

    # ----------------------------------------
    # Cluster Summary
    # ----------------------------------------

    st.subheader("📈 Products in Each Cluster")

    summary = (
        cluster_df
        .groupby("Cluster Label")["Sub-Category"]
        .count()
        .reset_index()
    )

    summary.columns = [
        "Demand Segment",
        "Number of Sub-Categories"
    ]

    st.dataframe(
        summary,
        use_container_width=True
    )

    st.markdown("---")

    st.success("""
Recommended Stocking Strategy

• High Volume Stable Demand → Maintain high inventory.

• Growing Demand → Increase stock gradually.

• Low Volume High Volatility → Stock cautiously.

• Premium Products → Maintain limited but consistent inventory.
""")

# ==========================================================
# NAVIGATION
# ==========================================================

if page == "📊 Sales Overview":
    sales_overview()

elif page == "📈 Forecast Explorer":
    forecast_explorer()

elif page == "🚨 Anomaly Report":
    anomaly_report()

elif page == "📦 Product Demand Segments":
    product_segments()