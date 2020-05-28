# from collections import Counter
#
# def countOccurrence(tup):
#     max=0
#
#     dct ={}
#     for i in tup:
#         count=0
#         for j in tup:
#             if j==i:
#                 count=count+1
#         dct[str(i)]=count
#         if(dct[str(i)]>max):
#             color=i
#
#     print(dct)
#     return color
#
#
# a=[[12,13],[1,2],[2,3],[2,3]]
# #
# # for i in a:
# #     print(a.count(i))
#
#
# z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
# print(Counter(z))
# print(countOccurrence(a))


import cv2


mask=cv2.imread("Original.jpg")

ret,mask=cv2.threshold(mask,0,255,cv2.THRESH_BINARY)
cv2.imshow("Black",mask*255)
cv2.waitKey(0)
