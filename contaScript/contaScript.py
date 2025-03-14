import os
import re
import sys
from collections import defaultdict


def get_shebang(file_path):
	"""Estrae lo shebang da un file eseguibile.

    Args:
        file_path (str): Il percorso del file di cui estrarre lo shebang.

    Returns:
        str|None: restituisce il percorso dell'interprete se presente, altrimenti None.
    """
	try:
		with open(file_path, 'r', encoding='utf-8') as f:
			match = re.match(r'^#!\s*(\S+)',  f.readline().strip())
			return match.group(1) if match else None
	except (UnicodeDecodeError, OSError):
		pass #return  None


def count_executables(directory):
	"""Raggruppa i file eseguibili in base allo shebang in una directory

    Args:
        directory (str): il percorso della directory da esplorare.

    Returns:
        dict: con chiave=shebang valore=conteggio.
    """
	count_by_shebang = defaultdict(int)

	for root, _, files in os.walk(directory):
		for file in files:
			path = os.path.join(root, file)
			shebang = get_shebang(path)
			count_by_shebang[shebang] += 1
				
	if None in count_by_shebang:
		del count_by_shebang[None]

	return count_by_shebang
	
	
def max_length_in_dict(d):
	"""Restituisce la len della stringa più lunga nel dizionario d
	
    Args:
        d (dict): Un dizionario con valori da cui calcolare la lunghezza.
        
    Returns:
        int: La lunghezza del valore più lungo. Se il dizionario è vuoto, restituisce 1.
    """
	return max((len(str(v)) for v in d.values()), default=1)


if __name__ == "__main__":
	if len(sys.argv) != 2:
		raise ValueError(f"Usage: contaScript.py <directory>")
		
	directory = sys.argv[1]
	if not os.path.isdir(directory):
		raise OSError(f"Error: {directory} is not a valid directory.")
	
	counts = count_executables(directory)
	max_count_len = max_length_in_dict(counts)
	for shebang, count in counts.items():
		print(f"{str(count).rjust(max_count_len)} #!{shebang}")


