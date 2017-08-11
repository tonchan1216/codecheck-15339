def main(argv):
  # このコードは引数と標準出力を用いたサンプルコードです。
  # このコードは好きなように編集・削除してもらって構いません。
  # ---
  # This is a sample code to use arguments and outputs.
  # Edit and remove this code as you like.
  for i, v in enumerate(argv):
    print(look_and_say(int(v))[:500])

#秘密の規則にそった数列を生成する関数
def look_and_say(num):
	temp = ''

	for i in range(1, num+1):
		if i == 1:
			temp = '1'
		else:
			temp = translate_sequence(temp)
	return temp

#入力文字列をルールに従って変換
def translate_sequence(target_sequence):
	target_list = []
	answer_sequence = ''

	while len(target_sequence) > 0:
		if len(target_sequence) == 1:
			target_list.append(target_sequence)
			break

		else:
			i = target_sequence[0]
			slice_index = 1
			for j in target_sequence[1:]:
				if i == j:
					slice_index += 1
				else:
					break
			
			target_list.append(target_sequence[:slice_index])
			target_sequence = target_sequence[slice_index:]


	for x in target_list:
		answer_sequence += str(x.count(x[0])) + x[0]
	return answer_sequence[:750]