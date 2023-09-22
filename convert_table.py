import argparse
from extractors import convert
import pandas as pd
def main():
    parser = argparse.ArgumentParser(description="Convert CSV files based on a template")
    parser.add_argument("--sources", nargs='+', required=True, help="List of source CSV files")
    parser.add_argument("--template", required=True, help="Template CSV file")
    parser.add_argument("--target", required=True, help="Target CSV file")
    args = parser.parse_args()
    source_files = args.sources #Multiple CSV files in a list
    template_file = args.template
    target_file_name = args.target
    tables:dict = {}
    source_table_name = source_files[0]
    template_table_name = template_file
    for index, source_file in enumerate(source_files):
        tables[f'table{index}'] = pd.read_csv(source_file)
    template_table = pd.read_csv(template_file)
    convert(tables,template_table,target_file_name,source_table_name,template_table_name)
if __name__ == "__main__":
    main()