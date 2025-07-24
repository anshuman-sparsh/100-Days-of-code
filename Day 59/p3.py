def count_consonants(s):
    consonants = "B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,W,X,Y,Z,b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z"
    count = 0
    for char in s:
        if char in consonants:
            count += 1
    return count


s = "This is not a world of consonants."
print(count_consonants(s))