# Write a program to fill in a letter template given below with name and date.

letter = '''Dear <|Name|>,
Assalamu Alaikum. Hope you are well by the grace of Allah. I'm also well. How is your study going on?
<|Date|>'''

print(letter.replace("<|Name|>", "Shimu").replace("<|Date|>", "02 February 2025"))