from search import search, title_length, article_count, random_article, favorite_article, multiple_keywords, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_titles
from unittest.mock import patch

# List of all available article titles for this search engine
# The benefit of using this is faster code - article_titles() will execute
# every time it gets called, but if the return value of it gets stored it into
# a variable, the function will not need to run every time the list of available
# articles is needed.
ARTICLE_TITLES = article_titles()

def test_example_unit_tests():
    # Storing into a variable so don't need to copy and paste long list every time
    # If you want to store search results into a variable like this, make sure you pass a copy of it when
    # calling a function, otherwise the original list (ie the one stored in your variable) is going to be
    # mutated. To make a copy, you may use the .copy() function for the variable holding your search result.
    dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']

    # Example tests, these do not count as your tests

    # Basic search, function #1
    assert search('dog') == dog_search_results

    # Advanced search option 1, function #2
    expected = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Landseer (dog)']
    assert title_length(25, dog_search_results.copy()) == expected

    # Advanced search option 2, function #3
    assert article_count(3, dog_search_results.copy()) == ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid']

    # Advanced search option 3, function #4
    assert random_article(3, dog_search_results.copy()) == 'Black dog (ghost)'

    # Advanced search option 4, function #5
    assert favorite_article('Guide dog', dog_search_results.copy()) == True

    # Advanced search option 5, function #6
    expected = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'USC Trojans volleyball', 'Mets de Guaynabo (volleyball)']
    assert multiple_keywords('volleyball', dog_search_results.copy()) == expected

# For all integration test functions, remember to put in patch so input() gets mocked out
@patch('builtins.input')
def test_example_integration_test(input_mock):
    keyword = 'dog'
    advanced_option = 1
    advanced_response = 25

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: [\'Edogawa, Tokyo\', \'Kevin Cadogan\', \'Endogenous cannabinoid\', \'Black dog (ghost)\', \'2007 Bulldogs RLFC season\', \'Mexican dog-faced bat\', \'Dalmatian (dog)\', \'Guide dog\', \'Georgia Bulldogs football\', \'Endoglin\', \'Sun dog\', \'The Mandogs\', \'Landseer (dog)\']\n'

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected

# TODO Write tests below this line. Do not remove.

def test_unit_test_volleyball():
    volleyball_search_results = ['USC Trojans volleyball', 'Mets de Guaynabo (volleyball)']

    # Basic search, function #1
    assert search('volleyball') == volleyball_search_results

    # Advanced search option 1, function #2
    expected = ['USC Trojans volleyball', 'Mets de Guaynabo (volleyball)']
    assert title_length(50, volleyball_search_results.copy()) == expected

    # Advanced search option 2, function #3
    assert article_count(1, volleyball_search_results.copy()) == ['USC Trojans volleyball']

    # Advanced search option 3, function #4
    assert random_article(1, volleyball_search_results.copy()) == 'Mets de Guaynabo (volleyball)'

    # Advanced search option 4, function #5
    assert favorite_article('volleyball in the valley', volleyball_search_results.copy()) == False

    # Advanced search option 5, function #6
    expected = ['USC Trojans volleyball', 'Mets de Guaynabo (volleyball)', 'Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)', 'Craig Martin (soccer)', "United States men's national soccer team 2009 results", 'China national soccer team', "Wake Forest Demon Deacons men's soccer"]
    assert multiple_keywords('soccer', volleyball_search_results.copy()) == expected

def test_unit_test_music():
    music_search_results = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'List of overtone musicians', 'Tim Arnold (musician)', 'Peter Brown (music industry)', 'Old-time music', 'Arabic music', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Annie (musical)', 'Alex Turner (musician)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Indian classical music', '1996 in music', 'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'English folk music (1500–1899)', 'David Levi (musician)', 'George Crum (musician)', 'Traditional Thai musical instruments', 'Charles McPherson (musician)', 'Les Cousins (music club)', 'Paul Carr (musician)', '2006 in music', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Texture (music)', 'Register (music)', '2007 in music', '2008 in music']


    # Basic search, function #1
    assert search('music') == music_search_results

    # Advanced search option 1, function #2
    expected = ['Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Old-time music', 'Arabic music', 'Aco (musician)', '1936 in music', '1996 in music', '2006 in music', '2007 in music', '2008 in music']
    assert title_length(14, music_search_results.copy()) == expected

    # Advanced search option 2, function #3
    assert article_count(15, music_search_results.copy()) == ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'List of overtone musicians', 'Tim Arnold (musician)', 'Peter Brown (music industry)', 'Old-time music', 'Arabic music']

    # Advanced search option 3, function #4
    assert random_article(13, music_search_results.copy()) == 'Old-time music'

    # Advanced search option 4, function #5
    assert favorite_article('Rock music', music_search_results.copy()) == True

    # Advanced search option 5, function #6
    expected = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'List of overtone musicians', 'Tim Arnold (musician)', 'Peter Brown (music industry)', 'Old-time music', 'Arabic music', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Annie (musical)', 'Alex Turner (musician)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Indian classical music', '1996 in music', 'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'English folk music (1500–1899)', 'David Levi (musician)', 'George Crum (musician)', 'Traditional Thai musical instruments', 'Charles McPherson (musician)', 'Les Cousins (music club)', 'Paul Carr (musician)', '2006 in music', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Texture (music)', 'Register (music)', '2007 in music', '2008 in music', 'Digital photography', 'Wildlife photography']
    assert multiple_keywords('photography', music_search_results.copy()) == expected

def test_unit_test_programming():
    programming_search_results = ['C Sharp (programming language)', 'Reflection-oriented programming', 'B (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Comparison of programming languages (basic instructions)', 'Ruby (programming language)', 'Semaphore (programming)']

    # Basic search, function #1
    assert search('programming') == programming_search_results

    # Advanced search option 1, function #2
    expected = ['C Sharp (programming language)', 'B (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Ruby (programming language)', 'Semaphore (programming)']
    assert title_length(30, programming_search_results.copy()) == expected

    # Advanced search option 2, function #3
    assert article_count(6, programming_search_results.copy()) == ['C Sharp (programming language)', 'Reflection-oriented programming', 'B (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Comparison of programming languages (basic instructions)']

    # Advanced search option 3, function #4
    assert random_article(6, programming_search_results.copy()) == 'Ruby (programming language)'

    # Advanced search option 4, function #5
    assert favorite_article('programming for dummies', programming_search_results.copy()) == False

    # Advanced search option 5, function #6
    expected = ['C Sharp (programming language)', 'Reflection-oriented programming', 'B (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Comparison of programming languages (basic instructions)', 'Ruby (programming language)', 'Semaphore (programming)', 'USC Trojans volleyball', 'Mets de Guaynabo (volleyball)']
    assert multiple_keywords('volleyball', programming_search_results.copy()) == expected

def test_unit_test_photography():
    photography_search_results = ['Digital photography', 'Wildlife photography']

    # Basic search, function #1
    assert search('photography') == photography_search_results

    # Advanced search option 1, function #2
    expected = ['Digital photography', 'Wildlife photography']
    assert title_length(40, photography_search_results.copy()) == expected

    # Advanced search option 2, function #3
    assert article_count(5, photography_search_results.copy()) == ['Digital photography', 'Wildlife photography']

    # Advanced search option 3, function #4
    assert random_article(3, photography_search_results.copy()) == ''

    # Advanced search option 4, function #5
    assert favorite_article('photography and the world', photography_search_results.copy()) == False

    # Advanced search option 5, function #6
    expected = ['Digital photography', 'Wildlife photography', 'C Sharp (programming language)', 'Reflection-oriented programming', 'B (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Comparison of programming languages (basic instructions)', 'Ruby (programming language)', 'Semaphore (programming)']
    assert multiple_keywords('programming', photography_search_results.copy()) == expected


def test_unit_test_soccer():
    soccer_search_results = ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)', 'Craig Martin (soccer)', "United States men's national soccer team 2009 results", 'China national soccer team', "Wake Forest Demon Deacons men's soccer"]

    # Basic search, function #1
    assert search('soccer') == soccer_search_results

    # Advanced search option 1, function #2
    expected = ['Will Johnson (soccer)', 'Steven Cohen (soccer)', 'Craig Martin (soccer)']
    assert title_length(21, soccer_search_results.copy()) == expected

    # Advanced search option 2, function #3
    assert article_count(4, soccer_search_results.copy()) == ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)', 'Craig Martin (soccer)']

    # Advanced search option 3, function #4
    assert random_article(6, soccer_search_results.copy()) == "Wake Forest Demon Deacons men's soccer"

    # Advanced search option 4, function #5
    assert favorite_article('Will Johnson (soccer)', soccer_search_results.copy()) == True

    # Advanced search option 5, function #6
    expected = ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)', 'Craig Martin (soccer)', "United States men's national soccer team 2009 results", 'China national soccer team', "Wake Forest Demon Deacons men's soccer", 'USC Trojans volleyball', 'Mets de Guaynabo (volleyball)']
    assert multiple_keywords('volleyball', soccer_search_results.copy()) == expected

@patch('builtins.input')
def test_wiki_search_volleyball(input_mock):
    keyword = 'volleyball'
    advanced_option = 2
    advanced_response = 2

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: [\'USC Trojans volleyball\', \'Mets de Guaynabo (volleyball)\']\n'
    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected

@patch('builtins.input')
def test_wiki_search_soccer(input_mock):
    keyword = 'soccer'
    advanced_option = 3
    advanced_response = 5

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: China national soccer team\n'

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected
# Write tests above this line. Do not remove.

# This automatically gets called when this file runs - this is how Python works.
# To actually make all your tests run, call all of your test functions here.
if __name__ == "__main__":
    # TODO Call all your test functions here
    test_unit_test_volleyball()
    test_unit_test_music()
    test_unit_test_photography()
    test_unit_test_programming()
    test_unit_test_soccer()
    test_wiki_search_volleyball()
    test_wiki_search_soccer()
    # Follow the correct indentation as these two examples
    test_example_unit_tests()
    test_example_integration_test()