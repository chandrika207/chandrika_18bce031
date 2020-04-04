t=int(input())
a=[]
for i in range(t):
  a1=input()
  a.append(a1)
for i in range(t):
    y=0
    st=list(a[i])
    while y<(len(st)-1):
        z=int(st[y])-int(st[y+1])
        if z>0:
            w=1
            while w!=(z+1):
                st.insert(y+w,')')
                w=w+1
        elif z<0:
            w=1
            while w!=(abs(z)+1):
                st.insert(y+w,'(')
                w=w+1
        y=y+abs(z)
        y=y+1
    p=int(st[0])
    q=int(st[-1])
    while p!=0:
        st.insert(0,'(')
        p=p-1
    while q!=0:
        st.append(')')
        q=q-1
    a[i]="".join(st)
for i in range(len(a)):
    print("case #"+str(i+1)+": "+a[i])