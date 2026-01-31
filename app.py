# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""

import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "STEM Data Explorer", "Contact"],
)

# Dummy STEM data
enzyme_kinetics_data = pd.DataFrame({
    "Enzyme": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
    "Substrate Concentration (mM)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Reaction rate (µmol/min)": pd.date_range(start="2024-01-01", periods=5),
})

protein_character_data = pd.DataFrame({
    "Protein": ["Hemoglobin", "Albumin", "Insulin", "Keratin", "Collagen"],
    "Molecular Weight (kDa)": [64.5, 66.5, 5.8, 54.0, 300.0],
    "Isoelectric Point (pI)": [6.8, 4.7, 5.3, 7.0, 6.5],
})

bacterial_growth_data = pd.DataFrame({
    "Time (hours)": [0, 2, 4, 6, 8],
    "Optical Density (OD600)": [0.05, 0.18, 0.52, 0.89, 1.10],
    "Temperature (°C)": [37, 37, 37, 37, 37]
})

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")
    col1, col2 = st.columns([1,2])
    # Collect basic information
    name = "Damien Ferreira"
    field = "Biochemistry"
    institution = "North-West University"

    # Display basic profile information
    with col1:
        st.write(f"**Name:** {name}")
        st.write(f"**Institution:** {institution}")
        st.write(f"**Field of Research:** {field}")
        st.write("""
        I am a biochemistry student with a strong interest in molecular biology,
        enzyme kinetics, and microbial physiology. 
        """)
        
    with col2:
        st.image(
            "Sunset (2).jpg",
            caption="Sunset (Damien Ferreira)", 
            use_column_width=True
    )

elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")

    # Upload publications file
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")

elif menu == "STEM Data Explorer":
    st.title("STEM Data Explorer")
    st.sidebar.header("Data Selection")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore", 
        ["Enzyme Kinetics", "Protein Characterization", "Bacterial Growt Data"]
    )

    if data_option == "Enzyme Kinetics":
        st.write("### Enzyme Kinetics Data")
        st.dataframe(enzyme_kinetics_data)
        # Add widget to filter by Energy levels
        rate_filter = st.slider("Filter by Reaction Rate (µmol/min)", 
                                
        float(enzyme_kinetics_data["Reaction Rate (µmol/min)"].min()),
        float(enzyme_kinetics_data["Reaction Rate (µmol/min)"].max()),
        (
            float(enzyme_kinetics_data["Reaction Rate (µmol/min)"].min()),
            float(enzyme_kinetics_data["Reaction Rate (µmol/min)"].max())
        )
    )
        
        filtered_enzymes = enzyme_kinetics_data[
            enzyme_kinetics_data["Reaction Rate (µmol/min)"].between(rate_filter[0], rate_filter[1])
        ]
        st.write(f"Filtered Results for Reaction Range {rate_filter}:")
        st.dataframe(filtered_enzymes)

        st.subheader("Reaction Rate (µmol/min) vs Substrate Concentration (mM)")
        st.line_chart(
        filtered_data.set_index("Substrate Concentration (mM)")["Reaction Rate (µmol/min)"]
    )
    
    elif data_option == "Protein Characterization":
        st.write("### Protein Characterization Data")
        st.dataframe(protein_character_data)
        # Add widget to filter by Brightness
        pI_filter = st.slider("Filter by Isoelectric Point (pI)", 
                              
        float(protein_character_data["Isoelectric Point (pI)"].min()),
        float(protein_character_data["Isoelectric Point (pI)"].max()),
        (
            float(protein_character_data["Isoelectric Point (pI)"].min()),
            float(protein_character_data["Isoelectric Point (pI)"].max())
        )
    )
        filtered_proteins = protein_character_data[
            protein_character_data["Isoelectric Point (pI)"].between(pI_filter[0], pI_filter[1])
        ]
        st.write(f"Filtered Results for Isoelectric Point {pI_filter}:")
        st.dataframe(filtered_proteins)

        st.subheader("Isoelectric Point (pI) vs Molecular Weight (kDa)")
        st.line_chart(
        filtered_data.set_index("Isoelectric Point (pI)")["Molecular Weight (kDa)"]
    )
    elif data_option == "Bacterial Growt Data":
        st.write("### Bacterial Growt Data")
        st.dataframe(bacterial_growth_data)
        # Add widgets to filter by temperature and humidity
        optical_density_filter = st.slider("Filter by Optical Density (OD600)", 
                                           
        float(bacterial_growth_data["Optical Density (OD600)"].min()),
        float(bacterial_growth_data["Optical Density (OD600)"].max()),
        (
            float(bacterial_growth_data["Optical Density (OD600)"].min()),
            float(bacterial_growth_data["Optical Density (OD600)"].max())
        )
    )
        filtered_bacteria_growth = bacterial_growth_data[
            bacterial_growth_data["Optical Density (OD600)"].between(pI_filter[0], pI_filter[1])
        ]
        st.write(f"Filtered Results for Optical Density (OD600) {optical_density_filter}:")
        st.dataframe(filtered_bacteria_growth)
        
        st.subheader("Temperature (°C) vs Optical Density (OD600)")
        st.line_chart(
        filtered_data.set_index("Temperature (°C)")["Optical Density (OD600)"]
    )
elif menu == "Contact":
    # Add a contact section
    st.title("Contact Me")
    st.write(
        "If you would like to collaborate, ask questions, or request additional information, "
        "please use the form below"
        )
    st.subheader("Send a Message")

    with st.form("Contact_Form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        subject = st.selectbox(
            "Subject", 
            ["General Inquiry","Research Collaboration","Data Request","Other"]
        )
        message = st.text_area("Message", height=150)
        submitted = st.form_submit_button("Send Message")

        if submitted:
            if not name or not email or not message:
                st.error("Please fill in all required fields.")
            else:
                st.success("Thank you your message has been submitted successfully")
                st.write("**Summary**")
                st.write(f"- Name: {name}")
                st.write(f"- Email: {email}")
                st.write(f"- Subject: {subject}")
                st.write(f"- Message: {message}")














