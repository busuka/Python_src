# http://abc042.contest.atcoder.jp/tasks/abc042_a

def is_haiku(s):
    nums = s.split()
    counts = {x: nums.count(x) for x in nums}
    try:
        if counts['5'] == 2 and counts['7'] == 1:
            print("YES")
        else:
            print("NO")
    except:
        print("NO")

def is_haiku_no1(s):
    nums = s.split()
    n = sorted([int(x) for x in nums])
    if n[0] == 5 and n[1] == 5 and n[2] == 7:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    is_haiku("5 7 5")
    is_haiku("7 7 5")
    is_haiku("3 5 7")
    is_haiku_no1("5 7 5")
