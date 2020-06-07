


class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
        
    def top3(self):
        return(sorted(self.times)[0:3])

def get_coach_data(filename):

        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(Athlete(templ.pop(0), templ.pop(0), templ))

    
james = get_coach_data('james2.txt')
print(james.name + "'s fastest times are: " + str(james.top3()))

