# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
from pathlib import Path
import scrapy
from scrapy.pipelines.images import ImagesPipeline


# 继承父类ImagesPipeline
class Skin_download_Pipeline(ImagesPipeline):
    pwd_path = ""

    # 根据图片地址对图片发送请求,重写父类方法
    def get_media_requests(self, item, info):
        # 用于目录名
        hero_dir_name = item['hero_name']
        # 用于图片名
        skins_img_name = item['skin_name']

        # 技能相关数据
        hero_name = item['hero_name']
        skill_name = item['skill_name']
        skill_cd = item['skill_cd']
        skill_cost = item['skill_cost']
        skill_content = item['skill_content']

        # 获取路径
        self.pwd_path = os.path.abspath(os.path.join(os.getcwd()))
        # 拼接图片路径
        skin_img = Path(f"{self.pwd_path}/王者英雄数据/{hero_dir_name}/{skins_img_name}.jpg")
        # 判断图片是否存在，存在则跳过
        if skin_img.is_file():
            print(f"<{hero_dir_name}>---<{skin_img}>该图片已存在.......")
            pass
        else:
            yield scrapy.Request(item['skin_link'], meta={'item': item})
            print(f"<{hero_dir_name}>---<{skin_img}>图片保存成功！")
        self.set_hero_skills(hero_name, skill_name, skill_cd, skill_cost, skill_content)

    # 指定图片名称，重写父类方法
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        img_path = item['hero_name']
        # 拼接图片路径
        img_Name = f"{img_path}/{item['skin_name']}.jpg"
        return img_Name

    # 保存英雄技能数据
    def set_hero_skills(self, hero_name, skill_name, skill_cd, skill_cost, skill_content):
        # 拼接技能数据路径
        skill_data = Path(f"{self.pwd_path}/王者英雄数据/{hero_name}")
        # 文件夹不存在时创建
        if os.path.exists(skill_data):
            pass
        else:
            os.mkdir(skill_data)
        # 判断返回的数据是否有空值
        if (hero_name is None) or (skill_name is None) or (skill_cd is None) or (skill_cost is None) or (skill_content is None):
            pass
        else:
            with open(f"{skill_data}/{hero_name}-技能介绍.txt", "a", encoding="utf-8") as w:
                w.write(f"技能名：<{skill_name}>\t\t{skill_cd}\t\t{skill_cost}\n{skill_content}\n")
