import json, datetime, urllib.request
import requests



class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        # TODO
        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise
        dzisiaj=datetime.date.today()
        f = open('ratios.json','r')
        ratios=json.load(f)
        f.close()
        for i in ratios:
            ratio=ratios[i]
            if ratio["date_fetched"]==dzisiaj and ratio["base_currency"]==self.base and ratio["target_currency"]==self.target:
                return True
        return False


    def fetch_ratio(self):
        # TODO
        # This function calls API for today's exchange ratio  Yes
        # Should ask API for today's exchange ratio with given base and target currency Yes
        # and call save_ratio method to save it


        url = f'https://api.exchangerate.host/convert?from={self.base}&to={self.target}'
        response = requests.get(url)
        data = response.json()
        kurs=data['result']
        self.save_ratio(kurs)
        return kurs


    def save_ratio(self, ratio):
        # TODO
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)
        f=open('ratios.json','r')
        kursy=json.load(f)
        f.close()
        czy_jest_w_pliku=False
        dzis=str(datetime.date.today())
        mx_ind="0"
        for i in kursy:
            kurs = kursy[i]
            if kurs["base_currency"]==self.base and kurs["target_currency"]==self.target:
                kurs["date_fetched"]=dzis
                kurs["ratio"]=ratio
                czy_jest_w_pliku=True
            mx_ind=i
        mx_ind=int(mx_ind)+1
        if not czy_jest_w_pliku:
            kursy[str(mx_ind)]={"base_currency":self.base,"target_currency":self.target,"date_fetched":dzis,"ratio":ratio}
        f = open('ratios.json', 'w')
        json.dump(kursy,f)
        f.close()




    def get_matched_ratio_value(self):
        # TODO
        # Should read file and receive exchange rate for given base and target currency from that file

        if self.was_ratio_saved_today():
            f = open('ratios.json', 'r')
            kursy = json.load(f)
            f.close()
            for i in kursy:
                kurs = kursy[i]
                if kurs["base_currency"] == self.base and kurs["target_currency"] == self.target:
                    return kurs["ratio"]

        else:
            return self.fetch_ratio()



amount,frm,to=input().split()
b=RatioObtainer(base=frm,target=to)
print(f'{amount} {frm} = {b.get_matched_ratio_value()*float(amount)} {to}')


