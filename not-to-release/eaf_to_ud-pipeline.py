import pympi
import re

elan_file = pympi.Eaf("kpv_izva20150705-02-b.eaf")

tiers = elan_file.get_tier_ids_for_linguistic_type('orthT')

utterances = []

for tier in tiers:

    annotations = elan_file.get_annotation_data_for_tier(tier)
    
    sent = []
    
    for a in annotations:
        
        if not re.findall(r"[\.!?…]$", a[2]):
            
            sent.append(a)
            
        else:
            
            sent.append(a)
            utterances.append(sent)
            sent = []

data = []

for u in utterances:
    
    start = []
    identifier = []
    text = []
    
    for i in u:
        
        start.append(i[1])
        identifier.append(i[3])
        text.append(i[2])

    sent = {}
    
    sent['start'] = min(start)
    sent['identifier'] = '+'.join(identifier)
    sent['text'] = ' '.join(text)
    
    data.append(sent)
    
data_sorted = sorted(data, key=lambda k: k['start']) 

file = open('UD_Komi_Zyrian-IKDP/not-to-release/kpv_izva20150705-02-b.txt', 'w')

for sent in data_sorted:
    
    file.write(f"{{{sent['identifier']}}} {sent['text'].replace('  ', ' ')}\n")
    
file.close()
