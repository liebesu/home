__author__ = 'liebesu'
#ÑÝÊ¾Õ¾http://wwww.yunsou.me
def response_worker():
  global news,totals
  dbconn = mdb.connect(DB_HOST, DB_USER, DB_PASS, 'baiduyun', charset='utf8')
  dbcurr = dbconn.cursor()
  dbcurr.execute('SET NAMES utf8')
  dbcurr.execute('set global wait_timeout=60000')
  while True:
    print "function response_worker",hc_r.qsize()
    # if hc_r.qsize()==0:
    #	 print "continue"
    #	 continue
    metadata, effective_url = hc_r.get()
    print "response_worker:", effective_url
    try:
      tnow = datetime.datetime.utcnow()
      date = (tnow + datetime.timedelta(hours=8))
      date = datetime.datetime(date.year, date.month, date.day)
      if news>=100:
        try:
          dbcurr.execute('INSERT INTO spider_statusreport(date,new_hashes,total_requests)  VALUES(%s,%s,%s) ON DUPLICATE KEY UPDATE ' +'total_requests=total_requests+%s,new_hashes=new_hashes+%s',
            (date, news,totals,totals,news))
        except Exception as ex:
          print "E10", str(ex)
        news=0
      id = re_urlid.findall(effective_url)[0]
      start = re_start.findall(effective_url)[0]
      if True:
        if 'getfollowlist' in effective_url: #type = 1
          follows = json.loads(metadata)
          print "-------------------------------------follows-------------------------------\n"
          uid = re_uid.findall(effective_url)[0]
          if "total_count" in follows.keys() and follows["total_count"]>0 and str(start) == "0":
            for i in range((follows["total_count"]-1)/ONEPAGE):
              try:
                dbcurr.execute('INSERT INTO urlids(uk, start, limited, type, status) VALUES(%s, %s, %s, 1, 0)' % (uid, str(ONEPAGE*(i+1)), str(ONEPAGE)))
              except Exception as ex:
                print "E1", str(ex)
                pass
          if "follow_list" in follows.keys():
            for item in follows["follow_list"]:
        if item['pubshare_count']==0:
          print "---------------------count ==0-------------------------------------------\n"
          #continue
              y = dbcurr.execute('SELECT id FROM user WHERE userid=%s', (item['follow_uk'],))
              y = dbcurr.fetchone()
              print "user uk",item['follow_uk']
              if not y:
                try:
                  dbcurr.execute('INSERT INTO user(userid, username, files, status, downloaded, lastaccess,avatar_url,fans_count,follow_count,album_count) VALUES(%s, "%s", %s, 0, 0, "%s","%s",%s,%s,%s)' % (item['follow_uk'], item['follow_uname'],item['pubshare_count'],tnow,item['avatar_url'],item['fans_count'],item['follow_count'],item['album_count']))
                except Exception as ex:
                  print "E13", str(ex)
                  pass
              else:
                print "-----------------userid exists---------------------------------\n"
          else:
            print "delete 1", uid, start
            dbcurr.execute('delete from urlids where uk=%s and type=1 and start>%s' % (uid, start))
        elif 'getfanslist' in effective_url: #type = 2
          fans = json.loads(metadata)
          print "----------------------------------------fans----------------------------------\n"
          uid = re_uid.findall(effective_url)[0]
          if "total_count" in fans.keys() and fans["total_count"]>0 and str(start) == "0":
            for i in range((fans["total_count"]-1)/ONEPAGE):
              try:
                dbcurr.execute('INSERT INTO urlids(uk, start, limited, type, status) VALUES(%s, %s, %s, 2, 0)' % (uid, str(ONEPAGE*(i+1)), str(ONEPAGE)))
              except Exception as ex:
                print "E2", str(ex)
                pass
          if "fans_list" in fans.keys():
            for item in fans["fans_list"]:
              if item['pubshare_count']==0:
        print "---------------------count ==0-------------------------------------------\n"
                #continue
              y = dbcurr.execute('SELECT id FROM user WHERE userid=%s', (item['fans_uk'],))
              y = dbcurr.fetchone()
              print "user uk",item['fans_uk']
              if not y:
                try:
                  dbcurr.execute('INSERT INTO user(userid, username, files, status, downloaded, lastaccess,avatar_url,fans_count,follow_count,album_count) VALUES(%s, "%s", %s, 0, 0, "%s","%s",%s,%s,%s)' % (item['fans_uk'], item['fans_uname'],item['pubshare_count'],tnow,item['avatar_url'],item['fans_count'],item['follow_count'],item['album_count']))
                except Exception as ex:
                  print "E23", str(ex)
                  pass
              else:
                print "-----------------userid exists---------------------------------\n"
          else:
            print "delete 2", uid, start
            dbcurr.execute('delete from urlids where uk=%s and type=2 and start>%s' % (uid, start))
        else:
          shares = json.loads(metadata)
          print "shares"
          uid = re_uid.findall(effective_url)[0]
          totals+=1
          if "total_count" in shares.keys() and shares["total_count"]>0 and str(start) == "0":
            for i in range((shares["total_count"]-1)/ONESHAREPAGE):
              try:
                dbcurr.execute('INSERT INTO urlids(uk, start, limited, type, status) VALUES(%s, %s, %s, 0, 0)' % (uid, str(ONESHAREPAGE*(i+1)), str(ONESHAREPAGE)))
              except Exception as ex:
                print "E3", str(ex)
                pass
          if "records" in shares.keys():
            for item in shares["records"]:
              print "-------------------------------------filename------------------ ",item['title']
              print "---------------------------------------------------------------\n"
              try:
                stamp_t=int(item["feed_time"])/1000
                t= time.localtime(int(stamp_t))
                share_time=time.strftime("%Y-%m-%d %H:%M:%S",t)
                urls=""
                if "shorturl" in item.keys():
                  urls=item['shorturl']
                news+=1
                length=""
                if "filelist" in item.keys():
                  length=str(item['filelist'][0]['size'])
                dbcurr.execute('INSERT INTO share(fid,userid, filename, shareid, status,filetype,share_time,create_time,urls,down,length) VALUES("%s",%s, "%s", %s, 0,"%s","%s","%s","%s",0,"%s")' % (sid(int(item['shareid'])),uid, item['title'], item['shareid'],get_category(get_ext(item['title'])),share_time,tnow,urls,length))
                # time.sleep(10)
              except Exception as ex:
                print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>E33\n", str(ex)
                print "item ---------------------------------------------\n"
                # time.sleep(10)
                pass
          else:
            print "delete 0", uid, start
            dbcurr.execute('delete from urlids where uk=%s and type=0 and start>%s' % (uid, str(start)))
        dbcurr.execute('delete from urlids where id=%s' % (id, ))
        dbconn.commit()
    except Exception as ex:
      print "E5", str(ex), id
    pid = re_pptt.findall(effective_url)
    if pid:
      print "pid>>>", pid
      ppid = int(pid[0])
      PROXY_LIST[ppid][6] -= 1
  dbcurr.close()
  dbconn.close()
#ÑÝÊ¾Õ¾http://wwww.yunsou.me
def worker(k):
  global success, failed
  dbconn = mdb.connect(DB_HOST, DB_USER, DB_PASS, 'baiduyun', charset='utf8')
  dbcurr = dbconn.cursor()
  dbcurr.execute('SET NAMES utf8')
  dbcurr.execute('set global wait_timeout=60000')
  while True:
    #dbcurr.execute('select * from urlids where status=0 order by type limit 1')
    dbcurr.execute('select * from urlids where status=0 limit %s,1'%(str(k),))
    d = dbcurr.fetchall()
    #print d
    if d:
      id = d[0][0]
      uk = d[0][1]
      start = d[0][2]
      limit = d[0][3]
      type = d[0][4]
      dbcurr.execute('update urlids set status=1 where id=%s' % (str(id),))
      url = ""
      if type == 0:
        url = URL_SHARE.format(uk=uk, start=start, id=id).encode('utf-8')
      elif  type == 1:
        url = URL_FOLLOW.format(uk=uk, start=start, id=id).encode('utf-8')
      elif type == 2:
        url = URL_FANS.format(uk=uk, start=start, id=id).encode('utf-8')
      if url:
        hc_q.put((type, url))
    if len(d)==0:
      print "\ndata user uk\n "
      dbcurr.execute('select * from user where status=0 limit %s,100'%(str(k*100),))
      print "user "
      d = dbcurr.fetchall()
      #print "uk",d
      if d:
        for item in d:
          try:
            print "update user",item[1]
            dbcurr.execute('insert into urlids(uk, start, limited, type, status) values("%s", 0, %s, 0, 0)' % (item[1], str(ONESHAREPAGE)))
            dbcurr.execute('insert into urlids(uk, start, limited, type, status) values("%s", 0, %s, 1, 0)' % (item[1], str(ONEPAGE)))
            dbcurr.execute('insert into urlids(uk, start, limited, type, status) values("%s", 0, %s, 2, 0)' % (item[1], str(ONEPAGE)))
            dbcurr.execute('update user set status=1 where userid=%s and id=%s' % (item[1],item[6]))
          except Exception as ex:
            print "E6", str(ex)
      else:
        time.sleep(1)
    dbconn.commit()
  dbcurr.close()
  dbconn.close()
#ÑÝÊ¾Õ¾http://wwww.yunsou.me
def req_worker(inx):
  s = requests.Session()
  while True:
    time.sleep(1)
    req_item = hc_q.get()
    req_type = req_item[0]
    url = req_item[1]
    try:
      r = s.get(url)
      hc_r.put((r.text, url))
    except:
      pass
for item in range(3):
  t = threading.Thread(target = req_worker, args = (item,))
  t.setDaemon(True)
  t.start()
for item in range(2):
  s = threading.Thread(target = worker, args = (item,))
  s.setDaemon(True)
  s.start()
for item in range(2):
  t = threading.Thread(target = response_worker, args = ())
  t.setDaemon(True)
  t.start()
while 1:
  pass