#Sichuan Mahjong Net
----

##阶段计划

###第一阶段
1. 麻将ENV
- support basic function
- support single patterns in win case:
    - 清一色
    - 大对
    - 七对
    - 杠牌
- support more patterns
2. 双人麻将
- dummy AI：
    - random discard an isolated tile
    - if there is a special action: do it
###第二阶段
2. 双人麻将
- ordinary AI
    - calculate the prob by every action
- smart AI
    - knows n tiles in forthcoming tilewall
    - knows part of the hand tile of the opponent
###第三阶段
- learning AI:
    - use gan in training AI and the player?
    - extend the model to four player case?
    - support more actions and patterns

###时间计划

- 1阶段： 2 月 (4月完成）
- 2阶段： 2-3 月
- 3阶段：
