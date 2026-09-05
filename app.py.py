import streamlit as st
import pandas as pd
from google import genai

# Page configuration
st.set_page_config(
    page_title="Retail Sales & Inventory Copilot",
    page_icon="🛍️",
    layout="wide"
)
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# Custom styling
st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(circle at 10% 10%, rgba(139,92,246,0.15), transparent 25%),
            radial-gradient(circle at 90% 15%, rgba(6,182,212,0.14), transparent 25%),
            radial-gradient(circle at 50% 90%, rgba(236,72,153,0.10), transparent 30%),
            #f8fafc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    .main-title {
        font-size: 44px;
        font-weight: 900;
        background: linear-gradient(
            90deg,
            #7c3aed,
            #2563eb,
            #06b6d4,
            #ec4899
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 19px;
        color: #64748b;
        margin-bottom: 12px;
        font-weight: 500;
    }

    h1, h2, h3 {
        font-weight: 800 !important;
        color: #172033;
    }

    div[data-testid="stMetric"] {
        background: rgba(255,255,255,0.9);
        padding: 22px;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 8px 25px rgba(15,23,42,0.08);
        transition: all 0.25s ease;
    }

    div[data-testid="stMetric"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 14px 35px rgba(124,58,237,0.18);
    }

    div[data-testid="stMetric"] label {
        color: #64748b !important;
        font-weight: 700 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #172033 !important;
        font-weight: 900 !important;
    }

    div[data-testid="stExpander"] {
        background: rgba(255,255,255,0.9);
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        box-shadow: 0 6px 20px rgba(15,23,42,0.06);
        margin-top: 12px;
        margin-bottom: 18px;
    }

    div[data-testid="stTextInput"] input {
        border-radius: 14px;
        border: 2px solid #e2e8f0;
        padding: 13px 16px;
        font-size: 16px;
    }

    div[data-testid="stTextInput"] input:focus {
        border-color: #8b5cf6;
        box-shadow: 0 0 0 3px rgba(139,92,246,0.15);
    }

    div[data-baseweb="select"] > div {
        border-radius: 12px;
        border: 1px solid #dbeafe;
    }

    div[data-testid="stAlert"] {
        border-radius: 16px;
        border: none;
        box-shadow: 0 5px 18px rgba(15,23,42,0.06);
    }

    div[data-testid="stDataFrame"] {
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 5px 18px rgba(15,23,42,0.06);
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #eef2ff 0%,
            #f5f3ff 45%,
            #ecfeff 100%
        );
        border-right: 1px solid #e0e7ff;
    }

    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #312e81 !important;
    }

    .stButton > button {
        border-radius: 12px;
        border: none;
        padding: 10px 20px;
        font-weight: 700;
        background: linear-gradient(
            90deg,
            #7c3aed,
            #2563eb
        );
        color: white;
        transition: all 0.25s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(124,58,237,0.25);
    }

    @media (max-width: 768px) {
        .main-title {
            font-size: 32px;
        }

        .subtitle {
            font-size: 16px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)




# Title
st.markdown(
    '<div class="main-title">🛍️ Retail Sales & Inventory Copilot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Smart sales analytics and inventory insights</div>',
    unsafe_allow_html=True
)

st.write("AI-powered assistant for sales and inventory management.")

# Load data
df = pd.read_csv("data/sales.csv")
inventory = pd.read_csv("data/inventory.csv")

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["Price"]
df["Date"] = pd.to_datetime(df["Date"])
# Filters
with st.sidebar:
    st.header("🎛️ Filters")

    st.subheader("📅 Date Filter")

    start_date = st.date_input(
        "Start Date",
        df["Date"].min().date()
    )

    end_date = st.date_input(
        "End Date",
        df["Date"].max().date()
    )

    st.subheader("🔎 Filters")

    selected_category = st.selectbox(
        "Select Category",
        ["All"] + list(df["Category"].unique())
    )

    selected_product = st.selectbox(
        "Select Product",
        ["All"] + list(df["Product"].unique())
    )

# Apply Filters
filtered_df = df.copy()
filtered_df = filtered_df[
    (filtered_df["Date"].dt.date >= start_date) &
    (filtered_df["Date"].dt.date <= end_date)
]

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]

if selected_product != "All":
    filtered_df = filtered_df[
        filtered_df["Product"] == selected_product
    ]

# Sales Data
with st.expander("📊 View Sales Data", expanded=False):
    st.dataframe(filtered_df, use_container_width=True)


st.markdown("## 📊 Sales Intelligence")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #eef2ff, #f5f3ff);
            padding: 18px;
            border-radius: 18px;
            border-left: 6px solid #7c3aed;
            margin-bottom: 10px;
        ">
            <h3 style="margin:0; color:#5b21b6;">
                📈 Product Performance
            </h3>
            <p style="margin:5px 0 0; color:#64748b;">
                Revenue generated by each product
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    product_sales = filtered_df.groupby("Product")["Revenue"].sum()

    st.bar_chart(
        product_sales,
        use_container_width=True
    )

with col2:
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #ecfeff, #eff6ff);
            padding: 18px;
            border-radius: 18px;
            border-left: 6px solid #0891b2;
            margin-bottom: 10px;
        ">
            <h3 style="margin:0; color:#0e7490;">
                📊 Category Performance
            </h3>
            <p style="margin:5px 0 0; color:#64748b;">
                Revenue contribution by category
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    category_sales = filtered_df.groupby("Category")["Revenue"].sum()

    st.bar_chart(
        category_sales,
        use_container_width=True
    )
st.markdown("## 🚨 Inventory Radar")
st.caption("AI-ready inventory health overview")

critical_stock = inventory[
    inventory["Stock"] <= inventory["Reorder_Level"] * 0.5
]

warning_stock = inventory[
    (inventory["Stock"] > inventory["Reorder_Level"] * 0.5) &
    (inventory["Stock"] <= inventory["Reorder_Level"])
]

    # Critical products
if not critical_stock.empty:
    st.markdown("### 🔴 Products Requiring Immediate Attention")
    st.dataframe(
        critical_stock,
        use_container_width=True
    )

elif not warning_stock.empty:
    st.success(
        "🟢 No critical stock detected. "
        "Some products are approaching their reorder level."
    )

else:
    st.success(
        "✅ Excellent! All products currently have healthy stock levels."
    )




# Inventory table
with st.expander("📦 View Complete Inventory", expanded=False):
    st.dataframe(
        inventory,
        use_container_width=True
    )

# Critical products
if not critical_stock.empty:

    st.markdown("### 🔴 Products Requiring Immediate Attention")

    st.dataframe(
        critical_stock,
        use_container_width=True
    )

elif not warning_stock.empty:

    st.success(
        "🟢 No critical stock detected. "
        "Some products are approaching their reorder level."
    )

else:

    st.success(
        "✅ Excellent! All products currently have healthy stock levels."
    )

# Low Stock Alert
st.subheader("🚨 Low Stock Alert")

low_stock = inventory[
    inventory["Stock"] <= inventory["Reorder_Level"]
]

st.markdown("## 📌 Business Pulse")

total_revenue = filtered_df["Revenue"].sum()
total_units = filtered_df["Quantity"].sum()
low_stock_count = len(low_stock)

if not filtered_df.empty:
    product_quantity = filtered_df.groupby("Product")["Quantity"].sum()
    best_product = product_quantity.idxmax()
else:
    best_product = "No Data"

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #ede9fe, #ddd6fe);
            padding: 22px;
            border-radius: 20px;
            box-shadow: 0 8px 20px rgba(124,58,237,0.15);
        ">
            <div style="font-size:16px;">💰 Total Revenue</div>
            <div style="font-size:30px; font-weight:800; color:#6d28d9;">
                ₹{total_revenue:,.0f}
            </div>
            <div style="color:#7c3aed;">Sales Performance</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #dbeafe, #bfdbfe);
            padding: 22px;
            border-radius: 20px;
            box-shadow: 0 8px 20px rgba(37,99,235,0.15);
        ">
            <div style="font-size:16px;">📦 Units Sold</div>
            <div style="font-size:30px; font-weight:800; color:#1d4ed8;">
                {total_units:,}
            </div>
            <div style="color:#2563eb;">Total Products Sold</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #ffedd5, #fed7aa);
            padding: 22px;
            border-radius: 20px;
            box-shadow: 0 8px 20px rgba(234,88,12,0.15);
        ">
            <div style="font-size:16px;">🚨 Low Stock</div>
            <div style="font-size:30px; font-weight:800; color:#ea580c;">
                {low_stock_count}
            </div>
            <div style="color:#c2410c;">Products Need Attention</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #dcfce7, #bbf7d0);
            padding: 22px;
            border-radius: 20px;
            box-shadow: 0 8px 20px rgba(22,163,74,0.15);
        ">
            <div style="font-size:16px;">🏆 Best Product</div>
            <div style="font-size:22px; font-weight:800; color:#15803d;">
                {best_product}
            </div>
            <div style="color:#16a34a;">Top Selling Product</div>
        </div>
        """,
        unsafe_allow_html=True
    )

if low_stock.empty:
    st.success("✅ All products have sufficient stock!")
else:
    st.warning(
        f"🚨 {len(low_stock)} product(s) need to be restocked."
    )

    with st.expander("📦 View Low Stock Products"):
        st.dataframe(
            low_stock,
            use_container_width=True
        )
        st.subheader("🏆 Best Selling Product")

if filtered_df.empty:
    st.warning("⚠️ No sales data available for the selected filters.")
else:
    product_quantity = filtered_df.groupby("Product")["Quantity"].sum()
    best_product = product_quantity.idxmax()
    best_quantity = product_quantity.max()

    st.success(
        f"🏆 **Top Selling Product:** {best_product}\n\n"
        f"📦 **{best_quantity} units sold**"
    )

# 🤖 RETAIL COPILOT
st.html("""
<div style="
    background: linear-gradient(135deg, #7c3aed, #2563eb, #0891b2);
    padding: 28px;
    border-radius: 24px;
    margin-top: 30px;
    margin-bottom: 20px;
    box-shadow: 0 12px 30px rgba(79,70,229,0.22);
">
    <div style="
        color: white;
        font-size: 32px;
        font-weight: 900;
    ">
        🤖 Retail Copilot
    </div>

    <div style="
        color: #e0f2fe;
        font-size: 17px;
        margin-top: 8px;
    ">
        Your AI-powered retail business assistant
    </div>

    <div style="
        display: inline-block;
        margin-top: 15px;
        padding: 7px 14px;
        border-radius: 20px;
        background: rgba(255,255,255,0.18);
        color: white;
        font-size: 14px;
        font-weight: 700;
    ">
        ● AI ANALYSIS ACTIVE
    </div>
</div>
""")

# Copilot Insights


if filtered_df.empty:

    st.warning("⚠️ No sales data available for the selected filters.")

else:

    copilot_product_sales = (
        filtered_df.groupby("Product")["Quantity"].sum()
    )

    copilot_best_product = copilot_product_sales.idxmax()
    copilot_best_quantity = copilot_product_sales.max()

    copilot_revenue = filtered_df["Revenue"].sum()
    copilot_units = filtered_df["Quantity"].sum()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(135deg, #ede9fe, #ddd6fe);
                padding: 20px;
                border-radius: 18px;
                border-left: 6px solid #7c3aed;
            ">
                <div style="font-size:15px; color:#6b21a8;">
                    🏆 Top Product
                </div>
                <div style="
                    font-size:22px;
                    font-weight:800;
                    color:#4c1d95;
                    margin-top:5px;
                ">
                    {copilot_best_product}
                </div>
                <div style="color:#7c3aed;">
                    {copilot_best_quantity} units sold
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(135deg, #dbeafe, #bfdbfe);
                padding: 20px;
                border-radius: 18px;
                border-left: 6px solid #2563eb;
            ">
                <div style="font-size:15px; color:#1d4ed8;">
                    💰 Revenue
                </div>
                <div style="
                    font-size:25px;
                    font-weight:800;
                    color:#1e3a8a;
                    margin-top:5px;
                ">
                    ₹{copilot_revenue:,.0f}
                </div>
                <div style="color:#2563eb;">
                    Selected period
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        if not low_stock.empty:

            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(135deg, #ffedd5, #fed7aa);
                    padding: 20px;
                    border-radius: 18px;
                    border-left: 6px solid #f97316;
                ">
                    <div style="font-size:15px; color:#c2410c;">
                        🚨 Restock Alert
                    </div>
                    <div style="
                        font-size:25px;
                        font-weight:800;
                        color:#9a3412;
                        margin-top:5px;
                    ">
                        {len(low_stock)}
                    </div>
                    <div style="color:#c2410c;">
                        Products need attention
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                """
                <div style="
                    background: linear-gradient(135deg, #dcfce7, #bbf7d0);
                    padding: 20px;
                    border-radius: 18px;
                    border-left: 6px solid #22c55e;
                ">
                    <div style="font-size:15px; color:#15803d;">
                        ✅ Inventory Status
                    </div>
                    <div style="
                        font-size:22px;
                        font-weight:800;
                        color:#166534;
                        margin-top:5px;
                    ">
                        Healthy
                    </div>
                    <div style="color:#15803d;">
                        No restock alerts
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # -------------------------------
    # Ask Retail Copilot
    # -------------------------------

    st.markdown("### 💬 Ask Retail Copilot")

    question = st.text_input(
        "Ask a question about your sales and inventory:",
        placeholder="Example: Which product is selling the most?"
    )

    if question:

        context = f"""
You are a Retail Sales & Inventory Copilot.

Sales summary:
- Total revenue: ₹{copilot_revenue:,.0f}
- Total units sold: {copilot_units}
- Best-selling product: {copilot_best_product}
- Best-selling quantity: {copilot_best_quantity}

Low-stock products:
{", ".join(low_stock["Product"].tolist()) if not low_stock.empty else "None"}

User question:
{question}

Answer clearly and briefly using only the provided sales and inventory information.
"""

        try:

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=context
            )

            st.markdown(
                """
                <div style="
                    background: linear-gradient(135deg, #f0f9ff, #eef2ff);
                    padding: 18px;
                    border-radius: 16px;
                    border-left: 5px solid #2563eb;
                    margin-top: 15px;
                ">
                    <div style="
                        font-size:16px;
                        font-weight:800;
                        color:#1e40af;
                        margin-bottom:8px;
                    ">
                        🤖 Gemini Copilot Response
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(response.text)

        except Exception as e:

            st.error(f"Gemini Error: {e}")
    
 
# Sales Prediction
st.subheader("🔮 Sales Prediction")
st.caption("Predict tomorrow's demand using recent sales trend")

daily_sales = (
    filtered_df.groupby("Date")["Quantity"]
    .sum()
    .reset_index()
)

if daily_sales.empty:

    st.warning("⚠️ No sales data available for prediction.")

else:

    last_7_days = daily_sales.tail(7)

    average_daily_sales = last_7_days["Quantity"].mean()
    predicted_sales = round(average_daily_sales)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Predicted Next day sales",f"{predicted_sales}units")
        
    with col2:
        st.metric("Average daily sales ",f"{round(average_daily_sales)}units")
    st.markdown("### 📈 Recent Sales Trend")

    st.line_chart(
        last_7_days.set_index("Date")["Quantity"]
    )

    st.info(
        f"💡 Based on the last 7 available days, "
        f"estimated next-day sales are **{predicted_sales} units**."
    )

    st.caption(
        "Prediction is based on the average sales of the last 7 available days."
    )

# Product Search
selected_product = st.selectbox(
    "Select a product",
    df["Product"].unique(),
    key="product_search"
)

product_data = df[df["Product"] == selected_product]

selected_revenue = product_data["Revenue"].sum()
selected_quantity = product_data["Quantity"].sum()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "📦 Units Sold",
        selected_quantity
    )

with col2:
    st.metric(
        "💰 Total Revenue",
        f"₹{selected_revenue:,.0f}"
    )

st.subheader("📋 Product Sales Details")

st.dataframe(
    product_data,
    use_container_width=True
)
