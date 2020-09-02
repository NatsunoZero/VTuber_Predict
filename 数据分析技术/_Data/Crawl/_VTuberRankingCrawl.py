# %% 
import urllib.request  # 用去获取网站链接请求
from bs4 import BeautifulSoup  # 用于读取网站内容
import re
import csv
import codecs
import os
import time
import datetime

#%%
class CrawlVTB:
    fileName = ""
    fileHead = ""

    def create_csv(self):
        '''创建用于保存的文件'''
        with open(self.fileName,'w', newline='', encoding='utf-8-sig') as f:
            csv_write = csv.writer(f)
            csv_write.writerow(self.fileHead)


    def write_csv(self, rank, name, chanName, agencyName, fansCount, playedCount):
        '''逐行写入内容'''
        with open(self.fileName, 'a+', newline='', encoding='utf-8-sig') as f:
            csv_write = csv.writer(f)
            data_row = [rank, name, chanName, agencyName, fansCount, playedCount]
            csv_write.writerow(data_row)
    def print_log_info(self, log):
        '''输出log'''
        os.system('cls')
        print(log)

    def execute(self):
        '''执行爬取的函数'''
        loopStop = 0
        for page in range(1,41):

            url = "http://virtual-youtuber.userlocal.jp/document/ranking?page={}".format(page)
            self.print_log_info("正在写入第"+str(page)+"页")
            f = urllib.request.urlopen(url)
            html = f.read().decode('utf-8')
            soup = BeautifulSoup(html, "html.parser")

            _dataRaw = soup.findAll(name="tr", attrs={"data-href":re.compile("^/user/")}) # 查找所有属性data-herf以/user/开头的tr元素

            for item in _dataRaw:
                rank = item.find('strong').string.strip().replace('位', '') # 顺位 去除‘位
                _nameColumn = item.find(name="td", attrs={"class":"col-name"})
                name = _nameColumn.find(name="a", attrs={"href":re.compile("^/user/")}).string.strip() # character名字
                chanName = _nameColumn.find(name="span", attrs={"class":"text-secondary"})
                chanName =  '' if chanName==None else chanName.string.strip() # channal名字
                agencyName = _nameColumn.find(name="a", attrs={"href":re.compile("^/office/")})
                agencyName = '' if agencyName==None else agencyName.string # agency名字（所属）
                _fansColumn = item.find(name="td", attrs={"class":"vertical text-right text-nowrap"})
                fansCount = _fansColumn.find(name="span", attrs={"class":"text-success font-weight-bold"}).string.replace('人', '').strip() # fans数，去除‘人’
                playedCount = _fansColumn.find(name="span", attrs={"class":"text-danger font-weight-bold"}).string.replace('回', '').strip() # 再生数，去除‘回’
                self.write_csv(rank,name,chanName,agencyName,fansCount,playedCount)
                self.print_log_info("正在写入 "+rank+"位: "+name)
            self.print_log_info("第"+str(page)+"页写入完成")
            loopStop+=1
            if(loopStop>=5):
                loopStop = 0
                time.sleep(0.5)
        self.print_log_info("全部写入完成")    

    def __init__(self, fileName, fileHead):
        self.fileName = fileName
        self.fileHead = fileHead
        self.create_csv()
        self.execute()
# %%
today=datetime.date.today()
def main():
    formatted_today=today.strftime('%Y%m%d')
    fileName = "[" + formatted_today + "] vtuber_ranking_crawl_result.csv"
    fileHead = ["順位","ネーム","チャンネルネーム","所属グループ","登録者数","再生回数"]
    cvtb = CrawlVTB (fileName, fileHead)
if __name__=="__main__":
    main()
# %%
