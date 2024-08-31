meme_dict = {
            "CRİNGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "Bir şakaya karşılık cevap"
            }
            
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
   print(meme_dict[word])
else:
   print("hatalı kelime girdiniz başka kelime deneyiniz")
