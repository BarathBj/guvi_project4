import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu


df = pd.read_csv("L:\GUVI_PYTHON\GUVI_CAPSTONE_PROJECTS\project_4\Airbnb.csv")

st.set_page_config(layout= "wide")
st.title("AIRBNB DATA ANALYSIS")
st.write("")

row1 = st.columns(2)
with row1[0]:
    sub_columns = st.columns(3)

    with sub_columns[0]:
        menu = option_menu("Menu", ["Home","Data-Analysis", "About"], 
                            icons=["house", "graph-up", "exclamation-triangle"],
                            menu_icon="cast",
                            default_index=0,
                            styles={"icon": {"color": "orange", "font-size": "30px"}}
                            )


if menu == 'Home':
     
    st.header("About Airbnb")
    st.write("")
    st.write('''***Airbnb is an online marketplace that connects people who want to rent out
              their property with people who are looking for accommodations,
              typically for short stays. Airbnb offers hosts a relatively easy way to
              earn some income from their property.Guests often find that Airbnb rentals
              are cheaper and homier than hotels.***''')
    st.write("")
    st.write('''***Airbnb Inc (Airbnb) operates an online platform for hospitality services.
                  The company provides a mobile application (app) that enables users to list,
                  discover, and book unique accommodations across the world.
                  The app allows hosts to list their properties for lease,
                  and enables guests to rent or lease on a short-term basis,
                  which includes vacation rentals, apartment rentals, homestays, castles,
                  tree houses and hotel rooms. The company has presence in China, India, Japan,
                  Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy,
                  Norway, Portugal, Russia, Spain, Sweden, the UK, and others.
                  Airbnb is headquartered in San Francisco, California, the US.***''')
    
    st.header("Background of Airbnb")
    st.write("")
    st.write('''***Airbnb was born in 2007 when two Hosts welcomed three guests to their
              San Francisco home, and has since grown to over 4 million Hosts who have
                welcomed over 1.5 billion guest arrivals in almost every country across the globe.***''')
    
    



if menu == 'Data-Analysis':
    st.markdown(f""" <style>.stApp {{
                background-size: cover}}
                </style>""",unsafe_allow_html=True)

    with row1[1]:
        analysis = st.selectbox("Exploratory Analysis of Airbnb Listing Data", ["Distribution of Listings by Country",
                                                                        "Price Variation by Selected Feature",
                                                                        "Frequency of Selected Feature",
                                                                        "Sum of Price and Beds by Number of Bedrooms",
                                                                        "Average Price by Cancellation Policy",
                                                                        "Sum of Price and Beds by Property Type",
                                                                        "Sum of Price and Guests Included by Cancellation Policy",
                                                                        "Sum of Price and Average Review Scores Rating by Number of Bathrooms"
                                                                        ])
    
    if analysis == "Distribution of Listings by Country":

        sub_columns = st.columns(2)

        with sub_columns[0]:

            country_counts = df['country'].value_counts().reset_index()
            country_counts.columns = ['country', 'count']

            fig = px.pie(country_counts, values='count', names='country', title='Country Distribution')
            fig.update_layout(title_x=0.3)
            st.plotly_chart(fig)
    

    if analysis == "Price Variation by Selected Feature":

        sub_columns = st.columns(2)

        with sub_columns[1]:
                    sub_columns_1 = st.columns(2)

                    with sub_columns_1[1]:
                        yaxis = st.selectbox("", ['price',
                                                  'security_deposit',
                                                  'cleaning_fee',
                                                  'extra_people_fee',
                                                ])

        with sub_columns[0]:
            fig = px.bar(df, x='country', y = yaxis, title=f"{yaxis} by Country")
            fig.update_layout(xaxis_title='Country', yaxis_title = yaxis , xaxis_tickangle=-45, title_x=0.35)
            st.plotly_chart(fig)

    if analysis == "Frequency of Selected Feature":

        sub_columns = st.columns(2)

        with sub_columns[1]:
                    sub_columns_1 = st.columns(2)

                    with sub_columns_1[1]:
                        yaxis = st.selectbox("", ['property_type',
                                                  "country",
                                                  "bed_type",
                                                ])

        with sub_columns[0]:
            property_type_counts = df[yaxis].value_counts().reset_index()
            property_type_counts.columns = [yaxis, 'count']

            fig = px.bar(property_type_counts, x='count', y=yaxis, title=f'Frequency of {yaxis}', orientation='h')
            fig.update_layout(xaxis_title='Frequency', yaxis_title= yaxis, xaxis_tickangle=-45, title_x=0.35)
            st.plotly_chart(fig)
    
    if analysis == "Sum of Price and Beds by Number of Bedrooms":

        agg_df = df.groupby('bedrooms').agg({'price': 'sum', 'beds': 'sum'}).reset_index()

        # Create a bar-line chart with Plotly Express
        fig = px.bar(agg_df, x='bedrooms', y='price', title='Sum of Price and Sum of Beds by Number of Bedrooms')
        fig.add_scatter(x=agg_df['bedrooms'], y=agg_df['beds'], mode='lines', name='Sum of Beds', yaxis='y2')

        # Update layout
        fig.update_layout(
            xaxis_title='Number of Bedrooms',
            yaxis=dict(title='Sum of Price', side='left', color='blue'),
            yaxis2=dict(title='Sum of Beds', side='right', overlaying='y', color='green')
        )
        st.plotly_chart(fig)
    
    if analysis == "Average Price by Cancellation Policy":
        avg_price_by_cancellation = df.groupby('cancellation_policy')['price'].mean().reset_index()
        bar_fig = px.bar(avg_price_by_cancellation, x='cancellation_policy', y='price', title='Average Price by Cancellation Policy')
        bar_fig.update_xaxes(title='Cancellation Policy')
        bar_fig.update_yaxes(title='Average Price')
        st.plotly_chart(bar_fig)
    
    if analysis == "Sum of Price and Beds by Property Type":
        # Aggregate the data by property type
        agg_property_df = df.groupby('property_type').agg({'price': 'sum', 'beds': 'sum'}).reset_index()

        # Create a bar-line chart for property type
        property_fig = px.bar(agg_property_df, x='property_type', y='price', title='Sum of Price and Sum of Beds by Property Type')
        property_fig.add_scatter(x=agg_property_df['property_type'], y=agg_property_df['beds'], mode='lines', name='Sum of Beds', yaxis='y2')

        # Update layout for property type
        property_fig.update_layout(
            xaxis_title='Property Type',
            yaxis=dict(title='Sum of Price', side='left', color='blue'),
            yaxis2=dict(title='Sum of Beds', side='right', overlaying='y', color='green')
        )
        st.plotly_chart(property_fig)

    if analysis == "Sum of Price and Guests Included by Cancellation Policy":
        # Aggregate the data by cancellation policy
        agg_cancel_df = df.groupby('cancellation_policy').agg({'price': 'sum', 'guests_included': 'sum'}).reset_index()

        # Create a bar-line chart for cancellation policy
        cancel_fig = px.bar(agg_cancel_df, x='cancellation_policy', y='price', title='Sum of Price and Sum of Guests Included by Cancellation Policy')
        cancel_fig.add_scatter(x=agg_cancel_df['cancellation_policy'], y=agg_cancel_df['guests_included'], mode='lines', name='Sum of Guests Included', yaxis='y2')

        # Update layout for cancellation policy
        cancel_fig.update_layout(
            xaxis_title='Cancellation Policy',
            yaxis=dict(title='Sum of Price', side='left', color='blue'),
            yaxis2=dict(title='Sum of Guests Included', side='right', overlaying='y', color='green')
        )
        st.plotly_chart(cancel_fig)

    if analysis == "Sum of Price and Average Review Scores Rating by Number of Bathrooms":
        # Aggregate the data by number of bathrooms
        agg_bathroom_df = df.groupby('bathrooms').agg({'price': 'sum', 'review_scores_rating': 'mean'}).reset_index()

        # Create a bar-line chart for number of bathrooms
        bathroom_fig = px.bar(agg_bathroom_df, x='bathrooms', y='price', title='Sum of Price and Average Review Scores Rating by Number of Bathrooms')
        bathroom_fig.add_scatter(x=agg_bathroom_df['bathrooms'], y=agg_bathroom_df['review_scores_rating'], mode='lines', name='Average Review Scores Rating', yaxis='y2')

        # Update layout for number of bathrooms
        bathroom_fig.update_layout(
            xaxis_title='Number of Bathrooms',
            yaxis=dict(title='Sum of Price', side='left', color='blue'),
            yaxis2=dict(title='Average Review Scores Rating', side='right', overlaying='y', color='green')
        )

        st.plotly_chart(bathroom_fig)






if menu == "About":

    st.markdown(f""" <style>.stApp {{ 
                    background-size: cover}}
                    </style>""",unsafe_allow_html=True)
    
    with row1[1]:
        
        st.header("ABOUT THIS PROJECT")

    st.subheader(":orange[1. Data Collection:]")

    st.write('''***Gather data from Airbnb's public API or other available sources.
        Collect information on listings, hosts, reviews, pricing, and location data.***''')
    
    st.subheader(":orange[2. Data Cleaning and Preprocessing:]")

    st.write('''***Clean and preprocess the data to handle missing values, outliers, and ensure data quality.
        Convert data types, handle duplicates, and standardize formats.***''')
    
    st.subheader(":orange[3. Exploratory Data Analysis (EDA):]")

    st.write('''***Conduct exploratory data analysis to understand the distribution and patterns in the data.
        Explore relationships between variables and identify potential insights.***''')
    
    st.subheader(":orange[4. Visualization:]")

    st.write('''***Create visualizations to represent key metrics and trends.
        Use charts, graphs, and maps to convey information effectively.
        Consider using tools like Matplotlib, Seaborn, or Plotly for visualizations.***''')
    
    st.subheader(":orange[5. Geospatial Analysis:]")

    st.write('''***Utilize geospatial analysis to understand the geographical distribution of listings.
        Map out popular areas, analyze neighborhood characteristics, and visualize pricing variations.***''')