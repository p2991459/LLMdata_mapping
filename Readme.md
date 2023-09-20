# CSV DATA MAPPING USING PYTHON

Steps to run the code
1. clone the repository
2. Install python 
3. create virtualenv using python -m venv venv
4. Install the requirements using pip install -r requirements.txt


Run the following command after putting your csv file in the project directory

python create_table.py --sources <<table1.csv>> --template <<template.csv>> --target <<output.csv>>

## example uses:

python convert_table.py --sources .\table_A.csv --template .\template.csv --target target.csv


## Work with multiple files

python convert_table.py --sources table1.csv table2.csv table3.csv --template .\template.csv --target target.csv