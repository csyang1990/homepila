from flask import Flask, request, render_template, session, redirect, url_for, flash  #abort
from apscheduler.schedulers.background import BackgroundScheduler
import pandas as pd
import numpy as np
from datetime import datetime , timedelta
import time, os
import sqlite3
import json
import logging
from logging.handlers import TimedRotatingFileHandler
import sys,linecache,select
from dateutil.relativedelta import relativedelta
from calendar import monthrange
# pd.set_option('display.max_rows', 5)
# pd.set_option('display.max_columns', 99)

app = Flask(__name__)
app.secret_key = "super secret key"


def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print('YANG_EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

mylogger = logging.getLogger("[YANG]")
# mylogger.setLevel(logging.INFO)
mylogger.setLevel(logging.DEBUG)

# myhandler = TimedRotatingFileHandler(path, when="s", interval=10, encoding="utf-8", backupCount=5)
myhandler = TimedRotatingFileHandler("myloggingfile.log", when="D", interval=30, encoding="utf-8", backupCount=99)
formatter = logging.Formatter('%(name)s [ %(levelname)s ] %(lineno)d - %(asctime)s - %(message)s')
myhandler.setFormatter(formatter)
mylogger.addHandler(myhandler)
stream_hander = logging.StreamHandler()
stream_hander.setFormatter(formatter)
mylogger.addHandler(stream_hander)




# yfile = r'E:\근무표\필라테스2.xlsx'
# dfcust = pd.read_excel(yfile, sheet_name='고객정보')
# dfpeop = pd.read_excel(yfile, sheet_name='직원정보')
# dfregi = pd.read_excel(yfile, sheet_name='등록정보')
# dfpres = pd.read_excel(yfile, sheet_name='예약정보')
# dfwork = pd.read_excel(yfile, sheet_name='사용정보')
# dfgood = pd.read_excel(yfile, sheet_name='상품정보')
# dfmore = pd.read_excel(yfile, sheet_name='수당정보')
# dfschA = pd.read_excel(yfile, sheet_name='근무표A')
# dfschB = pd.read_excel(yfile, sheet_name='근무표B')
# dfschC = pd.read_excel(yfile, sheet_name='근무표C')

ysdtnew = ''
yjscust = yjspeop = yjsregi = yjswork = yjspres = yjsgood = yjsmore = yjsschA = yjsschB = yjsschC = yjspay = ''
ydfworkgrpmrg = ydfregi = ydfwork = ydfpeop = ydfmore = ydfpay = ydfwork3piv = pd.DataFrame()
def yfqrydb():
    global ysdtnew
    global yjscust, yjspeop, yjsregi, yjswork, yjspres, yjsgood, yjsmore, yjsschA, yjsschB, yjsschC, yjspay
    global ydfworkgrpmrg, ydfregi, ydfwork, ydfpeop, ydfmore, ydfpay, ydfwork3piv


    # ydbfile = r'E:\yangdbpila\ydfpila.db'
    # ysdtnew = time.strftime('%m-%d %H:%M:%S', time.localtime(os.path.getmtime(ydbfile)))
    # print('Netdt, Olddt : ', ysdtnew, ysdtnew)


    # time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getmtime(ydbfile)))
    yconnpila = sqlite3.connect(ydbfile)
    # dfcust.to_sql('tbcust', yconnpila, if_exists='replace', index=False)
    # dfpeop.to_sql('tbpeop', yconnpila, if_exists='replace', index=False)
    # dfregi.to_sql('tbregi', yconnpila, if_exists='replace', index=False)
    # dfwork.to_sql('tbwork', yconnpila, if_exists='replace', index=False)
    # dfpres.to_sql('tbpres', yconnpila, if_exists='replace', index=False)

    # dfgood.to_sql('tbgood', yconnpila, if_exists='replace', index=False)
    # dfmore.to_sql('tbmore', yconnpila, if_exists='replace', index=False)

    # dfschA.to_sql('tbschA', yconnpila, if_exists='replace', index=False)
    # dfschB.to_sql('tbschB', yconnpila, if_exists='replace', index=False)
    # dfschC.to_sql('tbschC', yconnpila, if_exists='replace', index=False)
    # yconnpila.commit()
    ydfcust = pd.read_sql('select * from tbcust order by 시작날짜 desc', yconnpila)
    ydfpeop = pd.read_sql('select * from tbpeop', yconnpila)
    ydfregi = pd.read_sql('select * from tbregi order by 등록일자 desc', yconnpila)
    ydfwork = pd.read_sql('select * from tbwork order by 사용일자 desc', yconnpila)
    ydfpres = pd.read_sql('select * from tbpres order by 예약일자 desc', yconnpila)
    ydfgood = pd.read_sql('select * from tbgood', yconnpila)
    ydfmore = pd.read_sql('select * from tbmore', yconnpila)
    ydfschA = pd.read_sql('select * from tbschA', yconnpila)
    ydfschB = pd.read_sql('select * from tbschB', yconnpila)
    ydfschC = pd.read_sql('select * from tbschC', yconnpila)
    # ydfpay = pd.read_sql('select * from tbpay', yconnpila)
    yconnpila.close()

    ydfpres['예약일자'] = ydfpres['예약일자'].str[:10]
    ydfpres['시간'] = ydfpres['시간'].str[:5]
    ydfcust['시작날짜'] = ydfcust['시작날짜'].str[:10]
    ydfpeop['등록일자'] = ydfpeop['등록일자'].str[:10]
    ydfregi['등록일자'] = ydfregi['등록일자'].str[:10]
    ydfwork['사용일자'] = ydfwork['사용일자'].str[:10]
    ydfwork['시작시간'] = ydfwork['시작시간'].str[11:16]
    ydfschA['날짜'] = ydfschA['날짜'].str[:10]
    ydfschB['날짜'] = ydfschB['날짜'].str[:10]
    ydfschC['날짜'] = ydfschC['날짜'].str[:10]

    ysdtnew = time.strftime('%m-%d %H:%M:%S', time.localtime(os.path.getmtime(ydbfile)))
    # print('Netdt, Olddt : ', ysdtnew, ysdtnew)
    print(ysdtnew, ydfcust.shape, ydfpeop.shape, ydfregi.shape, ydfwork.shape, ydfpres.shape, ydfgood.shape, ydfmore.shape, ydfschA.shape, ydfschB.shape, ydfschC.shape, ydfpay.shape)

    # 고객정보에 등록정보 사용정보 더하고 남은횟수 계산
    ydfregigrp = ydfregi.groupby(['고객이름'])['등록비'].agg(['sum', 'count'])
    ydfregigrp.columns = ['등록비총합', '등록횟수']
    ydfregigrpmrg = ydfcust.merge(ydfregigrp, on=['고객이름'], how='left')
    ydfregigrp2 = ydfregi.groupby(['고객이름'])['상품횟수'].agg(['sum'])
    ydfregigrp2.columns = ['상품총횟수']
    ydfregigrpmrg2 = ydfregigrpmrg.merge(ydfregigrp2, on=['고객이름'], how='left')
    ydfworkgrp = ydfwork.groupby(['고객이름'])['사용시간'].agg(['sum', 'count'])
    ydfworkgrp.columns = ['사용총시간', '사용횟수']
    ydfworkgrpmrg = ydfregigrpmrg2.merge(ydfworkgrp, on=['고객이름'], how='left')
    ydfworkgrpmrg['남은횟수'] = ydfworkgrpmrg['상품총횟수'] - ydfworkgrpmrg['사용총시간']

    # PAY 구하기
    # 사용관리 + 직원관리  on=['직원이름', '직급']  ====> 직원관리에서 이전 직급 관리 안됨
    # ====> 사용관리에서 직급을 수동으로 제대로 관리하기 = 사용관리만으로 직원별/직급별 급여 확인 가능
    ydfwork2 = ydfwork.copy()
    ydfwork2['상품종류2'] = ydfwork2['상품종류'].str[:2]
    ydfwork2['상품종류2'] = ydfwork2['상품종류2'].str.replace('개인|비기|기본', '일반', regex=True)
    ydfwork2['상품종류2'] = ydfwork2['상품종류2'] + ydfwork2['내외']
    ydfwork2['사용월'] = ydfwork2['사용일자'].str[:7]
    ydfwork2piv = ydfwork2.pivot_table(values='사용시간', index=['직원이름', '사용월', '직급'], columns='상품종류2', aggfunc='sum').reset_index()
    ydfwork2piv['총일한시간'] = ydfwork2piv.sum(axis=1)
    ydfwork2piv['120초과'] = np.where(ydfwork2piv['총일한시간'] > 120, ydfwork2piv['총일한시간'] - 120, 0)
    ydfwork2piv['100초과'] = np.where((ydfwork2piv['총일한시간'] > 100) & (ydfwork2piv['총일한시간'] <= 120), ydfwork2piv['총일한시간'] - 100, 0)
    # Merge하기 - 센터
    # ydfpeoppiv = ydfpeop[['직원이름', '센터', '직급']].merge(ydfwork2piv, on=['직원이름', '직급'], how='left')
    ydfpeoppiv = ydfwork2piv.merge(ydfpeop[['직원이름', '센터']], on=['직원이름'], how='left')
    # Merge하기 - 수당정보
    ydfpeoppivmrg = ydfpeoppiv.merge(ydfmore, on=['센터', '직급'], how='left').fillna(0)
    # 이번날짜 반영
    # ynow = datetime.now()
    # ythismonthdays = monthrange(ynow.year, ynow.month)
    ydfpeoppivmrg['월급여'] = ydfpeoppivmrg['기본급'] \
                           + ydfpeoppivmrg['일반내'] * ydfpeoppivmrg['내일반'] + ydfpeoppivmrg['일반외'] * ydfpeoppivmrg['외일반'] \
                           + ydfpeoppivmrg['듀엣내'] * ydfpeoppivmrg['내듀엣'] + ydfpeoppivmrg['듀엣외'] * ydfpeoppivmrg['외듀엣'] \
                           + ydfpeoppivmrg['그룹내'] * ydfpeoppivmrg['내그룹'] + ydfpeoppivmrg['그룹외'] * ydfpeoppivmrg['외그룹'] \
                           + ydfpeoppivmrg['100초과'] * ydfpeoppivmrg['초과100'] + ydfpeoppivmrg['120초과'] * ydfpeoppivmrg['초과120']
    ydfpay = ydfpeoppivmrg.sort_values(['사용월','센터','직원이름'], ascending=[False, True, True]).copy()

    # PAY관련 고객별,상품별,월별 일한시간 계산
    ydfwork3piv = ydfwork2.pivot_table(values='사용시간', index=['직원이름', '고객이름', '사용월'], columns='상품종류2', aggfunc='sum').reset_index()
    ydfwork3piv['총일한시간'] = ydfwork3piv.sum(axis=1)

    # 근무표
    ydstart = '2019-01-01'
    yiperiods = 31
    # ylpeopa = ydfpeop[ydfpeop['센터']=='센터A']['직원이름'].tolist()
    ylpeop = ydfpeop[['직원이름', '센터']]  # .tolist()
    ydtrng = pd.date_range(start=ydstart, periods=yiperiods, freq='D')
    ydfsch = pd.DataFrame('일', index=ylpeop, columns=ydtrng)



    # BTN 생성
    ydfworkgrpmrg['BUTTON'] = np.nan
    ydfpeop['BUTTON'] = np.nan
    ydfregi['BUTTON'] = np.nan
    ydfwork['BUTTON'] = np.nan
    ydfpres['BUTTON'] = np.nan

    # 출력물 구하기
    yslastmonth = (datetime.now() - relativedelta(months=1)).strftime('%Y-%m')
    yjscust = ydfworkgrpmrg.to_json(orient='split')
    yjspeop = ydfpeop.to_json(orient='split')
    yjsregi = ydfregi[ydfregi['등록일자'] >= yslastmonth].to_json(orient='split')
    yjswork = ydfwork[ydfwork['사용일자'] >= yslastmonth].to_json(orient='split')
    yjspres = ydfpres.to_json(orient='split')
    yjsgood = ydfgood.to_json(orient='split')
    yjsmore = ydfmore.to_json(orient='split')
    yjsschA = ydfschA.to_json(orient='split')
    yjsschB = ydfschB.to_json(orient='split')
    yjsschC = ydfschC.to_json(orient='split')
    yjspay = ydfpay.to_json(orient='split')

    

# yjspeoppivmrg = ''
def yfgetpay(ymonth):
    # global yjspeoppivmrg

    # 사용정보에 급여정보 계산하기
    ydfworkt = ydfwork[ydfwork['사용일자'].str.contains(ymonth)]
    ydfwork2 = ydfworkt.copy()
    ydfwork2['상품종류2'] = ydfwork2['상품종류'].str[:2]
    ydfwork2['상품종류2'] = ydfwork2['상품종류2'].str.replace('개인|비기|기본', '일반', regex=True)
    ydfwork2['상품종류2'] = ydfwork2['상품종류2'] + ydfwork2['내외']
    ydfwork2piv = ydfwork2.pivot_table(values='사용시간', index='직원이름', columns='상품종류2', aggfunc='sum')
    ydfpeoppiv = ydfpeop[['직원이름', '센터', '직급']].merge(ydfwork2piv, on=['직원이름'], how='left')
    ydfpeoppiv['총일한시간'] = ydfpeoppiv.sum(axis=1)
    ydfpeoppiv['120초과'] = np.where(ydfpeoppiv['총일한시간'] > 120, ydfpeoppiv['총일한시간'] - 120, 0)
    ydfpeoppiv['100초과'] = np.where((ydfpeoppiv['총일한시간'] > 100) & (ydfpeoppiv['총일한시간'] <= 120), ydfpeoppiv['총일한시간'] - 100, 0)

    ydfpeoppivmrg = ydfpeoppiv.merge(ydfmore, on=['센터', '직급'], how='left').fillna(0)
    ydfpeoppivmrg['월급여'] = ydfpeoppivmrg['기본급'] \
                           + ydfpeoppivmrg['일반내'] * ydfpeoppivmrg['내일반'] + ydfpeoppivmrg['일반외'] * ydfpeoppivmrg['외일반'] \
                           + ydfpeoppivmrg['듀엣내'] * ydfpeoppivmrg['내듀엣'] + ydfpeoppivmrg['듀엣외'] * ydfpeoppivmrg['외듀엣'] \
                           + ydfpeoppivmrg['그룹내'] * ydfpeoppivmrg['내그룹'] + ydfpeoppivmrg['그룹외'] * ydfpeoppivmrg['외그룹'] \
                           + ydfpeoppivmrg['100초과'] * ydfpeoppivmrg['초과100'] + ydfpeoppivmrg['120초과'] * ydfpeoppivmrg['초과120']
    ydfpeoppivmrg['년월'] = ymonth

    # yjspeoppivmrg = ydfpeoppivmrg.to_json(orient='split')

    yconnpila = sqlite3.connect(ydbfile)
    ydfpeoppivmrg.to_sql('tbpay', yconnpila, if_exists='append', index=False)
    yconnpila.commit()
    yconnpila.close()
    print('yfgetpay', ymonth, ydfwork2.shape, ydfpeoppivmrg.shape)


@app.route('/')
@app.route('/LOGIN')
def LOGIN():
    session.clear()

    sid = request.args.get('username', type=str)
    spass = request.args.get('password', type=str)
    print(sid, spass)

    session['YID'] = sid
    mylogger.debug("Login Try {0} {1}".format(request.remote_addr, sid))
    if sid in yladmin:
        return redirect(url_for('admin'))
    elif sid in ylsusera:
        return redirect(url_for('suser'))
    else:
        flash('유저네임이나 암호가 맞지 않습니다.')
        return render_template('main_login.html')

@app.route('/logout')
def logout():
    session.clear()
    #return redirect(url_for('index'))
    return LOGIN()


@app.route('/suser')
def suser():
    ysesskey = session['YID']
    print('Session Key YID Value : ', ysesskey)
    mylogger.debug("Login OK Suser {0} {1}".format(request.remote_addr, ysesskey))

    if ysesskey in ylsusera:
        return render_template('main_pila.html')
    else:
        flash('세션이(Suser) 만료되었습니다.')
        return render_template('main_login.html')

@app.route('/admin')
def admin():
    ysesskey = session['YID']
    print('Session Key YID Value : ', ysesskey)
    mylogger.debug("Login OK Admin {0} {1}".format(request.remote_addr, ysesskey))
    if ysesskey in yladmin:
        return render_template('main_pila_admin.html')
    else:
        flash('세션이(Admin) 만료되었습니다.')
        return render_template('main_login.html')


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)




@app.route('/AServer')
def AServer():
    return  json.dumps([ysdtnew, datetime.now().strftime('%m-%d %H:%M:%S')])

@app.route('/ACUST')
def ACUST():
    return yjscust
@app.route('/AMAN12')
def AMAN12():
    s0 = request.args.get('ys0', type=str)
    print('AMAN12 : ', request.remote_addr, s0)
    ydfworkgrpmrg2 = ydfworkgrpmrg[ydfworkgrpmrg['고객이름'] == s0].drop(columns=['BUTTON', 'ID'])
    return ydfworkgrpmrg2.to_json(orient='split')
@app.route('/AMAN121')
def AMAN121():
    s0 = request.args.get('ys0', type=str)
    print('AMAN121 : ', request.remote_addr, s0)
    ydfregi2 = ydfregi[ydfregi['고객이름'] == s0].drop(columns=['BUTTON', '고객이름', 'ID'])
    return ydfregi2.sort_values(['등록일자'], ascending=[False]).to_json(orient='split')
@app.route('/AMAN122')
def AMAN122():
    s0 = request.args.get('ys0', type=str)
    ydfwork2 = ydfwork[ydfwork['고객이름'] == s0].drop(columns=['BUTTON', '고객이름', 'ID'])
    return ydfwork2.sort_values(['사용일자'], ascending=[False]).to_json(orient='split')

@app.route('/APEOP')
def APEOP():
    return yjspeop
@app.route('/AREGI')
def AREGI():
    return yjsregi
@app.route('/AWORK')
def AWORK():
    return yjswork
@app.route('/APRES')
def APRES():
    return yjspres

@app.route('/AGOOD')
def AGOOD():
    return yjsgood
@app.route('/AMORE')
def AMORE():
    return yjsmore

@app.route('/ASCHA')
def ASCHA():
    return yjsschA
@app.route('/ASCHB')
def ASCHB():
    return yjsschB
@app.route('/ASCHC')
def ASCHC():
    return yjsschC
@app.route('/APAY')
def APAY():
    return yjspay
@app.route('/AMAN72')
def AMAN72():
    s0 = request.args.get('ys0', type=str)
    s1 = request.args.get('ys1', type=str)
    print('AMAN72 : ', request.remote_addr, s0, s1)
    ydfpay2 = ydfpay[(ydfpay['직원이름'] == s0) & (ydfpay['사용월'].str.contains(s1, regex=True, na=False))].drop(columns=['직원이름'])
    return ydfpay2.to_json(orient='split')
@app.route('/AMAN721')
def AMAN721():
    s0 = request.args.get('ys0', type=str)
    s1 = request.args.get('ys1', type=str)
    ydfwork3piv2 = ydfwork3piv[(ydfwork3piv['직원이름'] == s0) & (ydfwork3piv['사용월'].str.contains(s1, regex=True, na=False))].drop(columns=['직원이름'])
    # ydfregi2 = ydfwork3piv[ydfwork3piv['직원이름'] == s0].drop(columns=['BUTTON', '직원이름', 'ID'])
    return ydfwork3piv2.sort_values(['사용월'], ascending=[False]).to_json(orient='split')
@app.route('/AMAN722')
def AMAN722():
    s0 = request.args.get('ys0', type=str)
    s1 = request.args.get('ys1', type=str)
    ydfwork2 = ydfwork[(ydfwork['직원이름'] == s0) & (ydfwork['사용일자'].str.contains(s1, regex=True, na=False))].drop(columns=['BUTTON', '직원이름', 'ID'])
    return ydfwork2.sort_values(['사용일자'], ascending=[False]).to_json(orient='split')



@app.route('/READLOG')
def READLOG():
    s0 = request.args.get('ys0', type=str)
    print('APRESMODAL : ', request.remote_addr, s0)
    yflog = r"E:\yangproject\homepila\myloggingfile.log"
    ydflog = pd.read_table(yflog, names=['logs'])
    ydflog2 = ydflog[ydflog['logs'].str.contains(s0, regex=True, na=False)]
    return ydflog2.sort_values(['logs'], ascending=[False]).to_json(orient='split')[:500]

@app.route('/APRESMODAL')
def APRESMODAL():
    s0 = request.args.get('ys0', type=str) # Modify or Create

    sid = request.args.get('ys1', type=str)
    sidcrt = datetime.now().strftime('%Y%m%dT%H%M%S')
    s2 = request.args.get('ys2', type=str)
    s3 = request.args.get('ys3', type=str)
    s4 = request.args.get('ys4', type=str)
    s5 = request.args.get('ys5', type=str)
    s6 = request.args.get('ys6', type=str)
    s7 = request.args.get('ys7', type=str)
    s8 = request.args.get('ys8', type=str)
    s9 = request.args.get('ys9', type=str)

    ysip = request.remote_addr
    ydatascrt = (sidcrt, s2, s3, s4, s5, s6, s7, s8, s9)
    ydatasmod = (s2, s3, s4, s5, s6, s7, s8, s9, sid)
    print('APRESMODAL : ', ysip, sidcrt, ydatasmod)

    yconnpres = sqlite3.connect(ydbfile)
    cur = yconnpres.cursor()
    try:
        if s0 == 'Create':
            cur.execute("insert into tbpres values (?,?,?,?,?   ,?,?,?,?)", ydatascrt)
            mylogger.info("예약관리 생성 {0} {1} {2}".format(ysip, "ID", ','.join(ydatascrt)))
        else:
            cur.execute('update tbpres set 예약일자=?, 요일=?, 시간=?, 고객이름=?, 인원수=?, 직원이름=?, 예약시간=?, 예약메모=? where ID = ?', ydatasmod)
            mylogger.info("예약관리 수정 {0} {1} {2}".format(ysip, "ID", ','.join(ydatasmod)))
        yconnpres.commit()
    except:
        print('ERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORError:  예약관리')
        mylogger.error('ERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORError:  예약관리')
        PrintException()
    finally:
        yconnpres.close()

    # 새로 입력된 DB에서 Query
    yfqrydb()
    return yjspres









if __name__ == '__main__':
    ydbfile = r'E:\yangproject\homepila\yangdbpila\ydfpila.db'
    yladmin = ['yang', 'admin']
    ylsusera = ['susera', 'suser']
    ylsuserb = ['suserb']
    ylsuserc = ['suserc']


    yfqrydb()

    ysched = BackgroundScheduler()
    ysched.add_job(yfqrydb, 'cron', minute='*/10')
    ysched.add_job(yfgetpay, 'cron', day='1', args=[datetime.now().strftime('%Y-%m')])
    ysched.start()


    # app.run()
    app.run(host='0.0.0.0', port=5000)
