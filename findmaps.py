#/usr/bin/python
#Author :: akemi403
#Name Project :: Find Maps

import requests,json,os

class FindMaps:

	def __init__(self):
		self.CheckOS()
		self.banner()


	def CheckOS(self):
		if os.name == "posix":
			os.system("clear")
		elif os.name == "nt":
			os.system("cls")


	def banner(self):
		print("""
░▒█▀▀▀░░▀░░█▀▀▄░█▀▄░░░▒█▀▄▀█░█▀▀▄░▄▀▀▄░█▀▀
░▒█▀▀░░░█▀░█░▒█░█░█░░░▒█▒█▒█░█▄▄█░█▄▄█░▀▀▄
░▒█░░░░▀▀▀░▀░░▀░▀▀░░░░▒█░░▒█░▀░░▀░█░░░░▀▀▀

|| Temukan Alamat yang ingin ada ketahui ||
||          Author : AKEMI404            ||
===========================================
[1]. Temukan Alamat berdasarkan tempat
[2]. Temukan beberapa alamat berdasarkan tempat
[3]. Temukan Alamat berdasarkan Langtitude Longtitude
			""")
		try:
			select = input("Pilihan : ")
			if select == '1':
				self.GetAlamat()
			elif select == '2':
				self.GetAlamatSpecific()
			elif select == '3':
				self.GetAlamatGeocode()
			else:
				print("Tentukan pilihan anda..")
		except(KeyboardInterrupt):
			print("\n")
			print("="*50)
			print("Terima kasih telah menggunakan tools ini")
			print("="*50)

	def alamat(self):
		print("="*50)
		alamat = input("Masukan Alamat/Tempat : ")
		return alamat

	def GetAlamat(self):
		api = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={}&inputtype=textquery&fields=formatted_address,name,geometry&key=AIzaSyAkhtm4rgX9PKld5WoTTsSi_FHU3H3dXdg".format(self.alamat())
		r = requests.get(api)
		data = json.loads(r.text)
		jmlh = len(data['candidates'])

		i = 0
		if data['status'] == "OK":
			while i < jmlh:
				nama = data['candidates'][i]['name']
				lengkap = data['candidates'][i]['formatted_address']
				lang = data['candidates'][i]['geometry']['location']['lat']
				lng = data['candidates'][i]['geometry']['location']['lng']
				print("="*50)
				print("Data Ke {}".format(i+1))
				print("="*50)
				print("Nama Tempat    : {}".format(nama))
				print("Alamat Lengkap : {}".format(lengkap))
				print('Langtitude     : {}'.format(lang))
				print("Longtitude     : {}".format(lng))

				i += 1
			print("="*50)
		else:
			print("="*50)
			print("Alamat yang anda cari tidak ditemukan..")
			print("="*50)			

	def GetAlamatSpecific(self):
		print("="*50)
		print("Note: Silahkan cari alamat dengan specific, contohnya = 'Bioskop di Jakarta, Mall di Jakarta'")
		api = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key=AIzaSyAkhtm4rgX9PKld5WoTTsSi_FHU3H3dXdg".format(self.alamat())
		r = requests.get(api)
		data = json.loads(r.text)
		jmlh = len(data['results'])
		print("="*50)
		print("Menemukan {} Alamat".format(jmlh))
		print("="*50)

		if data['status'] == "OK":
			i = 0
			while i < jmlh:
				nama = data['results'][i]['name']
				alamat = data['results'][i]['formatted_address']
				lang = data['results'][i]['geometry']['location']['lat']
				lng = data['results'][i]['geometry']['location']['lng']
				print("Nama Tempat    : {}".format(nama))
				print("Alamat Lengkap : {}".format(alamat))
				print("Langtitude     : {}".format(lang))
				print('Longtitude     : {}'.format(lng))
				print("="*50)
				i += 1

		else:
			print("Alamat yang anda cari tidak ditemukan..")

	def GetAlamatGeocode(self):

		lat = input("Masukan Langtitude : ")
		lng = input("Masukan Longtitude : ")

		api = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key=AIzaSyAkhtm4rgX9PKld5WoTTsSi_FHU3H3dXdg&result_type=street_address".format(lat,lng)

		r = requests.get(api)
		data = json.loads(r.text)
		jmlh = len(data['results'])
		print("="*50)
		print("Menemukan {} Alamat".format(jmlh))
		print("="*50)


		i = 0
		while i < jmlh:
			alamat = data['results'][i]['formatted_address']

			jmlh_data = len(data['results'][i]['address_components'])

			a = 0
			while a < jmlh_data:
				types = data['results'][i]['address_components'][a]['types'][0]
				data_alamat = data['results'][i]['address_components'][a]
				data_alamat = data_alamat['long_name']


				if types == 'country':
					print("Negara    : {}".format(data_alamat))
				elif types == 'administrative_area_level_1':
					print("Provinsi  : {}".format(data_alamat))
				elif types == 'administrative_area_level_2':
					print("Kota/Kab  : {}".format(data_alamat))
				elif types == 'administrative_area_level_3':
					print("Kecamatan : {}".format(data_alamat))
				elif types == 'administrative_area_level_4':
					print("Kelurahan : {}".format(data_alamat))
				elif types == 'postal_code':
					print("Kode POS  : {}".format(data_alamat))

				a += 1
			print("Alamat Lengkap : {}".format(alamat))
			print("="*50)

			i += 1

if __name__ == "__main__":
	FindMaps()