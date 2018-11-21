'''
问题描述
　　数轴上有一条长度为L（L为偶数)的线段，左端点在原点，右端点在坐标L处。有n个不计体积的小球在线段上，开始时所有的小球都处在偶数坐标上，速度方向向右，速度大小为1单位长度每秒。
　　当小球到达线段的端点（左端点或右端点）的时候，会立即向相反的方向移动，速度大小仍然为原来大小。
　　当两个小球撞到一起的时候，两个小球会分别向与自己原来移动的方向相反的方向，以原来的速度大小继续移动。
　　现在，告诉你线段的长度L，小球数量n，以及n个小球的初始位置，请你计算t秒之后，各个小球的位置。
提示
　　因为所有小球的初始位置都为偶数，而且线段的长度为偶数，可以证明，不会有三个小球同时相撞，小球到达线段端点以及小球之间的碰撞时刻均为整数。
　　同时也可以证明两个小球发生碰撞的位置一定是整数（但不一定是偶数）。
输入格式
　　输入的第一行包含三个整数n, L, t，用空格分隔，分别表示小球的个数、线段长度和你需要计算t秒之后小球的位置。
　　第二行包含n个整数a1, a2, …, an，用空格分隔，表示初始时刻n个小球的位置。
输出格式
　　输出一行包含n个整数，用空格分隔，第i个整数代表初始时刻位于ai的小球，在t秒之后的位置。
样例输入
3 10 5
4 6 8
样例输出
7 9 9
样例说明
　　初始时，三个小球的位置分别为4, 6, 8。
'''

# from collections import OrderedDict, Counter
def main(n, L, t, init_loc):
    """
    Args:
        n: 小球数量
        L: 轨道长度
        t: 时间
        init_loc: 每个小球的初始位置，list
    Return:
        v_loc: 字典,key;小球index，value:[方向，位置]
    """
    # v_loc = OrderedDict()    
    v_loc = {}
    for i in range(n):
        v_loc[i] = [1, init_loc[i]]
    for j in range(t):
        for key in range(n):
            direction_last = v_loc[key][0]
            loc_last = v_loc[key][1]
            loc = loc_last + direction_last * 1
            if loc == L:
                direction = -1
            elif loc == 0:
                direction = 1
            else:
                direction = direction_last
            v_loc[key] = [direction, loc]
        for i in range(n):
            for j in range(i,n):
                if v_loc[i][1] == v_loc[j][1]:
                    v_loc[i][0] *= -1
                    v_loc[j][0] *= -1
    return list(map(lambda x: x[1],v_loc.values()))
#     return v_loc

import time
start = time.time()
print(main(3, 10, 5,[4,6,8]))
end = time.time()
print(end-start)