import streamlit as st
import pandas as pd
import plotly.express as px

# Load data (assuming CSV is available locally)
df = pd.read_csv("cleaned_growth_data.csv")

# Streamlit App Setup
st.set_page_config(page_title="Morocco Macro Tracker", layout="wide")
st.title("🇲🇦 Morocco Macro Tracker")
st.markdown("Track economic growth indicators in Morocco over the years.")

# Sidebar filters
indicators = df["Indicator"].unique()
default_value = indicators[0] if len(indicators) > 0 else None
selected_indicators = st.sidebar.multiselect(
    "Select Indicators",
    indicators,
    default=[default_value] if default_value else []
)

years = sorted(df["Year"].unique())
selected_years = st.sidebar.slider("Select Year Range", int(min(years)), int(max(years)), (int(min(years)), int(max(years))))

# Filtered data
filtered_df = df[(df["Indicator"].isin(selected_indicators)) &
                 (df["Year"] >= selected_years[0]) &
                 (df["Year"] <= selected_years[1])]

# Plotting
fig = px.line(filtered_df, x="Year", y="Growth Rate", color="Indicator", markers=True,
              title="Growth Rate Over Time")
fig.update_layout(legend_title_text='Indicator', height=600)

st.plotly_chart(fig, use_container_width=True)

# Summary stats
st.subheader("📊 Summary Statistics")
grouped = filtered_df.groupby("Indicator")["Growth Rate"]
summary_df = grouped.agg(["mean", "max", "min"]).reset_index()
st.dataframe(summary_df.style.format({"mean": "{:.2f}", "max": "{:.2f}", "min": "{:.2f}"}))

# Footer
st.markdown("---")
st.caption("Built by Zaineb · Master's in AI & Data Science")
