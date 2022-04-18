BOT_NAME = 'wangzhe_skins'

SPIDER_MODULES = ['wangzhe_skins.spiders']
NEWSPIDER_MODULE = 'wangzhe_skins.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39'

# 设置爬取间隔(s)
DOWNLOAD_DELAY = 1

# ROBOTSTXT_OBEY = True
# 下载中间件
DOWNLOADER_MIDDLEWARES = {
   'wangzhe_skins.middlewares.SeleniumMiddleware': 543,
}
# 管道配置
ITEM_PIPELINES = {
   'wangzhe_skins.pipelines.Skin_download_Pipeline': 300,
}
# 图片目录
IMAGES_STORE = './王者英雄数据'
