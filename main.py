from num2words import num2words
import os

def count_vote(voted_data,candidate_list):
    total_vote_list = [ for i in range(candidate_list) if i]

def vote_ballet(voters_list,candidate_list):
    voted_data = {key:0 for key in voters_list}
    os.system('cls')
    for key in voted_data:
        print(f' The candidate list is as follows:')
        for i in range(len(candidate_list)):
            print(f'{i} - {candidate_list[i]}\n')
        voted_data[key] = int(input(f'{key} choose a number from the above list to cast your vote:\n'))
        os.system('cls')
    count_vote(voted_data,candidate_list)






def start_voter_list(candidates_list):
    number_of_voters = int(input('Enter the total number of voters:\t'))
    if number_of_voters > 0:
        voters_list = [input(f'Enter the name of {num2words(i+1, to="ordinal_num")} voter:\t') for i in range(number_of_voters)]
        if '' not in voters_list:
            vote_ballet(voters_list,candidates_list)

        else:
            print('The Voter list Can\'t be empty')
            start_voter_list(candidates_list)


    else:
        print('The number of voters can\'t be empty or zero!!!')
        start_voter_list(candidates_list)




def start_election():
    print("!!!Welcome to the election voting program!!!")
    candidates_number = int(input('Enter the number of candidates:\t'))
    if candidates_number>0:
        candidates_list = [input(f'Enter the name of {num2words(i, to="ordinal_num")} Candidate:\t') for i in range(candidates_number)]

        if '' not in candidates_list:
            start_voter_list(candidates_list)
        else:
            print('Candidates list can\'t be empty')
            start_election()
    else:
        print('The number of candidates can\'t be empty or zero!!!')
        start_election()

start_election()
