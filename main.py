import boto3
import cookielib,urllib2,urllib

class Downloads(object):

	def FileToAWS(self):

		s3 = boto3.resource('s3')
		data = open('TF201904.zip', 'rb')
		s3.Bucket('jhmcnet').put_object(Key='TF201904.zip', Body=data)
     

	def FileFromUrl(self,url, localFileName = None):        
		

		request = urllib2.Request(url)
		response = urllib2.urlopen(request)    
             
		output = open(localFileName,'wb')
		output.write(response.read())
		output.close()


	def __init__(self):
        
		'''Define o cookie para a conexao'''
		self._logged_in = False
		self._cookies = cookielib.CookieJar()
		self._opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self._cookies))
		urllib2.install_opener(self._opener)
      
if __name__ == '__main__':
    try:
        print 'Baixando' 
        d = Downloads()
        d.FileFromUrl('http://www.caixa.gov.br/Downloads/fgts-sefip-grf/TF201904.zip','TF201904.zip')
        print 'Concluido'
        print 'Enviando a AWS'
        d.FileToAWS()
        print 'Upload concluido'
    except Exception as e:
        print 'Erro' , e