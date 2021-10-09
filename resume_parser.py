from tika import parser  
from question_generation import pipeline

nlp = pipeline("question-generation")

def getTextFromPdf(resume):
    parsed_pdf = parser.from_file(resume)
    data = parsed_pdf['content'] 
    return data

def getQuestions(text):
    return nlp(text)

def generate(resume):
    text = getTextFromPdf(resume=resume)
    questions = getQuestions(text=text)
    return questions