# 需要覆盖的州
states_needs = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

# 广播站
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

# 最后存储的广播站
final_stations = set()

# 贪婪算法
while states_needs:
    best_statious = None
    # 覆盖的州
    states_covered = set()
    # key,value
    for station, states_for_station in stations.items():
        covered = states_needs & states_for_station
        if len(covered) > len(states_covered):
            best_statious = station
            states_covered = covered
        states_needs -= states_covered
        final_stations.add(best_statious)

print(final_stations)
