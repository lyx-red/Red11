# 猜拳游戏
'''
1.玩家出拳
2.电脑随机出拳
3.判断输赢：玩家胜/电脑胜/平局
'''
# 导入模块
import random
player = int(input('请玩家出拳（0--石头，1--剪刀，2--布）：'))
computer = random.randint(0,2)
print(computer)
# 玩家获胜的情况
if(player == 0 and computer ==1)or(player == 1 and computer ==2)or(player == 2 and computer ==0):
    print('玩家获胜')
elif player == computer:
    print('平局，再来一局')
else:
    print('电脑获胜')
