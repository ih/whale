
import csv
import numpy

#def dict_filter(it, *keys):

#    for d in it:
#        yield dict((k, d[k]) for k in keys)

#def 

def main():

	# Sample code
	#soundFileNames = [ x[0] for x in reader ]
	#labels = [ x[1] for x in reader ]
	#print headerLine
	#for row in soundFileNames:
	#	print row

	#reader = csv.reader( open( "data/train.csv", "rb" ), delimiter = ',' )
	#headerLine = reader.next()
	#rowsFromCsvFile = list( reader )
	#soundFileNames = [ [ each_row[0] ] for each_row in rowsFromCsvFile ]
	#labels         = [ [ each_row[1] ] for each_row in rowsFromCsvFile ]

	# latest problem: bool -> everything is false! how to get 0s to
	# False and 1s to True? - search for how to read 0 and 1 as bool in
	# python (might have to read as int, then convert with a function).
	dataset = numpy.genfromtxt(open('data/train.csv','r'), delimiter=',',
		dtype=["S20", float])[1:]
	target = [ x[0] for x in dataset ]
	train = [ x[1] for x in dataset ]
	for lbl in train:
		print lbl

	#soundFileNames = x[:][0]
	#labels = [ int( label ) for label in x[:][1] ]
	#labels = x[0:]
	#for lbl in labels:
	#	print lbl

#	reader = csv.DictReader( open( "data/train.csv", "rb" ) );
#	for d in dict_filter(reader, 'clip_name'):
#   		print d

if __name__=="__main__":

    main()

