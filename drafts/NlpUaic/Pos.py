from suds.client import Client

def get_pos_tags(text:str):
    client=Client('http://nlptools.info.uaic.ro/WebPosRo/PosTaggerRoWS?wsdl')
    # print(client)
    return client.service.parseSentence_TXT(text)
    # return client.service.parseText_TXT(text)

if __name__ == '__main__':
	text='Ana are mere?'
	res=get_pos_tags(text)
	print(res)
