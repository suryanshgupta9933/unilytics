# Importing Dependencies
import streamlit as st

from src.utils import format_number
from src.countries import top_10_countries, global_traffic
from src.branded import detect_brand_term, branded_traffic
from src.charts import avg_ctr_by_position, click_variance

# Page Config
st.set_page_config(
    page_title="Unilytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.set_option('deprecation.showPyplotGlobalUse', False)

# Page Title
st.title("Unilytics")
st.markdown("Get insights on your brand's online presence with Unilytics")
st.markdown("---")

# Sidebar
st.sidebar.title("Upload Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["xlsx"])
upload_button = st.sidebar.button("Upload")

# Main Section
if uploaded_file and upload_button:
    st.markdown("### :blue[Insights Analysis]")
    with st.expander("Global Traffic", expanded=False):
        clicks, impressions = global_traffic(uploaded_file)
        st.markdown("#### Clicks: " + format_number(clicks))
        st.markdown("#### Impressions: " + format_number(impressions))
        st.markdown("#### CTR: " + str(round(clicks/impressions, 2) * 100) + "%")

    with st.expander("Top 10 Countries", expanded=False):
        top_10 = top_10_countries(uploaded_file)
        st.dataframe(top_10)

    with st.expander("Branded Traffic", expanded=False):
        brand_term = detect_brand_term(uploaded_file)
        clicks, impressions = branded_traffic(uploaded_file, brand_term)
        st.markdown("#### Clicks: " + format_number(clicks))
        st.markdown("#### Impressions: " + format_number(impressions))
        st.markdown("#### CTR: " + str(round(clicks/impressions, 2) * 100) + "%")

    with st.expander("Charts", expanded=False):
        st.markdown("#### Average CTR by Position")
        st.pyplot(fig=avg_ctr_by_position(uploaded_file))
        st.markdown("#### Click Variance")
        st.pyplot(fig=click_variance(uploaded_file))