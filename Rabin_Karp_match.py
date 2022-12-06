import UNSPSC_structure

class string_to_int:

    def __init__(self) -> None:
        pass

    def rabin_karp_helper(self, pattern, text):
        d = 26 # a b c ... z
        q = 5381 # large prime number
        m = len(pattern)
        n = len(text)
        p = 0 # hash for pattern
        t = 0 # hash for text
        h = 1
        i = 0
        j = 0
        
        res = []
        
        for i in range(m-1):
            h = (h*d) % q
        
        for i in range(m):
            p = (d*p + ord(pattern[i])) % q
            t = (d*t + ord(text[i])) % q
        
        for i in range(n-m+1):
            if p == t:
                for j in range(m):
                    if text[i+j] != pattern[j]:
                        break
                j += 1
                if j == m:
                    res.append(i)
            
            if i < n-m:
                t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q
                
                if t < 0:
                    t = t + q
                    
        return res

# UNSPSC_Tree = UNSPSC_structure.getTree()
# print(UNSPSC_Tree)
ava_words = ['cloud', 'services', 'saas', 'service', 'agreement', 'business', 'only', 'only']
# UN = "cloudservicessaasserviceagreementdatabaseproductsforbusinessuseonly"
# *set() * is the unpack the list and each element is passed as different parameters.
# set will remove duplicates and using [] merge all the remaining elements to form a new list
ava_words_set = [*set(ava_words)]
UN = "Cloud services - saas - service agreement - database products - for business use only"
count = 0

xyz = string_to_int()
for item in ava_words_set:
    count += len(xyz.rabin_karp_helper(item, UN))

print(count)

