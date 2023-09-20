import pandas as pd
import openai
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from generator_llms import openai_code_generator

def read_tables(tables:dict):
    '''Merege the tables if found more than one'''
    if len(tables.keys())>1:
        '''perform merge option here'''
        #TODO: WE WILL IMPLEMENT THIS IN FUTURE
        pass
    elif len(tables.keys())==1:
        '''Feed the csv directly to  the model'''
        # print(f"INFO: Input Table dict: {tables}")
        source_table = tables["table0"]
        return source_table
    else:
        '''raise the error'''

def column_matching(column_list, template_column):
    # Calculate cosine similarity between the template_column and each column name
    vectorizer = TfidfVectorizer(analyzer='char', lowercase=True, use_idf=False, norm=None)
    tfidf_matrix = vectorizer.fit_transform([template_column] + column_list)
    cosine_similarities = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:]).flatten()

    # Get the index of the column with the highest similarity score
    best_match_index = np.argmax(cosine_similarities)
    best_match_column = column_list[best_match_index]
    best_similarity_score = cosine_similarities[best_match_index]

    return best_match_column

def get_target_columns(source_table,template_table):
    targets = {}
    for column in template_table.columns.tolist():
        matched = column_matching(source_table.columns.tolist(),column)
        targets[column] = matched
        if template_table[column].dtype != source_table[matched].dtype:
            temp = source_table.columns.tolist()
            temp.remove(matched)
            new_match = column_matching(temp,column)
            targets[column] = new_match
    return targets


def create_target_table(targets:dict,source_table,target_file_name):
    target_table = pd.DataFrame()
    for col1, col2 in targets.items():
        target_table[col1] = source_table[col2]
    target_table.to_csv(target_file_name, index=False)
    return target_table



def convert(tables:dict,template_table,target_file_name,source_table_name,template_table_name):
    source_table = read_tables(tables)
    targets = get_target_columns(source_table,template_table)
    target_table = create_target_table(targets,source_table,target_file_name)
    generated_code = openai_code_generator(template_table,target_table,target_file_name,source_table_name,template_table_name)
    print(f"INFO: Genreated Code is: {generated_code}")
    exec(generated_code)

