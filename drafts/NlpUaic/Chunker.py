from suds.client import Client

def get_np_chunk(text:str):
    client = Client('http://nlptools.info.uaic.ro/WebNpChunkerRo/NpChunkerRoWS?wsdl')
    return client.service.chunkText(text)


if __name__=='__main__':
	text='Creierul este bun.La ce se pune?'
	res=np_chunk(text)
	print res	
	with open('chunked.xml','w') as f:
	    f.write(res)



