import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CSV Data Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Preview
    st.subheader("Data Preview")
    st.dataframe(df.head())

    # Summary
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # Column selector
    column = st.selectbox("Choose a column to plot", df.columns)

    # Plot bar chart
    value_counts = df[column].value_counts()
    if column.lower() == 'survived' and 0 in value_counts.index and 1 in value_counts.index:
        value_counts.index = ['No', 'Yes']  # Optional relabeling

    st.subheader(f"Distribution of {column}")
    fig, ax = plt.subplots()
    value_counts.plot(kind='bar', ax=ax)
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    st.pyplot(fig)
