t=['+--+-+-','+---+-+','+--+-+-','+-+-+-+']
l=[idx.replace('+','1').replace('-','0')for idx in t]
print(list(map(lambda x:chr(int(x,2)))))

for i in []:
    