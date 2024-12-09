# =============================================================================
# LINEAR REGRESSION VISUALISATION
# =============================================================================

# DESCRIPTION
# This Python code creates a linear regression plot based on a study conducted
# by Powell et al. (2013). It visualises the correlation between smoking intensity 
# and lung cancer risk in men and women, as well as overall odds ratios (OR).
# The dataset contains odds ratio values (OR), along with their confidence intervals,
# for different smoking intensities: Never Smoked, Light/Trivial (1-9 cigarettes/d), 
# Moderate (10-19 cigarettes/d), and Heavy/Very Heavy (>20 cigarettes/d).
# The plot is faceted into three categories: Overall Odds Ratio, Men Odds Ratio,
# and Women Odds Ratio. Error bars represent the confidence intervals for each OR.
#
# PLEASE NOTE: THIS CODE IS FOR EDUCATIONAL PURPOSES ONLY! Partly synthetic data
# is used.
# Additional information is available in the README file.

# =============================================================================
# LIBRARIES
# =============================================================================
import pandas as pd
import plotly.express as px

# =============================================================================
# DATA IMPORT
# =============================================================================
# Load the data from the Excel file
df = pd.read_excel("/Users/fabiothon/Desktop/Code/Smoking/data.xlsx")
synthetic_df = pd.read_excel("/Users/fabiothon/Desktop/Code/Smoking/data.xlsx", 
                             sheet_name = "Synthetic data")

# =============================================================================
# DATA TRANSFORMATION
# =============================================================================
# Odds Ratio overall
df["or_lower"] = df["or"] - df["or_lower"]
df["or_upper"] = df["or_upper"] - df ["or"]

# =============================================================================
# VISUALISATION
# =============================================================================
fig_overall = px.scatter(
    df, 
    x = "number", 
    y = "or", 
    trendline = "ols",
    facet_col = "category",
    error_y_minus = "or_lower", 
    error_y = "or_upper",
    labels = {"number": "Smoking Intensity", "or": "Odds Ratio (OR)"},
    title = "Summary: Linear Regression of Smoking Intensity vs. Odds Ratio (OR)"
)
fig_overall.update_xaxes(dtick=1)
fig_overall.show()

fig_synthetic = px.scatter(
    synthetic_df, 
    x = "number", 
    y = "or", 
    trendline = "ols",
    color = "category",
    labels = {"number": "Smoking Intensity", "or": "Odds Ratio (OR)"},
    title = "Synthetic data: Linear Regression of Smoking Intensity vs. Odds Ratio (OR)"
)
fig_synthetic.update_xaxes(dtick=1)
fig_synthetic.show()