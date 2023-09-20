from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    truck_q = deque(truck_weights)
    now_weight = 0
    while bridge:
        if truck_q:
            lose_weight = bridge.popleft()
            now_weight -= lose_weight
            if now_weight + truck_q[0] <= weight:
                truck = truck_q.popleft()
                bridge.append(truck)
                now_weight += truck
            else:
                bridge.append(0)
        else:
            bridge.popleft()
        answer += 1

    return answer