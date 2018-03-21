# Return a custom score for dataminecup 2013
def custom_score(y, y_pred):
    return abs(y - y_pred).sum()/5111