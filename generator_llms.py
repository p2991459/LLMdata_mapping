import openai

api_key = "PASTE_YOUR_OPENAI_KEY"

def openai_code_generator(template_table,target_table,target_file_name,source_table_name,template_table_name):
    prompt = f"""
                you are a python developer
                you got 2 csv files -
                1. {target_file_name}
                2. {template_table_name}

                both the files have same data but some columns could be in different formats
                example as dates could be in different form
                other columns may have different formats too so look for all columns
                most columns have dtype object
                your task is to format {source_table_name} columns in the format of template.csv columns

                - read both datasets I am providing you
                - generate code to change formats of new_dataset columns and at the end of code export the csv named as {target_file_name}

                Now I'm providing you with both tables 5 rows to see the format

                {target_file_name}

                {target_table.head()} 
                -----------------------------------
                {template_table_name}

                {template_table.head()}
                ------------------------------------

                Your output should be a piece of pure executable Python code starting with the import statement.
                important - avoid indentation error at the start
                Id's and numbers should not be lost
                do not add indexes as new column 
                both the files are in same folder

            """


    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the appropriate OpenAI engine
        prompt=prompt,
        max_tokens=500,  # Adjust the token limit as needed
        api_key=api_key,
        temperature = 0
    )

    response_text = response.choices[0].text.strip()

    return response_text


def dict_generater(source_file, template_file):
    prompt = f"""
                you are a data analysist
                - I'm providing you 2 tables
                    1. source table
                    2. template table

                - you need to make a new dataset by the data of source table in the format of template table
                - in the new dataset columns name will be same as template table but data will be getted from source table

                for now your task is to make a python dictionary to target the columns of source table to extract data for new dataset
                in the dictionary keys will be the columns names of template table and values will be the column names of source table from where we can extract data for new dataset

                now I'm providing you the tables

                source table - 
                {source_file.head()}
                --------------------------------

                template table - 
                {template_file.head()}
                ---------------------------------

                your output should be clean python dictionary like a printed dictionary in the terminal not in the code with variable

            """

    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the appropriate OpenAI engine
        prompt=prompt,
        max_tokens=500,  # Adjust the token limit as needed
        api_key=api_key,
        temperature=0.01
    )
    response_text = response.choices[0].text.strip()
    return response_text