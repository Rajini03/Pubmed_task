import requests
import pandas as pd
import xml.etree.ElementTree as ET
import re
import traceback
PUBMED_API_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def fetch_pubmed_papers(query, debug=False):
    """Fetch papers from PubMed based on the query."""
    
    if debug:
        print(f"DEBUG: Fetching papers for query: {query}")

    # Simulating API response
    results = [
        {"PubmedID": "12345678", "Title": "A Study on Cancer Treatment", "Publication Date": "2024-01-01"}
    ]

    if debug:
        print("DEBUG: Results fetched from PubMed:", results)

    return results



def fetch_paper_details(paper_ids):
    """Fetch details of papers using their PubMed IDs."""
    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "xml"
    }
    response = requests.get(f"{PUBMED_API_BASE}efetch.fcgi", params=params)

    if response.status_code != 200:
        raise Exception("Failed to fetch paper details.")

    return parse_paper_details(response.content)


def parse_paper_details(xml_data):
    """Parse XML data and extract required details."""
    root = ET.fromstring(xml_data)
    papers = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.find(".//PMID").text
        title = article.find(".//ArticleTitle").text
        pub_date = article.find(".//PubDate/Year")
        pub_date = pub_date.text if pub_date is not None else "Unknown"

        authors = article.findall(".//Author")
        non_academic_authors = []
        company_affiliations = []
        email = "N/A"

        for author in authors:
            affiliation = author.find(".//Affiliation")
            if affiliation is not None:
                aff_text = affiliation.text.lower()

                if re.search(r'pharma|biotech|inc|corp|llc|ltd', aff_text):
                    non_academic_authors.append(author.find(".//LastName").text)
                    company_affiliations.append(affiliation.text)

                email_elem = re.search(r'[\w\.-]+@[\w\.-]+', aff_text)
                if email_elem:
                    email = email_elem.group()

        if company_affiliations:
            papers.append([pmid, title, pub_date, "; ".join(non_academic_authors), "; ".join(company_affiliations), email])

    return papers


def save_results_to_csv(results, filename):
    """Save the fetched PubMed papers to a CSV file."""

     
    print("DEBUG: Function save_results_to_csv called from:")
    traceback.print_stack()  # Prints the function call stack
    
    # Debug: Print fetched results
    print("DEBUG: Results fetched from PubMed:", results)

    # If results are empty, print a warning
    if not results:
        print("WARNING: No papers were found. The CSV file will only contain headers.")

    # Save results to CSV
    df = pd.DataFrame(results)
    try:
        df.to_csv(filename, index=False, encoding="utf-8")
        print(f" Results successfully saved to {filename}")
    except Exception as e:
        print(f" ERROR: Failed to save results to {filename} - {e}")
