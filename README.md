#  Morocco Macro Tracker

An interactive data dashboard that visualizes key macroeconomic indicators in Morocco between 2016 and 2020.

Built using **Python**, **pandas**, **Plotly**, and **Streamlit**.

##  Features

- Interactive line charts for:
  - GDP growth (PIB en volume)
  - Sector growth (agriculture, industry, etc.)
- Year range filter
- Multi-indicator selection
- Summary statistics (mean, max, min)
- Clean and simple UI for quick insights

##  Technologies Used

- Python
- pandas
- Plotly
- Streamlit

##  Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/morocco-macro-tracker.git
cd morocco-macro-tracker
```

### 2. Add the cleaned data file

Make sure the file `cleaned_growth_data.csv` is in the same folder as the app script.
You can download it from the project or generate it with preprocessing steps.

### 3. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit app

```bash
streamlit run morocco_growth.py
```

## 📁 Data Source

The macroeconomic data is sourced from public Moroccan government statistics (HCP, MEF) and manually cleaned for this project.

[https://data.gov.ma/data/fr/dataset/26d56c9c-df51-472b-bf8d-c9a246f3d8ca/resource/5c22ab72-5622-4d04-8685-2e5169f2e6fe/download/statistiques-macroeconomiques-sectoriels-sociaux.xlsx](https://data.gov.ma/data/fr/dataset/26d56c9c-df51-472b-bf8d-c9a246f3d8ca/resource/5c22ab72-5622-4d04-8685-2e5169f2e6fe/download/statistiques-macroeconomiques-sectoriels-sociaux.xlsx)

## ✨ Demo

https://morocco-macro-tracker.streamlit.app/

## 👩‍💻 Author

Built with ❤️ by **Zaineb**, AI & Data Science Master's student based in Morocco.

