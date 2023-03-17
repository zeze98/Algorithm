def solution(chicken):
    answer = 0
    coupon = chicken
    while coupon >= 10:
        x = coupon // 10
        y = coupon % 10
        answer += x
        coupon = x + y
    return answer