from PIL import Image

def compressing(name):
    image1 = Image.open(name)
    print(image1.size)
    width2 = 32
    width = image1.size[0]
    height = image1.size[1]  
    height2 = int(height / width * width2)
    image3 = image1.resize([width2,height2]) #, Image.BICUBIC)
    image3 = image3.quantize(15)
    #image3.save('D:\\games\\test3.png')
    final = []
    list_ = image3.load()
    pal = image3.getpalette()
    for y in range(height2):
        rs=[]
        for x in range(width2):
            px = image3.getpixel((x,y))
            r=pal[px*3]
            g=pal[px*3+1]
            b=pal[px*3+2]
            #print (px, r,g,b)
            if r == 255 and g == 255 and b == 255:
                rs.append(0)
            else:
                rs.append((r, g, b))
        final.append(rs)    
            
    return final  

def fin(img, map):
    final = compressing(img)
    f = open(str(map) +'.py', 'w')
    f.write('grid = ' + str(final) + '\n')
    f.close()

if __name__ == '__main__':
    name = str(input())
    fin(name, name.split('.')[0])
