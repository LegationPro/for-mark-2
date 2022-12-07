# ADDITIONAL UTILS

import re

def add_up_all_scores(*args):
    result = 0
    for n in list(*args):
        result += n
        
    return result

def loadScores(file_path: str):
    bowler_name = 'johnny_with_big_balls' 
    scores_cache = dict()
    scores_cache[bowler_name] = {
        'weeks': dict(
            {
                'game_1': 0,
                'game_2': 0,
                'game_3': 0,
            }
        )
    }
    
    f = open(file_path, 'r')
    count = 0
    scores = list()
    
    for line in f:
        
        for score in line.split():
            score = score.replace(',', '')
            if score.isdigit():
                scores.append(int(score))
                
        scores_cache[bowler_name]['weeks']['game_1'] = scores[0]
        scores_cache[bowler_name]['weeks']['game_2'] = scores[1]
        scores_cache[bowler_name]['weeks']['game_3'] = scores[2]
        count += 1
    
    f.close()
    
    return scores_cache[bowler_name]

def addScores(bowler_scores: dict, week: int, *args):
    n = 0
    for score in list(*args):
        n+=1
        bowler_scores['weeks'][week][f'game_{n}'] = score
    
    
def updateScore(johnny_scores: dict, week: int, game_num: str, score: int):
    johnny_scores['weeks'][week][game_num] = score

def saveScores(file_path: str, johnny_scores: dict):
    f = open(file_path, 'w')
    game_1 = johnny_scores['weeks']['game_1']
    game_2 = johnny_scores['weeks']['game_2']
    game_3 = johnny_scores['weeks']['game_3']
    
    n = johnny_scores['weeks']
    
    f.write(f'week {n}, {game_1}, {game_2}, {game_3}\n')
    f.close()
    print("ok")

def calcAverage(johnny_scores: dict):
    if len(johnny_scores['weeks']) == 0:
        return 0
        
    average_num: int = 0
    
    for week in johnny_scores['weeks']:
        scores = week['game_1'] + week['game_2'] + week['game_3']
        average_num += scores
    
    return average_num / len(johnny_scores['weeks'])

def highScore(johnny_scores: dict):
    highest = 0
    
    print("TESTING" + johnny_scores['weeks'])
    
    for week in johnny_scores['weeks']:
        game_1 = week['game_1']
        game_2 = week['game_2']
        game_3 = week['game_3']
        
        if highest < game_1:
            highest = game_1
            
        if highest < game_2:
            highest = game_2
            
        if highest < game_3:
            highest = game_3    
    
    return highest


def lowScore(johnny_scores: dict):
        lowest = 9999
        
        for week in johnny_scores['weeks']:
            game_1 = week['game_1']
            game_2 = week['game_2']
            game_3 = week['game_3']
            
            if lowest > game_1:
                lowest = game_1
                
            if lowest > game_2:
                lowest = game_2
                
            if lowest > game_3:
                lowest = game_3
        return lowest


def highSeries(johnny_scores: dict):
    highest_series = 0
    
    for week in johnny_scores['weeks']:
        current_series = week['game_1'] + week['game_2'] + week['game_3']
        
        if highest_series < current_series:
            highest_series = current_series
        
    return highest_series


def lowSeries(johnny_scores: dict):
    lowest_series = 9999
    
    for week in johnny_scores['weeks']:
        current_series = week['game_1'] + week['game_2'] + week['game_3']
        
        if lowest_series > current_series:
            lowest_series = current_series
    
    return lowest_series

def has_300_game(johnny_scores: dict):
    for week in johnny_scores['weeks']:
        game_1 = week['game_1']
        game_2 = week['game_2']
        game_3 = week['game_3']
        
        if game_1 >= 300 or game_2 >= 300 or game_3 >= 300:
            return True
    
    return False

def has_700_series(johnny_scores: dict):
    for week in johnny_scores['weeks']:
        game_1 = week['game_1']
        game_2 = week['game_2']
        game_3 = week['game_3']
    
    if game_1 >= 700 or game_2 >= 700 or game_3 >= 700:
        return True

    return False

def has_800_series(johnny_scores: dict):
    for week in johnny_scores['weeks']:
        game_1 = week['game_1']
        game_2 = week['game_2']
        game_3 = week['game_3']
    
    if game_1 >= 800 or game_2 >= 800 or game_3 >= 800:
        return True

    return False

def print_scores(title: str, johhny_scores: dict):
    output: str = "" 
    game_1 = johhny_scores['weeks']['game_1']
    game_2 = johhny_scores['weeks']['game_2']
    game_3 = johhny_scores['weeks']['game_3']
    output = output + f"{title} first game: {game_1} second game: {game_2} third game: {game_3}\n"
    
    print(output)    
    

def init():
    scores = loadScores('./scores.md')
    print_scores("test", scores)
    saveScores('./scores.md', scores)
    
if __name__ == '__main__':
    init()