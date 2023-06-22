from datetime import datetime
from decouple import config

class ProjectMapper: 
    def map(self, proj, elk_proj, owner, category):
        if not elk_proj.timestamp:
            elk_proj.timestamp = datetime.now()
        if owner != '':
            elk_proj.owner = owner

        if proj[0] != '':
            elk_proj.date = format_date(proj[0])

        if proj[1] != '':
            elk_proj.number_projects = int(proj[3])
        
        if proj[2] != '':
            elk_proj.number_test_cases = int(proj[4])

        if proj[3] != '':
            elk_proj.number_keywords = int(proj[5])

        if proj[4] != '':
            elk_proj.number_variables = int(proj[5])

        if proj[5] != '':
            elk_proj.number_lines = int(proj[5])


def format_date(s):
    if s != 'Null' and s != 'None' and s != '':
        s = s.split('.')[0]
        return s
    else:
        s = ' '
        return s
    

