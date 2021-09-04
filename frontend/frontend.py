import streamlit as st
import numpy as np
import pandas as pd
from markdown_predictions.trainer import get_test_data

def main():
    # Register your pages
    pages = {
        "CSV Uploader": page_1,
        "Markdown Selector": page_2,
        "Summary": page_3,
    }

    st.sidebar.title("Markdown Selection Tool")

    # Widget to select your page, you can choose between radio buttons or a selectbox
    page = st.sidebar.selectbox("Select your page", tuple(pages.keys()))
    #page = st.sidebar.radio("Select your page", tuple(pages.keys()))

    # Display the selected page with the session state
    pages[page]()

def page_1():
    file_csv = st.file_uploader("Upload your CSV here", type=([".csv"]))

    if file_csv:
        df = get_test_data(f'raw_data/{file_csv.name}')
        if "df" not in st.session_state:
            st.session_state.df = df
            st.session_state.df['markdown_PRE'] = 0.0
        st.session_state.df
        st.write('CSV Summary')
        num_products = len(df)
        st.write(f'Number of products: {num_products}')
        df['full_stock'] = df['avail_warehouse_stock_PRE'] + df['total_store_stock_PRE']
        stock = df['full_stock'].sum()
        st.write(f'Total stock: {stock}')
        st.write('Stock per target & category')
        # # TODO: Updte column names after get_data merge
        # target_stock = df.groupby(['Sous-cible','Catégorie'])['full_stock'].agg('sum')
        # target_stock
        target = st.number_input('Set unit sales target', min_value=0, max_value = 100, value=0)
        target_percent = target/100
        unit_target = float(stock) * target_percent
        st.write(f'Unit sales target: {round(unit_target)}')
        if st.button('Set Markdowns'):
            page_2()

def page_2():
    st.title("Under construction!")

def page_3():
    st.title("Also under construction!")

main()


# number = st.number_input('Choose a markdown', min_value=0, max_value = 50, step=10, value=0)
# st.write('The current number is ', number)
