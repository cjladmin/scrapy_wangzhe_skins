## <center>✨获取王者荣耀全部皮肤原画✨</center>
 - 王者荣耀英雄资料：[https://pvp.qq.com/web201605/herolist.shtml](https://pvp.qq.com/web201605/herolist.shtml)

 - 除皮肤原画外，还有抓取所有英雄的技能信息，包含：
    - 技能名
    - 技能冷却
    - 技能消耗
    - 技能介绍

 - 运行命令：`scrapy crawl hero_skins_skills`

 - 目录结构：

```
project
│   README.md
│   scrapy.cfg   
│
└───wangzhe_skins
│   │   __init__.py
│   │   items.py
│   │   middlewares.py
│   │   pipelines.py
│   │   settings.py
│   │
│   └───spiders
│       │   __init__.py
│       │   hero_skins_skills.py
│   
└───王者英雄数据
    └───xxx(英雄名)
    	│   xxx(皮肤名).jpg
    	│   xxx(英雄名)-技能介绍.txt
```