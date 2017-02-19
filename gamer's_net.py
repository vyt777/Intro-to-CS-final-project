# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
# 
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
# 
# Note that each sentence will be separated from the next by only a period. There will 
# not be whitespace or new lines between sentences.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below. 
# 
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not 
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
# 
# Return:
#   The newly created network data structure
def names(example_input):
    list_of_names=[]
    example_input =example_input.replace('.', '. ')
    list_of_input=example_input.split()
    for e in list_of_input:
        if e =='is':
            list_of_names.append(list_of_input[list_of_input.index(e)-1])
            list_of_input.remove(e)
    return list_of_names


def nullnet(list_of_names):
    net={}
    for e in list_of_names:
        net[e]={}
    return net


def connections_in_net(example_input, list_of_names, net):
    last_ind=0
    for name in list_of_names:
        name_index=example_input[last_ind:].find(name)+len(name)+last_ind
        sample= ' is connected to ' 
        start_ind=example_input[name_index:].find(sample) + len(sample) + name_index
        last_ind=example_input[start_ind:].find('.')+start_ind
        connections =example_input[start_ind:last_ind]
        connections = connections.split(', ')
        net[name]['connections']=connections
    return net


def games_in_net(example_input, list_of_names, net):
    last_ind=0
    for name in list_of_names:
        name_index=example_input[last_ind:].find(name)+len(name)+last_ind
        sample=' likes to play '
        start_ind=example_input[name_index:].find(sample) + len(sample) + name_index
        last_ind=example_input[start_ind:].find('.')+start_ind
        games=example_input[start_ind:last_ind]
        games= games.split(', ')
        net[name]['games']=games
    return net


def create_data_structure(example_input):
    list_of_names=names(example_input)
    nulnet_end=nullnet(list_of_names)
    net_conn=connections_in_net(example_input, list_of_names, nulnet_end)
    net= games_in_net(example_input, list_of_names, net_conn)
    return net

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.
def get_connections(net, user):
    if user in net:
        if 'connections' in net[user]:
            return net[user]['connections']
        else:
            return []
    else: 
        return None

# ----------------------------------------------------------------------------- 
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(net, user):
    if user in net:
        if 'games' in net[user]:
            return net[user]['games']
        else:
            return []
    else: 
        return None

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(net, user_A, user_B):
    if user_A in net and user_B in net:
        if 'connections' in net[user_A]:
            if user_B not in net[user_A]['connections']:
                net[user_A]['connections']+=[user_B]
            else:
                return net
        else:
            net[user_A]['connections']=[user_B]
    else:
        return False
    return net

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(net, user, games):
    if user in net:
        return net
    else:
        net[user] = {'connections': [], 'games': games}
    return net

# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
def clean_list(dirty_list):
    for name in dirty_list:
        while dirty_list.count(name)>1:
            dirty_list.remove(name)
    return dirty_list

def get_secondary_connections(net, user):
    secondary_conn=[]
    if user in net:
        for name in net[user]['connections']:
            secondary_conn+=net[name]['connections']
        return clean_list(secondary_conn)
    else:
        return None


# ----------------------------------------------------------------------------- 	
# count_common_connections(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def count_common_connections(net, user_A, user_B):
    if user_A not in net or user_B not in net:
        return False
    list_all_conn=net[user_A]['connections']+ net[user_B]['connections']
    list_occur_conn=[]
    for name in list_all_conn:
        if list_all_conn.count(name)>1:
            list_occur_conn+=[name]
            list_all_conn.remove(name)
    return len(list_occur_conn)

# ----------------------------------------------------------------------------- 
# find_path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print find_path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.

# checking if graph node is explored (that means this node has no branches to node that we looking for)
def is_explored(net, user):
    num_visited=0
    for name in net[user]['connections']:
        if 'visited' in net[name]:
            num_visited+=1
    if num_visited == len(net[user]['connections']):
        return True
    return False

def num_conn_user(net, user):
    names_in_conn=[]
    for name in net:
        if name is not 'path':
            names_in_conn+=net[name]['connections']
    num_names= names_in_conn.count(user)
    return num_names

def rev_find_path_to_friend(net, user_A, user_B):
    # if users not in net we can't find way between them
    if user_A not in net or user_B not in net:
        return None    
    if is_explored(net, user_A):
        net[user_A].update({'explored':'explored'})
        return []
    net['path']=[]
    # implementing the loop count to prevent infinite loop
    if 'visited' not in net[user_A]:
        net[user_A].update({'visited':0})
    net[user_A]['visited']+=1     
    if net[user_A]['visited']> num_conn_user(net, user_A):
        net[user_A]['visited']=0
        return []
    # if user at the end of graph is in connections of user we are searching from - we found the way between them
    if user_B in net[user_A]['connections']:
        net['path']+=[user_B]
        net['path']+=[user_A]
        return net['path']
    # implementing recursive search algorithm
    for name in net[user_A]['connections']:
        net['path']+= rev_find_path_to_friend(net, name, user_B)
        if user_B in net['path']:
            net['path']+=[user_A]
            return net['path']
    return net['path']

# reversing path due to project description requirements
def find_path_to_friend(net, user_A, user_B):
    path=rev_find_path_to_friend(net, user_A, user_B)
    if path==[] or path==None:
        return None
    return path[::-1]

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

def add_location(net, user, location):
    net[user] = {'location': [location]}
    return net


# This is such a simple procedure, so I created another one. Next procedure returns the number of 
# user's connection's. It takes net and username as input. If such user has no connections it returns "None".
def number_connections(net, user):
    if 'connections' in net[user]:
        return len(net[user]['connections'])
    else:
        return None

net = create_data_structure(example_input)
#Testing area
#print net
#print get_connections(net, "Debra")
#print get_connections(net, "Mercedes")
#print get_games_liked(net, "John")
#print add_connection(net, "John", "Freda")
#print add_new_user(net, "Debra", []) 
#print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
#print get_secondary_connections(net, "Mercedes")
#print count_common_connections(net, "Mercedes", "John")
#print find_path_to_friend(net, "John", "Ollie")
