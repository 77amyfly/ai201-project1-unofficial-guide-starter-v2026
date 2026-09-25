def judge(question, expects, answer, results) -> bool:
    n = lambda s: " ".join(s.lower().split())

    c1 = any(n(expects) in n(r.text) for r in results)                  
    cited = [r.source for r in results if n(r.source) in n(answer)]    
    c2 = bool(cited)                                                    
    c5 = all(any(n(expects) in n(r.text) for r in results if r.source == s)
             for s in cited) if cited else False                       

    print(f"    c1={int(c1)} c2={int(c2)} c5={int(c5)}")
    return c1 and c2 and c5