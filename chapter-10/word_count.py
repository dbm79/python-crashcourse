def count_words(filename):
    '''Will count the numbers of words in text and prints the results.'''

    try:
        with open(filename, 'r') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        message = 'Sorry the file: ' + filename + ' does not exist.'
        print(message)
    else:
        '''Count approx. number of words in text'''
        words = contents.split()
        num_words = len(words)
        print('The file: ' + filename + ' has about ' + str(num_words) + ' words.')

file = 'alice.txt'
count_words(file)
