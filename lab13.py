def mystery(s1, s2):
	d = dict()
	for char in s1:
		if char not in d.keys():
			d[char] = 0
		d[char] += 1

	for char in s2:
		if char not in d.keys():
			return False
		d[char] -= 1

	for key in d.keys():
		if d[key] != 0:
			return False
	return True

#compares if the two strings have the same characters, case sensitive

#print(mystery("cheaters", "teachers"))
#print(mystery("engineering", "gnireenigne"))
#print(mystery("Python", "nohtyp"))

def most_frequent(lst):
	d = dict()
	for i in lst:
		if i not in d.keys():
			d[i] = 0
		d[i] += 1

	val = (0, 0)
	for i in d.keys():
		if d[i] > val[1]:
			val = (i, d[i])
	return val[0]

#print(most_frequent([5, 9, 2, 9, 0, 5, 9, 7]))

def first_unique(lst):
	d = dict()
	for i in lst:
		if i not in d.keys():
			d[i] = 0
		d[i] += 1

	for i in d.keys():
		if d[i] == 1:
			return i

#print(first_unique([5, 9, 2, 9, 0, 5, 9, 7]))

def two_sum(lst, target):
	pass



class PlayList:
	def __init__(self):		
		self.songs = []

	def add_song(self, new_song_name):
		self.songs.append(new_song_name)

	def add_song_after(self, song_name, new_song_name):
		for i in range(len(self.songs)):
			if self.songs[i] == song_name:
				self.songs.insert(i, new_song_name)
				break

	def play_song(self, song_name):
		if song_name not in self.songs:
			raise KeyError("song_name not in playlist")
		else:
			return song_name

	def play_list(self):
		for i in self.songs:
			print(i)

p1 = PlayList()
p1.add_song("Jana Gana Mana")
p1.add_song("Kimi Ga Yo")
p1.add_song("The Star-Spangled Banner")
p1.add_song("March of the Volunteers")
p1.add_song_after("The Star-Spangled Banner", "La Marcha Real")
p1.add_song_after("Kimi Ga Yo", "Aegukga")
p1.add_song("Arise, O Compatriots")
p1.add_song("Chant de Ralliement")
p1.add_song_after("Chant de Railliement", "Himno Nacional Mexicano")
p1.add_song_after("Jana Gana Mana", "God Save The Queen")

p1.play_song("The Star-Spangled Banner")
p1.play_song("Jana Gana Mana")

p1.play_list()