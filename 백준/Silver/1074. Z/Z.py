import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())

Max_N = 2 ** N

ans = 0

while N != 0:

	N -= 1

	if r < Max_N and c < Max_N:
		ans += ( Max_N ) * ( Max_N ) * 0

	elif r < Max_N and c >= Max_N: 
		ans += ( Max_N ) * ( Max_N ) * 1
		c -= ( Max_N )

	elif r >= Max_N and c < Max_N: 
		ans += ( Max_N ) * ( Max_N ) * 2
		r -= ( Max_N )
 
	else:
		ans += ( Max_N ) * ( Max_N ) * 3
		r -= ( Max_N )
		c -= ( Max_N )
    
print(ans)