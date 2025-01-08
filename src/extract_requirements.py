import shutil
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
import json
import os


def check_file_exits(text_file_path):
    '''
    Functionality : 
    This functions Checks whether file is present at Given File Path Location.
    It Also check if it is presents then does it contain any content inside it or not .
    If the file is present and have contents it will return 1
    If the file is present and Doesnt have contents it will return 0
    if the file is not present then it will get catch into exception and return -1

    Params: text_file_path

    return : 1 or 0 or -1
    '''
    try:
        if os.path.getsize(text_file_path) > 0:
            print("file_is_present_and_has_content")
            return 1
        else:
            print("file_is_present_but_no_content")
            return 0
    except OSError as e:
        return -1



def convert_text_markdown(text_file_path):
    '''
    Functionality:
    1. Converts text file contents into Mardown format.
    2. This conversion is helpful for parsing contents inside the file.
    3. Using Standard Shutil Module we can convert txt file to mardown file 

    Params : text_file_path

    return : markdown_path 

    '''
    markdown_path="regulations.md"
    shutil.copyfile(text_file_path,markdown_path)
    return markdown_path
    
        


def get_sections_paragraphs_using_langchain_md_parser(markdown_path):
    '''
    Functionality:
    1. After converting text file to markdown file , this function is used to parse contents
    2. Function will return Langchain Document Object which contains following things
        a. page_contentt which contains text can be either Title of Paragraph 
        b. It contains other metadata as well which is not useful at moment but good to keep it 
        c. We used langchain as it internaly uses NLTK Perceptron model to parse contents and divide based on Title and paragraphs

    Params: markdown_path

    Return data

    Sample Data Object 

    [Document(page_content='Section 1: Data Privacy and Security', metadata={'source': 'regulations.md', 'last_modified': '2025-01-08T03:05:24', 'languages': ['eng'], 'filetype': 'text/markdown', 'filename': 'regulations.md', 'category': 'Title'}),

    '''
    try:
        loader = UnstructuredMarkdownLoader(markdown_path, mode="elements")
        data = loader.load()
        return data
    except Exception as e:
        print(e)
        return False
    

def align_paragraph_with_particular_section(data):

    '''
    Functionality:
    Job of this function is pretty easy to understand . we converted txt file to Markdown format so that langchain can parse contents 
    Langchain will parse into Title and paragraph
    This function Takes input data which contains Series of Title and Paragraph metadata .
    We need to connect Respective header to its paragraph for Summarizing each section 

    Params : data 

    Return section_content_list

    sample section_content_list:

    [{'section_title': 'Section 1: Data Privacy and Security','section_content_paragragh': ' Amazon places the highest priority on the protection of customer data.'}]
    
    
    '''

    section_content_list = [] # final o/p list of dictionaries where each dictionary is section title and paragraph
    current_index = 0
    for index , doc in enumerate(data): # enumerate langchain data for fetching Title and NarrativeText (paragraph)
        dict = doc.metadata
        if dict["category"] == "Title" :
            if current_index!=index:
                section_content_list.append(temp_dict) # Appending each Section with its paragraph Before new section starts 
                current_index = index
            temp_dict = {"section_title":"","section_content_paragragh":""}
            temp_dict["section_title"] = doc.page_content 
            
            current_section = doc.page_content 
        if dict["category"] == "NarrativeText":
            if temp_dict["section_title"] == current_section:
                temp_dict["section_content_paragragh"] += " "+doc.page_content

        if index == (len(data)-1):
            section_content_list.append(temp_dict)

    return section_content_list
    

def simulate_llm_summary(text_section,sentences_count):

    '''
    Functionality:

    Summarize the text paragraph for each sections using LSA Summarizer ,  We used sumy python open source project to similuate 

    Params : 
    1. text_section : Section Paragraph which needs to be summarize
    2. sentences_count : In how many sentences you want summary 

    return Summary of the section 
    
    
    '''

    
    parser = PlaintextParser.from_string(text_section, Tokenizer("english")) # Apply sumy parser to our section paragraphs

    summarizer = LsaSummarizer(Stemmer("english")) # Apply stemming in english language 
    summarizer.stop_words = get_stop_words("english") # remove stop words and get list of stop words

    summary = summarizer(parser.document, sentences_count) ## Call Summary function which return the summary 
    return summary


def get_summary_for_all_section_text(section_content_list,sentences_count):
    '''
     Functionality:
     1. This function will actually iterate all section paragraphs and call simulate_llm_summary function to get summary
     2. Will Store Dict objects into List after getting summary from the function along with section title and original text 

     params : 
     section_content_list: which contains header title and its paragraph content
     sentences_count: In how many sentences we need summarized version 

     return :
     section_summaries  which is actually list of dictionaries with keys section_number,original_text,section_summary

    
    '''


    section_summaries = []
    for sec_object in section_content_list:
        paragraph = sec_object["section_content_paragragh"]
        summary = simulate_llm_summary(paragraph, sentences_count)
        section_title = sec_object["section_title"]
        sentence_str = ""
        for sentence in summary:
            sentence_str+=str(sentence)
        section_summaries.append({"section_number":section_title,"original_text":paragraph,"section_summary":sentence_str})
    return section_summaries
    

def write_to_json_file(section_summaries):
    '''
    Functionality:
    Job of this function is to Dump the results which is in List to JSON Object and Store in users.json file 

    Params :
    section_summaries which is actually list of dictionaries with keys section_number,original_text,section_summary
    
    '''

    with open("extracted_requirements.json", "w") as file:
        json.dump(section_summaries, file, indent=4)
         


def run_summary_pipeline(text_file_path="regulations.txt",sentences_count=2):
    '''
    Main Function Entry point 
    Job of this function is to call all other functions in a flow 
    1. First it will check file exists or not , Does it contains text or not 
    2. if it contains normal flow starts else just return file is empty or not available 
    3. If valid file and has data , first it will convert into Markdown format as we can leverage Langchain which internally uses NLTK for parsing 
    4. Using Langchain we can parse contents into Section By Section and its respective content
    5. Then once we get section and its content we use Sumy to summarize the content using LSA technique 
    6. The LSA summarizer is the best one amognst all because it works by identifying patterns and relationships between texts, rather than soley rely on frequency analysis. This LSA summarizer generates more contextually accurate summaries by understanding the meaning and context of the input text.
    7. Store back all summaries into list of dictionaries with keys section_number,original_text,section_summary
    8. store them into json file

    Params:
    text_file_path : which contains text contents inside the file 
    sentences_count : How many sentences we need to summarize 

    return: error when normal flow breaks
    
    '''

    check_file_exits_response = check_file_exits(text_file_path)
    if check_file_exits_response == 1:
        markdown_path=convert_text_markdown(text_file_path)
        data = get_sections_paragraphs_using_langchain_md_parser(markdown_path)
        if data:
            section_content_list = align_paragraph_with_particular_section(data)
            section_summaries = get_summary_for_all_section_text(section_content_list,sentences_count)
            write_to_json_file(section_summaries)
            print("all_Jobs Done")
        else:
            return "file cannot be parsed" 
            
    elif check_file_exits_response == 0:
        return "Empty File Cannot run Summary Pipeline"
    else:
        return "File Doesnt Exists"
        
        


if __name__ == '__main__':
    run_summary_pipeline()