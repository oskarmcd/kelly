import random
import plotly.plotly as py
from plotly.graph_objs import *


def kelly(bankroll, edge, probability, counter, list=[]):
    # print()
    # print("BANKROLL:", bankroll)
    recommended_bet = bankroll * round(probability * (edge + 1.0) - 1.0, 2)

    if counter == 250:
        graph(list)
        return

    if recommended_bet < 0: # if recommended bet is negative, kelly criterion says it's worth betting on
        # print("RECOMMENDATION: don't bet.")
        return
    # else:
    #    print("RECOMMENDATION: bet should be", recommended_bet)

    # bool = input("did you win? (t:f)")
    result = random.random()

    if result <= probability:
        bankroll = bankroll + edge * recommended_bet
        list.append(bankroll)
        #print("WON")
    else:
        bankroll = bankroll - edge * recommended_bet
        list.append(bankroll)
        #print("LOST")

    return kelly(bankroll, edge, probability, counter + 1)


def graph(list):
    trace0 = Scatter(
        y=list
    )
    data = Data([trace0])

    py.iplot(data, filename='basic-line', evaluate=True)

kelly(10.0, 1.0, 0.60, 0)
