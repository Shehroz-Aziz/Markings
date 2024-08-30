import streamlit as st
import pandas as pd
from io import BytesIO
import io

# Function to convert DataFrame to Excel file
def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    return output.getvalue()

# Streamlit app
def main():
    st.title('Student Data to Excel Exporter')

    # Input for raw CSV data
    st.write('Paste your data here:')
    raw_data = st.text_area('Input Data (CSV format)', height=300)

    if st.button('Generate Excel'):
        if raw_data:
            try:
                # Read the raw data into a DataFrame
                df = pd.read_csv(io.StringIO(raw_data))

                # Generate the Excel file
                excel_data = to_excel(df)

                # Provide the download link
                st.download_button(
                    label='Download Excel File',
                    data=excel_data,
                    file_name='student_data.xlsx',
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
            except Exception as e:
                st.error(f'Error processing data: {e}')
        else:
            st.error('Please enter some data to process.')

if __name__ == '__main__':
    main()
