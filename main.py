def get_instance():
    ret = {
        'total_zones': 0,
        'total_sensors': 0,
        'zones_cost': [],
        'zone_covered_by_sensor': [],
        'sensor_covering_zone': []
    }
    with open('./instances/instance1.txt') as f:
        for count, line in enumerate(f):
            line = line.replace('\n', '')
            values = line.split(' ')
            if count == 0:
                ret['total_zones'] = int(values[0])
                ret['total_sensors'] = int(values[1])
            elif count == 1:
                ret['zones_cost'] = [int(x) for x in values]
            else:
                ret['zone_covered_by_sensor'].append([int(x) for x in values])  # zone 1 covered by sensor 1, 3....
        # iterate on sensor number
        for s in range(0, ret['total_sensors']):
            covered_zones = []
            # iterate on zones
            for z in ret['zone_covered_by_sensor']:
                # if current sensor is covering current zone
                if s + 1 in z:
                    # retrieve zone number by checking its index and append it to covered zone by this sensor
                    covered_zones.append(ret['zone_covered_by_sensor'].index(z) + 1)
            covered_zones.insert(0, len(covered_zones))
            ret['sensor_covering_zone'].append(covered_zones)  # sensor 1 is covering zones ...
        return ret


def enumeration_complete():
    instance = get_instance()
    print(instance)


if __name__ == "__main__":
    enumeration_complete()
