import os
import requests

#file_path = 'https://raw.githubusercontent.com/SPX372928/MyIPTV/master/%E6%B5%99%E6%B1%9FPLTV%E7%A7%BB%E5%8A%A8CDN%E4%BF%AE%E6%94%B9%E7%89%88.txt'
file_path = os.getenv('FILE_PATH')
tg_token = os.getenv('TG_TOKEN')
tg_talk_id = os.getenv('TG_TALK_ID')

def DownloadTXT():
    try:
        r = requests.get(file_path)
        r.encoding = 'utf-8'
        with open('input.txt', "wb") as fp:
            fp.write(r.content)
        print('文件写入成功')
    except Exception as e:
        print(e)

def getIPTVlist():

    '''
    #仅支持 txt 格式:
    CCTV1 4M1080,http://39.134.176.156/hwltc.tv.cdn.zj.chinamobile.com/PLTV/88888888/224/3221228809/index.m3u8
    CCTV1 8M1080,http://39.134.176.166/hwltc.tv.cdn.zj.chinamobile.com/PLTV/88888888/224/3221229818/index.m3u8
    '''
    IPTVList = []
    with open('input.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        total = len(lines)
        for i in range(0, total):
            line = lines[i].strip('\n').strip(' ')
            item = line.split(',', 1)
            if len(item) == 2:
                data = {
                    'title': item[0],
                    'url': item[1],
                }
                IPTVList.append(data)
    print('共读取 %s 个直播源！' %(len(IPTVList)))
    return IPTVList

def getM3UList(IPTVList):
    try:
        if len(IPTVList) > 0 :
            with open ('output.m3u','w',encoding='utf-8') as f:
                f.write("#EXTM3U\n")
                for item in IPTVList:
                    f.write("#EXTINF:-1, %s\n" % (item['title']))
                    f.write("%s\n" % (item['url']))
            print('共写入 %s 个直播源！' %(len(IPTVList)))
        else:
            print('无有效直播源！')
            pass
    except Exception as e:
        print(e)

def sendTg(tg_token,tg_chat_id):
    try:
        content = 'm3u更新成功'
        url = f'https://api.telegram.org/bot{tg_token}/sendMessage?chat_id={tg_chat_id}&text={content}'
        resp = requests.post(url)
    except Exception as e:
        print('Tg 通知推送异常，原因为: ' + str(e))
        print(traceback.format_exc())

if __name__ == '__main__':
    DownloadTXT()
    iptv = getIPTVlist()
    getM3UList(iptv)
    if tg_token and tg_talk_id:
        sendTg(tg_token,tg_talk_id)
