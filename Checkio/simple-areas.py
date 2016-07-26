import math

def simple_areas(*args):

    # 円の面積を求める.(直径が与えられる)
    if len(args) == 1:
        x = round(args[0] / 2, 2)
        return x * x * math.pi

    # 四角形の面積を求める.(横と縦が与えられる.)
    elif len(args) == 2:
        return args[0] * args[1]

    # 三角形の面積を求める.
    else:
        y = args

        # 正三角形の場合
        if y[0] == y[1] == y[2]:
            y = sorted(y)
            return round(y[0] * y[1] * math.sqrt(3) / 4, 2)

        # 正三角形でない場合.
        else:
            s = (y[0] + y[1] + y[2]) / 2.0
            return round(math.sqrt(s*(s - y[0])*(s - y[1]) * (s - y[2])), 2)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"
