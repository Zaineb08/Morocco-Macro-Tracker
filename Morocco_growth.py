"""
Morocco Macro Tracker - Interactive Dashboard
Visualizes key macroeconomic indicators in Morocco.
"""
import streamlit as st
import pandas as pd
import plotly.express as px

# ✅ This must be at the top and only once!
st.set_page_config(page_title="Morocco Macro Tracker", layout="wide")

# Load data with error handling
try:
    df = pd.read_csv("cleaned_growth_data.csv")
except FileNotFoundError:
    st.error(
        "❌ Error: cleaned_growth_data.csv file not found. "
        "Please ensure the data file is in the same directory as the script."
    )
    st.stop()
except pd.errors.EmptyDataError:
    st.error("❌ Error: The data file is empty.")
    st.stop()
except Exception as e:
    st.error(f"❌ Error loading data: {str(e)}")
    st.stop()

# Language selection
language = st.sidebar.selectbox("🌐 Choose language / Choisissez la langue", ["English", "Français"])

# Language-specific labels
if language == "English":
    st.title("Morocco Macro Tracker")
    st.markdown("Track economic growth indicators in Morocco over the years.")
    indicator_label = "Select Indicators"
    year_label = "Select Year Range"
    summary_title = "📊 Summary Statistics"
    footer_text = "Built with ❤️ by Zaineb · Student in Master's in AI & Data Science"
    chart_title = "Growth Rate Over Time"
    st.info("👈 Use the sidebar to select indicators and filter by year.")
else:
    st.title("Tableau de bord économique du Maroc")
    st.markdown("Suivez les indicateurs de croissance économique du Maroc au fil des années.")
    indicator_label = "Sélectionnez les indicateurs"
    year_label = "Sélectionnez la plage d'années"
    summary_title = "📊 Statistiques Résumées"
    footer_text = "Développé avec ❤️ par Zaineb · Etudiante en Master en IA et Data Science"
    chart_title = "Taux de croissance au fil du temps"
    st.info("👈 Utilisez la barre latérale pour sélectionner les indicateurs et filtrer par année.")

# Sidebar filters
indicators = df["Indicator"].unique()
default_value = indicators[0] if len(indicators) > 0 else None
selected_indicators = st.sidebar.multiselect(
    indicator_label,
    indicators,
    default=[default_value] if default_value else []
)

years = sorted(df["Year"].unique())
selected_years = st.sidebar.slider(
    year_label,
    int(min(years)), int(max(years)),
    (int(min(years)), int(max(years)))
)

# Filtered data
if not selected_indicators:
    st.warning(
        "⚠️ Please select at least one indicator from the sidebar "
        "to display the chart."
    )
    st.stop()

filtered_df = df[(df["Indicator"].isin(selected_indicators)) &
                 (df["Year"] >= selected_years[0]) &
                 (df["Year"] <= selected_years[1])]

# Plotting
fig = px.line(filtered_df, x="Year", y="Growth Rate", color="Indicator", markers=True,
              title=chart_title)
fig.update_layout(legend_title_text='Indicator', height=600)
fig.update_xaxes(dtick=1)

st.plotly_chart(fig, use_container_width=True)

# Summary stats
st.subheader(summary_title)
grouped = filtered_df.groupby("Indicator")["Growth Rate"]
summary_df = grouped.agg(["mean", "max", "min"]).reset_index()
st.dataframe(summary_df.style.format({"mean": "{:.2f}", "max": "{:.2f}", "min": "{:.2f}"}))

# Footer
st.markdown("---")
st.caption(footer_text)
