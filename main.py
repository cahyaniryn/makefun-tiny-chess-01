import json,os
from urllib.request import Request as r,urlopen as v
url=os.getenv("MAKEFUN_ENV_URL")
assert url
def P(p,d):return json.loads(v(r(url+p,data=json.dumps(d).encode(),headers={"content-type":"application/json"})).read())
V=(0,100,320,330,500,900,0);N=(-33,-31,-18,-14,14,18,31,33);R=(-16,-1,1,16);B=(-17,-15,15,17);D=B+R
b=[0]*128;k=[0,0];c=1;e=-1;T={};n=0;lim=50000;K=[0]*32
def F(f):
 global b,c,e
 b=[0]*128;z=f.split();s=0
 for a in z[0]:
  if a=="/":s=(s|15)+1
  elif a.isdigit():s+=int(a)
  else:
   p=" pnbrqk".index(a.lower());b[s]=p if a.isupper() else -p
   if p==6:k[a>"Z"]=s
   s+=1
 c=1-2*(z[1]=="b");e=-1 if z[3]=="-" else (8-int(z[3][1]))*16+ord(z[3][0])-97
def C(s,x):
 for t in (s+15*x,s+17*x):
  if t&136==0 and b[t]==x:return 1
 for d in N:
  t=s+d
  if t&136==0 and b[t]==2*x:return 1
 for d in D:
  t=s+d;j=1
  while t&136==0 and not b[t]:t+=d;j+=1
  if t&136==0 and b[t]*x>0 and (abs(b[t])==5 or abs(b[t])==4 and d in R or abs(b[t])==3 and d in B or abs(b[t])==6 and j==1):return 1
 return 0
def Y(s,t):
 if t>>4 in (0,7):
  for q in (5,4,3,2):yield s,t,q
 else:yield s,t,0
def G(x,q=0):
 for s in range(128):
  if s&136 or b[s]*x<=0:continue
  p=abs(b[s]);r=s>>4
  if p==1:
   d=-16*x;t=s+d
   if t&136==0 and not b[t] and (not q or t>>4 in (0,7)):
    yield from Y(s,t)
    if not q and r==(6 if x==1 else 1) and not b[t+d]:yield s,t+d,0
   for d in (-17*x,-15*x):
    t=s+d
    if t&136==0 and (b[t]*x<0 and abs(b[t])!=6 or t==e):
     yield from Y(s,t)
  else:
   for d in (N if p==2 else B if p==3 else R if p==4 else D):
    t=s+d
    while t&136==0 and b[t]*x<=0 and abs(b[t])!=6:
     if not q or b[t]:yield s,t,0
     if b[t] or p in (2,6):break
     t+=d
def M(m):
 global c,e
 f,t,q=m;p=b[f];ep=abs(p)==1 and t==e and not b[t]; u=b[t] or (-c if ep else 0),e,ep
 b[f]=0;b[t]=q*c if q else p
 if ep:b[t+16*c]=0
 if abs(p)==6:
  k[p<0]=t
  if abs(t-f)==2:
   a=f+(3 if t>f else -4);j=f+(1 if t>f else -1);b[j]=b[a];b[a]=0
 e=f-16*c if abs(p)==1 and abs(t-f)==32 else -1;c=-c
 return u
def U(m,u):
 global c,e
 cap,e,ep=u;p=b[m[1]];c=-c;b[m[0]]=c if m[2] else p;b[m[1]]=0
 if ep:b[m[1]+16*c]=cap
 elif cap:b[m[1]]=cap
 if abs(p)==6:
  k[p<0]=m[0]
  if abs(m[1]-m[0])==2:
   a=m[0]+(3 if m[1]>m[0] else -4);j=m[0]+(1 if m[1]>m[0] else -1);b[a]=b[j];b[j]=0
def L(x,q=0):
 for m in G(x,q):
  u=M(m);ok=not C(k[0 if x==1 else 1],-x);U(m,u)
  if ok:yield m
def E():
 v=0
 for s in range(128):
  if s&136 or not b[s]:continue
  p=b[s];x=1 if p>0 else -1;a=abs(p);r=s>>4;f=s&7;z=14-abs(2*f-7)-abs(2*r-7);adv=7-r if x==1 else r
  v+=(V[a]+(0,5*adv+2*z,4*z,4*z,2*adv,z,-3*z)[a])*x
 return c*v
def O(ms,hm,p):
 return sorted(ms,key=lambda m:(m==hm,b[m[1]]!=0 or m[1]==e,10*V[abs(b[m[1]] or 1)]-V[abs(b[m[0]])],m[2],p<32 and m==K[p]),reverse=True)
def X():
 global n
 n+=1
 if n>lim:raise RuntimeError
def Q(a,z,p):
 X();ch=C(k[0 if c==1 else 1],-c);v=E()
 if not ch:
  if v>=z:return z
  a=max(a,v)
 ms=list(L(c,not ch))
 if not ms:return -30000+p if ch else a
 for m in O(ms,None,p):
  u=M(m);v=-Q(-z,-a,p+1);U(m,u)
  if v>=z:return z
  a=max(a,v)
 return a
def A(d,a,z,p):
 X();ch=C(k[0 if c==1 else 1],-c)
 if d<=0:return Q(a,z,p)
 key=(tuple(b),c,e);hm=T.get(key)
 ms=list(L(c))
 if not ms:return -30000+p if ch else 0
 best=-32000;bm=None
 for m in O(ms,hm,p):
  u=M(m);v=-A(d-1,-z,-a,p+1);U(m,u)
  if v>best:best=v;bm=m
  a=max(a,v)
  if a>=z:
   if not b[m[1]] and not m[2] and p<32:K[p]=m
   break
 T[key]=bm
 return best
def I(m):
 f,t,q=m
 return "%c%c%c%c%s"%(97+(f&7),56-(f>>4),97+(t&7),56-(t>>4)," pnbrqk"[q] if q else "")
def Z(f,raw):
 global n
 F(f);T.clear();ms=[((8-int(a[1]))*16+ord(a[0])-97,(8-int(a[3]))*16+ord(a[2])-97," pnbrqk".find(a[4]) if len(a)>4 else 0) for a in raw]
 best=ms[0];n=0
 for d in range(1,32):
  cur=best
  try:
   a=-32000
   for m in O(ms,None,0):
    u=M(m);v=-A(d-1,-32000,-a,1);U(m,u)
    if v>a:a=v;cur=m
   best=cur
  except RuntimeError:break
 return I(best)
while 1:
 g=P("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":g=P("/move",{"game":g["game"],"move":Z(g["fen"],g["legal_moves"])})
