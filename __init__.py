# if __name__ == '__main__':
#     n = int(input("NHAP N: "))
#     x =float(input("NHAP X: "))
#     p,s = 1,1
#     for i in range(1,n+1):
#         p = p*x/i
#         s = s + p
#     print("GIa tri: ",s)
#  Bai 2
#     s,p,q = 2020,1,1
#     for i in range(1,n+1):
#         p =-p
#         q=q*x
#         s -= p*(q+1)/i
#         print("GT: ",s)

# Bai3
# if __name__ == '__main__':
#     n = int(input())
#     s = 0
#     r = range(1,n+1)
#     for i,j in zip(r,r[::-1]): s += i/j
#     print(s)
#Cho n in ra cac so nguyen to <= n
# def ktnt(x):
#     if x < 2: return 0
#     i = 2
#     while i*i<=x:
#         if x%i==0: return 0
#         i+=1
#     return 1
# if __name__ == '__main__':
#     n = int(input())
#     a = [i for i in range(1,n+1) if ktnt(i)]
#     print(*a)
# BUON VANG
# if __name__ == '__main__':
#     a = [int(x) for x in input().split()]
#     s = 0
#     # C1:
#     # enumerate: vi tri va gia tri
#     # for i,x in enumerate(a):
#     #     m = max(a[i+1:]+[0])
#     #     if m > x: s += m-x
#     # print("So tien: ",s)
#     # C2:
#     m = a[-1]
#     for x in a[::-1]:
#         if x<m: s+= m-x
#         m = max(m,x)
#     print("So tien: ",s)
# DEM CAP CO TONG GIOI HAN, cho so M va a1 ... an, dem so cap aiaj(i<j) ma ai + aj <= M
# if __name__ == '__main__':
#     M, *a = [int(x) for x in input().split()]
#     a.sort()
#     i,j = 0,len(a)-1
#     res =0
#     while i<j:
#         while j > i and a[i] + a[j] > M: j -=1
#         res += j-i
#         i+=1
#     print(res)
# Tap tam giac
# if __name__ == '__main__':
#     a = [int(x) for x in input().split()]
#     a.sort()
#     i,j = 0,0
#     res = 0
#     n = len(a)
#     while j < n:
#         while j < n and a[i] + a[i+1] > a[j]: j = j+1
#         res = max(res,j-i)
#         i +=1
#     print(res)
# Quet voi
if __name__ == '__main__':
    m = int(input())
    n = int(input())
    a = [0]*(m+1)
    for _ in range(n):
        u,v = map((int,input().split()))
        a[u] = 1
        a[v+1] = -1
    t =0
    res = 0
    for i in range(1,m+1):
        t += a[i]
        if t: res += 1
    print(res)

