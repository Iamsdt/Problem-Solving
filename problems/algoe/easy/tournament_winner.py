def tournamentWinner(competitions, results):
    di = {}

    for i in range(len(competitions)):
        team1, team2 = competitions[i]
        res = results[i]

        di[team1] = di.get(team1, 0) + 1 if res == 1 else 0
        di[team2] = di.get(team2, 0) + 1 if res == 0 else 0

    # sort the array based on teams
    # nlong
    # di = sorted(di.items(), key=lambda x: x[1], reverse=True)

    # let improve
    res = ""
    count = 0
    for i in di.keys():
        value = di[i]
        if count < value:
            res = i
            count = value

    # Write your code here.
    return res


if __name__ == "__main__":
    print(tournamentWinner(competitions=[["HTML", "C#"], [
          "C#", "Python"], ["Python", "HTML"]], results=[0, 0, 1]))
