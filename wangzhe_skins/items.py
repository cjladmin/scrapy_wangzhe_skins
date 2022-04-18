# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangzheSkinsItem(scrapy.Item):
    # 英雄名
    hero_name = scrapy.Field()
    # 皮肤名
    skin_name = scrapy.Field()
    # 皮肤链接
    skin_link = scrapy.Field()

    # 技能名
    skill_name = scrapy.Field()
    # 技能冷却
    skill_cd = scrapy.Field()
    # 技能消耗
    skill_cost = scrapy.Field()
    # 技能介绍
    skill_content = scrapy.Field()
    pass
