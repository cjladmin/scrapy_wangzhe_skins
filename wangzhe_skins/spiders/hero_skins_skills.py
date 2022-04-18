import scrapy
from ..items import WangzheSkinsItem


class GetHeroSkinsSpider(scrapy.Spider):
    name = 'hero_skins_skills'
    allowed_domains = ['pvp.qq.com']
    start_urls = ['https://pvp.qq.com/web201605/herolist.shtml']

    def parse(self, response):
        """
        <li>
            <a href="herodetail/107.shtml" target="_blank">
                <img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/107/107.jpg" width="91" height="91" alt="赵云">
                赵云
            </a>
        </li>
        """
        # 获取所有英雄列表
        hero_link_all_list = response.xpath('//div[@class="herolist-content"]/ul/li/a')
        # print(len(hero_link_all_list))
        for hero_link_all in hero_link_all_list:
            # 英雄名称
            hero_name = hero_link_all.xpath('./text()').extract_first()
            # 英雄链接
            hero_link = "https://pvp.qq.com/web201605/" + hero_link_all.xpath('./@href').extract_first()
            print("已获取英雄：<" + hero_name + ">的详情链接......")
            yield scrapy.Request(url=hero_link, callback=self.get_hero_skin)
            # break

    # 获取英雄皮肤
    def get_hero_skin(self, response):
        skills_flag = True
        # 获取英雄的皮肤列表
        skin_link_all_list = response.xpath('//div[@class="pic-pf"]/ul/li')
        for skin_link_all in skin_link_all_list:
            # 英雄名称
            hero_name = response.xpath('//h2[@class="cover-name"]/text()').extract_first()
            # 皮肤图片名称
            skin_name = skin_link_all.xpath('./p/text()').extract_first()
            # 皮肤图片链接
            skin_link = "https:" + skin_link_all.xpath('./i/img/@data-imgname').extract_first()
            if skills_flag:
                # 获取英雄技能列表
                skills_all_list = response.xpath('//div[@class="skill-show"]/div')
                for skills_all in skills_all_list:
                    # 技能名
                    skill_name = skills_all.xpath('./p[1]/b/text()').extract_first()
                    # 技能冷却
                    skill_cd = skills_all.xpath('./p[1]/span[1]/text()').extract_first()
                    # 技能消耗
                    skill_cost = skills_all.xpath('./p[1]/span[2]/text()').extract_first()
                    # 技能介绍
                    skill_content = skills_all.xpath('./p[2]/text()').extract_first()

                    item = WangzheSkinsItem()
                    # 返回技能名
                    item['skill_name'] = skill_name
                    # 返回技能冷却
                    item['skill_cd'] = skill_cd
                    # 返回技能消耗
                    item['skill_cost'] = skill_cost
                    # 返回技能介绍
                    item['skill_content'] = skill_content
                    # 返回英雄名
                    item["hero_name"] = hero_name
                    # 返回皮肤名
                    item["skin_name"] = skin_name
                    # 返回皮肤链接
                    item["skin_link"] = skin_link
                    skills_flag = False
                    yield item
            else:
                item = WangzheSkinsItem()
                # 返回技能名
                item['skill_name'] = None
                # 返回技能冷却
                item['skill_cd'] = None
                # 返回技能消耗
                item['skill_cost'] = None
                # 返回技能介绍
                item['skill_content'] = None
                # 返回英雄名
                item["hero_name"] = hero_name
                # 返回皮肤名
                item["skin_name"] = skin_name
                # 返回皮肤链接
                item["skin_link"] = skin_link

                yield item
