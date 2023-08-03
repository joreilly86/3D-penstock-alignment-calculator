import streamlit as st
import pandas as pd
import numpy as np

def get_column_name(dataframe, possible_names):
    """
    Return the column name from the dataframe that matches one of the possible names.
    If no match is found, return None.
    """
    for name in possible_names:
        if name in dataframe.columns:
            return name
    return None

def calculate_angle(a, b, c):
    ba = a - b
    bc = c - b
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)
    return np.degrees(angle)

def main():
    st.title('3D Penstock Alignment Deflection Angle Calculator 🧮')
        
    st.image('image.png',  width=500, caption='example of coordinates format in csv file')

    st.markdown("""
    ## Prepared by: James O'Reilly 📝
    ## Last Update: 2023-08-03 📅
    
    ## Deflection Angle Calculation

    The deflection angle between three points in a 3D space is calculated using the dot product and the cosine rule. The process is as follows:

    1. **Data Input**: The coordinates of each point along the penstock alignment are read from a CSV file. Each row in the CSV file represents a point, with 'x', 'y', and 'z' columns for the coordinates. Make sure you add these column names (x, y, z) to your CSV file as the first row (see screenshot above). The CSV file can be uploaded using the file uploader below.

    2. **Segment Creation**: For each set of three consecutive points (A, B, and C), two vectors are created: one from point A to B (vector AB) and another from point B to C (vector BC).

    3. **Angle Calculation**: The angle between these two vectors (which is the deflection angle at point B) is calculated using the dot product of the vectors and the cosine rule. The formula is as follows:

        `cosine_angle = dot_product(AB, BC) / (magnitude(AB) * magnitude(BC))`

        `angle = arccos(cosine_angle)`

        The angle is then converted from radians to degrees.

    4. **Result Display**: The calculated deflection angles are added to the data table and displayed below. Note there are no angles calculated for the start and end points.
    """)

    uploaded_file = st.file_uploader("Upload CSV", type=['csv'])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        
        x_col = get_column_name(data, ['x', 'X'])
        y_col = get_column_name(data, ['y', 'Y'])
        z_col = get_column_name(data, ['z', 'Z'])
        
        if None in [x_col, y_col, z_col]:
            st.error("CSV file must contain columns named 'x', 'y', and 'z' (case insensitive).")
            return
        
        data[x_col] = pd.to_numeric(data[x_col])
        data[y_col] = pd.to_numeric(data[y_col])
        data[z_col] = pd.to_numeric(data[z_col])

        angles = []
        supplementary_angles = []
        for i in range(1, len(data)-1):
            point1 = data.loc[i-1, [x_col, y_col, z_col]].values
            point2 = data.loc[i, [x_col, y_col, z_col]].values
            point3 = data.loc[i+1, [x_col, y_col, z_col]].values

            angle = calculate_angle(point1, point2, point3)
            angles.append(angle)
            supplementary_angles.append(180 - angle)

        data = data.iloc[1:-1]
        data['angle (°)'] = angles
        data['supplementary_angle (°)'] = supplementary_angles

        st.write(data)

if __name__ == "__main__":
    main()
