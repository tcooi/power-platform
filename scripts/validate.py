import json,os,re,sys
m=json.load(open(".claude-plugin/marketplace.json")); bad=0
for p in m["plugins"]:
    d=p["source"]; pj=f"{d}/.claude-plugin/plugin.json"
    if not os.path.exists(pj): print("missing",pj); bad+=1; continue
    j=json.load(open(pj))
    if j["name"]!=p["name"] or j.get("version")!=p.get("version"): print("name/version mismatch",p["name"]); bad+=1
    for f in os.listdir(f"{d}/agents"):
        t=open(f"{d}/agents/{f}").read()
        if not (f.endswith(".agent.md") and re.match(r"---\nname: .+\ndescription: .+\n---",t)): print("bad agent",f); bad+=1
print("OK" if not bad else "FAILED"); sys.exit(bad)
