import typer
from os import path
import pandas as pd
import json

app = typer.Typer()


@app.command()
def test(specification_filepath:str, output_filepath:str):
    print(f"output_filepath - {output_filepath}")
    print(f"specification_filepath - {specification_filepath}")
    if path.exists(specification_filepath):
        print(f"Specification file exists: {specification_filepath}")
    else:
        print(f"Specification file does not exist: {specification_filepath}")

@app.command()
def excel_to_json_array(specification_filepath:str, output_filepath:str):
    print(f"output_filepath - {output_filepath}")
    print(f"specification_filepath - {specification_filepath}")
    if path.exists(specification_filepath):
        print(f"Specification file exists: {specification_filepath}")

        # Load the Excel file
        excel_file = specification_filepath

        # Convert Excel sheet to DataFrame
        df = pd.read_excel(excel_file)

        # Convert DataFrame to JSON
        json_str = df.to_json(orient='records',force_ascii=False)

        # Load JSON string into a dictionary
        json_data = json.loads(json_str)

        # Save JSON to a file
        with open(output_filepath, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file,  indent=4, ensure_ascii=False)

        print(f"JSON data saved to: {output_filepath}")
    else:
        print(f"File does not exist: {specification_filepath}")

@app.command()
def excel_to_json_object(specification_filepath:str, output_filepath:str):
    print(f"output_filepath - {output_filepath}")
    print(f"specification_filepath - {specification_filepath}")
    if path.exists(specification_filepath):
        print(f"Specification file exists: {specification_filepath}")

        # Load the Excel file
        excel_file = specification_filepath

        # Convert Excel sheet to DataFrame
        df = pd.read_excel(excel_file)

        # Convert DataFrame to JSON
        records = df.to_json(orient='records',force_ascii=False)

        # Wrap the records array inside a parent JSON object
        json_data = {"records": json.loads(records)}

        # Write the wrapped JSON data to a file with pretty-printing
        with open(output_filepath, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        print(f"JSON data saved to: {output_filepath}")
    else:
        print(f"File does not exist: {specification_filepath}")        

if __name__ == "__main__":
    app()
