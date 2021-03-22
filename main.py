from num2words import num2words
import os
from time import sleep

def count_votes(voted_data,candidate_list):
    total_vote_list = [sum([1 for i in voted_data.values() if i == j ]) for j in range(len(candidate_list))]

    sleep(15)
    print('Hera are your voting result\nCandidate Name\tNumber of votes')
    for i in range(len(candidate_list)):
        print(f'{candidate_list[i]}\t{total_vote_list[i]}')
    total_vote_list.pop(0)
    candidate_list.pop(0)
    winner = candidate_list[total_vote_list.index(max(total_vote_list))]
    runnerup = candidate_list[total_vote_list.index(sorted(total_vote_list)[::-1][1])]
    vote_diff = sorted(total_vote_list)[::-1][0] - sorted(total_vote_list)[::-1][1]

    print(f'!!!!Candidate {winner} has won with {vote_diff} than candidate {runnerup}!!!')

def vote_ballet(voters_list,candidate_list):
    voted_data = {key:0 for key in voters_list}
    os.system('cls')
    for key in voted_data:
        print(f' The candidate list is as follows:')
        for i in range(len(candidate_list)):
            print(f'{i} - {candidate_list[i]}\n')
        voted_data[key] = int(input(f'{key} choose a number from the above list to cast your vote:\n'))
        os.system('cls')
        print(f'Thank you {key} for casting the vote.\nYou can move on now!!!.')
        sleep(4)
        os.system('cls')
        print('Waiting for next voter...')
        sleep(15)
        os.system('cls')
    count_votes(voted_data,candidate_list)

def start_voter_list(candidates_list):
    number_of_voters = int(input('Enter the total number of voters:\t'))
    os.system('cls')
    if number_of_voters > 0:
        voters_list = [input(f'Enter the name of {num2words(i+1, to="ordinal_num")} voter:\t') for i in range(number_of_voters)]
        os.system('cls')
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
    os.system('cls')
    if candidates_number>0:
        print('!!The 0\'th candidate should be named !!"NOTA"!!!!')
        candidates_list = [input(f'Enter the name of {num2words(i, to="ordinal_num")} Candidate:\t') for i in range(candidates_number+1)]
        os.system('cls')

        if '' not in candidates_list:
            start_voter_list(candidates_list)
        else:
            print('Candidates list can\'t be empty')
            start_election()
    else:
        print('The number of candidates can\'t be empty or zero!!!')
        start_election()

start_election()
