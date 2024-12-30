summary_prompt = """
You are tasked with writing a short summary under 100 words for a website that would provide insights on the brand's online presence.
Brand Term: {brand_term}
Webpage Data:
{webpage_data}
"""

ctr_chart_prompt = """
Analyze the given CTR chart and provide insights such as trends, significant observations, and potential recommendations under 100 words.
The plot shows the Average Click-Through Rate (CTR) per Position group.
"""

click_variance_prompt = """
Analyze the given Click Variance chart and provide insights such as trends, significant observations, and potential recommendations under 100 words.
The plot shows the variance in the number of clicks on a monthly basis.
"""