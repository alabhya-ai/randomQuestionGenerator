# this project takes info from pageInfo folder and uses it to generate random exercises.See doc.txt for manual.
import pandas as pd, random as rn, os

chapterPath = os.path.dirname(os.path.abspath(__file__))# directory of current file
sub = '' # subject number chosen by user
excelPath = chapterPath + r'\pageInfo\LessonPlan11.xlsx'# path to the excel database
file = pd.ExcelFile(excelPath)
print(chapterPath)

def subMap(sub): # sub = subject that is input by the user
    """Returns a dictionary that links chapters to their working hours and state of completion"""
    global file
    subj = pd.read_excel(file, sub)
    subInfo = dict() # returning dictionary
    for i in range(subj.__len__()):
        chapInfo = subj.iloc[i]
        if chapInfo['Completion'] == 'yes':
            subInfo[i] = (chapInfo['Chapter'], chapInfo['Completion'], chapInfo['Working Hours (TH)'])
    return subInfo

def subList(subject): # Displaying subject list
    """Lets user choose from a list of subjects and chapters"""
    global chapterPath, sub
    chapterPath = os.path.dirname(os.path.abspath(__file__)) # so that it works even when new subjects are selected
    # taking subject input
    subs = list() # will be returned
    # taking chapter input
    chapMap = subMap(subject) # all chapter numbers
    for chapter in chapMap:
        chap = chapMap[chapter] #   chapter number = (chapter name, completion, working hours)
        subs.append(f'{chapter}.\t{chap[0]}\t--({chap[2]} working hours)')
    
    # directory of required file
    chapterPath += f'\pageInfo\{subject}.txt'

    return subs
    

def generateQuestion(chapWise, Chap): # Generating the question
    """Generates a random question from the chapter that the user chose to take a test on"""
    global sub
    with open(chapterPath, 'r') as f:
        file = f.readlines() # all data in the file
        # book information
        bookIndex = dict(enumerate((i[:-1].strip() for i in file[0].split(':'))))
        del(bookIndex[0])
        # chapter information
        if chapWise:
            for lineNum, line in enumerate(file):
                if line == Chap + '\n':
                    fromBook = rn.randrange(1, len(bookIndex), 1) # from book
                    fromLine = file[lineNum + fromBook][2:] # line containing exercise info of the book
                    exercises = fromLine.split('|')[0].split(',') # exercise list
                    which = rn.randrange(1, len(exercises), 1) # an index to select exercise and question
                    fromExercise = exercises[which]
                    questionNum = fromLine.split('|')[1].split(',')[which]
                    return f'Question: {questionNum}\nChapter: {Chap}\nExercise: {fromExercise}\nReference: {bookIndex[fromBook]}'
        else:
            rnChap = rn.choice((i[0] for i in subMap(chapterPath.split('\\')[-1][:-3]).values())) # random chapter
            for lineNum, line in enumerate(file):
                    if line == rnChap + '\n':
                        fromBook = rn.randrange(1, len(bookIndex), 1) # from book
                        fromLine = file[lineNum + fromBook][2:] # line containing exercise info of the book
                        exercises = fromLine.split('|')[0].split(',') # exercise list
                        which = rn.randrange(1, len(exercises), 1) # an index to select exercise and question
                        fromExercise = exercises[which]
                        questionNum = fromLine.split('|')[1].split(',')[which]
                        return f'Question: {questionNum}\nChapter: {Chap}\nExercise: {fromExercise}\nReference: {bookIndex[fromBook]}'
                    
