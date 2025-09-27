import streamlit as st

# Set page title and header
st.title('Compound Interest Calculator')
st.markdown('---')

# Input fields
principal = st.number_input('Enter Principal Amount:', min_value=0.0, format='%f')
rate = st.number_input('Enter Annual Interest Rate (%):', min_value=0.0, format='%f')
time = st.number_input('Enter Times to compound in one year:', min_value=0.0, format='%f')

# Calculate button
if st.button('Calculate'):
    if principal > 0 and rate >= 0 and time >= 0:
        # Convert percentage to decimal
        rate_decimal = rate / 100
        
        # Calculate compound interest (assuming compounded annually for simplicity)
        final_amount = principal * (1 + rate_decimal) ** time
        
        # Display the result
        st.success(f'The final amount after {time} years will be: ${final_amount:,.2f}')
    else:
        st.error('Please enter valid positive numbers for Principal, Rate, and Time.')