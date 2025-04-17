# 🛰️ DISCOS-SatFetch

Fetch detailed satellite metadata using the [ESA DISCOS API](https://discosweb.esoc.esa.int/) and a list of SATNOs (NORAD catalog numbers).  
Ideal for research, analysis, and academic projects related to space debris, satellite tracking, or mission metadata.

---

## 🔧 Features

- Queries ESA's DISCOS database via REST API
- Accepts SATNOs (NORAD IDs) from a CSV file
- Outputs full satellite metadata to a clean CSV
- Easily configurable via `.env` file
- Simple, modular project structure

---

## 📁 Project Structure

```
discos-satfetch/
├── data/
│   └── input_satnos.csv           # Example input file (user-provided)
├── output/
│   └── satellite_data.csv         # Output (auto-generated)
├── src/
│   └── fetch_discos_data.py       # Main logic
├── .env                           # API key (not committed)
├── .env.example                   # Template for API key
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🚀 Quick Start

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/discos-satfetch.git
cd discos-satfetch
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Your `.env`

Copy the example and insert your DISCOS API key:

```bash
cp .env.example .env
```

Edit `.env`:

```env
DISCOS_API_KEY=your_actual_api_key_here
```

### 4. Prepare Your Input CSV

Ensure `data/input_satnos.csv` exists and contains a column named `Name` with SATNO values:

```csv
Name
25544
43013
43205
```

### 5. Run the Script

```bash
python src/fetch_discos_data.py
```

Output will be saved to: `output/satellite_data.csv`

---

## 📜 ESA Data Attribution

> Users are obliged to include the following source reference when using DISCOS data in derived works or redistributions:

> *For [providing our services/our research], we are using information from ESA DISCOS (Database and Information System Characterising Objects in Space), a single-source reference for launch information, object registration details, launch vehicle descriptions, as well as spacecraft information for all trackable, unclassified objects. We acknowledge ESA's efforts to maintain and operate this database with its APIs.*

Learn more: [https://discosweb.esoc.esa.int](https://discosweb.esoc.esa.int)

---

## 📘 License

MIT License

---

## 🙌 Contributions Welcome

Feel free to open issues or submit PRs for bug fixes, enhancements, or new features!
