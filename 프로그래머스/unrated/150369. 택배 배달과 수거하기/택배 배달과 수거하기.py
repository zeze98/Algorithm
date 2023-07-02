def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    road_to_delivery = 0
    road_to_pickup = 0

    for i in range(n):
        road_to_delivery += deliveries[i]
        road_to_pickup += pickups[i]

        while road_to_delivery > 0 or road_to_pickup > 0:
            road_to_delivery -= cap
            road_to_pickup -= cap
            answer += (n-i) * 2

    return answer