import sys

sysin = sys.stdin.readline

N, M = map(int, sysin().split())
pokemon = {}

for i in range(1,N+1):
    key = str(i)
    value = sysin().rstrip()
    pokemon[key] = value

reverse_pokemon = dict(map(reversed, pokemon.items()))

for j in range(M):
    find = sysin().rstrip()

    if ord(find[0]) > 59:
        print(reverse_pokemon[find])

    else:
        print(pokemon[find])