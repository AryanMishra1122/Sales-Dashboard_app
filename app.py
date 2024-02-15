import streamlit as st 
import pandas as pd
import plotly.express as px
import plotly
import numpy as  np
import cuufflinks as cf


# Function to load data from CSV file
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        st.error(f"An error occurred while loading the data: {str(e)}")
        return None

# Streamlit setup
st.set_page_config(page_title='Sales Dashboard')
st.title('Sales Dashboard')

# File path to your CSV file
file_path = "Sales data.csv"  # Replace this with the actual path to your CSV file

# Load data
df = load_data(file_path)

if df is not None:
    # Display DataFrame
    st.write("### Raw Data")
    st.dataframe(df)

    st.subheader('Data Selection')

    # Group by selection
    groupby_column = st.selectbox(
        'What would you like to analyze?',
        ('Product Category', 'Sub Category', 'Country', 'State', 'Year', 'Month')
    )

    if groupby_column:
        output_columns = ['Quantity', 'Revenue']
        df_grouped = df.groupby(by=[groupby_column], as_index=False)[output_columns].sum()
        st.dataframe(df_grouped)

        # Pie Chart
        st.subheader("Pie Chart")
        fig_pie = px.pie(
            df_grouped,
            values='Revenue',
            names=groupby_column,
            title=f'Distribution of Revenue by {groupby_column}',
            template='plotly_white'
        )
        st.plotly_chart(fig_pie)

        # Bar Chart
        st.subheader("Bar Chart")
        fig_bar = px.bar(
            df_grouped,
            x=groupby_column,
            y='Quantity',
            color='Revenue',
            color_continuous_scale=['red', 'yellow', 'green'],
            template='plotly_white'
        )
        st.plotly_chart(fig_bar)

        # Scatter Plot: Unit Cost vs Revenue
        st.subheader("Scatter Plot: Unit Cost vs Revenue")
        fig_scatter = px.scatter(
            df,
            x='Unit Cost',
            y='Revenue',
            title='Unit Cost vs Revenue',
            template='plotly_white'
        )
        st.plotly_chart(fig_scatter)

        # Line Chart: Revenue Over Time
        st.subheader("Line Chart: Revenue Over Time")
        df_monthly_revenue = df.groupby('Month')['Revenue'].sum().reset_index()
        fig_line = px.line(
            df_monthly_revenue,
            x='Month',
            y='Revenue',
            title='Monthly Revenue',
            template='plotly_white'
        )
        st.plotly_chart(fig_line)

