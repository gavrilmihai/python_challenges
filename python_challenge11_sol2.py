import json

def get_values(scores_dict, subject):
    """
    Return three values.
    
    This function receives scores in the form of dictionary from a JSON file
    and a subject and returns min, max and average score for that subject.
    """
    scores = []
    for every_line in scores_dict:
        scores.append(every_line.get(subject))
    return min(scores), max(scores), sum(scores)/len(scores)

file_input = True
while file_input:
    file_name = input("What is the file name: ")
    file_input = file_name
    try:
        with open(file_input, 'r') as jsonfile:
            todos = json.load(jsonfile)
        
            # let us find the subjects being scored
            subject = []
            #subject.append([subject for row in todos if r])
            for scoring_line in todos:
                if list(scoring_line) not in subject:
                    subject = list(scoring_line)
                    
            print(f'scores/{file_input}')
            for every_subject in subject[::-1]:
                min_val, max_val, ave_val = get_values (todos, every_subject)
                print(f'\t{every_subject}: min {min_val}, max {max_val}, average {ave_val}')
    
    except FileNotFoundError:
        pass