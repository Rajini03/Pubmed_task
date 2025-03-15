import typer
 
from pubmed_papers.fetch_papers import fetch_pubmed_papers, save_results_to_csv

app = typer.Typer()

@app.command()
def get_papers_list(query: str, file: str, debug: bool = False):
    """Fetch papers from PubMed based on the query and save them to a CSV file."""
    
    if debug:
        typer.echo(f"Searching for papers on: {query}")

    
    papers = fetch_pubmed_papers(query, debug)
    save_results_to_csv(papers, file)

    typer.echo(f"Results saved to {file}")
     

if __name__ == "__main__":
    app()
