from datetime import datetime
from decouple import config

class SmellMapper: 
    def map(self, smell, elk_smell, owner, category):
        if not elk_smell.timestamp:
            elk_smell.timestamp = datetime.now()

        if owner != '':
            elk_smell.owner = owner

        if category != '':
            elk_smell.category = category

        if smell[1] != '':
            elk_smell.project_name = smell[1]

        if smell[0] != '':
            elk_smell.version = format_date(smell[0])

        if smell[2] != '':
            elk_smell.test_case_name = smell[2]

        if len(smell) > 10:
            if smell[2] != '' and smell[3] != '':
                elk_smell.test_case_name = f'{smell[2]}{smell[3]}'

            if smell[4] != ''  and smell[4] != 'NaN':
                elk_smell.test_case_size = int(smell[4])
        
            if smell[5] != ''  and smell[5] != 'NaN':
                elk_smell.test_case_sequence = int(smell[5])

            if smell[6] != ''  and smell[6] != 'NaN':
                elk_smell.test_case_level = int(smell[6])

            if smell[7] != '':
                elk_smell.smell_name = smell[7]

            if smell[8] != '' and smell[8] != 'NaN':
                elk_smell.smell_raw_value = float(smell[8])

            if smell[9] != '' and smell[9] != 'NaN':
                elk_smell.smell_normalized_value = float(smell[9])

            if smell[10] != '':
                elk_smell.fixes = int(smell[10])
        else:
            if smell[3] != ''  and smell[3] != 'NaN':
                elk_smell.test_case_size = int(smell[3])
        
            if smell[4] != ''  and smell[4] != 'NaN':
                elk_smell.test_case_sequence = int(smell[4])

            if smell[5] != ''  and smell[5] != 'NaN':
                elk_smell.test_case_level = int(smell[5])

            if smell[7] != '':
                elk_smell.smell_name = smell[6]

            if smell[7] != '' and smell[7] != 'NaN':
                elk_smell.smell_raw_value = float(smell[7])

            if smell[8] != '' and smell[8] != 'NaN':
                elk_smell.smell_normalized_value = float(smell[8])

            if smell[9] != '':
                elk_smell.fixes = int(smell[9])

def format_date(s):
    if s != 'Null' and s != 'None' and s != '':
        s = s.split('.')[0]
        return s
    else:
        s = ' '
        return s