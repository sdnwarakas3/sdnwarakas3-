import base64, hashlib, json, os, socket, struct, threading, time
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

ROOT=os.path.dirname(os.path.abspath(__file__))
PORT=int(os.environ.get('PORT','8080'))
DATA_FILE=os.path.join(ROOT,'server-data.json')
SCHOOL='SDN-WARAKAS-3'
lock=threading.RLock(); clients=set()
try:
    with open(DATA_FILE,'r',encoding='utf-8') as f: state=json.load(f)
except Exception: state={'schools':{}}
state.setdefault('schools',{})

def save():
    tmp=DATA_FILE+'.tmp'
    with open(tmp,'w',encoding='utf-8') as f: json.dump(state,f,ensure_ascii=False,indent=2)
    os.replace(tmp,DATA_FILE)

def db():
    with lock:
        if SCHOOL not in state['schools']:
            state['schools'][SCHOOL]={'classes':{},'schoolSetting':{'nama':'SD NEGERI WARAKAS 3','tahun':'2026/2027'},'changedAt':0}
        return state['schools'][SCHOOL]

def frame(payload):
    b=payload.encode('utf-8'); n=len(b)
    if n<126: head=bytes([0x81,n])
    elif n<65536: head=bytes([0x81,126])+struct.pack('!H',n)
    else: head=bytes([0x81,127])+struct.pack('!Q',n)
    return head+b

def send(c,obj):
    try: c.sendall(frame(json.dumps(obj,separators=(',',':'),ensure_ascii=False)))
    except Exception: pass

def broadcast(obj,except_c=None):
    for c in list(clients):
        if c is not except_c: send(c,obj)

def recv_frame(c):
    h=c.recv(2)
    if len(h)<2: return None
    b1,b2=h; opcode=b1&15; masked=b2&128; n=b2&127
    if n==126: n=struct.unpack('!H',c.recv(2))[0]
    elif n==127: n=struct.unpack('!Q',c.recv(8))[0]
    mask=c.recv(4) if masked else b''
    data=b''
    while len(data)<n:
        x=c.recv(n-len(data))
        if not x: return None
        data+=x
    if masked: data=bytes(v^mask[i%4] for i,v in enumerate(data))
    if opcode==8: return None
    if opcode==9:
        # pong
        try: c.sendall(bytes([0x8A,len(data)])+data)
        except Exception: pass
        return ''
    if opcode in (1,2): return data.decode('utf-8','replace')
    return ''

def ws_handshake(c,headers):
    key=headers.get('sec-websocket-key','')
    if not key: return False
    accept=base64.b64encode(hashlib.sha1((key+'258EAFA5-E914-47DA-95CA-C5AB0DC85B11').encode()).digest()).decode()
    c.sendall(('HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Accept: '+accept+'\r\n\r\n').encode())
    return True

def ws_client(c):
    try:
        f=c.makefile('rb')
        req=f.readline().decode('latin1','ignore')
        headers={}
        while True:
            line=f.readline()
            if not line or line in (b'\r\n',b'\n'): break
            if b':' in line:
                k,v=line.decode('latin1').split(':',1); headers[k.strip().lower()]=v.strip()
        if 'websocket' not in headers.get('upgrade','').lower() or not ws_handshake(c,headers):
            c.close(); return
        clients.add(c)
        while True:
            raw=recv_frame(c)
            if raw is None: break
            if not raw: continue
            try: m=json.loads(raw)
            except Exception: continue
            if m.get('school')!=SCHOOL: continue
            t=m.get('type'); d=db()
            if t=='join':
                with lock:
                    if d['classes']:
                        send(c,{'type':'sync','classes':d['classes'],'schoolSetting':d['schoolSetting'],'accepted':True,'changedAt':d.get('changedAt',0)})
                    elif isinstance(m.get('classes'),dict):
                        d['classes']=m['classes']; d['schoolSetting']=m.get('schoolSetting') or d['schoolSetting']; d['changedAt']=int(m.get('changedAt') or time.time()*1000); save()
                        send(c,{'type':'sync','classes':d['classes'],'schoolSetting':d['schoolSetting'],'accepted':True,'changedAt':d['changedAt']})
            elif t=='update' and isinstance(m.get('classes'),dict):
                with lock:
                    incoming=int(m.get('changedAt') or time.time()*1000)
                    d['classes']=m['classes']; d['schoolSetting']=m.get('schoolSetting') or d['schoolSetting']; d['changedAt']=max(d.get('changedAt',0),incoming,int(time.time()*1000)); save()
                    payload={'type':'sync','classes':d['classes'],'schoolSetting':d['schoolSetting'],'accepted':True,'changedAt':d['changedAt']}
                broadcast(payload,c); send(c,payload)
    except Exception: pass
    finally:
        clients.discard(c)
        try: c.close()
        except: pass

class Handler(SimpleHTTPRequestHandler):
    def __init__(self,*a,**kw): super().__init__(*a,directory=ROOT,**kw)
    def do_GET(self):
        if self.path.split('?')[0]=='/health':
            body=json.dumps({'ok':True,'school':SCHOOL,'time':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}).encode()
            self.send_response(200); self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(body))); self.end_headers(); self.wfile.write(body); return
        if self.headers.get('Upgrade','').lower()=='websocket':
            c=self.connection; ws_client(c); return
        if self.path.split('?')[0]=='/': self.path='/APLIKASI_ADMINISTRASI_GURU_SDN_WARAKAS_3.html'
        self.send_response(200); super().end_headers()
    def log_message(self,*args): pass

print('SDN WARAKAS 3 - SERVER AKTIF')
print('Buka di komputer ini: http://localhost:%d/'%PORT)
print('Perangkat lain: http://IP-KOMPUTER-SERVER:%d/'%PORT)
ThreadingHTTPServer(('0.0.0.0',PORT),Handler).serve_forever()
