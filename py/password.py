from secrets import SystemRandom
from os import getcwd

random = SystemRandom()

def generate_password(method="random", length=None, scramble=0):
    """Generates a password.
    
    Keyword Arguments:
        method {str} -- Specifies if the password generated should be random letters and/or symbols, or if it should be generated in xkcd-style (A set number of words in sequence, with or without scrambling.) (default: {"random"})
        length {int} -- For 'random' passwords, this corresponds to the length of the password itself. For 'xkcd'-passwords, it corresponds to the number of words used. (default: {12, 4})
        scramble {int} -- Decides how many symbols should be scrambled into 'xkcd'-style passwords. (default: {0})
    
    Returns:
        str -- returns an UNENCRYPTED version of generated password. DO NOT leave it unencrypted in database.
    """

    if method == "random":
        length = 12
        possible_components = characters()
    
    if method == "xkcd":
        length = 4
        scramble = True
        possible_components = words()
    
    password = [random.choice(possible_components) for i in range(length)]
    password = "".join(password)

    if scramble > 0:
        password = fuck_it_up(password)

    return password


def fuck_it_up(password, amount=3):
    """scrambles passwords by mashing symbols into it at random locations.
    
    Arguments:
        password {str} -- string to be scrambled.
    
    Keyword Arguments:
        amount {int} -- amount of symbols to mash into password. (default: {3})
    
    Returns:
        str -- scrambled password.
    """
    password = [char for char in password]
    symbols = r"!#%&/()=?\_-:;@$}{]["

    for _ in range(amount):
        i = random.randint(0, len(password))
        symbol = random.choice(symbols)

        password.insert(i, symbol)

    return "".join(password)


def characters(include_capital_letters=True, include_symbols=True):
    """Allowed characters to feed to password.
    
    Keyword Arguments:
        include_capital_letters {bool} -- Shall it include capital letters? (recommended) (default: {True})
        include_symbols {bool} -- Shall it include symbols? (recommended) (default: {True})
    
    Returns:
        list -- List of characters allowed to be generated from.
    """
    letters = r"abcdefghijklmnopqrstuvwxyz"
    possible_chars = [char for char in letters]

    if include_capital_letters:
        possible_chars += [char for char in letters.upper()]

    if include_symbols:
        possible_chars += [symbol for symbol in r"!#%&/()=?\_-:;@$}{]["]
        
    return possible_chars


def words():
    """Creates list of the 10'000 most used english word where all words at sub-5 length has been filtered out.
    
    Returns:
        list -- Returns a list of longer words from the english language.
    """
    filename = "words.txt"
    with open(f"{getcwd()}/{filename}", encoding="utf-8") as f:
        words = f.read().split("\n")
    
    return [e for e in words if len(e) > 5]
