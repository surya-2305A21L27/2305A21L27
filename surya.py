import streamlit as st

# Defining Generator Efficiency function
def Gen_Eff(V, CL, IL, K, Rse, Ra):
    Pout = K * V * IL # Output power
    CUL = ((K * IL)**2)*(Rse + Ra) /1000  # Copper losses
    Pin = Pout + (CL*1000)+CUL  # Input power
    Eff = (Pout / Pin)   # Efficiency
    return Eff, CUL

# Streamlit app
st.title("2305A21L27 - P10")
st.markdown("this is my calculates the effeciency of DC series generator at various loads")

# Input fields
st.header("Input Parameters")
V = st.number_input("V:in Volt", value=220.0, step=10.0)
IL = st.number_input("IL:Amps", value=10.0, step=0.1)
Rse = st.number_input("Rse:Ohms", value=0.1, step=0.01)
Ra = st.number_input("Ra:Ohms", value=0.05, step=0.01)
CL = st.number_input("CL:in kilo Watts", value=50.0, step=1.0)
K = st.number_input("Loading on Generator (K)", value=1.0, step=0.1, min_value=0.0, max_value=1.0)


# Calculate efficiency and copper loss
if st.button("Calculate"):
    Eff, CUL = Gen_Eff(V, CL, IL, K, Rse, Ra)
    
    # Display results
    st.write("### Results")
    st.write(f"Efficiency =  {Eff:.2f}")
    st.write(f"CUL =  {CUL:.2f} kilo watts")
else:
    st.write("Enter values and click 'Calculate'.")