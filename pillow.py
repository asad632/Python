# from PIL import Image
# # img1=Image.open('photo.jpg')
# # img1.save('photo.pdf')
# # max_size = (250,250)
# # img1.thumbnail(max_size)
# # img1.save('photosmall.jpg')
#
# import os
#
# # for item in os.listdir():
# #     if item.endswith('.jpg'):
# #         img1 = Image.open(item)
# #         filename,extension = os.path.splitext(item)
# #         img1.save(f'{filename}.png')
#
# from PIL import ImageEnhance
#
# ###  --------- sharpness-------
#
# # img1 = Image.open('photo.jpg')
# # enhancer = ImageEnhance.Sharpness(img1)
# # enhancer.enhance(15).save('photo1.jpg')    # extra sharp
# # enhancer.enhance(0).save('photo2.jpg') # blure
# # enhancer.enhance(1).save('photo3.jpg') # oragnal
#
#
# # ### --------color-----
# # img1 = Image.open('photo.jpg')
# # enhancer = ImageEnhance.Color(img1)
# # enhancer.enhance(5).save('photo1.jpg')    # extra color
# # enhancer.enhance(0).save('photo2.jpg') # black&white
# # enhancer.enhance(1).save('photo3.jpg') # oragnal
#
#
# #### =------------- brightness------
#
# # img1 = Image.open('photo.jpg')
# # enhancer = ImageEnhance.Brightness(img1)
# # enhancer.enhance(5).save('photo1.jpg')    # extra white
# # enhancer.enhance(0).save('photo2.jpg') # black
# # enhancer.enhance(1).save('photo3.jpg') # oragnal
# #
#
# ####-------------contrast=------
#
# # img1 = Image.open('photo.jpg')
# # enhancer = ImageEnhance.Contrast(img1)
# # enhancer.enhance(2).save('photo1.jpg')    # extra
# # enhancer.enhance(0).save('photo2.jpg') # 00
# # enhancer.enhance(1).save('photo3.jpg') # oragnal
#
# # #####-------------blur------------
#
# # from PIL import ImageFilter
#
# # img1 = Image.open('photo.jpg')
# # img1.filter(ImageFilter.GaussianBlur(radius=7)).save('photo1.jpg') # (radius=5)from 2 to -----100