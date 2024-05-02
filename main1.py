import streamlit as st
from openpyxl import Workbook
import base64

def process_input(input_data):
    # Your backend processing code here
    # For demonstration purposes, let's just write the input data to an Excel file
    wb = Workbook()
    ws = wb.active
    ws.append(input_data)
    return wb

# Streamlit app
def main():
    st.title("Excel File Generator")

    # Input form
    st.subheader("Enter Data")
    patient_name = st.text_input("Patient Name")
    contact = st.text_input("Contact")
    address = st.text_input("Address")
    date = st.text_input("Date")

    input_data = [patient_name, contact, address, date]

    # Process input and generate Excel file
    if st.button("Generate Excel"):
        wb = process_input(input_data)

        # Save the Excel file
        excel_file = "output.xlsx"
        wb.save(excel_file)

        # Provide download link
        st.subheader("Download Excel File")
        excel_file_path = excel_file
        with open(excel_file_path, "rb") as f:
            file_content = f.read()
            file_content_base64 = base64.b64encode(file_content).decode("utf-8")
            href = f'<a href="data:application/octet-stream;base64,{file_content_base64}" download="{excel_file}">Click here to download</a>'
            st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
