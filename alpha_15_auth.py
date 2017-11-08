import hashids
from hashids import Hashids


def main():
	numbers_orig = raw_input("Please enter alphanumeric  random number: > ").strip()
	digit_length = len(str(numbers_orig))
	numbers = numbers_orig[:14]
	sec = numbers_orig[14:]
	product_id = raw_input("Please enter the product id: > ").strip()
	serial_number = raw_input("Please enter serial_number: > ").strip()
	batch_number = raw_input("Please enter batch_number: > ").strip()

	key = str(serial_number)+str(batch_number)+str(digit_length)+str(product_id)

	generate_lcg(numbers, sec, key, serial_number, batch_number)


def generate_lcg(alpha_numbers, sec, key, serial_number, batch_number):
	hashids = Hashids(min_length=14, salt=key)
	hashidEncoded = hashids.decode(alpha_numbers)
	if hashidEncoded == ():
		print 'unauthentic'
		return 0
	else:
		final = str(hashidEncoded)[1:16]
		if int(serial_number) <= 9:
			final = final[14:] + final[:14]
			print final
		str_random = final[5:]
		plaintext_bytes = [ord(i) for i in str_random]
		a = 0
		a = sum(plaintext_bytes)
		sec_random = str(a).zfill(3)

		if sec == sec_random[2]:
			print 'authentic'
		else:
			print 'unauthentic'



if __name__ == "__main__":
	main()




