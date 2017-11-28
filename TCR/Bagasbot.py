# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,tempfile,requests,urllib,datetime
from bs4 import BeautifulSoup

#cl = LINETCR.LINE()
#cl.login(token="ElhAsfzfjUzOrbE5dqUd.7rvSHV/LyctaRlOw94IEBq.htZ0W7ND5wiwKLeT1MCBkeBvSScmrhbxFfpeEVAuC6o=")
#cl.loginResult()

cl = LINETCR.LINE()
cl.login(token="Ena4w8Rzn5E3IIGturwb.tm69+BZYzCo2216hqBH2EW.LtkYOm6AnGIYuVNmNf4KshOWkKJCxh/Cm41NRCmVqh8=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="Env40FFnRdfqnifL64u3.4gs4vFQ2ZDJ4ZJmde9iYCW.TjXWHd3eVqeE+nMpz8CJiRpIWZEt+x8J3/gIklLwwU0=")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="EnBcm7F3xVCAE0ekZUS4.2DOZ9op9gZAAwdXvIQ9eva.sr4+TpMmQtuDwoA6lQCGnVrCJ1brmpTPVwB+6nwR4NA=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="Enjfby6ZUNSn4RX7r6o8.PCoyIwFGUA9fLOHh0kfVca.uQgWTgYO5AwyfZcUsKsI6sqq3UcfdFM86dZ4YlHy7Cc=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="EnGCYJLMd0zTE8EWvQl0.//VN+UihxA78sRvheIQgSa.boGmwztbXU6X3xFLj4gyaGqGnzvpiif7TxYkBhz8b4g=")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="EnfW15vw6zhvYlEXujue.M1OpijDgbpEDUrG8FUMnpG.x10mD2M+QVCprP+lnc3toUS50SJU7N0PBlx0kAoebL4=")
ki5.loginResult()

ki6 = LINETCR.LINE()
ki6.login(token="En9nW65CcRcGCoXu13c0.M+y4G2kYzq7XWBdPVsLk0a.H/kArDdYsTKKF9YLe5BLK+QAu6ai16h7feJGNvw+bQU=")
ki6.loginResult()

ki7 = LINETCR.LINE()
ki7.login(token="EnuyeXS1WhiwLCUgxWO3.76rJ2assFNAANg3z5+J9eW.OZf5HvJX7p1uPdmTtrlHPFSbNfUxfjtFn42e/cVEJRU=")
ki7.loginResult()

ki8 = LINETCR.LINE()
ki8.login(token="EntK0VTQ3xQ3YGtcAED0.SFFTth/bb4oQpAOXLovMGa.n5DwpFU20pb+UDqcvV4FNrG6TbLowpbkcZP+V2CS70g=")
ki8.loginResult()

ki9 = LINETCR.LINE()
ki9.login(token="EnAGSnXRFI0bCaGLNRJ9.DfOC90kAkZb62E+5rZ9o2q.of7bDajxPD6rP18YwlkMf/YDzs0ZmLq1SIPfIKLMBCo=")
ki9.loginResult()

ki10 = LINETCR.LINE()
ki10.login(token="EnKLOkVhH47cFf19BLg1.JKfDjR5tnKKNvQUbn25VOq.8f4fXMHHAQUtg1PMX5ezKmh5ce0SBh7SYJCvl5ErNeE=")
ki10.loginResult()

kibackup = LINETCR.LINE()
kibackup.login(token="EnnZfvKD0ZlEVwfU9Va8./CDT8Axtakm/Aw3hWEruwa.QFgzB3uerEJyb+bvY3xhOSJwVC8///+E+Z302TRE+zc=")
kibackup.loginResult()

kibackup1 = LINETCR.LINE()
kibackup1.login(token="Enqd8P0Rc7472C305h35.QqGgMhY9kLDgSox4VBZHTq.Ne8xfy6N28zdXmAkimjETfCMhpwY/+dnJBwrG2nzBbw=")
kibackup1.loginResult()

print "login success plak"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""╔══════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║====[B̴̸͌͌A̴̸͌͌G̴̸͌͌A̴̸͌͌S̴̸͌͌B̴̸͌͌O̴̸͌͌T̴̸͌͌]====
║   Owner : ✰Bagas✰
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║[C̶̲̅ᴏ̶̲̅ᴍ̶̲̅ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅ᴅ̶̲̅]
║╔═════════════
║╠[★]Myhelp
║╠[★]Mybot
║╠[★]Ginfo
║╠[★]1name
║╠[★]Me
║╠[★]K1-K10 
║╠[★]Gift-Gift3
║╠[★]Contact
║╠[★]Mid
║╠[★]All mid
║╠[★]TL:「Text」
║╠[★]Allbio:「Text」
║╠[★]MyName:「Text」
║╠[★]Myname 「Check name」
║╠[★]Mybio 「Check bio」
║╠[★]Mypict 「Check dp」
║╠[★]Mycover 「Check cover」
║╠[★]Mid:「mid」
║╠[★]Contact 「On/Off」
║╠[★]Name1 「Cname bot」
║╠[★]Ppc 「cover dp,home」
║╠[★]Steal dp
║╠[★]Steal home
║╠[★]Mid Bot
║╠[★]Speed/Sp
║╠[★]Cctv(Cyduk)
║╠[★]Jam「On/Off
║╠[★]Sayang Kamu dmna
║╠[★]Absen/Responsename
║╠[★]Getbio
║╠[★]/contact
║╠[★]Say 「ikutin Kata'」
║╠[★]Gn Nama Group
║╠[★]Group Cancel:
║╠[★]Jam Say:「Nama」
║╠[★]Message set:
║╠[★]Message
║╠[★]instagram
║╠[★]Mid @
║╠[★]Creator
║╠[★]Pesan set:「Text」
║╚════════════
║[C̶̲̅ᴏ̶̲̅ᴍ̶̲̅ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅ᴅ̶ ̶̲̅ɪ̶̲̅ɴ̶̲̅ ̶̲̅G̶̲̅ʀ̶̲̅ᴏ̶̲̅ᴜ̶̲̅ᴘ̶̲̅]
║╔════════════
║╠[★]Tagall
║╠[★]Kick:「mid」
║╠[★]Invite:「mid」
║╠[★]Cancel
║╠[★]Buka/Open 
║╠[★]Banlist
║╠[★]Mcheck 「Check banlist」
║╠[★Tutup/Close
║╠[★]Invite:gcreator
║╠[★]Allprotect
║╠[★]Protect「On/Off」
║╠[★]Qr 「On/Off」] 
║╠[★]Cancel 「On/Off」] 
║╠[★]Invite 「On/Off」]
║╠[★]Add (on/off)]
║╠[★]Ginfo
║╠[★]Keluar/Kabur]
║╠[★]Bot Out] 
║╠[★]Pantekk 「Rata」
║╠[★]Gn 「Nama Grup」]
║╠[★]K1~ 「Tagall & Out」
║╠[★]K1,2,3 IN 「BOT1,2,3 Masuk」
║╠[★]Ki1,2,3 「BOT1,2,3 Kick」
║╠[★]Gurl 「ID」]
║╠[★]Vk「@nama」]
║╠[★]Ban 「@」
║╠[★]Unban 「@」
║╠[★]Ban:]
║╠[★]Unban:]
║╠[★]Bot Like]
║╠[★]Like temen]
║╠[★]Cctv]
║╠[★]Ciduk]
║╠[★]Glist]
║╠[★]/invitemeto: (idgroup)]
║╠[★]Respon/Absen]
║╠[★]Speed/Sp] 
║╠[★]Woy/woi/Bot] Random Chat 
║╠𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║╠ID LINE:☞ http://line.me/ti/p/~akunb4ru ☜
║╠𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
╚═══════════════════════════════════
"""

Setgroup =""" 
    [Admin Menu]
==============
||[Protect QR]
||- Qr on/off
||[Protect Join]
||- Join on/off
||[Mid Via Contact]
||- Contact on/off
||-[Cancel Invited]
||- Cancel all
==============
   B̴̸͌͌A̴̸͌͌G̴̸͌͌A̴̸͌͌S̴̸͌͌B̴̸͌͌O̴̸͌͌T̴̸͌͌
=============="""
KAC=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,kibackup]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
ki6mid = ki6.getProfile().mid
ki7mid = ki7.getProfile().mid
ki8mid = ki8.getProfile().mid
ki9mid = ki9.getProfile().mid
ki10mid = ki10.getProfile().mid
kibackupmid = kibackup.getProfile().mid
Bots=[mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid,ki10mid,kibackupmid]
owner =["u4ccebdfdbcf265c3b6db5e8741b8767b"]
admin = ["u4ccebdfdbcf265c3b6db5e8741b8767b"]
wait = {
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':False,
    'message':"""тerima Kasih Telah Menambahkan Saya Jadi Teman
≫ B̴̸͌͌A̴̸͌͌G̴̸͌͌A̴̸͌͌S̴̸͌͌B̴̸͌͌O̴̸͌͌T̴̸͌͌ ≪

ᴜsᴇ :
•sᴇʟғʙᴏᴛ•
•ʙᴏᴛᴘʀᴏᴛᴇᴄᴛ•
•‎sɪʀɪ ʀᴏᴏᴍ ʟᴀᴍᴀ/ʙᴀʀᴜ•

sᴜᴘᴘᴏʀᴛᴇᴅ ʙʏ:

• S҉̶̶̘̟̼̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊K҉̶̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊Y҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊ྈT҉̶̘̟̼̉̈́͐͋͌̊Σ̶Δ̶M҉̶̘̟̼̉̈́͐͋͌̊҉ͩ͂ྈB҉̶̶̘̟̼̉̈́͐͋͌̊Ω҉̶̘̟̼̉̈́͐͋͌̊T҉̶̘̟̼̉̈́͐͋͌̊S҉̶̘̟̼̉̈́͐͋͌̊ •
      •B̴̸̴̴̸̴̴̸̴̴̸̴̲̲͌͌͌͌͌͌͌͌̅͌͌͌͌͌͌͌͌A̴̸̴̴̸̴̴̸̴̴̸̴̲̲͌͌͌͌͌͌͌͌̅͌͌͌͌͌͌͌͌G̴̸̴̴̸̴̴̸̴̴̸̴̲̲͌͌͌͌͌͌͌͌̅͌͌͌͌͌͌͌͌A̴̸̴̴̸̴̴̸̴̴̸̴̲̲͌͌͌͌͌͌͌͌̅͌͌͌͌͌͌͌͌S̴̸̴̴̸̴̴̸̴̴̸̴̲̲͌͌͌͌͌͌͌͌̅͌͌͌͌͌͌͌͌B̴̸̴̴̸̴̴̸̴̴̸̴̲̲͌͌͌͌͌͌͌͌̅͌͌͌͌͌͌͌͌O̴̸̴̴̸̴̴̸̴̴̸̴̲̲͌͌͌͌͌͌͌͌̅͌͌͌͌͌͌͌͌T̴̸̴̴̸̴̴̸̴̴̸̴̲̲͌͌͌͌͌͌͌͌̅͌͌͌͌͌͌͌͌•
•A̶҉̶҉̶҉̶N̶҉̶҉̶҉̶I̶҉̶҉̶҉̶M̶҉̶҉̶҉̶E̶҉̶҉̶҉̶ T̶҉̶҉̶҉̶E̶҉̶҉̶҉̶A̶҉̶҉̶҉̶M̶҉̶҉̶҉̶ B̶҉̶҉̶҉̶O̶҉̶҉̶҉̶T̶҉̶҉̶҉̶•
""",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "Contact":False,
    "cName":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":False,
    "Protectjoin":False,
    "Protectcancl":False,
    "Protectcancel":False,
    "protectionOn":False,
    "atjointicket":True,
    "tag":True,
    "Backup":False,
    "likeOn":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{},
    'copy':False,
    'target':{},
    'midsTarget':{}
    }

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile() 
backup = cl.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："] 
    for tex in tex:
      for command in commands:
        if string ==command:
          return True

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    
            if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        cl.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
                    
        if op.type == 26:
            msg=op.message
            if "@"+cl.getProfile().displayName in msg.text:
                    if wait["tag"] == True:
                        tanya = msg.text.replace("@"+cl.getProfile().displayName,"")
                        jawab = (cl.getProfile().displayName+" sedang sibuk/Off\nJika penting silakan Pesonal chat")
                        jawaban = (jawab)
                        cl.sendText(msg.to,jawaban)

        #------Protect Group Kick start------#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if cl.getGroup(op.param1).preventJoinByTicket == False:
              if op.param2 in Bots:
                pass
              else:
                try:
                  cl.sendText(op.param1,cl.getContact(op.param2).displayName + "Jangan Buka Kode QR Njiiir")
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  X = cl.getGroup(op.param1)
                  X.preventJoinByTicket = True
                  cl.updateGroup(X)
                except:
                  random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Jangan Buka Kode QR Njiiir")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  Z = cl.getGroup(op.param1)
                  Z.preventJoinByTicket = True
                  cl.updateGroup(X)
        #------Protect Group Kick finish-----#
        if op.type == 19:
          if op.param2 not in admin and Bots:
            if op.param2 in Bots:
             pass
          elif wait["Protect"] == True:
           wait ["blacklist"][op.param2] = True
           random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Cancel Invite User start------#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            group = cl.getGroup(op.param1)
            gMembMids = [contact.mid for contact in group.invitee]
            if op.param2 not in Bots:
              random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
        #------Cancel Invite User Finish------#
            
        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots:
                  cl.acceptGroupInvitation(op.param1)
                else:
                  cl.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if kimid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots:
                  ki.acceptGroupInvitation(op.param1)
                else:
                  ki.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
            
            if ki2mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots:
                  ki2.acceptGroupInvitation(op.param1)
                else:
                  ki2.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if ki3mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots:
                  ki3.acceptGroupInvitation(op.param1)
                else:
                  ki3.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if ki4mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots:
                  ki4.acceptGroupInvitation(op.param1)
                else:
                  ki4.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if ki5mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots:
                  ki5.acceptGroupInvitation(op.param1)
                else:
                  ki5.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if ki6mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots:
                  ki6.acceptGroupInvitation(op.param1)
                else:
                  ki6.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if ki7mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots:
                  ki7.acceptGroupInvitation(op.param1)
                else:
                  ki7.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if ki8mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots:
                  ki8.acceptGroupInvitation(op.param1)
                else:
                  ki8.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if ki9mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots:
                  ki9.acceptGroupInvitation(op.param1)
                else:
                  ki9.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if ki10mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots:
                  ki10.acceptGroupInvitation(op.param1)
                else:
                  ki10.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if kibackupmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots:
                  kibackup.acceptGroupInvitation(op.param1)
                else:
                  kibackup.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
        #------Joined User Kick start------#
        if op.type == 17: #awal 17 ubah 13
          if wait["Protectjoin"] == True:
            if op.param2 not in Bots: # Awalnya admin doang
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              cl.sendText(op.param1, "Protect Join nya On Boss\nMatiin dulu kali mau Ada yang Gabung")
        #------Joined User Kick start------#
        if op.type == 32: #Yang Cancel Invitan langsung ke kick
          if wait["Protectcancel"] == True:
            if op.param2 not in Bots:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])   
        
        if op.type == 19:
          if op.param2 not in Bots:
            if op.param3 in mid:
              if op.param2 not in Bots:
                try:
                  G = ki.getGroup(op.param1)
                  G.preventJoinByTicket = False
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(op.param1)
                  kibackup.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kibackup.kickoutFromGroup(op.param1,[op.param2])
                  H = kibackup.getGroup(op.param1)
                  H.preventJoinByTicket = False
                  kibackup.updateGroup(H)
                  Ticket = kibackup.reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  #cl.sendText(op.param1, "Makasih Brader")
                  #kibackup.sendText(op.param1, "Sama² Brader")
                  #kibackup.sendText(op.param1, "Ane Balik Dulu\nAssalamualaikum")
                  #cl.sendText(op.param1, "Wa'alaikumsalam")
                  kibackup.leaveGroup(op.param1)
                  G = cl.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  kibackup.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kibackup.kickoutFromGroup(op.param1,[op.param2])
                  H = kibackup.getGroup(op.param1)
                  H.preventJoinByTicket = False
                  kibackup.updateGroup(H)
                  Ticket = kibackup.reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  cl.sendText(op.param1, "Makasih Brader")
                  kibackup.sendText(op.param1, "Sama² Brader")
                  kibackup.sendText(op.param1, "Ane Balik Dulu\nAssalamualaikum")
                  cl.sendText(op.param1, "Wa'alaikumsalam")
                  kibackup.leaveGroup(op.param1)
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
            if op.param3 in kimid:
              if op.param2 not in Bots:
                try:
                  G = cl.getGroup(op.param1)
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in ki2mid:
              if op.param2 not in Bots:
                try:
                  G = ki3.getGroup(op.param1)
                  ki3.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ki3.updateGroup(G)
                  Ticket = ki3.reissueGroupTicket(op.param1)
                  ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ki3.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in ki3mid:
              if op.param2 not in Bots:
                try:
                  G = ki4.getGroup(op.param1)
                  ki4.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ki4.updateGroup(G)
                  Ticket = ki4.reissueGroupTicket(op.param1)
                  ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ki4.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in ki4mid:
              if op.param2 not in Bots:
                try:
                  G = ki5.getGroup(op.param1)
                  ki5.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ki5.updateGroup(G)
                  Ticket = ki5.reissueGroupTicket(op.param1)
                  ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ki5.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in ki5mid:
              if op.param2 not in Bots:
                try:
                  G = ki6.getGroup(op.param1)
                  ki6.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ki6.updateGroup(G)
                  Ticket = ki6.reissueGroupTicket(op.param1)
                  ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ki6.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in ki6mid:
              if op.param2 not in Bots:
                try:
                  G = ki7.getGroup(op.param1)
                  ki7.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ki7.updateGroup(G)
                  Ticket = ki7.reissueGroupTicket(op.param1)
                  ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ki7.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in ki7mid:
              if op.param2 not in Bots:
                try:
                  G = ki8.getGroup(op.param1)
                  ki8.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ki.updateGroup(G)
                  Ticket = ki8.reissueGroupTicket(op.param1)
                  ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ki8.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in ki8mid:
              if op.param2 not in Bots:
                try:
                  G = ki9.getGroup(op.param1)
                  ki9.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ki9.updateGroup(G)
                  Ticket = ki9.reissueGroupTicket(op.param1)
                  ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ki9.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in ki9mid:
              if op.param2 not in Bots:
                try:
                  G = ki10.getGroup(op.param1)
                  ki10.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ki10.updateGroup(G)
                  Ticket = ki10.reissueGroupTicket(op.param1)
                  ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ki10.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in ki10mid:
              if op.param2 not in Bots:
                try:
                  G = cl.getGroup(op.param1)
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(op.param1)
                  ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        cl.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e

#--------------------------------                      
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message


            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
                    
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        ki2.sendText(msg.to,"deleted")
                        ki3.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        ki2.sendText(msg.to,"It is not in the black list")
                        ki3.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        ki2.sendText(msg.to,"already")
                        ki3.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        ki2.sendText(msg.to,"aded")
                        ki3.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        ki2.sendText(msg.to,"deleted")
                        ki3.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        ki2.sendText(msg.to,"It is not in the black list")
                        ki3.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Admin menu"]:
              #if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Sett)
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("K1 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("K1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("K2 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("K2 gn ","")
                    ki2.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("K3 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("K3 gn ","")
                    ki3.updateGroup(X)
                else:
                    ki3.sendText(msg.to,"It can't be used besides the group.")
            elif "Crott " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pas
            elif "Crott1 " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ki.kickoutFromGroup(msg.to,[target])
                   except:
                      pas
            elif "Crott2 " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ki2.kickoutFromGroup(msg.to,[target])
                   except:
                      pas
            elif "Crott3 " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ki3.kickoutFromGroup(msg.to,[target])
                   except:
                      pas
            elif "Crott4 " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ki5.kickoutFromGroup(msg.to,[target])
                   except:
                      pas
            elif "Crott6 " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ki6.kickoutFromGroup(msg.to,[target])
                   except:
                      pas
            elif "Crott7 " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ki7.kickoutFromGroup(msg.to,[target])
                   except:
                      pas
            elif "Crott8 " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ki8.kickoutFromGroup(msg.to,[target])
                   except:
                      pas
            elif "Crott9 " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ki9.kickoutFromGroup(msg.to,[target])
                   except:
                      pas
            elif "Crott10 " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ki10.kickoutFromGroup(msg.to,[target])
                   except:
                      pas
            elif "Crott11 " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      kibackup.kickoutFromGroup(msg.to,[target])
                   except:
                      pas
            elif "Invite " in msg.text:
              #if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "K1 invite " in msg.text:
              #if msg.from_ in admin:
                midd = msg.text.replace("K1 invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "K2 invite " in msg.text:
              #if msg.from_ in admin:
                midd = msg.text.replace("K2 invite ","")
                ki2.findAndAddContactsByMid(midd)
                ki2.inviteIntoGroup(msg.to,[midd])
            elif "K3 invite " in msg.text:
              #if msg.from_ in admin:
                midd = msg.text.replace("K3 invite ","")
                ki3.findAndAddContactsByMid(midd)
                ki3.inviteIntoGroup(msg.to,[midd])
            elif "K4 invite " in msg.text:
              #if msg.from_ in admin:
                midd = msg.text.replace("Bot4 invite ","")
                ki4.findAndAddContactsByMid(midd)
                ki4.inviteIntoGroup(msg.to,[midd])
            elif "K5 invite " in msg.text:
              #if msg.from_ in admin:
                midd = msg.text.replace("Bot5 invite ","")
                ki5.findAndAddContactsByMid(midd)
                ki5.inviteIntoGroup(msg.to,[midd])
            elif "Bot invite " in msg.text:
              #if msg.from_ in admin:
                midd = msg.text.replace("Bot invite ","")
                random.choice(KAC).findAndAddContactsByMid(midd)
                random.choice(KAC).inviteIntoGroup(msg.to,[midd])
    #--------------- SC Add Admin ---------
            elif "Admin add @" in msg.text:
              print "[Command]Staff add executing"
              _name = msg.text.replace("Admin add @","")
              _nametarget = _name.rstrip('  ')
              gs = cl.getGroup(msg.to)
              gs = ki.getGroup(msg.to)
              gs = ki2.getGroup(msg.to)
              gs = ki3.getGroup(msg.to)
              gs = ki4.getGroup(msg.to)
              gs = ki5.getGroup(msg.to)
              gs = ki6.getGroup(msg.to)
              gs = ki7.getGroup(msg.to)
              gs = ki8.getGroup(msg.to)
              gs = ki9.getGroup(msg.to)
              gs = ki10.getGroup(msg.to)
              targets = []
              for g in gs.members:
                if _nametarget == g.displayName:
                  targets.append(g.mid)
              if targets == []:
                random.choice(KAC).sendText(msg.to,"Contact not found")
              else:
                for target in targets:
                  try:
                    admin.append(target)
                    cl.sendText(msg.to,"Admin Ditambahkan")
                  except:
                    pass
                #print "[Command]Staff add executed"
              #else:
                #cl.sendText(msg.to,"Command denied.")
                #cl.sendText(msg.to,"Admin permission required.")
                
            elif "Admin remove @" in msg.text:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = ki2.getGroup(msg.to)
                gs = ki3.getGroup(msg.to)
                gs = ki4.getGroup(msg.to)
                gs = ki5.getGroup(msg.to)
                gs = ki6.getGroup(msg.to)
                gs = ki7.getGroup(msg.to)
                gs = ki8.getGroup(msg.to)
                gs = ki9.getGroup(msg.to)
                gs = ki10.getGroup(msg.to)
                #gs = k1.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"Admin Dihapus")
                        except:
                            pass
                #print "[Command]Staff remove executed"
              #else:
                #cl.sendText(msg.to,"Command denied.")
                #cl.sendText(msg.to,"Admin permission required.")
                
            elif msg.text in ["Adminlist","adminlist"]:
              if admin == []:
                  cl.sendText(msg.to,"The stafflist is empty")
              else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "||Admin Destroyer Bot||\n=====================\n"
                  for mi_d in admin:
                      mc += "••>" +cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
    #--------------------------------------
    #-------------- Add Friends ------------
            elif "Bot add @" in msg.text:
              if msg.toType == 2:
                if msg.from_ in owner:
                  print "[Command]Add executing"
                  _name = msg.text.replace("Bot Add @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  gs = ki.getGroup(msg.to)
                  gs = ki2.getGroup(msg.to)
                  gs = ki3.getGroup(msg.to)
                  gs = ki4.getGroup(msg.to)
                  gs = ki5.getGroup(msg.to)
                  gs = ki6.getGroup(msg.to)
                  gs = ki7.getGroup(msg.to)
                  gs = ki8.getGroup(msg.to)
                  gs = ki9.getGroup(msg.to)
                  gs = ki10.getGroup(msg.to)
                  gs = kibackup.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    random.choice(KAC).sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        ki.findAndAddContactsByMid(target)
                        ki2.findAndAddContactsByMid(target)
                        ki3.findAndAddContactsByMid(target)
                        ki4.findAndAddContactsByMid(target)
                        ki5.findAndAddContactsByMid(target)
                        ki6.findAndAddContactsByMid(target)
                        ki7.findAndAddContactsByMid(target)
                        ki8.findAndAddContactsByMid(target)
                        ki9.findAndAddContactsByMid(target)
                        ki10.findAndAddContactsByMid(target)
                        kibackup.findAndAddContactsByMid(target)
                      except:
                        cl.sendText(msg.to,"Error")
              else:
                cl.sendText(msg.to,"Perintah Ditolak.")                
                cl.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
              #else:
                #cl.sendText(msg.to,"Perintah Ditolak")
                #cl.sendText(msg.to,"Perintah ini Hana Untuk Owner Kami")
                  
    #-------------=SC AllBio=----------------
            elif "Allbio:" in msg.text:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki6.getProfile()
                    profile.statusMessage = string
                    ki6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki7.getProfile()
                    profile.statusMessage = string
                    ki7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki8.getProfile()
                    profile.statusMessage = string
                    ki8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki9.getProfile()
                    profile.statusMessage = string
                    ki9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki10.getProfile()
                    profile.statusMessage = string
                    ki10.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kibackup.getProfile()
                    profile.statusMessage = string
                    kibackup.updateProfile(profile)
                    cl.sendText(msg.to,"Bio berubah menjadi " + string + "")
    #--------------=Finish=----------------
    #--------------= SC Ganti nama Owner=--------------
            elif "MyName:" in msg.text:
              #if msg.from_ in admin:
                string = msg.text.replace("MyName:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Name Menjadi : " + string + "")
    #-------------- copy profile----------
            elif "Steal group" in msg.text:
                   group = cl.getGroup(msg.to)
                   path =("http://dl.profile.line-cdn.net/" + group.pictureStatus)
                   cl.sendImageWithUrl(msg.to, path)
    #-----------------=Selesai=------------------#
            elif "Spamcontact @" in msg.text:
                _name = msg.text.replace("Spamcontact @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       ki.sendText(g.mid,"MAAF KAKAK GANGGU ")
                       ki.sendText(g.mid,"SIBUK GAKKKK")  
                       ki2.sendText(g.mid,"UDH MAKAN KAH KAK")  
                       ki3.sendText(g.mid,"LAGI APA KAKAK")
                       ki4.sendText(g.mid,"DMANA KAKAK TINGGAL")
                       ki5.sendText(g.mid,"SPAM KITA BAGUS GAK ")
                       ki6.sendText(g.mid,"ENAKIN YA KAK")
                       ki7.sendText(g.mid,"UNCH")
                       ki8.sendText(g.mid,"TAYANG")
                       ki9.sendText(g.mid,"MMUCH")
                       ki10.sendText(g.mid,"THANKS KAKAK !")
                       kibackup.sendText(g.mid,"UNDH MELIHAT SPAM KITA")
                       ki1.sendText(msg.to, "Done")
                       print " Spammed !"
#------------------------------------------------------------------#
            elif msg.text in ["Mybot"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                cl.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                cl.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                cl.sendMessage(msg)
           
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                cl.sendMessage(msg)
           
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki10mid}
                cl.sendMessage(msg)
           
                msg.contentType = 13
                msg.contentMetadata = {'mid': kibackupmid}
                cl.sendMessage(msg)
           
#------------------------------------------------------------------#
            elif msg.text in ["Me"]:
              ##if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)
            elif msg.text in ["Bot1"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
              #if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
              ##if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                kibackup.sendMessage(msg)
                ki12.sendMessage(msg)
                ki13.sendMessage(msg)
                ki14.sendMessage(msg)
                ki15.sendMessage(msg)
                ki16.sendMessage(msg)
                ki17.sendMessage(msg)
                ki18.sendMessage(msg)
            elif msg.text in ["Cancel","cancel"]:
              ##if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["bot cancel","Bot cancel"]:
            ##if msg.from_ in admin:
                if msg.toType == 2:
                    G = ki.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"No one is inviting")
                        else:
                            ki.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Buka qr","Open qr","Ourl","Open","Buka"]:
              ##if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"QR Sudah Dibuka")
                    else:
                        cl.sendText(msg.to,"Sudah Terbuka Boss")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["K1 open"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Plak")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["K2 open"]:
                if msg.toType == 2:
                    X = ki2.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki2.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"Done Plak")
                    else:
                        ki2.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki2.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["k3 open"]:
                if msg.toType == 2:
                    X = ki3.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki3.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki3.sendText(msg.to,"Done Plak")
                    else:
                        ki3.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        ki3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki3.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Tutup qr","Close qr","Curl","Close","Tutup"]:
              #if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kode QR Sudah Di Tutup")
                    else:
                        cl.sendText(msg.to,"Sudah Tertutup Boss")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
                     
            elif "Ginfo" == msg.text:
              if msg.toType == 2:
                if msg.from_ in admin:
                  ginfo = cl.getGroup(msg.to)
                  try:
                    gCreator = ginfo.creator.displayName
                  except:
                    gCreator = "Error"
                  if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                      sinvitee = "0"
                    else:
                      sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventJoinByTicket == True:
                      QR = "Close"
                    else:
                      QR = "Open"
                    cl.sendText(msg.to,"[Group Name]\n" + "[•]" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + "[•]" + gCreator + "\n\n[Group Status]\n" + "[•]Status QR =>" + QR + "\n\n[Group Picture]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                  else:
                    cl.sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Can not be used outside the group")
                  else:
                    cl.sendText(msg.to,"Not for use less than group")
                
            #elif "My mid" == msg.text:
              #cl.sendText(msg.to, msg.from_)
            elif "Mid bot" == msg.text:
              ##if msg.from_ in admin:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                ki6.sendText(msg.to,ki6mid)
                ki7.sendText(msg.to,ki7mid)
                ki8.sendText(msg.to,ki8mid)
                ki9.sendText(msg.to,ki9mid)
                ki10.sendText(msg.to,ki10mid)
                kibackup.sendText(msg.to,ki10mid)
                
            elif "Mymid" == msg.text:
              #if msg.from_ in admin:
                cl.sendText(msg.to, msg.from_)
           
            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Galau"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif "TL:" in msg.text:
              #if msg.from_ in admin:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Names Menjadi : " + string + "")
            elif "1name:" in msg.text:
                string = msg.text.replace("1name:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "2name:" in msg.text:
                string = msg.text.replace("2name:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "3name:" in msg.text:
                string = msg.text.replace("3name:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "4name:" in msg.text:
                string = msg.text.replace("4name:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "5name:" in msg.text:
                string = msg.text.replace("5name:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "6name:" in msg.text:
                string = msg.text.replace("6name:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "7name:" in msg.text:
                string = msg.text.replace("7name:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                    ki7.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "8name:" in msg.text:
                string = msg.text.replace("8name:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                    ki8.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "9name:" in msg.text:
                string = msg.text.replace("9name:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                    ki9.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "10name:" in msg.text:
                string = msg.text.replace("10name:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki10.getProfile()
                    profile.displayName = string
                    ki10.updateProfile(profile)
                    ki10.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "name11:" in msg.text:
                string = msg.text.replace("name11:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = kibackup.getProfile()
                    profile.displayName = string
                    kibackup.updateProfile(profile)
                    kibackup.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "name12:" in msg.text:
                string = msg.text.replace("name12:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = kibackup.getProfile()
                    profile.displayName = string
                    kibackup1.updateProfile(profile)
                    kibackup1.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif msg.text in ["Mc "]:
              #if msg.from_ in admin:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
                
#-------------------- Protect Mode ------------
            elif msg.text in ["Allprotect on","Mode on"]:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group On􀜁􀇊􏿿")
                    else:
                        cl.sendText(msg.to,"Kick Joined Group On􀜁􀇊􏿿")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Udah On")
                    else:
                        cl.sendText(msg.to,"Udah On")
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Invit On")
                    else:
                        cl.sendText(msg.to,"Invit on")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Invit On")
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                    else:
                        cl.sendText(msg.to,"Cancel on")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                if wait["protectionOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect On")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["protectionOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect On")
                    else:
                        cl.sendText(msg.to,"Done")
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Link On")
                    else:
                        cl.sendText(msg.to,"Link On")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Link On")
                    else:
                        cl.sendText(msg.to,"done")

            elif msg.text in ["Allprotect off","Mode Off"]:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"Kick Joined Gtoup Off�")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Udah Mati Gblk")
                    else:
                        cl.sendText(msg.to,"Udah Mati Gblk")

                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Invite Off")
                    else:
                        cl.sendText(msg.to,"Invite OFF")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Invite Off")
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                if wait["protectionOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["protectionOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Off")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
#----------------------------------------------
            elif msg.text in ["Protect on","protect on"]:
              #if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect set to ON")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect set to ON")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Protect off","protect off"]:
              #if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect set to Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect set to Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel on","cancel on"]:
              #if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel set to ON")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel set to ON")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel off","cancel off"]:
              #if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel set to ON")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel set to ON")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Invite on","invite on"]:
              #if msg.from_ in admin:
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Invit set to ON")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Invit set to ON")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel off","cancel off"]:
              #if msg.from_ in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Invit set to Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Invit set to Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr on","qr on"]:
              #if msg.from_ in admin:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR set to ON")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR set to ON")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
              #if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR set to Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR set to Off")
                    else:
                        cl.sendText(msg.to,"done")
                        
            elif msg.text in ["Contact On","Contact on","contact on"]:
              #if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              #if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Join on","Auto join on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
              #if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Join off","Auto join off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
              #if msg.from_ in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
              #if msg.from_ in admin:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
              #if msg.from_ in admin:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
              #if msg.from_ in admin:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
              #if msg.from_ in admin:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
                        
            elif msg.text in ["Status","Set","Set view","Cek"]:
              #if msg.from_ in admin:
                md =    "-= Bot Setting =-\n\n"
                if wait["Backup"] == True: md+="[Ж]Backup: [On]\n"
                else: md+="[Ж]Backup: [Off]\n"
                if wait["Contact"] == True: md+="[Ж]Contact: [On]\n"
                else: md+="[Ж]Contact: [Off]\n"
                if wait["autoJoin"] == True: md+="[Ж]Auto Join: [On]\n"
                else: md +="[Ж]Auto Join: [Off]\n"
                if wait["autoCancel"] == True:md+="[Ж]Group Cancel: [On]" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "[Ж]Group Cancel [Off]\n"
                if wait["leaveRoom"] == True: md+="[Ж]Auto Leave: [On]\n"
                else: md+="[Ж]Auto Leave: [Off]\n"
                if wait["timeline"] == True: md+="[Ж]Share: [On]\n"
                else:md+="[Ж]Share: [Off]\n"
                if wait["autoAdd"] == True: md+="[Ж]Auto Add: [On]\n"
                else:md+="[Ж]Auto Add: [Off]\n"
                if wait["Protectjoin"] == True: md+="[Ж]Protect: [On]\n"
                else: md+="[Ж]Protect: [Off]\n"
                if wait["Protectgr"] == True: md+="[Ж]Link Protect: [On]\n"
                else: md+="[Ж]Link Protect: [Off]\n"
                if wait["Protectcancl"] == True: md+="[•]Invitation Protect: [On]\n"
                else: md+="[Ж]Invitation Protect: [Off]\n"
                if wait["Protectcancel"] == True: md+="[[Ж]]Cancel Protect: [On]\n"
                else: md+="[Ж]Cancel Protect: [Off]\n"
                cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id","Ginfo"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif "album removeat’" in msg.text:
                gid = msg.text.replace("album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
              #if msg.from_ in admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
              #if msg.from_ in admin:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change:","")
                cl.sendText(msg.to,"message changed")
            elif "Message set: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
#---------------------Sc invite owner ke group------
            elif "/invitemeto: " in msg.text:
              #if msg.from_ in admin:
                gid = msg.text.replace("/invitemeto: ","")
                if gid == "":
                  ki.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    ki.findAndAddContactsByMid(msg.from_)
                    ki.inviteIntoGroup(gid,[msg.from_])
                  except:
                    ki.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#--------===---====--------------
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
              #if msg.from_ in admin:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment off","comment off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Url"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["K1 url"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["K2 url"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki2.updateGroup(x)
                    gurl = ki2.reissueGroupTicket(msg.to)
                    ki2.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["K3 url"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki3.updateGroup(x)
                    gurl = ki3.reissueGroupTicket(msg.to)
                    ki3.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["Jam on"]:
              #if msg.from_ in admin:
                if wait["clock"] == True:
                    ki.sendText(msg.to,"Bot 1 jam on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = ki.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"Jam Selalu On")
            elif msg.text in ["Jam off"]:
              #if msg.from_ in admin:
                if wait["clock"] == False:
                    ki.sendText(msg.to,"Bot 4 jam off")
                else:
                    wait["clock"] = False
                    ki.sendText(msg.to,"Jam Sedang Off")
        #-------------Fungsi Jam on/off Finish-------------------#           
         
        #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["Change clock"]:
                n = msg.text.replace("Change clock","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
        #-------------Fungsi Change Clock Finish-----------------#           
        
         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["Jam Update"]:
                if wait["clock"] == True:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"(%H:%M)")
                    profile = ki.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"Sukses update")
                else:
                    ki.sendText(msg.to,"Aktifkan jam terlebih dulu")
        #-------------Fungsi Jam Update Finish-------------------#

            elif msg.text == "Cctv":
              #if msg.from_ in admin:
                cl.sendText(msg.to, "Cek CCTV")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
                  pass
                now2 = datetime.datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                #print wait2
              
            elif msg.text == "Ciduk":
                 #if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                #print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "=====Di Read Oleh=====%s\n=====Anime BOT=====\n\n=====Pelaku CCTV=====\n%s=====CCTV=====\n•Panuan\nAmin Yallah[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik Cctv dulu Koplak\nBaru Ketik Ciduk\nDASAR PIKUN ♪")
                        
            elif msg.text in ["@set"]:
              #if msg.from_ in admin:
                 if msg.toType == 2:
                   cl.sendText(msg.to, "「Lurking On」")
                   try:
                       del wait2['readPoint'][msg.to]
                       del wait2['readMember'][msg.to]
                   except:
                       pass
                   wait2['readPoint'][msg.to] = msg.id
                   wait2['readMember'][msg.to] = ""
                   wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                   wait2['ROM'][msg.to] = {}
                   print "set point"

            elif msg.text in ["Cyduk"]:
              #if msg.from_ in admin:
                 if msg.toType == 2:
                    print "\nSider aktif..."
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, " Daftar Sider :\n╔═════[~TERSANGKA~]═════╗%s\n╚═════[~TERSANGKA~]═════╝%s\n===========================\nIn the last seen point:\n[%s]\n===========================\nѕuppσrt вч:\n•A̶҉̶҉̶҉̶N̶҉̶҉̶҉̶I̶҉̶҉̶҉̶M̶҉̶҉̶҉̶E̶҉̶҉̶҉̶ T̶҉̶҉̶҉̶E̶҉̶҉̶҉̶A̶҉̶҉̶҉̶M̶҉̶҉̶҉̶ B̶҉̶҉̶҉̶O̶҉̶҉̶҉̶T̶҉̶҉̶҉̶•\n✍T҉̶̘̟̼̉̈́͐͋͌̊Σ̶Δ̶M҉̶̘͈̺̪͓̺ͩ͂̾ͪ̀̋ ̶̶̶D̶̶꙯꙯꙰꙰͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎E̶̶꙯꙯꙰꙰͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎S̶̶꙯꙯꙰꙰͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎T̶̶꙯꙯꙰꙰͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎R̶̶꙯꙯꙰꙰͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎O̶̶꙯꙯꙰꙰͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎Y̶̶꙯꙯꙰꙰͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎E̶̶꙯꙯꙰꙰͎͎͎͎͎͎͎͎͎͎͎͎͎͎͎R̶̶꙯꙯꙰꙰͎͎͎͎͎͎͎͎͎͎͎͎͎͎Sβ̶Ω̶T҉̶̘̟̼̉̈́͐͋͌̊✈" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "\nReading Point Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print "lukers"
                        cl.sendText(msg.to, "Auto set reading point in:\n" + (wait2['setTime'][msg.to]))
                    else:
                        cl.sendText(msg.to, "Set reading point first")


#-----------------------------------------------

#-----------------------------------------------
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["Masuk","~"]:
              #if msg.from_ in owner or admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        kibackup.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki.sendText(msg.to,"ALL COMPLETE JOIN BOSS..!!!")
                        H = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        H.preventJoinByTicket = True
                        cl.updateGroup(H)
                        print "Semua Sudah Lengkap"
                        
            elif msg.text in ["."]:
              #if msg.from_ in owner or admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        
            elif msg.text in ["Sayang Kamu dmna"]:
              #if msg.from_ in owner or admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki.sendText(msg.to,"Apa sayang aku disini")
                        cl.sendText(msg.to,"gapapa sayang aku sange")
                        ki.sendText(msg.to,"ugh sini ngentot sayang")
                        cl.sendText(msg.to,"Aku udh crott sayang makasih ya")
                        ki.sendText(msg.to,"Udh puas kan sayang☺ydh aku out ya sayang")
                        H = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        H.preventJoinByTicket = True
                        cl.updateGroup(H)
                        cl.getGroup(msg.to)
                        ki.leaveGroup(msg.to)
                        
            elif msg.text in ["K1~"]:
              #if msg.from_ in owner or admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki.sendText(msg.to,"Hay kakak numpang lewat ya")
                        group = ki.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members]
      
                        cb = ""
                        cb2 = ""
                        strt = int(0)
                        akh = int(0)
                        for md in nama:
                            akh = akh + int(6)
      
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
      
                            strt = strt + int(7)
                            akh = akh + 1
                            cb2 += "@nrik \n"
      
                        cb = (cb[:int(len(cb)-1)])
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
      
                        try:
                            ki.sendMessage(msg)
                        except Exception as error:
                          print error
                        ki.sendText(msg.to,"Oke,sekian terimakasih😚")
                        H = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        H.preventJoinByTicket = True
                        cl.updateGroup(H)
                        cl.getGroup(msg.to)
                        ki.leaveGroup(msg.to)
                        
            elif msg.text in ["K2~"]:
              #if msg.from_ in owner or admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.sendText(msg.to,"Hay kakak numpang lewat ya")
                        group = ki.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members]
      
                        cb = ""
                        cb2 = ""
                        strt = int(0)
                        akh = int(0)
                        for md in nama:
                            akh = akh + int(6)
      
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
      
                            strt = strt + int(7)
                            akh = akh + 1
                            cb2 += "@nrik \n"
      
                        cb = (cb[:int(len(cb)-1)])
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
      
                        try:
                            ki2.sendMessage(msg)
                        except Exception as error:
                          print error
                        ki2.sendText(msg.to,"Oke,sekian terimakasih😚")
                        H = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        H.preventJoinByTicket = True
                        cl.updateGroup(H)
                        cl.getGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        
            elif msg.text in ["K3~"]:
              #if msg.from_ in owner or admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.sendText(msg.to,"Hay kakak numpang lewat ya")
                        group = ki.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members]
      
                        cb = ""
                        cb2 = ""
                        strt = int(0)
                        akh = int(0)
                        for md in nama:
                            akh = akh + int(6)
      
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
      
                            strt = strt + int(7)
                            akh = akh + 1
                            cb2 += "@nrik \n"
      
                        cb = (cb[:int(len(cb)-1)])
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
      
                        try:
                            ki3.sendMessage(msg)
                        except Exception as error:
                          print error
                        ki3.sendText(msg.to,"Oke,sekian terimakasih😚")
                        H = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        H.preventJoinByTicket = True
                        cl.updateGroup(H)
                        cl.getGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        
            elif msg.text in ["K1 in"]:
              #if msg.from_ in owner or admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        H = ki.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        H.preventJoinByTicket = True
                        ki.updateGroup(H)
                        
            elif msg.text in ["K2 in"]:
              #if msg.from_ in owner or admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        H = ki.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        H.preventJoinByTicket = True
                        ki2.updateGroup(H)
                        
            elif msg.text in ["K3 in"]:
              #if msg.from_ in owner or admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        H = ki.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        H.preventJoinByTicket = True
                        ki3.updateGroup(H)

    #----------------------Fungsi Join Group Finish---------------#

    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["Cabut","Keluar","Huss"]:
              #if msg.from_ in admin:
                if msg.toType == 2:
                  ki.sendText(msg.to,"Thanks ya udh di invit di grup ini😚")
                  ki.sendText(msg.to,"Sampai jumpa Kembali Sayang😚")
                  cl.getGroup(msg.to)
                  ki.leaveGroup(msg.to)
                  ki2.leaveGroup(msg.to)
                  ki3.leaveGroup(msg.to)
                  ki4.leaveGroup(msg.to)
                  ki5.leaveGroup(msg.to)
                  ki6.leaveGroup(msg.to)
                  ki7.leaveGroup(msg.to)
                  ki8.leaveGroup(msg.to)
                  ki9.leaveGroup(msg.to)
                  ki10.leaveGroup(msg.to)
                  kibackup.leaveGroup(msg.to)
                  
            elif msg.text in ["K1 @bye"]:
              #if msg.from_ in admin:
                if msg.toType == 2:
                  cl.getGroup(msg.to)
                  ki.leaveGroup(msg.to)
                  
            elif msg.text in ["K2 @bye"]:
              #if msg.from_ in admin:
                if msg.toType == 2:
                  cl.getGroup(msg.to)
                  ki2.leaveGroup(msg.to)
                  
            elif msg.text in ["K3 @bye"]:
              #if msg.from_ in admin:
                if msg.toType == 2:
                  cl.getGroup(msg.to)
                  ki3.leaveGroup(msg.to)
                  
            elif msg.text in ["Gbye"]:
              #if msg.from_ in admin:
                if msg.toType == 2:
                  cl.getGroup(msg.to)
                  cl.leaveGroup(msg.to)

    #-------------Fungsi Leave Group Finish---------------#
    
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Anu","Ena"]:
              #if msg.from_ in admin:
              	 if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
  
                    cb = ""
                    cb2 = ""
                    strt = int(0)
                    akh = int(0)
                    for md in nama:
                        akh = akh + int(6)
  
                        cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
  
                        strt = strt + int(7)
                        akh = akh + 1
                        cb2 += "@nrik \n"
  
                    cb = (cb[:int(len(cb)-1)])
                    msg.contentType = 0
                    msg.text = cb2
                    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
  
                    try:
                        cl.sendMessage(msg)
                    except Exception as error:
                      print error
                    
            elif "Steal home @" in msg.text:
              #if msg.from_ in admin:
                 print "[Command]dp executing"
                 _name = msg.text.replace("Steal home @","")
                 _nametarget = _name.rstrip('  ')
                 gs = cl.getGroup(msg.to)
                 targets = []
                 for g in gs.members:
                     if _nametarget == g.displayName:
                         targets.append(g.mid)
                 if targets == []:
                     ki.sendText(msg.to,"Contact not found")
                 else:
                     for target in targets:
                         try:
                             contact = cl.getContact(target)
                             cu = cl.channel.getCover(target)
                             path = str(cu)
                             cl.sendImageWithUrl(msg.to, path)
                         except:
                             pass
                 print "[Command]dp executed"			
 #------------------------------------------------------------------
            elif "Steal dp @" in msg.text:
              #if msg.from_ in admin:
                 print "[Command]dp executing"
                 _name = msg.text.replace("Steal dp @","")
                 _nametarget = _name.rstrip('  ')
                 gs = cl.getGroup(msg.to)
                 targets = []
                 for g in gs.members:
                     if _nametarget == g.displayName:
                         targets.append(g.mid)
                 if targets == []:
                     ki.sendText(msg.to,"Contact not found")
                 else:
                     for target in targets:
                         try:
                             contact = cl.getContact(target)
                             path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                             cl.sendImageWithUrl(msg.to, path)
                         except:
                             pass
                 print "[Command]dp executed"
                 
            elif "Getname @" in msg.text:
              #if msg.from_ in admin:
                 _name = msg.text.replace("Getname @","")
                 _nametarget = _name.rstrip(" ")
                 gs = cl.getGroup(msg.to)
                 for h in gs.members:
                   if _nametarget == h.displayName:
                      cl.sendText(msg.to,"[DisplayName]:\n" + h.displayName )
                   else:
                     pass
                   
            elif msg.text in ["Backup:on","backup:on"]:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Backup On\n\n"+ datetime.datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup On\n\n"+ datetime.datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"already on\n\n"+ datetime.datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Backup:off","backup:off"]:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Backup Off\n\n"+ datetime.datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup Off\n\n"+ datetime.datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.datetime.today().strftime('%H:%M:%S'))
            elif "Getbio @" in msg.text:
              #if msg.from_ in admin:
                 _name = msg.text.replace("Getbio @","")
                 _nametarget = _name.rstrip(" ")
                 gs = cl.getGroup(msg.to)
                 for h in gs.members:
                   if _nametarget == h.displayName:
                      cl.sendText(msg.to,"[StatusMessage]:\n" + h.statusMessage) 
                   else:
                     pass
            elif "Getcontact" in msg.text:
              #if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
            elif msg.text in ["Myname"]:
              #if msg.from_ in admin:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[DisplayName]===\n" + h.displayName)
            elif msg.text in ["Mybio"]:
              #if msg.from_ in admin:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[StatusMessage]===\n" + h.statusMessage)
            elif msg.text in ["Mypict"]:
              #if msg.from_ in admin:
                    h = cl.getContact(mid)
                    cl.sendImageWithUrl(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Mycover"]:
              #if msg.from_ in admin:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendImageWithUrl(msg.to, path)
            elif 'instagram ' in msg.text.lower():
              #if msg.from_ in admin:
                if msg.from_ in admin:
                  try:
                      instagram = msg.text.lower().replace("instagram ","")
                      html = requests.get('https://www.instagram.com/' + instagram + '/?')
                      soup = BeautifulSoup(html.text, 'html5lib')
                      data =soup.find_all('meta', attrs={'property':'og:description'})
                      text = data[0].get('content').split()
                      data1 =soup.find_all('meta', attrs={'property':'og:image'})
                      text1 = data1[0].get('content').split()
                      user = "Name: " + text[-2] + "\n"
                      user1 = "Username: " + text[-1] + "\n"
                      followers = "Followers: " + text[0] + "\n"
                      following = "Following: " + text[2] + "\n"
                      post = "Post: " + text[4] + "\n"
                      link = "Link: "+ "https://www.instagram.com/" + instagram
                      detail = "======INSTAGRAM INFO USER======\n"
                      details = "\n======INSTAGRAM INFO USER======"
                      cl.sendText(msg.to, detail+ user + user1 + followers + following + post + link + details)
                      cl.sendImageWithUrl(msg.to, text1[0])
                  except Exception as njer:
                          cl.sendText(msg.to, str(njer))
    #-------------Fungsi Tag All Finish---------------#
    #-------------Tag All Test------------------------#
    #-------------------------------------------------#
            elif msg.text in ["Bot Like", "Bot like"]:
              #if msg.from_ in admin:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Owner")
                try:
                  likePost()
                except:
                  pass
                
            elif msg.text in ["Like temen", "Bot like temen"]:
              #if msg.from_ in admin:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Teman Boss")
                try:
                  autolike()
                except:
                  pass
        #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill "]:
              #if msg.from_ in admin:
                if msg.toType == 2:
                    group = random.choice(KAC).getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Selamat tinggal")
                        random.choice(KAC).sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
        #----------------Fungsi Banned Kick Target Finish----------------------#   
        #------------ Copy & Backup -------------#
            elif msg.text in ["Backup","backup"]:
              #if msg.from_ in admin:
                try:
                  cl.updateDisplayPicture(backup.pictureStatus)
                  cl.updateProfile(backup)
                  cl.sendText(msg.to,"Backup done")
                except Exception as e:
                  cl.sendText(msg.to, str (e))
                
            elif "Copy @" in msg.text:
              #if msg.from_ in admin:
                if msg.toType == 2:
                  print"[Copy]"
                  _name = msg.text.replace("Copy @","")
                  _nametarget = _name.rstrip(' ')
                  gs = cl.getGroup(msg.to)
                  targets=[]
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    cl.sendText(msg.to,"Not Found")
                  else:
                    for target in targets:
                      try:
                        cl.CloneContactProfile(target)
                        cl.sendText(msg.to,"Success Copy")
                      except Exception as e:
                        print e
                      
            elif "Copy1 @" in msg.text:
              #if msg.from_ in admin:
                if msg.toType == 2:
                  print"[Copy]"
                  _name = msg.text.replace("Copy1 @","")
                  _nametarget = _name.rstrip(' ')
                  gs = ki.getGroup(msg.to)
                  targets=[]
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    cl.sendText(msg.to,"Not Found")
                  else:
                    for target in targets:
                      try:
                        ki.CloneContactProfile(target)
                        ki.sendText(msg.to,"Success Copy")
                      except Exception as e:
                        print e
                      
            elif "Copy2 @" in msg.text:
              #if msg.from_ in admin:
                if msg.toType == 2:
                  print"[Copy]"
                  _name = msg.text.replace("Copy2 @","")
                  _nametarget = _name.rstrip(' ')
                  gs = ki2.getGroup(msg.to)
                  targets=[]
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    cl.sendText(msg.to,"Not Found")
                  else:
                    for target in targets:
                      try:
                        ki2.CloneContactProfile(target)
                        ki2.sendText(msg.to,"Success Copy")
                      except Exception as e:
                        print e
                      
            elif "Copy3 @" in msg.text:
              #if msg.from_ in admin:
                if msg.toType == 2:
                  print"[Copy]"
                  _name = msg.text.replace("Copy3 @","")
                  _nametarget = _name.rstrip(' ')
                  gs = ki.getGroup(msg.to)
                  targets=[]
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    cl.sendText(msg.to,"Not Found")
                  else:
                    for target in targets:
                      try:
                        ki3.CloneContactProfile(target)
                        ki3.sendText(msg.to,"Success Copy")
                      except Exception as e:
                        print e
                      
            elif "Copy4 @" in msg.text:
              #if msg.from_ in admin:
                if msg.toType == 2:
                  print"[Copy]"
                  _name = msg.text.replace("Copy4 @","")
                  _nametarget = _name.rstrip(' ')
                  gs = ki.getGroup(msg.to)
                  targets=[]
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    cl.sendText(msg.to,"Not Found")
                  else:
                    for target in targets:
                      try:
                        ki4.CloneContactProfile(target)
                        ki4.sendText(msg.to,"Success Copy")
                      except Exception as e:
                        print e
                      
            elif "Copy5 @" in msg.text:
              #if msg.from_ in admin:
                if msg.toType == 2:
                  print"[Copy]"
                  _name = msg.text.replace("Copy5 @","")
                  _nametarget = _name.rstrip(' ')
                  gs = ki5.getGroup(msg.to)
                  targets=[]
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    cl.sendText(msg.to,"Not Found")
                  else:
                    for target in targets:
                      try:
                        ki5.CloneContactProfile(target)
                        ki5.sendText(msg.to,"Success Copy")
                      except Exception as e:
                        print e
                      
            elif "Copy6 @" in msg.text:
              #if msg.from_ in admin:
                if msg.toType == 2:
                  print"[Copy]"
                  _name = msg.text.replace("Copy6 @","")
                  _nametarget = _name.rstrip(' ')
                  gs = ki6.getGroup(msg.to)
                  targets=[]
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    cl.sendText(msg.to,"Not Found")
                  else:
                    for target in targets:
                      try:
                        ki6.CloneContactProfile(target)
                        ki6.sendText(msg.to,"Success Copy")
                      except Exception as e:
                        print e
                      
            elif "Copy7 @" in msg.text:
              #if msg.from_ in admin:
                if msg.toType == 2:
                  print"[Copy]"
                  _name = msg.text.replace("Copy7 @","")
                  _nametarget = _name.rstrip(' ')
                  gs = ki7.getGroup(msg.to)
                  targets=[]
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    cl.sendText(msg.to,"Not Found")
                  else:
                    for target in targets:
                      try:
                        ki7.CloneContactProfile(target)
                        ki7.sendText(msg.to,"Success Copy")
                      except Exception as e:
                        print e
                      
            elif "Copy8 @" in msg.text:
              #if msg.from_ in admin:
                if msg.toType == 2:
                  print"[Copy]"
                  _name = msg.text.replace("Copy8 @","")
                  _nametarget = _name.rstrip(' ')
                  gs = ki8.getGroup(msg.to)
                  targets=[]
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    cl.sendText(msg.to,"Not Found")
                  else:
                    for target in targets:
                      try:
                        ki8.CloneContactProfile(target)
                        ki8.sendText(msg.to,"Success Copy")
                      except Exception as e:
                        print e
                    
            elif "Copy9 @" in msg.text:
              #if msg.from_ in admin:
                if msg.toType == 2:
                  print"[Copy]"
                  _name = msg.text.replace("Copy9 @","")
                  _nametarget = _name.rstrip(' ')
                  gs = ki9.getGroup(msg.to)
                  targets=[]
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    cl.sendText(msg.to,"Not Found")
                  else:
                    for target in targets:
                      try:
                        ki9.CloneContactProfile(target)
                        ki9.sendText(msg.to,"Success Copy")
                      except Exception as e:
                        print e
                      
            elif "Copy10 @" in msg.text:
              #if msg.from_ in admin:
                if msg.toType == 2:
                  print"[Copy]"
                  _name = msg.text.replace("Copy10 @","")
                  _nametarget = _name.rstrip(' ')
                  gs = ki10.getGroup(msg.to)
                  targets=[]
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    cl.sendText(msg.to,"Not Found")
                  else:
                    for target in targets:
                      try:
                        ki10.CloneContactProfile(target)
                        ki10.sendText(msg.to,"Success Copy")
                      except Exception as e:
                        print e
                      
            elif "11copy @" in msg.text:
              #if msg.from_ in admin:
                if msg.toType == 2:
                  print"[Copy]"
                  _name = msg.text.replace("11copy @","")
                  _nametarget = _name.rstrip(' ')
                  gs = kibackup.getGroup(msg.to)
                  targets=[]
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    cl.sendText(msg.to,"Not Found")
                  else:
                    for target in targets:
                      try:
                        kibackup.CloneContactProfile(target)
                        kibackup.sendText(msg.to,"Success Copy")
                      except Exception as e:
                        print e
                      
            elif "12copy @" in msg.text:
              #if msg.from_ in admin:
                if msg.toType == 2:
                  print"[Copy]"
                  _name = msg.text.replace("12copy @","")
                  _nametarget = _name.rstrip(' ')
                  gs = kibackup.getGroup(msg.to)
                  targets=[]
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    cl.sendText(msg.to,"Not Found")
                  else:
                    for target in targets:
                      try:
                        kibackup1.CloneContactProfile(target)
                        kibackup1.sendText(msg.to,"Success Copy")
                      except Exception as e:
                        print e
        #-----------------Steal Cpc-----------------------#
        #-----------------Test Steal cpc-----------------------#  
            elif "Nuke" in msg.text:
              #if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Nuke","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    gs = ki7.getGroup(msg.to)
                    gs = ki8.getGroup(msg.to)
                    gs = ki9.getGroup(msg.to)
                    gs = ki10.getGroup(msg.to)
                    cl.sendText(msg.to,"􀜁􀇔􏿿 See You Bitch 􀜁􀇔􏿿")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                        ki2.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[ki4,ki5,ki6,ki7]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"Group cleanse")
                                
        #----------------Fungsi Kick User Target Start----------------------#
            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki3.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki3.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
                        
            elif "Ki " in msg.text:
                  if msg.from_ in admin:
                       G = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       G.preventJoinByTicket = False
                       cl.updateGroup(G)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       targets = []
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                          try:
                              ki.sendText(msg.to,"Yahh Tercyduk ama eneng😄")
                              ki.kickoutFromGroup(msg.to,[target])
                          except:
                             pass
                       ki.sendText(msg.to,"Done, See YOU😚")
                       H = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       H.preventJoinByTicket = True
                       cl.updateGroup(H)
                       cl.getGroup(msg.to)
                       ki.leaveGroup(msg.to)
                       
            elif "Ki2 " in msg.text:
                  if msg.from_ in admin:
                       G = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       G.preventJoinByTicket = False
                       cl.updateGroup(G)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       targets = []
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                          try:
                              ki2.sendText(msg.to,"Yahh Tercyduk ama eneng😄")
                              ki2.kickoutFromGroup(msg.to,[target])
                          except:
                             pass
                       ki2.sendText(msg.to,"Done, See YOU😚")
                       H = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       H.preventJoinByTicket = True
                       cl.updateGroup(H)
                       cl.getGroup(msg.to)
                       ki2.leaveGroup(msg.to)
                       
            elif "Ki3 " in msg.text:
                  if msg.from_ in admin:
                       G = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       G.preventJoinByTicket = False
                       cl.updateGroup(G)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       targets = []
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                          try:
                              ki3.sendText(msg.to,"Yahh Tercyduk ama eneng😄")
                              ki3.kickoutFromGroup(msg.to,[target])
                          except:
                             pass
                       ki.sendText(msg.to,"Done, See YOU😚")
                       H = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       H.preventJoinByTicket = True
                       cl.updateGroup(H)
                       cl.getGroup(msg.to)
                       ki3.leaveGroup(msg.to)
                                    
        #----------------Fungsi Kick User Target Finish----------------------#      
            elif "Blacklist @ " in msg.text:
              #if msg.from_ in admin:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Succes Plak")
                                except:
                                    cl.sendText(msg.to,"error")
            
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Banned @" in msg.text:
              #if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Banned] Sukses"
                    _name = msg.text.replace("Banned @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    gs = ki7.getGroup(msg.to)
                    gs = ki8.getGroup(msg.to)
                    gs = ki9.getGroup(msg.to)
                    gs = ki10.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Dilarang Banned Bot")
                        ki.sendText(msg.to,"Dilarang Banned Bot")
                        ki2.sendText(msg.to,"Dilarang Banned Bot")
                        ki3.sendText(msg.to,"Dilarang Banned Bot")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun telah sukses di banned")
                            except:
                                cl.sendText(msg.to,"Error")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            #----------------Mid via Tag--------------
            elif "Mid @" in msg.text:
              #if msg.from_ in admin:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            #-----------------------------------------
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              #if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    gs = ki7.getGroup(msg.to)
                    gs = ki8.getGroup(msg.to)
                    gs = ki9.getGroup(msg.to)
                    gs = ki10.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan.....")
                        ki.sendText(msg.to,"Tidak Ditemukan.....")
                        ki2.sendText(msg.to,"Tidak Ditemukan.....")
                        ki3.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                cl.sendText(msg.to,"Error")
          #----------------Fungsi Unbanned User Target Finish-----------------------#
           
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Nyanyi"]:
              #if msg.from_ in admin:
                ki.sendText(msg.to,"Aku belum mandi")
                ki2.sendText(msg.to,"Tak tun tuang")
                ki3.sendText(msg.to,"Tak tun tuang")
                ki4.sendText(msg.to,"Tapi masih cantik juga")
                ki5.sendText(msg.to,"Tak tun tuang")
                ki6.sendText(msg.to,"Tak tun tuang")
                ki7.sendText(msg.to,"apalagi kalau sudah mandi")
                ki8.sendText(msg.to,"Tak tun tuang")
                ki9.sendText(msg.to,"Pasti cantik sekali")
                ki10.sendText(msg.to,"yiha")
                kibackup.sendText(msg.to,"Kalau orang lain melihatku")
                ki.sendText(msg.to,"Tak tun tuang")
                ki2.sendText(msg.to,"Badak aku taba bana")
                ki3.sendText(msg.to,"Tak tun tuang")
                ki4.sendText(msg.to,"Tak tuntuang")
                ki5.sendText(msg.to,"Tapi kalau langsuang diidu")
                ki6.sendText(msg.to,"Tak tun tuang")
                ki7.sendText(msg.to,"Atagfirullah baunya")
                ki8.sendText(msg.to,"Males lanjutin ah")
                ki9.sendText(msg.to,"Kalau Cowok ganteng yang lewat")
                ki10.sendText(msg.to,"Aku acuah jo nyeh")
                kibackup.sendText(msg.to,"kalau apak gaek yang lewat")
                ki.sendText(msg.to,"Aku aniang je nyeh")
                ki2.sendText(msg.to,"Yang penting indak")
                ki3.sendText(msg.to,"Manggaduah urang tak tuntuang")
                ki4.sendText(msg.to,"Walau acok galak surang")
                ki5.sendText(msg.to,"Tak tuntuang Tak tuntaung")
                ki6.sendText(msg.to,"Walau sangko Urang")
                ki7.sendText(msg.to,"Awak datang tak tuntuang")
                ki8.sendText(msg.to,"Tapi hati isil...Liiyess")
                ki9.sendText(msg.to,"https://www.youtube.com/watch?v=ShEkg2zU0AY")
        #-------------Fungsi Spam Finish---------------------#

        #-------------Fungsi Broadcast Start------------#
            elif "Bc: " in msg.text:
              #if msg.from_ in admin:
                bctxt = msg.text.replace("Bc: ","")
                a = cl.getGroupIdsJoined()
                for taf in a:
                  cl.sendText(taf, (bctxt))
                  
            elif msg.text in ["Restart"]:
              #if msg.from_ in admin:
                cl.sendText(msg.to, "Bot has been restarted")
                restart_program()
                print "@Restart"
      #--------------Fungsi Broadcast Finish-----------#

            elif msg.text in ["Glist"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[~]%s\n" % (cl.getGroup(i).name + "[" + str(len(cl.getGroup(i).members)) + "]")
                cl.sendText(msg.to,"========[List Group]========\n"+ h +"Total Group :" +str(len(gid)))

      #--------------List Group------------
       #------------ Keluar Dari Semua Group------
            elif msg.text in ["Bot out","Op bye"]:
              #if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                gid = ki6.getGroupIdsJoined()
                gid = ki7.getGroupIdsJoined()
                gid = ki8.getGroupIdsJoined()
                gid = ki9.getGroupIdsJoined()
                gid = ki10.getGroupIdsJoined()
                for i in gid:
                  ki.leaveGroup(i)
                  ki2.leaveGroup(i)
                  ki3.leaveGroup(i)
                  ki4.leaveGroup(i)
                  ki5.leaveGroup(i)
                  ki6.leaveGroup(i)
                  ki7.leaveGroup(i)
                  ki8.leaveGroup(i)
                  ki9.leaveGroup(i)
                  ki10.leaveGroup(i)
                if wait["lang"] == "JP":
                  cl.sendText(msg.to,"Sampai jumpa Lagi Sayang")
                else:
                  cl.sendText(msg.to,"He declined all invitations")
#------------------------End---------------------

 #-----------------End-----------
            elif msg.text in ["Hi"]:
                ki.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                ki2.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                ki3.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")

#-----------------------------------------------
            elif msg.text in ["Cv say hinata pekok"]:
                ki.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                ki2.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                ki3.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say didik pekok"]:
                ki.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                ki2.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                ki3.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say bobo ah","Bobo dulu ah"]:
                ki.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                ki2.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                ki3.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say chomel pekok"]:
                ki.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                ki2.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                ki3.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Welcome"]:
                ki.sendText(msg.to,"Selamat datang di Group Kami")
                ki.sendText(msg.to,"Jangan nakal ok!")
                
            elif "Say " in msg.text:
                string = msg.text.replace("Say ","")
                if len(string.decode('utf-8')) <= 50:
                    ki.sendText(msg.to," " + string + " ")
                    ki2.sendText(msg.to," " + string + " ")
                    ki3.sendText(msg.to," " + string + " ")
                    ki4.sendText(msg.to," " + string + " ")
                    ki5.sendText(msg.to," " + string + " ")
                    ki6.sendText(msg.to," " + string + " ")
                    ki7.sendText(msg.to," " + string + " ")
                    ki8.sendText(msg.to," " + string + " ")
                    ki9.sendText(msg.to," " + string + " ")
                    ki10.sendText(msg.to," " + string + " ")
                    kibackup.sendText(msg.to," " + string + " ")
#-----------------------------------------------
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ki2.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ki3.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ki4.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ki5.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ki6.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ki7.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ki8.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ki9.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ki10.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kibackup.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------

       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Responsename","Absen"]:
              #if msg.from_ in admin:
                ki.sendText(msg.to,"Nayla")
                ki2.sendText(msg.to,"Nisa Beiby")
                ki3.sendText(msg.to,"Sisi Salsabila ")
                ki4.sendText(msg.to,"Ayuditha")
                ki5.sendText(msg.to,"Jelly Jelo")
                ki6.sendText(msg.to,"Aprilla Vigee ")
                ki7.sendText(msg.to,"Elvia Caroline ")
                ki8.sendText(msg.to,"Nheyla Putri")
                ki9.sendText(msg.to,"Putri Riri ")
                ki10.sendText(msg.to,"Yulan Erika")
                kibackup.sendText(msg.to,"Stella Winda")
                ki.sendText(msg.to,"ALL COMPLETE BOSS...!")
                
            elif msg.text in ["Respon","respon"]:
              #if msg.from_ in admin:
                   ki.sendText(msg.to,"IM STAY HERE FOR YOU")
                   ki2.sendText(msg.to,"IM STAY HERE FOR YOU")
                   ki3.sendText(msg.to,"IM STAY HERE FOR YOU")
                   ki4.sendText(msg.to,"IM STAY HERE FOR YOU")
                   ki5.sendText(msg.to,"IM STAY HERE FOR YOU")
                   ki6.sendText(msg.to,"IM STAY HERE FOR YOU")
                   ki7.sendText(msg.to,"IM STAY HERE FOR YOU")
                   ki8.sendText(msg.to,"IM STAY HERE FOR YOU")
                   ki9.sendText(msg.to,"IM STAY HERE FOR YOU")
                   ki10.sendText(msg.to,"IM STAY HERE FOR YOU")
                   kibackup.sendText(msg.to,"IM STAY HERE FOR YOU")
      #-------------Fungsi Respon Finish---------------------#
                            

      #-------------Fungsi Balesan Respon Start---------------------#
            elif msg.text in ["Aku bobo dlu ya"]:
                ki.sendText(msg.to,"Mau kemana sayang")
                ki2.sendText(msg.to,"Yahhhh kok bobo 😭")
                ki3.sendText(msg.to,"Awas kamu nakal")
                ki4.sendText(msg.to,"Kalau dia nakal kita cari OM OM Baru")
                ki5.sendText(msg.to,"Ya udh skrng kita cari gadung yuk mumpung dia tdr")
                ki6.sendText(msg.to,"Ayuk Kalian pada ikut gak ?")
                ki7.sendText(msg.to,"Ikut dong")
                ki8.sendText(msg.to,"Gmna yah")
                ki9.sendText(msg.to,"Ikut aja Nheyla Putri")
                ki10.sendText(msg.to,"Iya kamu Ikut Aja")
                kibackup.sendText(msg.to,"Yuk ah jalan Guys")
                
            elif "apakah" in msg.text.lower():
                durian = ['iya','tidak']
                jawaban = random.choice(durian)
                ki.sendText(msg.to,jawaban)
                
      #-------------Fungsi Balesan Respon Finish---------------------#

       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["Speed","Sp"]:
              #if msg.from_ in admin and owner:
                start = time.time()
                cl.sendText(msg.to, "Menghitung Kecepatan...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sDetik" % (elapsed_time))
                
            elif msg.text in ["Sp all","Speed all"]:
                if msg.from_ in admin:
                    start = time.time()
                    cl.sendText(msg.to, "Sabar BOSSKU...!!!")
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                    ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                    ki2.sendText(msg.to, "%sseconds" % (elapsed_time))
                    ki3.sendText(msg.to, "%sseconds" % (elapsed_time))
                    ki4.sendText(msg.to, "%sseconds" % (elapsed_time))
                    ki5.sendText(msg.to, "%sseconds" % (elapsed_time))
                    ki6.sendText(msg.to, "%sseconds" % (elapsed_time))
                    ki7.sendText(msg.to, "%sseconds" % (elapsed_time))
                    ki8.sendText(msg.to, "%sseconds" % (elapsed_time))
                    ki9.sendText(msg.to, "%sseconds" % (elapsed_time))
                    ki10.sendText(msg.to, "%sseconds" % (elapsed_time))
                    kibackup.sendText(msg.to, "%sseconds" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#

      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban:"]:
              #if msg.from_ in admin:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Kirim contact")
                #ki.sendText(msg.to,"Kirim contact")
                #kk.sendText(msg.to,"Kirim contact")
                #kc.sendText(msg.to,"Kirim contact")
            elif msg.text in ["Unban"]:
              #if msg.from_ in admin:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Kirim contact")
                #ki.sendText(msg.to,"Kirim contact")
                #kk.sendText(msg.to,"Kirim contact")
                #kc.sendText(msg.to,"Kirim contact")
            elif msg.text in ["Mcheck"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 Nothing in the blacklist")
                else:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 following is a blacklist")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "➡" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)

      #-------------Fungsi Banned Send Contact Finish------------------#
            elif msg.text in ["Creator"]:
              msg.contentType = 13
              msg.contentMetadata = {'mid': 'u4ccebdfdbcf265c3b6db5e8741b8767b'}
              cl.sendText(msg.to,"======================")
              cl.sendMessage(msg)
              cl.sendText(msg.to,"======================")
              cl.sendText(msg.to,"Itu Creator Kami\n•A̶҉̶҉̶҉̶N̶҉̶҉̶҉̶I̶҉̶҉̶҉̶M̶҉̶҉̶҉̶E̶҉̶҉̶҉̶ T̶҉̶҉̶҉̶E̶҉̶҉̶҉̶A̶҉̶҉̶҉̶M̶҉̶҉̶҉̶ B̶҉̶҉̶҉̶O̶҉̶҉̶҉̶T̶҉̶҉̶҉̶•")
                
      #-------------Fungsi Chat ----------------
            elif msg.text in ["Woy","woy","Woi","woi","bot","Bot"]:
                 quote = ['Istri yang baik itu Istri yang Mengizinkan Suaminya untuk Poligami 😂😂😂.','Kunci Untuk Bikin Suami Bahagia itu cuma satu..\nIzinkan Suamimu Untuk Selingkuh Coyyy ','Ah Kupret Lu','Muka Lu Kaya Jamban','Ada Orang kah disini?','Sange Euy','Ada Perawan Nganggur ga Coy?']
                 psn = random.choice(quote)
                 cl.sendText(msg.to,psn)
            
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist"]:
              #if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"No Account Expired")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "•" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)

    #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["Kill ban"]:
              #if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    
            elif msg.text in ["Clear ban"]:
              if msg.from_ in admin:
                wait["blacklist"] = {}
                with open('st2__b.json', 'w') as fp:
                 json.dump(wait, fp, sort_keys=True, indent=4)
                cl.sendText(msg.to,"Succes Clear Ban")
                
            elif msg.text in ["Clear"]:
              #if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif ("Ban @" in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned")
                   except:
                      pass
                    
            elif "Unban1 @" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        print "[Unban]ok"
                        _name = msg.text.replace("Unban @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = ki2.getGroup(msg.to)
                        gs = ki3.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Not found")
                           
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Succes")
                                except:
                                    ki.sendText(msg.to,"Success")
#-----------------------------------------------
            elif "Vk " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
                  
            elif "random: " in msg.text:
              #if msg.from_ in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("random: ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
                    
            elif "Ppc @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Ppc @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cu = cl.channel.getCover(target)          
                            path2 = str(cu)
                            cl.sendImageWithUrl(msg.to, path)
                            cl.sendImageWithUrl(msg.to, path2)
                        except Exception as e:
                                    raise e
                        
            elif msg.text in ["Tag on"]:
                 #if msg.from_ in admin:
                    if wait["tag"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already set to on")
                        else:
                            cl.sendText(msg.to,"Tag On")
                    else:
                        wait["tag"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Tag On")
                        else:
                            cl.sendText(msg.to,"already set to on")
            elif msg.text in ["Tag off"]:
              #if msg.from_ in admin:
                 if wait["tag"] == False:
                     if wait["lang"] == "JP":
                         cl.sendText(msg.to,"Already set to off")
                     else:
                         cl.sendText(msg.to,"Tag Off")
                 else:
                     wait["tag"] = False
                     if wait["lang"] == "JP":
                         cl.sendText(msg.to,"Tag Off")
                     else:
                         cl.sendText(msg.to,"Already set to off")
                         
            elif msg.text in ["Auto like:on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["Auto like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already")

#---------CCTV-----------
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
            else:
              cl.sendText
          except:
             pass
#---------------------
        #if op.type == 17:
          #if op.param2 in Bots:
            #return
          #ginfo = cl.getGroup(op.param1)
          #cl.sendText(op.param1, "Selamat Datang Di Grup  " + ">>>" + str(ginfo.name) + "<<<" + "\n" + "Founder Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName + "\n\n" + "Budayakan Baca Note !!! yah Ka 😊\nSemoga Betah Kk 😘")
          #cl.sendText(op.param1, "Founder Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
          #cl.choice(KAC).sendText(op.param1,"Budayakan Baca Note !!! yah Ka 😊\nSemoga Betah Kk 😘")
          #print "MEMBER HAS JOIN THE GROUP"
#------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.datetime.now()
    nowT = datetime.datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def autolike():
			for zx in range(0,20):
				hasil = cl.activity(limit=20)
				if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
					try:    
						cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by Anu")
						ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by Anu\n\n ☞ http://line.me/ti/p/~akunb4ru")
						ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						ki2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by Anu\n\n ☞ http://line.me/ti/p/~akunb4ru")
						ki3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						ki3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by Anu\n\n ☞ http://line.me/ti/p/~akunb4ru")
						ki4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						ki4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by Anu\n\n ☞ http://line.me/ti/p/~akunb4ru")
						ki5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						ki5.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by Anu\n\n ☞ http://line.me/ti/p/~akunb4ru")
						ki6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						ki6.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by Anu\n\n ☞ http://line.me/ti/p/~akunb4ru")
						ki7.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						ki7.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by Anu\n\n ☞ http://line.me/ti/p/~akunb4ru")
						ki8.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						ki8.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by Anu\n\n ☞ http://line.me/ti/p/~akunb4ru")
						ki9.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						ki9.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by Anu\n\n ☞ http://line.me/ti/p/~akunb4ru")
						ki10.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						ki10.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by Anu\n\n ☞ http://line.me/ti/p/~akunb4ru")
						kibackup.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						kibackup.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by Anu\n\n ☞ http://line.me/ti/p/~akunb4ru")
						
						print "DiLike"
					except:
							pass
				else:
						print "Sudah DiLike"
			time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

#thread3 = threading.Thread(target=autolike)
#thread3.daemon = True
#thread3.start()
#--------------------
def likePost():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == True:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in owner:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki7.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki8.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki9.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki10.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kibackup.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by Me\n\n ☞ http://line.me/ti/p/~akunb4ru")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Plak"
                
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.datetime.now()
                nowT = datetime.datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
