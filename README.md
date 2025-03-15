# PubMed Papers Fetcher  

## 📌 Project Overview  
This project is a Python-based CLI tool that fetches research papers from **PubMed** based on a user query. It filters papers with at least one author affiliated with a pharmaceutical or biotech company and saves the results as a **CSV file**.  

## 🚀 Features  
- Fetch research papers from **PubMed** using a query.  
- Filter papers based on author affiliation.  
- Save results in **CSV format**.  
- Supports **command-line arguments**.  
- Includes **debug mode** for detailed logs.  

## 🛠️ Installation  

### Prerequisites  
- Python **3.12+**  
- [Poetry](https://python-poetry.org/docs/) (for dependency management)  

### Steps  
1. **Clone the repository**  
    
2. **Install dependencies using Poetry**
   - poetry install
- **Usage**
-Fetch Papers and Save to CSV
-poetry run python -m pubmed_papers.cli "cancer treatment" results.csv

**Enable Debug Mode**:
poetry run python -m pubmed_papers.cli "cancer treatment" results.csv --debug

**📂 Project Structure**

pubmed_papers/

│── pubmed_papers/

│   ├── __init__.py

│   ├── cli.py          # CLI script

│   ├── fetch_papers.py # Fetch and filter PubMed papers

│   ├── utils.py        # Helper functions

│── tests/              # Unit tests

│── pyproject.toml      # Poetry dependencies

│── README.md           # Project documentation


**📝 Example Output** : 
CSV File (results.csv):-

PubmedID,Title,Publication Date

12345678,A Study on Cancer Treatment,2024-01-01


