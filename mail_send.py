import os
import time
import zipfile

import win32com.client as win32

nowdate = time.strftime("%Y%m%d")


class SendMail:
    """调用Outlook发送邮件"""

    def __init__(self):
        self.outlook = win32.Dispatch("outlook.Application")
        self.mail = self.outlook.CreateItem(0)

    def send_mail(self):
        # 发送多个收件人以分号分隔，中间用加号连接；实例：'@'+';'+'@'
        addressee = 'yanzhiyong@inovance.com' + ';' + 'fanhai@inovance.com' + ';' + 'yangqunwu@inovance.com'
        result, failednum, passnum = self.make_message()
        self.zip_dir('reports')
        # addressee = 'yangqunwu@inovance.com'
        self.mail.SentOnBehalfOfName = "zhengjunpeng@inovance.com"  # 发件人（邮箱或账号）
        self.mail.To = addressee  # 收件人
        # self.mail.CC = "receiver"        # 抄送人
        self.mail.Subject = "%s汇服务引用uweb接口自动化结果" % nowdate  # 邮件主题
        self.mail.BodyFormat = 2  # 2表示用Html format，可调整格式
        # HTMLBody插入图片：先把要插入的图片当做一个附件添加，然后在HtmlBody中调用这个图片
        self.mail.Attachments.Add(r"E:\uweb_reference_check\allurereports.zip")  # 添加附件
        os.remove("allurereports.zip")
        passpercent = '{:.0%}'.format(passnum / (passnum + failednum))
        self.mail.HtmlBody = "本次通过率: %s<br>失败用例：%s<br>google浏览器快捷方式-属性-目标变更为'xxx(之前的目标路径) --allow-file-access-from-files'，重新打开浏览器，打开压缩包中index.html即可查看报告" % (
            passpercent, str(result))  # 邮件正文
        # self.mail.HtmlBody = '测试添加附件'
        # self.mail.Attachments.Add(r"C:\Users\Administrator\Pictures\Camera Roll\共产党宣言.png")    # 添加正常的附件
        # self.mail.Display()        # 显示发送邮件界面
        if failednum > 0:
            self.mail.Send()  # 发送
        else:
            self.mail.Send()  # 发送

    def make_message(self):
        lm = open("./reports/data/behaviors.csv", 'rb')
        passnum, failednum = 0, 0
        caselist = []
        while True:
            lll = lm.readline()
            if lll:
                resultlist = lll.decode("utf-8").replace('"', "").split(",")
                # caselist.append("%s  %s  %s" % (resultlist[2], resultlist[3], resultlist[5]))
                if len(resultlist[5]) == 1 and resultlist[5] == "1":
                    passnum += 1
                elif len(resultlist[3]) == 1 and resultlist[3] == "1":
                    failednum += 1
                    caselist.append(resultlist[2])
                elif len(resultlist[4]) == 1 and resultlist[4] == "1":
                    failednum += 1
                    caselist.append(resultlist[2])
            else:
                break
        return caselist, failednum, passnum

    def zip_dir(self, dir_):
        with zipfile.ZipFile('allurereports.zip', 'w') as z:
            z.write(dir_, arcname=(dn := os.path.basename(dir_)))
            for root, dirs, files in os.walk(dir_):
                for fn in files:
                    z.write(
                        fp := os.path.join(root, fn),
                        arcname=dn + '/' + os.path.relpath(fp, dir_)
                    )
