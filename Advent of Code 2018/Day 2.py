import collections

class OrderedSet(collections.MutableSet):
 
    def __init__(self, iterable=None):
        self.end = end = [] 
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = end[1] = self.map[key] = [key, curr, end]

    def discard(self, key):
        if key in self.map:        
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)

            
if __name__ == '__main__':
    s = OrderedSet('abracadaba')
    t = OrderedSet('simsalabim')
    print(s | t)
    print(s & t)
    print(s - t)

test_box_ids = ['abcdef','bababc','abbcde','abcccd','aabcdd','abcdee','ababab']
part_2_test_ids = [
'abcde',
'fghij',
'klmno',
'pqrst',
'fguij',
'axcye',
'wvxyz',
]

real_box_ids = [
	'cvfueihajytpmrdkgsxfqplbxn',
	'cbzueihajytnmrdkgtxfqplbwn',
	'cvzucihajytomrdkgstfqplqwn',
	'cvzueilajytomrdkgsxfqwnbwn',
	'cvzueihajytomrdkgsgwqphbwn',
	'wuzuerhajytomrdkgsxfqplbwn',
	'cyzueifajybomrdkgsxfqplbwn',
	'cvzueihajxtomrdkgpxfqplmwn',
	'ivzfevhajytomrdkgsxfqplbwn',
	'cvzueihajytomrdlgsxfqphbbn',
	'uvzueihajjtomrdkgsxfqpobwn',
	'cvzupihajytomrdkgsxfqplpwe',
	'cvzueihajyvomrdkgsxfqplbrl',
	'cczueihajytomrdkgsnfqpxbwn',
	'cvzueigajytdmrdkgsxyqplbwn',
	'cvzujihljytomrdkgsxuqplbwn',
	'cvzueisajytomrddgsxkqplbwn',
	'cvzneihajytomrdkgsgaqplbwn',
	'cvzueihajytomrdkgsinmplbwn',
	'cveueihajyromrdkgsxfqplown',
	'cypueihajytotrdkgzxfqplbwn',
	'cvzuoihajytomvdqgsxfqplbwn',
	'cvzuekhejytwmrdkgsxfqplbwn',
	'cvzseihajytomrdkgsxfqgmbwn',
	'cvfuhihajytomrdkgsxfqplbwi',
	'cvzueihujxtomrdkgsufqplbwn',
	'cvzueihdjytomrdogsxfqplbwh',
	'cvzueihdjyfohrdkgsxfqplbwn',
	'cvtudihajytolrdkgsxfqplbwn',
	'cvzueihajytymrdkgshzqplbwn',
	'cvzuebhajytomxdkgsxfqplbwt',
	'cvzulihajyxomrdkgsbfqplbwn',
	'cvzueihajywomrdkgsxfqplbts',
	'cvzueihajytouodkdsxfqplbwn',
	'cvzueihajytomgdkgqxfqklbwn',
	'cvzubihajytomvdkgsxfqplmwn',
	'cvhueihajyyocrdkgsxfqplbwn',
	'zvzueihajytourdkgsxflplbwn',
	'cvzbeihajytomadkgsxfoplbwn',
	'cvzueihajytomrdkgnxfqplbsl',
	'cvfueihajftkmrdkgsxfqplbwn',
	'cvzuexhajytomryugsxfqplbwn',
	'cvzueihajytomsckgsxfqalbwn',
	'cvzuexhajytomrdkbsxfqpluwn',
	'cvzueihajytbmrtkgsxwqplbwn',
	'cvzueihajytomrdigsxfqqlbsn',
	'cvzweihajytomydkgsxfmplbwn',
	'bvzteihajytimrdkgsxfqplbwn',
	'cvzueihajytpmrdkgsxfcpbbwn',
	'cvzueigsjltomrdkgsxfqplbwn',
	'cvzueihajytomrikgsxfopldwn',
	'cvzueihajstomrdkgsxfqplgon',
	'cvzueimajytomrnkxsxfqplbwn',
	'cvzleihagatomrdkgsxfqplbwn',
	'cvbueihajotomrdkgsxfqjlbwn',
	'cvzueihajytomrdkgsxfqppnvn',
	'hvzueihajytomrdkghxfkplbwn',
	'cvzueigajytxmrdkgsxfqplbjn',
	'cvzueihaaxtokrdkgsxfqplbwn',
	'cvzueihajyeomrdkgujfqplbwn',
	'cvzueiwajpoomrdkgsxfqplbwn',
	'cvzieidtjytomrdkgsxfqplbwn',
	'cvzueihalytomrakbsxfqplbwn',
	'wtzueihajytomrdkgsxfqplbwq',
	'cvzuelhaiytomrdkgsxfqplcwn',
	'cvzueihajytomrdkgsxfqslswd',
	'cvzueihajytomrykgssfqplbon',
	'cvzueihfjytovrdegsxfqplbwn',
	'cvzueihajytomldqgsxfqplbwy',
	'cvzleihjjytomrtkgsxfqplbwn',
	'cvzueihaldtomrdtgsxfqplbwn',
	'cvzueihajytzmrdkgsxfeplqwn',
	'cvzueihrjytomddkgsxfqpgbwn',
	'cyzulihajytokrdkgsxfqplbwn',
	'cvsueihajytoordfgsxfqplbwn',
	'fvzueyhajytomrdkgaxfqplbwn',
	'cczueihajytobrdkgsefqplbwn',
	'cvzueihajytomcdrgscfqplbwn',
	'cvzuexhajyvomrdkgssfqplbwn',
	'cvzsmihajyiomrdkgsxfqplbwn',
	'cvzzeihajttomrdkgsxzqplbwn',
	'cvzseihajytomrdkgsxfqpebvn',
	'cvzueihajgthmrdkgsbfqplbwn',
	'ruzueihajytomrdkgsxfqphbwn',
	'cvzueihajytofrdkgsnfrplbwn',
	'cvzuetdajytojrdkgsxfqplbwn',
	'fvzueihajytomrdkghxfqpobwn',
	'cvzueihsjytomrdkgsxfqglbxn',
	'cvzueihajytowrdkgsxfqpsbun',
	'cvzteihaiytomrdkfsxfqplbwn',
	'cvzueihajytkmrdkrsxfqplvwn',
	'cvzueihajyoomrdkasxfqjlbwn',
	'lvzurihajytkmrdkgsxfqplbwn',
	'cvzueihajyyomrdagsxfqelbwn',
	'cvfueihajytomrdkgsxfqplbbx',
	'cvwueihajytommdkgkxfqplbwn',
	'cvzucicajytomrdkgsxcqplbwn',
	'dvzueihahytgmrdkgsxfqplbwn',
	'cvzuechajytomrdkgsxfqelwwn',
	'cvzuekhajytomrdkgsxknplbwn',
	'cvtueihajytomphkgsxfqplbwn',
	'cvzueihabytnzrdkgsxfqplbwn',
	'cvzusihajytomrdkgfxfqplban',
	'cvfueihajytomcdfgsxfqplbwn',
	'mvzueihapytomrdkgsxfdplbwn',
	'cvzueihajytomhdkgsxmqppbwn',
	'jvsueihajytomrdkgsxfqplbln',
	'cvzujihajybomrdkgsxtqplbwn',
	'cvzuekhawytomrdkgsxfqplbwc',
	'svzueihanytomrdogsxfqplbwn',
	'cvzujihajytodrdkgslfqplbwn',
	'cvgdeihajytorrdkgsxfqplbwn',
	'cvzbeihajytoprdkgsxfqplbyn',
	'cvzueihkyytomjdkgsxfqplbwn',
	'cvzuelhojytomrdkgsxfqjlbwn',
	'evzueihajytimrdkgsxfqpsbwn',
	'cvzueihajydomrdkjsxfqplbjn',
	'ovzteihajytosrdkgsxfqplbwn',
	'cvzueihajyaomrdzgsxfqplbgn',
	'cvzuewhajmtomrdkgsufqplbwn',
	'cvzueihajqtomhukgsxfqplbwn',
	'cvzueihajytomzqkgsxfqplbwk',
	'cazuewhakytomrdkgsxfqplbwn',
	'clzueihatytomrdkgzxfqplbwn',
	'dvzueihajytomqdkgsxfqpnbwn',
	'cvzueidajdtomrdkgsxtqplbwn',
	'cvzueihabytowrdkgsxoqplbwn',
	'cvzujihwjytomrdkgsxeqplbwn',
	'cvtuedhajytomrdkgsxfqplbbn',
	'cvzueihajcgomrdkgsxfqplswn',
	'cvzuephajyiomrdngsxfqplbwn',
	'cvzueihajythmqdkgsxfqplbwf',
	'cvzueitajytomrdkgsxfepvbwn',
	'cvzueihajytomydkgsxfqplvwb',
	'dvzueshajytomrddgsxfqplbwn',
	'cvzueihajytomrdkgvxfqpwben',
	'cvzueihajytomrdkgvxfpplwwn',
	'cvzuefhajftomrdkgsxfqrlbwn',
	'cvzueihajytpmrvkgsxfqplbcn',
	'cvzueihajytohrdkgsxfqxnbwn',
	'cvzueihajytomrdposxfqulbwn',
	'cozueihajytomrpkgsxfqrlbwn',
	'cvzuuihaxytomrdkgsxfqplbtn',
	'cvzueihajytomrbzgsxyqplbwn',
	'cveueihajyxoqrdkgsxfqplbwn',
	'cvzueihajytomrkkgsxfqptbrn',
	'cvzuezhajatomrdkssxfqplbwn',
	'cpzueihajytomrdkgsxfhplbwo',
	'lviueihajytomrekgsxfqplbwn',
	'cvzueihwjytomrdkusxfyplbwn',
	'cvzgeihajytomwdkgsxfrplbwn',
	'cvzsejhzjytomrdkgsxfqplbwn',
	'cvzuuihajytomrdkgsxfqdlbwz',
	'cvzjeihajytomrdugsxftplbwn',
	'cvzueihaxytomrrkgsxfmplbwn',
	'cvzueihajgtomrdhgsxfqplwwn',
	'cvzulihajytomedkgsxfqplewn',
	'cvzueivajytomrdkmsxfqplbwc',
	'cvzuervajytomrdkgsxfwplbwn',
	'cvzuemhcjytomrdkgslfqplbwn',
	'cvzyerhauytomrdkgsxfqplbwn',
	'cvzueihaoytomrdkgsyfqplewn',
	'cvzueihanytomrdkgsafkplbwn',
	'cvzueihajvtomrdugsxfqpcbwn',
	'chzueihajytamrdxgsxfqplbwn',
	'cvzueihalytomrdsgsxfqplbln',
	'cvzueihajytoyaykgsxfqplbwn',
	'tlzueihajyeomrdkgsxfqplbwn',
	'cvpueihajytbmrdkgsxfxplbwn',
	'cvzueihajytomjdkgsxuqplkwn',
	'cvzueihajygomrdkgkxfqplbwg',
	'cvzueihajhtomrdkgbxsqplbwn',
	'cvzurihajytomrdkgsafqplbwx',
	'cdzuezhajytomrdkgsxrqplbwn',
	'cvbueihajytotrwkgsxfqplbwn',
	'cwzkeihajytomrdkgsxfqplbwh',
	'cvzheihajytolrikgsxfqplbwn',
	'cozuevhajytomrdkgkxfqplbwn',
	'chzueihajytomrjkgsxfqulbwn',
	'cvzueihkjyromrdkgsxvqplbwn',
	'cvzveihajytomrdkgsxpqplnwn',
	'cvzueihajytoirdkgsxfqihbwn',
	'cvoueihajytomrdkgsxfqpdawn',
	'pvzueihajytomrdkgnxfqplbfn',
	'cvzueihakytomxdkgssfqplbwn',
	'cvzueivajytomrdbgsxaqplbwn',
	'cvzueihajytokrdkgszrqplbwn',
	'cvzuevhajytomrdkgsxgqplbwi',
	'cvzueihajylomrdkgsxflplbpn',
	'hvzueihajytomvdkgsxfqplgwn',
	'cvzleihajytymrrkgsxfqplbwn',
	'crzueieajytomrdkgsxfqplbon',
	'cszueihajytomrdlgqxfqplbwn',
	'cvzueihacytomrdkgsxfjblbwn',
	'cvzreihajytomrdkgsxfqplzun',
	'cvzurihajytomrdkgsxiqplawn',
	'uvzueihajyhovrdkgsxfqplbwn',
	'cvzueihajyqodrdkgssfqplbwn',
	'cvzwiihrjytomrdkgsxfqplbwn',
	'cqzueihajytomrdkgjxfqplban',
	'cvmueihajytoordkgsxfqplbyn',
	'cypueihajytomrdkgzxfqplbwn',
	'cvzueihajykomrdkgsmfqplbtn',
	'cvzueidajytimrdkgsxfqpdbwn',
	'cvzheihajytomrdkgsxfqpfewn',
	'dvzueihajytumrdzgsxfqplbwn',
	'cvzueixajytomrdkgsvfqplgwn',
	'cvzuevhzjyzomrdkgsxfqplbwn',
	'cvyeeihajytomrdkgsxnqplbwn',
	'cvzueihajytomrdkggtpqplbwn',
	'cvzceiyajytomrdkgexfqplbwn',
	'cvzuelhajyyomrdkzsxfqplbwn',
	'cvzhzihajygomrdkgsxfqplbwn',
	'cvzueihwjytomrdkgsgfqplbrn',
	'cvzsevhajytomrdkgqxfqplbwn',
	'cvzueiuajytomrdkgsxfppebwn',
	'nvzueihajytemrdkgsxwqplbwn',
	'cvzueihajytocgdkgsxfqvlbwn',
	'cczusihajytomrdkgsxfqplbpn',
	'cmzueihajytomrdkbsxwqplbwn',
	'cvzumfdajytomrdkgsxfqplbwn',
	'cvzueihcjytomrdkgsxfqplbkl',
	'cvzueihajytomawknsxfqplbwn',
	'kvzueihijytomrdkgsxdqplbwn',
	'cdzutihajytomrdkgsxfkplbwn',
	'cvzufihadylomrdkgsxfqplbwn',
	'cvzueihajytomrgkxsxfqphbwn',
	'cvzuewhajyzomrdkgsxfqelbwn',
	'cvzueihajytomrdkgqxfqelbwc',
	'cvzueshajyoomrdkgsxfqflbwn',
	'cvzueihajyromrekgixfqplbwn',
	'chzugihajytomrdkgsxfqplawn',
	'cvzueihajytomrdkgsxfhpmbwy',
	'cvzueihacytodxdkgsxfqplbwn',
	'cvzurihajytourdkgsdfqplbwn',
	'cvzzeihmjytomrddgsxfqplbwn',
	'cvzucyhajygomrdkgsxfqplbwn',
	'ckzueihzjytomrdkgsxwqplbwn',
	'cvlueihajmtozrdkgsxfqplbwn',
	'cvzkeihajytomrdkgsxfqclbwc',
	'cvzueihajytomrdkgsxgdplbwa',
	'cvzueihyjytoxrdkgcxfqplbwn',
	'cvzueizavytomfdkgsxfqplbwn',
	'cvzueihajwtosrdkgsxfqllbwn',
	'cvzueihajytomrdaksxfqpllwn',
	'cvzuuihojytombdkgsxfqplbwn',
	'cvzuiibajytpmrdkgsxfqplbwn',
	'cvzueihajyuomydkgsxfqplzwn',
	'cvzueihajytimrmkgsxfqplfwn',
	'cvzueihajytomrdkgzxfqpljwo',
]

def has_2(box_id):
	print(f"Searching for 2 letters in {box_id}")
	for needle in box_id:
		print(f"Searching for 2 {needle}s")
		if box_id.count(needle) == 2:
			print(f"Found 2 {needle}s")
			return True
	print(f"No 2 count")
	return False

def has_3(box_id):
	print(f"Searching for 3 letters in {box_id}")
	for needle in box_id:
		print(f"Searching for 3 {needle}s")
		if box_id.count(needle) == 3:
			print(f"Found 3 {needle}s")
			return True
	print(f"No 3 count")
	return False

def calulate_checksums(box_id_list):
	count_2 = 0
	count_3 = 0
	for box_id in box_id_list:
		if has_2(box_id):
			count_2 += 1
			print(f"count_2 is now {count_2}")
		if has_3(box_id):
			count_3 += 1
			print(f"count_3 is now {count_2}")
		checksum = count_2 * count_3
		print(checksum)

def find_closes_matching_ids(box_id_list):
	# sets = {}
	match_found = {}
	match_index = None
	for left_box_id in box_id_list:
		# char_set = set(box_id)
		# sets[box_id] = char_set
		for right_box_id in box_id_list:
			print(f"Now comparing: {left_box_id} : {right_box_id}")
			similarity_score = 0

			for position, needle in enumerate(left_box_id):
				if right_box_id[position] != needle:
					similarity_score += 1
					match_index = position
				if similarity_score > 1:
					break
			if similarity_score == 1:
				print(f"Match found: {left_box_id} : {right_box_id}")
				match_found["left"] = left_box_id
				match_found["right"] = right_box_id
				match_found["index"] = match_index
				break
		if match_found:
			left = match_found["left"]
			right = match_found["right"]
			intersection = left[:match_found["index"]] + left [match_found["index"]+1:]
			print(f"Matched set {left} & {right} = {intersection}")
			print(left)
			print(right)
			print(intersection)
			break

if __name__ == '__main__':
	find_closes_matching_ids(real_box_ids)