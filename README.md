# 3D Penstock Alignment Deflection Angle Calculator 🧮

## Overview 📖
This repository contains a Streamlit app designed for calculating the deflection angles between successive points along a 3D penstock alignment.

---

## Requirements 🛠️

- Python 3.x
- Streamlit
- pandas
- NumPy

To install the necessary packages, run:
```bash
pip install streamlit pandas numpy
```

---

## Usage 🚀
1. Clone the repository.
2. Navigate to the directory and run `streamlit run app.py`.

---

## Functionality 📋
The Streamlit app performs the following tasks:

### Data Input 📤
- Accepts a CSV file containing 3D coordinates (`x`, `y`, `z`) for each point along the penstock alignment.
- Check out the example csv file `penstock 03-08-23.csv`.

### Segment Creation 🔗
- For each set of three consecutive points (`A`, `B`, `C`), two vectors (`AB`, `BC`) are generated.

### Angle Calculation 📐
- The deflection angle at point `B` is calculated using the dot product and the cosine rule.

```python
cosine_angle = dot_product(AB, BC) / (magnitude(AB) * magnitude(BC))
angle = arccos(cosine_angle)
```

The angle is converted from radians to degrees.

### Result Display 📊
- Displays a data table containing calculated deflection angles.

---

## Author 📝
Prepared by: James O'Reilly

---

## References 📚
- NumPy v1.21.2 Documentation: [Link](https://numpy.org/doc/1.21/)
- pandas v1.3.3 Documentation: [Link](https://pandas.pydata.org/pandas-docs/version/1.3/)
- Streamlit Documentation: [Link](https://docs.streamlit.io/)

---

For technical queries, feel free to reach out to the author.
