import docx,json,re
d=docx.Document('src.docx')
shots=[]
for t in d.tables:
    rows=t.rows
    if not rows or rows[0].cells[0].text.strip()!='#': continue
    cur=None
    for r in rows[1:]:
        c=[x.text.strip() for x in r.cells]
        if c[0].startswith('Prompt') or (len(set(c))==1 and 'Prompt' in c[0]):
            if cur: cur.setdefault('prompts',[]).append(c[0])
            continue
        cur=dict(id=c[0],time=c[1],src=c[2],vis=c[3],line=c[4],txt=c[5],audio=c[6])
        shots.append(cur)
json.dump(shots,open('shots.json','w'),ensure_ascii=False,indent=1)
print(len(shots))
for s in shots: print(s['id'],'|',s['time'],'|',s['src'],'|',s['line'][:70],'| P:',len(s.get('prompts',[])))
