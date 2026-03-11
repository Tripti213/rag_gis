from rapidfuzz import process,fuzz

class FuzzyMatcher:
    def __init__(self, vocab):

        self.vocab=vocab

        self.common_words=[
            "water","bodies","body",

            "lake","lakes",
            "pond","ponds",
            "dam","dams",
            "reservoir","reservoirs",
            "barrage","barrages",
            "check-dam","check-dams",
            "canals","canal",
            "creeks","creek",
            "groundwater-recharge","recharge-structures",
            "storage-tanks",
            "talab",
            "step-wells","step-well",
            "irrigation","agriculture",
            "bore-wells","wells","well",

            "capacity","larger","greater","than","above","below",
            "list","give","show","find",
            "smaller","bigger","between",

            "top","best","largest","smallest",
            "minimum","maximum"
        ]

        self.stop_words = [
    "how","many","are","is","in","of","the","present","there",
    "what","which","where","list","give","show","find"
]
        self.full_vocab=list(set(self.vocab+self.common_words))


    short_map={
    "dms": "dams",
    "dm": "dam",
    "lks": "lakes",
    "lk": "lake",
    "rsrv": "reservoir"
}
    def correct(self,query):

        words=query.lower().split()
        corrected=[]

        for w in words:
            if w in self.stop_words:
                corrected.append(w)
                continue
        #handles short words typo    
            if w in self.short_map:
                corrected.append(self.short_map[w])
                continue
        #already correct query input
            if w in self.full_vocab:
                corrected.append(w)
                continue

            if len(w)<=3:
                corrected.append(w)
                continue

        #if not correct input, chck len 1st and then score
            scorer=fuzz.partial_ratio if len(w)<=3 else fuzz.ratio

            match=process.extractOne(w,self.full_vocab,scorer=scorer)

            if match and match[1]>85:
                corrected.append(match[0])
            else:
                corrected.append(w)

        return " ".join(corrected)