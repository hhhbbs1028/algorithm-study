def divide_teams(players, team1=None, index=0, all_teams=None):
    if team1 is None:
        team1 = []
    if all_teams is None:
        all_teams = []

    n = len(players)
    team_size = n // 2

    # 팀1이 원하는 크기에 도달한 경우
    if len(team1) == team_size:
        team2 = [p for p in players if p not in team1]
        all_teams.append((team1[:], team2))
        return all_teams

    # 더 이상 선택할 원소가 없으면 종료
    if index == n:
        return all_teams

    # 현재 원소를 팀1에 추가
    team1.append(players[index])
    divide_teams(players, team1, index + 1, all_teams)
    team1.pop()  # 백트래킹

    # 현재 원소를 팀1에 포함하지 않음
    divide_teams(players, team1, index + 1, all_teams)

    return all_teams


# 예제 실행
players = [1, 2, 3, 4, 5, 6]
teams = divide_teams(players)
print(teams)

# 결과 출력
for team1, team2 in teams:
    print(f"Team 1: {team1}, Team 2: {team2}")

# 가능한 경우의 수
print(f"Total number of combinations: {len(teams)}")
