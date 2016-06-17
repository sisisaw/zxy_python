# 约瑟夫和他朋友还有39个犹太人,围成一个圈,喊到3的人就自杀。那么约瑟夫和他的朋友怎样才能活下来?
def joseph(people, begin, count):
    member = [x for x in range(1,people+1)]
    death = (begin + count - 2) % len(member)
    for i in range(people-2):
        print('out:', member[death])
        del member[death]
        death = (death + count - 1) % len(member)
    print(member)

joseph(41,1,3)



