from requests import Session
from bs4 import BeautifulSoup as bs
import json

class Unincor( ):
    def __init__( self ) -> None:
        self.creds = None
        self.session = Session( )
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        }
        
        self.load_creds( )
    
    def load_creds( self ):
        try:
            with open( "creds.json", "r" ) as file:
                self.creds = json.load( file )   
        except: 
            print( "[!] Erro em carregar notas.json" )
        
    def login( self ):
        self.session.get( 'https://sei.unincor.br/index.xhtml' )

        params = {
            "form": "form",
            "form:usuario": f"{ self.creds[ 'user' ] }",
            "form:senha": f"{ self.creds[ 'pass' ] }",
            "javax.faces.source": "form:loginBtn:loginBtn",
            "javax.faces.partial.event": "click",
            "javax.faces.partial.execute": "form:loginBtn:loginBtn @component",
            "javax.faces.partial.render": "@component",
            "javax.faces.ViewState": "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",
            "org.richfaces.ajax.component": "form:loginBtn:loginBtn",
            "form:loginBtn:loginBtn": "form:loginBtn:loginBtn",
            "rfExt": "null",
            "AJAX:EVENTS_COUNT": "1",
            "javax.faces.partial.ajax": "true"
        }

        cookie_val = self.session.cookies.get_dict( )[ 'JSESSIONID' ]
        self.session.post( url= f'https://sei.unincor.br/index.xhtml;jsessionid={ cookie_val }', headers= self.headers, data= params )

        params = {
            "formMenuLateral": "formMenuLateral",
            "javax.faces.ViewState": "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",
            "javax.faces.source": "clink10",
            "javax.faces.partial.event": "click",
            "javax.faces.partial.execute": "clink10 @component",
            "javax.faces.partial.render": "@component",
            "org.richfaces.ajax.component": "clink10",
            "clink10": "clink10",
            "rfExt": "null",
            "AJAX:EVENTS_COUNT": "1",
            "javax.faces.partial.ajax": "true"
        }
        
        self.session.post( url= "https://sei.unincor.br/visaoAluno/telaInicialVisaoAluno.xhtml", headers= self.headers, data= params )

        return self.get_soup_instance( url= 'https://sei.unincor.br/visaoAluno/minhasNotasAlunos.xhtml', headers= self.headers )
        
    def get_soup_instance( self, url, headers= None, params= None ):
        page = self.session.get( url= url, headers= headers, params= params )
        return bs( page.text, 'html.parser' )

def remove_unicode( str ):
        encoded_string = str.encode( 'ascii', 'ignore' )
        return encoded_string.decode( )  

def main( ):
    unincor = Unincor( )
    soup = unincor.login( )
    materias_table = soup.find( "tbody", { 'id': 'form:periodo:0:notas:tb' } )

    materias = materias_table.find_all( "tr" )

    for m in materias:
        _, disciplina, freq, notas_group, _, _ = m.find_all( "td" )

        print( disciplina.text )
        print( f"\tFrequencia: { freq.text }" )

        notas = notas_group.find( "div" ).find_all( "div" )

        for n in notas:
            nome, valor = n.find_all( "span" )

            if valor.text != "--":
                print( f"\t{ nome.text }: { valor.text }" )
    
if __name__ == "__main__":
    main( )