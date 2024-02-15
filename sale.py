import streamlit as st 
import pandas as pd
import numpy as np
import plotly.express as px



# Streamlit setup
st.set_page_config(page_title='Sales Dashboard')
st.title('Sales Dashboard')

st.sidebar.subheader('Description')
st.sidebar.write('The dataset contains information about sales transactions, including details such as the customer age, gender, location, and the products sold.')
st.sidebar.write('The dataset includes data on both the cost of the product and the revenue generated from its sale, allowing for calculations of profit and profit margins.')
st.sidebar.write('The quantity column provides information on the volume of products sold, which could be used to analyze sales trends over time.')
st.sidebar.write('The dataset includes information on customer age and gender, which could be used to analyze purchasing behavior across different demographic groups.')

df=pd.read_csv('Sales data.csv')

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

