number_keys = int(input())
key_raliability = list(map(int, input().split()))
total_clicks = int(input())
number_clicks = list(map(int, input().split()))
frequency_clicks = [0] * (number_keys + 1)
for click in number_clicks:
    frequency_clicks[click] += 1
frequency_clicks.pop(0)
for key in range(number_keys):
    if frequency_clicks[key] > key_raliability[key]:
        print('YES')
    else:
        print('NO')
