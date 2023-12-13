
import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	sous_total = 0
	for i in range(len(data)):
		sous_total += data[i][INDEX_PRICE]* data[i][INDEX_QUANTITY]
	
	taxes = sous_total * 0.15
	total = sous_total + taxes
	return f"{name}\nSOUS TOTAL     {sous_total:.2f} $\nTAXES           {taxes:.2f} $\nTOTAL          {total:.2f} $"


def format_number(number, num_decimal_digits):
	forme = "{:,.{}f}".format(float(number), num_decimal_digits)
	forme_espace = forme.replace(",", " ")
	return forme_espace

def get_triangle(num_rows):
	BORDER_CHAR = "+"
	TRIANGLE_CHAR = "A"

	# Calculer la largeur
	triangle_width = 1 + 2 * (num_rows - 1)

	# Construire première et dernière ligne (bordures pleines)
	border_row = BORDER_CHAR * (triangle_width + 2)

	# Afficher le triangle
	result = border_row
	# Pour chaque ligne du triangle
	for i in range(num_rows):
		triangle_chars = TRIANGLE_CHAR * (i * 2 + 1)
		result += "\n" + f"{BORDER_CHAR}{triangle_chars : ^{triangle_width}}{BORDER_CHAR}"
	result += "\n" + border_row

	return result


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 3, 35.99)]))

	print(format_number(100.1114, 3))

	print(get_triangle(3))
	#print(get_triangle(5))
