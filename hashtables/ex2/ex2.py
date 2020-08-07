#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # outputs array of strings
    route = [None] * length
    # create a dictionary of all tickets
    tix = {}
    for t in tickets:
        tix[t.source] = t.destination
    
    # "The crux of this problem requires us to 'link' tickets together"
    link = tix["NONE"] # first ticket

    for i in range(length):
        route[i] = link
        link = tix[link] # update the link ot the next one


    return route
