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
    ["Researcher Profile", "Biochemistry Calculator", "STEM Data Explorer", "Contact"],
)

# Dummy STEM data
enzyme_kinetics_data = pd.DataFrame({
    "Enzyme": ["Amylase", "Catalase", "Lipase", "Protease", "Urease"],
    "Substrate Concentration (mM)": [1, 2, 3, 4, 5],
    "Reaction Rate (µmol/min)": [5.1, 9.3, 12.7, 14.9, 15.2]
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
        st.write("""
        The pages that follow are some things that I found interesting. 
        """)
        
    with col2:
        st.image(
            "Sunset (2).jpg",
            caption="Sunset (Damien Ferreira)", 
            use_column_width=True
    )

elif menu == "Biochemistry Calculator":
    st.title("Biochemistry Calculator & Analysis")
    st.write(
        "This page provides interactive tools for performing common biochemistry "
        "and microbial physiology calculations."
    )

    calculator = st.selectbox(
        "Select a calculation:",
        [
            "Michaelis–Menten Enzyme Kinetics",
            "Beer–Lambert Law",
            "Bacterial Growth Rate"
        ]
    )

    # Michaelis–Menten Kinetics
    if calculator == "Michaelis–Menten Enzyme Kinetics":
        st.subheader("Michaelis–Menten Equation")

        st.latex(r"v = \frac{V_{max}[S]}{K_m + [S]}")

        col1, col2 = st.columns(2)

        with col1:
            vmax = st.number_input("Vmax (µmol/min)", min_value=0.0, value=100.0)
            km = st.number_input("Km (mM)", min_value=0.01, value=5.0)

        with col2:
            substrate = st.number_input("Substrate Concentration [S] (mM)", min_value=0.0, value=10.0)

        if st.button("Calculate Reaction Rate"):
            rate = (vmax * substrate) / (km + substrate)
            st.success(f"Reaction Rate (v): **{rate:.2f} µmol/min**")

    # Beer–Lambert Law
    elif calculator == "Beer–Lambert Law":
        st.subheader("Beer–Lambert Law")

        st.latex(r"A = \varepsilon \cdot l \cdot c")

        col1, col2 = st.columns(2)

        with col1:
            absorbance = st.number_input("Absorbance (A)", min_value=0.0, value=0.75)
            path_length = st.number_input("Path Length (cm)", min_value=0.01, value=1.0)

        with col2:
            epsilon = st.number_input(
                "Molar Absorptivity ε (L·mol⁻¹·cm⁻¹)",
                min_value=0.01,
                value=15000.0
            )

        if st.button("Calculate Concentration"):
            concentration = absorbance / (epsilon * path_length)
            st.success(f"Concentration (c): **{concentration:.6f} mol/L**")

    # Bacterial Growth Rate
    elif calculator == "Bacterial Growth Rate":
        st.subheader("Bacterial Specific Growth Rate")

        st.latex(r"\mu = \frac{\ln N_2 - \ln N_1}{t_2 - t_1}")

        col1, col2 = st.columns(2)

        with col1:
            N1 = st.number_input("Initial Cell Density (N₁)", min_value=0.01, value=0.1)
            t1 = st.number_input("Initial Time t₁ (hours)", min_value=0.0, value=0.0)

        with col2:
            N2 = st.number_input("Final Cell Density (N₂)", min_value=0.01, value=0.8)
            t2 = st.number_input("Final Time t₂ (hours)", min_value=0.01, value=6.0)

        if st.button("Calculate Growth Rate"):
            mu = (np.log(N2) - np.log(N1)) / (t2 - t1)
            st.success(f"Specific Growth Rate (μ): **{mu:.3f} h⁻¹**")

elif menu == "STEM Data Explorer":
    st.title("STEM Data Explorer")
    st.sidebar.header("Data Selection")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore", 
        ["Enzyme Kinetics", "Protein Characterization", "Bacterial Growth Data"]
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
        filtered_enzymes.set_index("Substrate Concentration (mM)")["Reaction Rate (µmol/min)"]
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
        filtered_proteins.set_index("Isoelectric Point (pI)")["Molecular Weight (kDa)"]
    )
    elif data_option == "Bacterial Growth Data":
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
            bacterial_growth_data["Optical Density (OD600)"].between(optical_density_filter[0], optical_density_filter[1])
        ]
        st.write(f"Filtered Results for Optical Density (OD600) {optical_density_filter}:")
        st.dataframe(filtered_bacteria_growth)
        
        st.subheader("Temperature (°C) vs Optical Density (OD600)")
        st.line_chart(
        filtered_bacteria_growth.set_index("Optical Density (OD600)")["Temperature (°C)"]
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






















