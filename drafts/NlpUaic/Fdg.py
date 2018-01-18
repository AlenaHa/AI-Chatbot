from suds.client import Client
# import xml.etree.ElementTree as ET


def get_deps(text:str):
	client = Client('http://nlptools.info.uaic.ro/WebFdgRo/FdgParserRoWS?wsdl')
	return client.service.parseText(text)


if __name__ == '__main__':
	text='Neuroendoscopia, în principiu cu aparatura endoscopică modernă uzuală, permite intervenţiile în ventriculii cerebrali, inervenţii mixte, microscopie-endoscopie pentru vizualizări ale unghiurilor dificile ale leziunii, aborduri spinale transperitoneale sau transpleurale ablative sau pentru implantarea instrumentaţiei spinale.'
	print get_deps(text)



# 'sbj. comma <about> comma rest'

# root=ET.fromstring(result)
# for sent in root:
#     sent_id = sent.attrib['id']
#     for token in sent:
#         current_head = token.attrib['head']
#         # if int(current_head) > 0:
#         # print()
#         if 'Type' in token.attrib and token.attrib['Type'] == 'predicative':
#             has_pred=True
#             # print('the pred:',token.text)
#             break
#     if not has_pred:









# print(result)
# root=ET.fromstring(result)

# path=r'D:\fii res\3\ia\proiect\ChatBotMedical\Adnotarea\ParsareTexte\DocumenteOutput\\'
# file='Fisier1.xml'
# tree = ET.parse(path+file)
# root = tree.getroot()
#
# for sent in root:
#     for token in sent:
#         print(token.text,end='')
#     print()

# for sent in root:
#     has_pred=False
#     sent_id = sent.attrib['id']
#     for token in sent:
#         pass



# print(result,end='\n\n')

# 'care sunt cauzele autismului?'
# '[cauzele autismului sunt[:]] '

# rel: pred_dir.obj(lemma)

# {'concept=autism': {
#     'rels': {
#         'are_cauză':['cauze'],
#         'p2': []
#     }
# }
# }


# 'x este de trei feluri: a, b, c.'
# 'de cate feluri este x?'



# synonims={
#     'feluri':'tipuri',
#     'cauze':'simptome',
# }

# query_pron={
# 'cine'#cui, care, ce, cât(căți, câte)
# }

# relations=[]
#
# '''
#
# de [ ce, unde, cat/cati/cate subst ]
# similar: cu, pe, la, prin, din
#
# ccx* pred sub | sub pred ccx*
#
# '''
#
# root=ET.fromstring(result)
# for sent in root:
#     has_pred=False
#     sent_id = sent.attrib['id']
#     for token in sent:
#         current_head = token.attrib['head']
#         # if int(current_head) > 0:
#         # print()
#         if 'Type' in token.attrib and token.attrib['Type'] == 'predicative':
#             has_pred=True
#             # print('the pred:',token.text)
#             break
#     if not has_pred:
'''
cauzele insomniei
general: [ atr subst | adj ]* subiect
'''

        # print('Ce doresti?')
#
# '''
#
# stud: * despre <concept>
#
# cbot: <concept> *
# stud: * se <vb> | * această <subst> ?
# cbot:
#
# stud: rel(a,b) *
# cbot:
#
# '''