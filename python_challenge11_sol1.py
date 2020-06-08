'''
Day 11 json maths:
For this exercise, you must produce the highest, lowest, and average test scores for each subject in each class. Given two files (9a.json and 9b.json)
in the scores directory, we would see the following example output:
scores/9a.json
    science: min 75, max 97, average 86.4
    literature: min 78, max 98, average 83.6
    math: min 65, max 100, average 85.0
'''
import json
import statistics
def parcing(file):
    """This function open the exam result file ,load it as json , the calculat lowest,average and highst scores per exam """
    math_results=[]
    literature_results=[]
    science_results=[]
    Dict_Results={}
    with open(file) as f:
        results=json.load(f)
        for dict in results :
            for k,v in dict.items():
                if k == 'math' :
                    math_results.append(v)
                elif k == 'literature' :
                    literature_results.append(v)
                elif k == 'science':
                    science_results.append(v)
                else:
                    print('Found not expected discipline results')
    Dict_Results.update({'science':science_results})
    Dict_Results.update({'literature':literature_results})
    Dict_Results.update({'math':math_results})
    return Dict_Results
files=['9a.json','9b.json']
for file in files :
    Results= parcing(file)
    print(f'Scores/{ file }')
    for k,v in Results.items():
        print(f'{ k }: min {min(v)}, max { max(v) }, average { statistics.mean(v) }')
    print('\n')
