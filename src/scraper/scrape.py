import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        self.url_tactic = "https://attack.mitre.org/tactics/enterprise/"
        self.base_url_techinique = "https://attack.mitre.org/tactics/"
        self.save_file = "ATP.txt"
    def fetch_tactic(self, url):
        """
        Fetch each tacitcs from https://attack.mitre.org/tactics/enterprise/
        to prepare Tactic ID for fetching techniques.

        Parameters
        ----------
        url : string
            url of target site.

        Returns
        -------
        None
            nothing

        Raises
        ------
        RequestTimeoutError
            when a page can not accessible
        RateLimitError
            when you kidding the admin site
        """
        r = requests.get(url)
        ttps= dict()
        
        if r.ok:
            soup = BeautifulSoup(r.content, 'html.parser')
            trs = soup.findAll('tr')
            for i in range(len(trs)):
                if i > 0 :
                    tactic = list(trs[i])
                    name = ""
                    ttp = ''
                    for td in range(len(tactic)) : 
                        if td == 1 :
                            ttp = tactic[td].text
                        if td == 3:
                            name = tactic[td].text

                    ttps[i] = [name.strip("\n"),ttp.strip("\n")]
        return ttps
                        


    def fetch_techinique(self):
        ttps = self.fetch_tactic(self.url_tactic)
        tcs = dict()
        for i in range(1,len(ttps)):
            r = requests.get(f"{self.base_url_techinique}{ttps[i][1]}")
            tcs[ttps[i][0]]= []
            if r.ok:
                soup = BeautifulSoup(r.content, 'html.parser')
                trs = soup.findAll('tr')
                
               
                for tr in range(len(trs)) :
                    tr = trs[tr]
                    if tr.get("class") == ['technique']:
                        tr = list(tr)
                        for td in range(len(tr)): 
                            if td == 1 :
                                id =  tr[td].text
                            if td == 3 :
                                name =tr[td].text
                        tcs[ttps[i][0]].append([id.strip("\n"),name.strip("\n")])
                # print(tc)
        return(tcs)


                    

    def save_ttp(self):
       pass

    def visualize(self):
        pass

    def run(self):
        pass

if __name__ == "__main__":
    cls = Scraper()
    cls.fetch_techinique()