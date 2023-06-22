import streamlit as st
from edenred_to_zoho import html_file_to_csv
import pandas as pd

st.header("Convert Edenred Expense to CSV for Zoho")

input_html = st.text_area(label="Edenred expense html table")

if st.button(label="Process"):
    # process html to get csv
    data,skipped_rows = html_file_to_csv(input_html)

    # load the final csv into df
    df = pd.DataFrame(data=data)
    df.columns = ["Time", "Description", "Type", "Status", "Amount"]
    
    # Display skipped rows from the table
    st.write("Skipped rows")
    st.dataframe(pd.DataFrame(skipped_rows,columns=df.columns))
    
    # download button shown
    st.download_button(label="Download", data=df.to_csv(), file_name="zoho.csv")    
        

    