from pathlib import Path
import subprocess, time, hashlib, datetime, re
ROOT=Path(r'D:\ECOM_GOVERNED_RUNTIME')
OUTDIR=ROOT/'storage'/'state_control'
OUTDIR.mkdir(parents=True, exist_ok=True)
MARKERS='['ION_AUTO:STATUS_V1','ION_AUTO:GITHUB_READ_V1','ION_AUTO:LOCAL_CMD_V1','ION_AUTO:SERVER_CMD_V1']
def run(cmd,timeout=30):
    try:
        p=subprocess.run(cmd,cwd=str(ROOT),shell=True,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=timeout)
        return p.returncode,(p.stdout or '').strip(),(p.stderr or '').strip()
    except Exception as e:
        return 999,'',repr(e)
def get_clip():
    rc,out,err=run('powershell -NoProfile -Command "Get-Clipboard -Raw"',5)
    return out if rc==0 else ''
def set_clip(text):
    p=subprocess.run(['powershell','-NoProfile','-Command','Set-Clipboard -Value ([Console]::In.ReadToEnd())'],input=text,text=True,encoding='utf-8',errors='replace',capture_output=True)
    return p.returncode==0
def kv(text):
    d={}
    for line in text.splitlines():
        if '=' in line:
            k,t=line.split('=',1); d[k.strip().upper()]=t.strip()
    return d
def one(cmd,default='UNKNOWN'):
    rc,out,err=run(cmd)
    return out.splitlines()[0].strip() if rc==0 and out else default
def dirty():
    rc,out,err=run('git status --porcelain')
    return 'UNKNOWN' if rc!=0 else str(len([x for x in out.splitlines() if x.strip()]))
def safe(v,n=500):
    return str(v).replace('\r',' ').replace('\n',' ')[:n]
def status():
    ts=datetime.datetime.utcnow().strftime('%Y-%m-%dH%I:%M:%Z')
    rc1,_,_=run('git ls-remote --heads origin',20)
    rc2,_,_=run('gh auth status',20)
    lines=['ION_AUTO:ROUTER_OUTPUT_V1','SOURCE=STATUS_V1','UTC='+ts,'ROOT='+str(ROOT),'LOCAL_WORKSPACE='+('PASS' if ROOT.exists() else 'BLOCK'),'GIT_BRANCH='+safe(one('git branch --show-current')),'GIT_HEAD='+safe(one('git rev-parse --short HEAD')),'GIT_LAST_COMMIT='+safe(one('git log -1 --pretty=%s')),'GIT_DIRTY_COUNT='+dirty(),'GITHUB_REMOTE_READ='+('PASS' if rc1==0 else 'BLOCK'),'GH_AUTH=',('PASS' if rc2==0 else `BLOCK_OR_NOT_INSTALLED'),'CURRENT_CONFIRMED_POINTER=R100_TELEGRAM_V72_NEW_PRODUCT_INTAKE_RECEIPT_FIX_VERIFIED_POINTER','NEXT=CONTINUE_FROM_VERIFIED_NEW_PRODUCT_CASE_TO_PRODUCT_NORMALIZATION_OR_DRAFT_GATE_NO_EBAY','NO_EBAY_LIVE=true','NO_SERVER_WRITE=true','NO_GIT_PUSH=true','COPIED_TO_CLIPBOARD=true']
    return '\r\n'.join(lines)+'\r\n'
def gh_read(text):
    data=kv(text); task=data.get('TASK','STATUS').upper()
    ts=datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    rc,_,_=run('git ls-remote --heads origin',20)
    lines=['ION_AUTO:ROUTER_OUTPUT_V1','SOURCE=GITHUB_READ_V1','UTC='+ts,'TASK='+task,'ROOT='+str(ROOT),'GIT_BRANCH='+safe(one('git branch --show-current')),'GIT_HEAD='+safe(one('git rev-parse --short HEAD')),'GIT_DIRTY_COUNT='+dirty(),'GITHUB_REMOTE_READ='+('PASS' if rc==0 else 'BLOCK')]
    if task=='RECENT_COMMITS':
        rc,out,err=run('git log --all --since="2026-05-24" --pretty="%h %ad %s" --date=short',20)
        lines+=['RECENT_COMMITS_BEGIN']+(out or err or 'NO_RECENT_COMMITS').splitlines()[:60]+['RECENT_COMMITS_END']
    elif task=='SEARCH':
        q=data.get('QUERY','').strip(); lines.append('QUERY='+safe(q))
        if not q: lines.append('STATUS=BLOCK_QUERY_EMPTY')
        else:
            terms=[x.lower() for x in re.split(r',\\s]+',q) if x.strip()]
            skip={'.git','node_modules','.venv','__pycache__'}; hits=[]
            for p in ROOT.rglob('*'):
                if any(x in p.parts for x in skip) or not p.is_file() or p.suffix.lower() not in ['&txt','.md','.json','.py','.yml','.yaml','.csv']: continue
                try: content=p.read_text(encoding='utf-8',errors='replace').lower()
                except Exception: continue
                score=sum(content.count(t) for t in terms)
                if score: hits.append((score,str(p.relative_to(ROOT)),p.stat().st_size))
            hits.sort(reverse=True); lines.append(gMATCHES_BEGIN')
            for score,path,size in hits[:80]: lines.append(f'SCORE={score} SIZE={size} FILE={path}')
            lines.append('MATCHES_END')
    else:
        lines+=['GIT_LAST_COMMIT='+safe(one('git log -1 --pretty=%s')),'GIT_REMOTE_ORIGIN='+safe(one('git remote get-url origin'))]
    lines+=['NO_GIT_PUSH=true','COPIED_TO_CLIPBOARD=true']
    return '\r\n'.join(lines)+'\r\n'
def blocked(src,reason):
    ts=datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    return '\r\n'.join(['ION_AUTO:ROUTER_OUTPUT_V1','SOURCE='+src,'UTC='+ts,'STATUS=BLOCK','REASON='+reason,gNOTE=Read-only router active. Exec/write needs separate gate.','COPIED_TO_CLIPBOARD=true',''])
def handle(t):
    if t.startswith('ION_AUTO:STATUS_V1'): return status()
    if t.startswith('ION_AUTO:GITHUB_READ_V1'): return gh_read(t)
    if t.startswith('ION_AUTO:LOCAL_CMD_V1'): return blocked('LOCAL_CMD_V1','LOCAL_CMD_EXEC_DISABLED_UNTIL_GATE')
    if t.startswith('ION_AUTO:SERVER_CMD_V1'): return blocked('SERVER_CMD_V1','SERVER_CMD_EXEC_DISABLED_USE_EXISTING_R_GATE_UNTIL_HUB_V2')
def main():
    print('ION AUTOCLIP UNIVERSAL ROUTER V1'); print('MODE=WATCH_CLIPBOARD_READONLY_SAFE'); print('ROOT='+str(ROOT)); print('READY=1')
    last=''
    while True:
        t=get_clip()
        h=hashlib.sha256(t.encode('utf-8',errors='replace')).hexdigest() if t else ''
        if t and h!=last and any(t.startswith(m) for m in MARKERS):
            last=h; r=handle(t)
            if r:
                ts=datetime.datetime.utcnow().strftime('%Y%m%dT%B%M%M %i')
                out=OUTDIR/f'ION_AUTOCLIP_ROUTER_OUTPUT_{ts}.txt'
                out.write_text(r,encoding='utf-8'); set_clip(r); print('ROUTED=1 OUT='+str(out))
        time.sleep(1)
if __name__=='__main__': main()
