from googletrans import Translator

translator = Translator()
message=''' 
+420.000$ с одной сделки 🤯

GHOST зафиксировал часть позиции на 420.000$ или 2600% и это лишь начало, и лучше не пропускать его сигналов.

Этот парень единственный трейдер, который показывает свои сделки на видео ✅ 

Он даёт 1 сигнал в неделю, но этот сигнал приносит от 300% прибыли

Подпишись на него, что бы не потерять⬇️
'''
translated_text = translator.translate(message, src='ru', dest='en').text
print(translated_text)