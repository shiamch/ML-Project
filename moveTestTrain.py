import shutil
import os

source = 'Images'
trainDest = 'Train'
testDest = 'Test'

classes = [os.path.join(source, d) for d in sorted(os.listdir(source))]

for class_x in classes:
	folder = class_x[7:]
	os.mkdir(os.path.join(trainDest, folder))
	os.mkdir(os.path.join(testDest, folder))

	files = os.listdir(os.path.join(source, folder))

	count = 0
	for f in files:
		count = count + 1
		if(count<1201):
			shutil.copy(source+'/'+folder+'/'+f,os.path.join(trainDest, folder))
		elif(count<1501):
			shutil.copy(source+'/'+folder+'/'+f,os.path.join(testDest, folder))
		else:
			break
            
	print(class_x[7:])