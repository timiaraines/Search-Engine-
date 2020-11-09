from search import title_to_info, keyword_to_titles, search, article_info, article_length, title_timestamp, favorite_author, multiple_keywords, display_result
from search_tests_helper import print_basic, print_advanced, print_advanced_option, get_print
from wiki import article_metadata, title_to_info_map, keyword_to_titles_map
from unittest.mock import patch
from copy import deepcopy

# List of all available article titles for this search engine
# The benefit of using this is faster code - these functions will execute
# every time it gets called, but if the return value of it gets stored it into
# a variable, the function will not need to run every time the list of available
# articles is needed.
METADATA = article_metadata()
TITLE_TO_INFO = title_to_info_map()
KEYWORD_TO_TITLES = keyword_to_titles_map()

# Storing into a variable so don't need to copy and paste long list every time
DOG = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']

TRAVEL = ['Time travel']

MUSIC = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', '2009 in music', 'Rock music', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', '2006 in music', 'Tony Kaye (musician)', 'Texture (music)', '2007 in music', '2008 in music']

PROGRAMMING = ['C Sharp (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Covariance and contravariance (computer science)', 'Personal computer', 'Ruby (programming language)']

SOCCER = ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']

PHOTO = ['Digital photography']

SCHOOL = ['Edogawa, Tokyo', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)']

PLACE = ['2009 in music', 'List of dystopian music, TV programs, and games', '2006 in music', '2007 in music', '2008 in music']

DANCE = ['List of Canadian musicians', '2009 in music', 'Old-time music', '1936 in music', 'Indian classical music']

def test_example_title_to_info_tests():
    ''' Tests for title_to_info(), function #1. '''
    # Example tests, these do not count as your tests
    assert title_to_info(METADATA) == TITLE_TO_INFO

    # Create fake metadata to test
    fake_metadata = [['an article title', 'andrea', 1234567890, 103, ['some', 'words', 'that', 'make', 'up', 'sentence']],
                     ['another article title', 'helloworld', 987123456, 8029, ['more', 'words', 'could', 'make', 'sentences']]]

    # Expected value of title_to_info with fake_metadata
    expected = {'an article title': {'author': 'andrea', 'timestamp': 1234567890, 'length': 103}, 
                'another article title': {'author': 'helloworld', 'timestamp': 987123456, 'length': 8029}}
    assert title_to_info(deepcopy(fake_metadata)) == expected

def test_example_keyword_to_titles_tests():
    ''' Tests for keyword_to_titles(), function #2. '''
    # Function #2
    assert keyword_to_titles(METADATA) == KEYWORD_TO_TITLES

    # Create fake metadata to test
    fake_metadata = [['an article title', 'andrea', 1234567890, 103, ['some', 'words', 'that', 'make', 'up', 'sentence']],
                     ['another article title', 'helloworld', 987123456, 8029, ['more', 'words', 'could', 'make', 'sentences']]]

    # Expected value of keyword_to_titles with fake_metadata
    expected = {'some': ['an article title'], 'words': ['an article title', 'another article title'], 'that': ['an article title'], 'make': ['an article title', 'another article title'], 'up': ['an article title'], 'sentence': ['an article title'], 'more': ['another article title'], 'could': ['another article title'], 'sentences': ['another article title']}

    assert keyword_to_titles(deepcopy(fake_metadata)) == expected

def test_example_unit_tests():
    # Example tests, these do not count as your tests

    # Basic search, function #3
    assert search('dog') == DOG

    # Advanced search option 1, function #4
    expected = {'Black dog (ghost)': {'author': 'SmackBot', 'timestamp': 1220471117, 'length': 14746}, 'Mexican dog-faced bat': {'author': 'AnomieBOT', 'timestamp': 1255316429, 'length': 1138}, 'Dalmatian (dog)': {'author': 'J. Spencer', 'timestamp': 1207793294, 'length': 26582}, 'Guide dog': {'author': 'Sarranduin', 'timestamp': 1165601603, 'length': 7339}, 'Sun dog': {'author': 'Hellbus', 'timestamp': 1208969289, 'length': 18050}}
    assert article_info(deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 2, function #5
    expected = ['Mexican dog-faced bat', 'Guide dog']
    assert article_length(8000, deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 3, function #6
    expected = {'Black dog (ghost)': 1220471117, 'Mexican dog-faced bat': 1255316429, 'Dalmatian (dog)': 1207793294, 'Guide dog': 1165601603, 'Sun dog': 1208969289}
    assert title_timestamp(deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 4, function #7
    assert favorite_author('J. Spencer', deepcopy(DOG), TITLE_TO_INFO) == True
    assert favorite_author('Andrea', deepcopy(DOG), TITLE_TO_INFO) == False

    # Advanced search option 5, function #8
    expected = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']
    assert multiple_keywords('soccer', deepcopy(DOG)) == expected

# For all integration test functions, remember to put in patch so input() gets mocked out
@patch('builtins.input')
def test_example_integration_test(input_mock):
    keyword = 'dog'
    advanced_option = 2
    advanced_response = 8000

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Mexican dog-faced bat', 'Guide dog']\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected

# TODO Write tests below this line. Do not remove.
def test_title_to_info_boyband():
    ''' Tests for title_to_info(), function #1. '''
    assert title_to_info(METADATA) == TITLE_TO_INFO

    # Create fake metadata to test
    boyband_metadata = [['boyband crazy', 'sza', 1234567890, 9000, ['boy', 'band', 'sing', 'dance', 'cute', 'love']],
                     ['surfaces', 'surface_lover123', 9877485456, 80009, ['new', 'boyband', 'singers', 'tour', 'dancer']]]

    # Expected value of title_to_info with boyband_metadata
    expected = {'boyband crazy': {'author': 'sza', 'timestamp': 1234567890, 'length': 9000}, 
                'surfaces': {'author': 'surface_lover123', 'timestamp': 9877485456, 'length': 80009}}
    assert title_to_info(deepcopy(boyband_metadata)) == expected

def test_title_to_info_cartoon():
    ''' Tests for title_to_info(), function #1. '''
    assert title_to_info(METADATA) == TITLE_TO_INFO

    # Create fake metadata to test
    cartoon_metadata = [['chowder', 'cartoon network', 45678904321, 1200, ['cartoon', 'kids', 'shows', 'entertainment', 'food', 'funny']],
                     ['loud house', 'nickelodeon', 9432176483, 800, ['kids', 'cartoon', 'entertainment', 'funny', 'family']]]

    # Expected value of title_to_info with fake_metadata
    expected = {'chowder': {'author': 'cartoon network', 'timestamp': 45678904321, 'length': 1200}, 
                'loud house': {'author': 'nickelodeon', 'timestamp': 9432176483, 'length': 800}}
    assert title_to_info(deepcopy(cartoon_metadata)) == expected
    
def test_title_to_info_food():
    ''' Tests for title_to_info(), function #1. '''
    assert title_to_info(METADATA) == TITLE_TO_INFO

    # Create fake metadata to test
    food_metadata = [['chips', 'lays', 4563211234, 3245, ['snacks', 'food', 'lays', 'dish', 'fried', 'yummy']],
                     ['chicken dinners in 10', 'young mom', 943543215, 7654, ['food', 'chicken', 'easy', 'yummy', 'family']]]

    # Expected value of title_to_info with fake_metadata
    expected = {'chips': {'author': 'lays', 'timestamp': 4563211234, 'length': 3245}, 
                'chicken dinners in 10': {'author': 'young mom', 'timestamp': 943543215, 'length': 7654}}
    assert title_to_info(deepcopy(food_metadata)) == expected
    

def test_keyword_to_titles_boyband():
    ''' Tests for keyword_to_titles(), function #2. '''
    # Function #2
    assert keyword_to_titles(METADATA) == KEYWORD_TO_TITLES

    # Create fake metadata to test
    boyband_metadata = [['boyband crazy', 'sza', 1234567890, 9000, ['boy', 'band', 'sing', 'dance', 'cute', 'love']],
                     ['surfaces', 'surface_lover123', 9877485456, 80009, ['new', 'band', 'singers', 'tour', 'dance']]]

    # Expected value of keyword_to_titles with cartoon_metadata
    expected = {'boy': ['boyband crazy'], 'band': ['boyband crazy', 'surfaces'], 'sing': ['boyband crazy'], 'dance': ['boyband crazy', 'surfaces'], 'cute': ['boyband crazy'], 'love': ['boyband crazy'], 'new': ['surfaces'], 'singers': ['surfaces'], 'tour': ['surfaces']}

    assert keyword_to_titles(deepcopy(boyband_metadata)) == expected
    
def test_keyword_to_titles_cartoon():
    ''' Tests for keyword_to_titles(), function #2. '''
    # Function #2
    assert keyword_to_titles(METADATA) == KEYWORD_TO_TITLES

    # Create fake metadata to test
    cartoon_metadata = [['chowder', 'cartoon network', 45678904321, 1200, ['cartoon', 'kids', 'shows', 'entertainment', 'food', 'funny']],
                     ['loud house', 'nickelodeon', 9432176483, 800, ['kids', 'cartoon', 'entertainment', 'funny', 'family']]]

    # Expected value of keyword_to_titles with food_metadata
    expected = {'cartoon': ['chowder', 'loud house'], 'kids': ['chowder', 'loud house'], 'shows': ['chowder'], 'entertainment': ['chowder', 'loud house'], 'food': ['chowder'], 'funny': ['chowder', 'loud house'], 'family': ['loud house']}
    
    assert keyword_to_titles(deepcopy(cartoon_metadata)) == expected

def test_keyword_to_titles_food():
    ''' Tests for keyword_to_titles(), function #2. '''
    # Function #2
    assert keyword_to_titles(METADATA) == KEYWORD_TO_TITLES

    # Create fake metadata to test
    food_metadata = [['chips', 'lays', 4563211234, 3245, ['snacks', 'food', 'lays', 'dish', 'fried', 'yummy']],
                     ['chicken dinners in 10', 'young mom', 943543215, 7654, ['food', 'chicken', 'easy', 'yummy', 'family']]]

    # Expected value of keyword_to_titles with boyband_metadata
    expected = {'snacks': ['chips'], 'food': ['chips', 'chicken dinners in 10'], 'lays': ['chips'], 'dish': ['chips'], 'fried' : ['chips'], 'yummy': ['chips', 'chicken dinners in 10'], 'chicken': ['chicken dinners in 10'], 'easy': ['chicken dinners in 10'], 'family': ['chicken dinners in 10']}
    
    assert keyword_to_titles(deepcopy(food_metadata)) == expected
    
def test_unit_travel():

    # Basic search, function #3
    assert search('travel') == TRAVEL

    # Advanced search option 1, function #4
    expected = {'Time travel': {'author': 'Thug outlaw69', 'timestamp': 1140826049, 'length': 35170}}
    assert article_info(deepcopy(TRAVEL), TITLE_TO_INFO) == expected

    # Advanced search option 2, function #5
    expected = ['Time travel']
    assert article_length(48000, deepcopy(TRAVEL), TITLE_TO_INFO) == expected

    # Advanced search option 3, function #6
    expected = {'Time travel': 1140826049}
    assert title_timestamp(deepcopy(TRAVEL), TITLE_TO_INFO) == expected

    # Advanced search option 4, function #7
    assert favorite_author('Thug outlaw69', deepcopy(TRAVEL), TITLE_TO_INFO) == True
    assert favorite_author('Miazaa', deepcopy(TRAVEL), TITLE_TO_INFO) == False

    # Advanced search option 5, function #8
    expected = ['Time travel', 'Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']
    assert multiple_keywords('Dog', deepcopy(TRAVEL)) == expected
    
def test_unit_music():

    # Basic search, function #3
    assert search('MusIc') == MUSIC

    # Advanced search option 1, function #4
    expected = {'List of Canadian musicians': {'author': 'Bearcat', 'timestamp': 1181623340, 'length': 21023}, 'French pop music': {'author': 'Brandon', 'timestamp': 1172208041, 'length': 5569}, 'Noise (music)': {'author': 'Epbr123', 'timestamp': 1194207604, 'length': 15641}, '1922 in music': {'author': 'Jafeluv', 'timestamp': 1242717698, 'length': 11576}, '1986 in music': {'author': 'Michael', 'timestamp': 1048918054, 'length': 6632}, 'Kevin Cadogan': {'author': 'Renesis', 'timestamp': 1144136316, 'length': 3917}, '2009 in music': {'author': 'SE KinG', 'timestamp': 1235133583, 'length': 69451}, 'Rock music': {'author': 'Sabrebd', 'timestamp': 1258069053, 'length': 119498}, 'Lights (musician)': {'author': 'Espo3699', 'timestamp': 1213914297, 'length': 5898}, 'Tim Arnold (musician)': {'author': 'Sohohobo', 'timestamp': 1181480380, 'length': 4551}, 'Old-time music': {'author': 'Badagnani', 'timestamp': 1124771619, 'length': 12755}, 'Arabic music': {'author': 'Badagnani', 'timestamp': 1209417864, 'length': 25114}, 'Joe Becker (musician)': {'author': 'Gary King', 'timestamp': 1203234507, 'length': 5842}, 'Richard Wright (musician)': {'author': 'Bdubiscool', 'timestamp': 1189536295, 'length': 16185}, 'Voice classification in non-classical music': {'author': 'Iridescent', 'timestamp': 1198092852, 'length': 11280}, '1936 in music': {'author': 'JohnRogers', 'timestamp': 1243745950, 'length': 23417}, '1962 in country music': {'author': 'Briguy52748', 'timestamp': 1249862464, 'length': 7954}, 'List of dystopian music, TV programs, and games': {'author': 'Notinasnaid', 'timestamp': 1165317338, 'length': 13458}, 'Steve Perry (musician)': {'author': 'Woohookitty', 'timestamp': 1254812045, 'length': 22204}, 'David Gray (musician)': {'author': 'RattleandHum', 'timestamp': 1159841492, 'length': 7203}, 'Alex Turner (musician)': {'author': 'CambridgeBayWeather', 'timestamp': 1187010135, 'length': 9718}, 'List of gospel musicians': {'author': 'Absolon', 'timestamp': 1197658845, 'length': 3805}, 'Indian classical music': {'author': 'Davydog', 'timestamp': 1222543238, 'length': 9503}, '1996 in music': {'author': 'Kharker', 'timestamp': 1148585201, 'length': 21688}, 'Traditional Thai musical instruments': {'author': 'Badagnani', 'timestamp': 1191830919, 'length': 6775}, '2006 in music': {'author': 'Suduser85', 'timestamp': 1171547747, 'length': 105280}, 'Tony Kaye (musician)': {'author': 'Bondegezou', 'timestamp': 1141489894, 'length': 8419}, 'Texture (music)': {'author': 'J Lorraine', 'timestamp': 1161070178, 'length': 3626}, '2007 in music': {'author': 'Squilly', 'timestamp': 1169248845, 'length': 45652}, '2008 in music': {'author': 'Ba11innnn', 'timestamp': 1217641857, 'length': 107605}}
    assert article_info(deepcopy(MUSIC), TITLE_TO_INFO) == expected

    # Advanced search option 2, function #5
    expected = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', 'Tony Kaye (musician)', 'Texture (music)']
    assert article_length(28000, deepcopy(MUSIC), TITLE_TO_INFO) == expected

    # Advanced search option 3, function #6
    expected = {'List of Canadian musicians': 1181623340, 'French pop music': 1172208041, 'Noise (music)': 1194207604, '1922 in music': 1242717698, '1986 in music': 1048918054, 'Kevin Cadogan': 1144136316, '2009 in music': 1235133583, 'Rock music': 1258069053, 'Lights (musician)': 1213914297, 'Tim Arnold (musician)': 1181480380, 'Old-time music': 1124771619, 'Arabic music': 1209417864, 'Joe Becker (musician)': 1203234507, 'Richard Wright (musician)': 1189536295, 'Voice classification in non-classical music': 1198092852, '1936 in music': 1243745950, '1962 in country music': 1249862464, 'List of dystopian music, TV programs, and games': 1165317338, 'Steve Perry (musician)': 1254812045, 'David Gray (musician)': 1159841492, 'Alex Turner (musician)': 1187010135, 'List of gospel musicians':  1197658845, 'Indian classical music': 1222543238, '1996 in music':  1148585201, 'Traditional Thai musical instruments':  1191830919, '2006 in music': 1171547747, 'Tony Kaye (musician)': 1141489894, 'Texture (music)': 1161070178, '2007 in music': 1169248845, '2008 in music': 1217641857}
    assert title_timestamp(deepcopy(MUSIC), TITLE_TO_INFO) == expected

    # Advanced search option 4, function #7
    assert favorite_author('Squilly', deepcopy(MUSIC), TITLE_TO_INFO) == True
    assert favorite_author('A2chainz', deepcopy(MUSIC), TITLE_TO_INFO) == False

    # Advanced search option 5, function #8
    expected = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', '2009 in music', 'Rock music', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', '2006 in music', 'Tony Kaye (musician)', 'Texture (music)', '2007 in music', '2008 in music', 'List of Canadian musicians', '2009 in music', 'Old-time music', '1936 in music', 'Indian classical music']
    assert multiple_keywords('dance', deepcopy(MUSIC)) == expected

def test_unit_programming():

    # Basic search, function #3
    assert search('PROGRAMMING') == PROGRAMMING

    # Advanced search option 1, function #4
    expected = {'C Sharp (programming language)': {'author': 'Eaglizard', 'timestamp': 1232492672, 'length': 52364}, 'Python (programming language)': {'author': 'Lulu of the Lotus-Eaters', 'timestamp': 1137530195, 'length': 41571}, 'Lua (programming language)': {'author': 'Makkuro', 'timestamp': 1113957128, 'length': 0}, 'Covariance and contravariance (computer science)': {'author': 'Wakapop', 'timestamp': 1167547364, 'length': 7453}, 'Personal computer': {'author': 'Darklock', 'timestamp': 1220391790, 'length': 45663}, 'Ruby (programming language)': {'author': 'Hervegirod', 'timestamp': 1193928035, 'length': 30284}}
    assert article_info(deepcopy(PROGRAMMING), TITLE_TO_INFO) == expected

    # Advanced search option 2, function #5
    expected = ['Lua (programming language)']
    assert article_length(0, deepcopy(PROGRAMMING), TITLE_TO_INFO) == expected

    # Advanced search option 3, function #6
    expected = {'C Sharp (programming language)': 1232492672, 'Python (programming language)': 1137530195, 'Lua (programming language)': 1113957128, 'Covariance and contravariance (computer science)': 1167547364, 'Personal computer': 1220391790, 'Ruby (programming language)': 1193928035}
    assert title_timestamp(deepcopy(PROGRAMMING), TITLE_TO_INFO) == expected

    # Advanced search option 4, function #7
    assert favorite_author('Wakapop', deepcopy(PROGRAMMING), TITLE_TO_INFO) == True
    assert favorite_author('Louis Fitz', deepcopy(PROGRAMMING), TITLE_TO_INFO) == False

    # Advanced search option 5, function #8
    expected = ['C Sharp (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Covariance and contravariance (computer science)', 'Personal computer', 'Ruby (programming language)', 'Edogawa, Tokyo', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)']
    assert multiple_keywords('SCHOOL', deepcopy(PROGRAMMING)) == expected
    
def test_unit_empty():

    # Basic search, function #3
    assert search('') == []

    # Advanced search option 1, function #4
    expected = {}
    assert article_info(deepcopy([]), TITLE_TO_INFO) == expected

    # Advanced search option 2, function #5
    expected = []
    assert article_length(0, deepcopy([]), TITLE_TO_INFO) == expected

    # Advanced search option 3, function #6
    expected = {}
    assert title_timestamp(deepcopy([]), TITLE_TO_INFO) == expected

    # Advanced search option 4, function #7
    assert favorite_author('Louis Fitz', deepcopy([]), TITLE_TO_INFO) == False

    # Advanced search option 5, function #8
    expected = ['Edogawa, Tokyo', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)']
    assert multiple_keywords('SCHOOL', deepcopy([])) == expected

@patch('builtins.input')
def test_integration_travel(input_mock):
    keyword = 'TrAvEl'
    advanced_option = 2
    advanced_response = 0

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected

@patch('builtins.input')
def test_integration_music(input_mock):
    keyword = 'music'
    advanced_option = 4
    advanced_response = "Timia ZoAnn"

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', '2009 in music', 'Rock music', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', '2006 in music', 'Tony Kaye (musician)', 'Texture (music)', '2007 in music', '2008 in music']\nYour favorite author is not in the returned articles!\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected
    
@patch('builtins.input')
def test_integration_programming(input_mock):
    keyword = 'PROGRAMMING'
    advanced_option = 5
    advanced_response = 'photo'

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['C Sharp (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Covariance and contravariance (computer science)', 'Personal computer', 'Ruby (programming language)', 'Digital photography']\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected


# Write tests above this line. Do not remove.

# This automatically gets called when this file runs - this is how Python works.
# To make all tests run, call all test functions inside the if statement.
if __name__ == "__main__":
    # TODO Call all your test functions here
    # Follow the correct indentation as these two examples
    # As you're done with each function, uncomment the example test functions
    # and make sure they pass
    test_example_title_to_info_tests()
    test_title_to_info_boyband()
    test_title_to_info_food()
    test_title_to_info_cartoon()
    test_example_keyword_to_titles_tests()
    test_keyword_to_titles_boyband()
    test_keyword_to_titles_cartoon()
    test_keyword_to_titles_food()
    test_example_unit_tests()
    test_unit_travel()
    test_unit_music()
    test_unit_programming()
    test_unit_empty()
    test_example_integration_test()
    test_integration_travel()
    test_integration_music()
    test_integration_programming()
