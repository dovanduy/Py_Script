# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 18:14
# @Author  : chengz
# @File    : debug.py
# @Software: PyCharm

strs={"data":{"flag":"1","map":{"CSQ":"长沙","CWQ":"长沙南","GBQ":"广州北","GGQ":"广州东","GZQ":"广州","IZQ":"广州南"},"result":["1nSvCOdMp442pMv%2FRPQC2dLrlLAnCLT%2FwFge21TnTplJkmHDV0TSIs7eAero%2B%2FIXE%2FIpnDTSb0Yy%0A%2BiHy2Rh2RvnyALon5lKiK5U5PHsBkFgDSTpREOcNJCUXB7li7LDxpyGhBRf%2BYvWonrkr2NmjP1zq%0AtjmjaUsqOptzst78ycpBZz3bEy4lddmXIjHdemsLs3tafBIM%2FKH5WG6YdE%2F9s6ou3ZQFRZswMRJA%0AIZl9MEDAMthSWv7EROuedikG9SiE6DT%2FBMZbXQZCWR%2B7qm49lOAS%2FyF1T5lBnt37EDhHTUmFNzNJ%0AMXeNxPIQzkE%3D|预订|62000G618400|G6181|SYQ|IOQ|CWQ|IZQ|16:50|19:40|02:50|Y|G5wMyUkqOBN5uUjmiOV8Vc52dwt4egD%2BwQavur8hdpBchTjWcgFjY2RgTlI%3D|20190116|3|Q9|06|11|1|0|||||||无||||无|无|5||O090M0O0|O9MO|0|0|null","%2F1P2%2BAQ0dbqnsaR3%2Bvt7HJXHKT1Cc1sBHxG%2FDhpeo4P1fV3mtTSNe%2FZJox3KftPlLQosMUjUqSyZ%0AQyyXnMgN2eWNUamN2XEx%2FQS4Jed%2B2s7Nsi5UIv0sZEj%2FUBZHF3gArzUKedEbVMcJ5tpUbEeAPYe8%0AQofmtOhBhLdPoPz2SAT5J6ULjIF01v39%2B8ei6olQADufisE8JFdPeiAgNZdM6a4O5UZ6RmdiPcFX%0AcTWZyyPma5nPC8W5JTUi4apEAjaLFA48otvhClCwcuyagFERmxWAcrscQ3ofygc7%2BmoYvZjdFXm0%0A|预订|77000G131406|G1311|CUW|IOQ|CWQ|IZQ|16:55|19:45|02:50|Y|5Ws7ExUGTEgoNgJJVSV%2FfIItMA98ASy0Nj0NZPGmUq0PHlyD|20190116|3|W3|14|19|1|0|||||||||||有|有|14||O0M090|OM9|0|0|null","K3fnHTDDRGmLm8y9ED7fBVE0p1MlL0zKAHSWRK4mtygrJ6SNL7hB72K8xJ5gx5WzQ9BD99m0R%2F2P%0AGmW7U%2BKCZsoabXyvJEwex064nUQkhvA%2B91ymjYE%2BLWsVxvY5HVAnRzJHaxsbwFTRI8kEPf%2FcpkZE%0AaAtGiT9uZlgl6%2BlHF5uwept0IJztrtvwTW0tX91BVUorT8zPrppqSf%2Fnenda%2Fxe508MqoJdRi7bz%0AcKYJ0OgVJTNaX%2B7ucjO3ht5vvnXuigvCdDmpzW49dDgYA%2BMgP4AqVUWgTue%2Fk5z2O5ZZQH0SKfTb%0A|预订|4f0000G8240L|G821|EAY|IOQ|CWQ|IZQ|17:11|19:55|02:44|Y|2WHnkHn3uAmSLHkZvVfCcUomQ%2FYmGDPhZnOU1ZzDfKNCeXX%2B|20190116|3|Y2|10|14|1|0|||||||||||有|有|19||O0M090|OM9|0|0|null","OwELMMeOaLbUN2apUTNI38wgkoKCzxEQpoC95X%2BjT2DWFcV7ZEw0QHrXjP2XO%2BsUGwuAfHInIhsc%0ApYa%2FB9dFOgedrIzy3ZK6DtsiySaOfTe6w8HDqEAdC3HNrYNFwbH39KBBOnwNkiXXnHJjfDhZaoJB%0AI%2F6EVcMt%2BOzvy8k7vwiSnTSKY9GSN9liOz2KfCT54fbVYlCoXAeX%2Fgj8SDLXowwmZlsU6AwTe0D5%0ArcxkxdrAFvZe9GrUaszYNElYQ4R0a176YTzBYSoV4Xp%2BsS2S6w%2Bs459z%2BsbXNCuP3dMwWGqc14VA%0A|预订|4e000G101907|G1019|WHN|IOQ|CWQ|IZQ|17:16|20:00|02:44|Y|wzmzapxiQlMpnRzvXaaowhHSiS25TUjgktDr3Oho3qx5LZae|20190116|3|N3|03|07|1|0|||||||||||有|有|17||O0M090|OM9|1|0|null","ydCW2Wml5K%2FqyvM9XN641QqEtKsZkF3kxTUcGuG%2BJNh1S0hXwydcovygUC8dYxFDC%2BSCIpQOmwr3%0AYb3VaGB07pln4XncfzmESQMrftxrPsXSJXdjivSIXKGo09G5DvZ1WPnq68xniRiCMH7ypKrOcvG7%0AgKd8D2VM9mIityGKy3iB8B4fRamn5zuLgqojn%2BvlZ%2BIjB834WoJ1crycoCr1sFSyoyMQpU%2B7KoNp%0AmzVSACvEezUCE6ph4m82iCG2%2Bb5I%2B%2BpJAgWF8pcWQX%2FHqAi6PyGmDsP1LgNDrhCylgvSq6cuMiWO%0A|预订|4e000G112909|G1129|WHN|IZQ|CWQ|GBQ|17:21|19:47|02:26|Y|TdvwIO8bJo37x3oYVgmf61cDW4j3Cy5Cb1QLYxM0iQ8DQVRB|20190116|3|N3|03|07|1|0||||||15|||||有|有|||O0M0P0|OMP|1|0|null","hR75MTkKMF%2Fy%2BH8euGaR5YIM94kTfrI%2FyeEVKW1WcrQfrmxmUny7dC6xXRZdAg94As%2FZJYL8hZal%0Ady5aVh5IjWTs28%2F%2F62NMITd6b7objDxFR2NosnefIaFY%2BLqsdhSUnCG%2FjhXOTyr4Myg1Z7di7rz0%0Avo%2BoCZ5pOe8wxib22YgswqWM4I9w%2Bve9o%2Be9LCqi2ZgUu%2Bcwo6m0V9hb8uhREdWOEq6%2FSXtogejP%0AfD%2FSAhBSfw755%2FojBdI9kFMgVaHDCCCf25AbjDGcYy6oXhsCd9IcmjiZc8NNXb92YmObvbk%3D|预订|2400000G650H|G65|BXP|IZQ|CWQ|IZQ|17:32|20:16|02:44|Y|r9VMKIflWjzx7aK0WHaJEuWdZwKBydOm7iEKbTcTQOtZSann|20190116|3|P4|12|16|1|0|||||||||||有|有|16||O0M090|OM9|0|0|null","pL6ZXtHRoQrE9OLgJSBUe6gonCQeC9FXTA8LXcXOWJJzB%2BYaQpOBoSf4zNmIoX437mdk1g8DSs3i%0A4CsKsubXiYitBOcwRbOhJDt5fA0ZU2%2BKbmL6K1w7VYTtqqou4YeJ5Zdr45v%2FHcVuVAhoHlS7k9HD%0A53PZy0iEjEIjyLeKcB2YwSs4O7alGQHbcohyEeDdsRu4EnOLjLKCh3BbZSoSRc6zKPT2lvLZm2Ri%0AdQ87M3DEM763a9w20HbHuyTsiX5oFFRP4Z9jGF8xMOwhejbXfzVvca4UmfUX799Uv4TLmgJobleq%0A|预订|8d0000G83406|G831|LAJ|IZQ|CWQ|IZQ|17:43|20:26|02:43|Y|PzvREsv4hAKC0clziAn4olMTBzCFvuoz6l2z7Sxh%2BfyTwqLN|20190116|3|J1|17|21|1|0|||||||||||有|有|19||O0M090|OM9|1|0|null","|预订|380000G5450A|G545|ZAF|ZHQ|CWQ|IZQ|17:48|20:31|02:43|N|%2BSNHFkpJdvTh91ddXbiuXij9E1h8m%2B7WpAC5rAk7lEqgvvjI|20190116|3|F1|06|10|1|0|||||||||||无|无|无||O0M090|OM9|1|0|null","5qI3X3fwhJWv2bw6HLvDO2Uk%2Bav2sEatSKdRP93cHEKTqYIri2JHf90c2Khqg1KzAXOKNOvoF%2FxK%0A18WMyZxfq%2BqTzYe1%2Bv52GqZFeMUzZ6VAV2hvaw6yp1mzqzsGj%2FLYQGZq2kP%2FP09QtfemAEXi5Wgf%0A0JEGjcHX0DSRNkj3lZ%2FFmrMk%2F9ikcf6glJbNbQ%2BfAckvmKAFLEkoE71Sljdz8Er8UcWXcz4evxGW%0AZZCIpky1j96QHea0sNN9PdzdXhS78fcek%2Buv9E46Ik6QWfCZb9xLX2uiYGGaQUTHYm7fq1CspiDC%0ATde0PthWJ%2Fw%3D|预订|6c000G61170C|G6117|CWQ|IZQ|CWQ|IZQ|17:55|20:39|02:44|Y|4gZiyYaWnxGDULkmbdAk2gIOKVpQAjYzjREwN2NUSKL1bxZV6Ig6K7IgKsU%3D|20190116|3|QX|01|05|1|0|||||||无||||有|有|8||O090M0O0|O9MO|1|0|null","vhJHHa%2FZx3vSTHQHiU2xWprl6B7efTZ3fYdz1LFQaBDpjDV7ac38T%2F%2BOxcSMtYj3OlBiaYXVlv%2BV%0Afj1IBBj4%2FH%2F0dv4Io5Dz3lNC8EbwVjXTKGIa%2BB8xVvd%2FDqTkq%2B2KYG9y9jGPK1TMy5odFgHoXdXB%0AjIu%2B4M2eA6F3ugwv8DnZZ6ylthLICnTPelXP4pqyILW920e8Vr9%2Bwa8vdvMYRlfFcUsfaey1AsNy%0AZoVp6bF4s0mOdRqMqN2dJ6TNAPwnRxzW%2F9latbNbCyVOcRBFr3mbhPp8qAMtX84rkHK1p3xWvxit%0A|预订|390000G55307|G553|OYN|IZQ|CWQ|IZQ|18:00|20:45|02:45|Y|5Mf%2B598hn2bYmY6HNpsCFZNwabW1tPTWl78F5QMHvh31AJdY|20190116|3|N4|05|09|1|0|||||||||||有|15|9||O0M090|OM9|1|0|null","LYCXaGOf3l%2BG3CbQhB3ckBb8%2F9An9SHUTum7ar4M7zBjC%2F8c7RktIlgEllzjGJ3F9FnozsrjaNz4%0AW3xA0PxyyXU1at4koxdO75yQAT%2Bczy72RHrfkLKu6hypZRxJXfvQIo8LXgDCw8E5fVs4DqcKGQOh%0AXV4cnL9DWbYS6yoh0f5rWV0CiiZYvM%2Bvo1S6BFh%2Fj1PgbnX3%2B%2FdFeTtwm86E1m1okaaKuv6IQnto%0A4lC8R9gh4NAdf4xw3a3muGCY3KOPyFx5U9dbkuo8KKeDsnb%2BcOxkvXYBelTfjyGiE3eYXe8fibVf%0A|预订|4p000G205801|G2055|JGK|IZQ|CWQ|IZQ|18:05|20:49|02:44|Y|XdSoIO%2B0iUUeUXLV7X%2Bjs%2FOyCws6D197%2FsA7D7gqUbqoU67j|20190116|3|KA|16|20|1|0|||||||||||有|有|有||O0M090|OM9|0|0|null","bNE548F%2FEKgUU4jzsdUc9G%2F2CWor6VMNgpkwrwP0ega%2BoRIzEYaF6ZOCS4OdXM5XO1faxAHQgln%2F%0AvFYiJ35T4UB1zkP%2BL78nGpK%2FePnX3CCEbjJXc0do6ZP784%2BSKxxFPrv2CNKWHroIe2ngqYm%2BhdpZ%0AkJrODs%2BZWBZhSQgZ13ddwcgCV5GrPfhdpaPFlLQ60V1Gdzjq5kThD%2FM7YT0d83WnSQYL9wK2p1wG%0AVCY%2Fj5e8AIavB70hjg%2B6oQEV%2FhQET%2B9ITnrt1JK2GAVv40Z8SnSenWz6FHHwAQGoiUHk0aCKTamj%0Aw5UAkKMDNx0%3D|预订|6c000G603303|G6033|YIQ|IOQ|CWQ|IZQ|18:10|20:54|02:44|Y|gFthMkPYKgLe8egBPBx4K37QvEer0vVfeTXlF0jjZ%2FHXyaFY1rFHmoZcchM%3D|20190116|3|Q6|03|07|1|0||||||10|无||||17|18|||O0M0O0P0|OMOP|0|0|null","K3fCGNGxh7dA7ROTBj9dXJWleKRjA%2B6G8FZfBcNztn3DYYLmObkPUEi%2Bdr5Y6cDsvLxvucaDuF3C%0AWlJftULP1IbMoDvYN7QUp1SLyeIfCINMPIsT9H4A8l4yfqJWNDIXlyHls%2BB7UOxkcjBOfJd8Lb2U%0ArQExknInCDpaBPw03jL0UbNSowmLNFGonGFQ7rXziWcA22w9sAnRZWOnYYerWUW65KofuVGFz%2FuQ%0A%2BJtnSaRgucpRR3bpo6dvBmTQV8vq6NzfO%2BOhL6f2veFICGXurV8l2VsEtlthO5EE9Lwn8FY%3D|预订|3800000G7540|G75|JOF|IOQ|CWQ|IZQ|18:16|21:00|02:44|Y|al%2BuC4R0tlTjhIMlSw3jat1XK%2Flzsmly%2FuOUpCW7V54sS9qF|20190116|3|F2|09|13|1|0|||||||||||无|有|19||O0M090|OM9|0|0|null","3aOsK5j323GwEV6dEueFl7PryLK18mVJveLd%2B3Ugb%2FWEvmXVIrYJ1IEPpNcEB1PrXRFfEztFJ%2FC4%0Ah2bA%2B%2BgyK8sPw%2BhFy4Q%2Fe3PUIH6EwRvYhyMM11NrZd1F0Rjm3BUUQJUKvEbtmcwmRd4MvWamdpi2%0A7OCnXj1CDskbvABDW%2FNJF0jxqyIZauvJJYrUNBFtS9IA41%2BjQMjnxIMRwZOdxupgEoMSPGbh%2FInA%0A6XSDLPLu%2BItxGhZUSQD4yX8FaQ5sjbb0V5H%2B1AqO8oao90KK2YCIFcZknFcRRVP%2BP%2FYjG6g%2B8MLa%0AmBRdO32Eazg%3D|预订|6c000G60250I|G6025|CWQ|IOQ|CWQ|GBQ|18:21|20:47|02:26|Y|kQi%2BaqZ8kfehye5WVPJI27cGQ%2FusVQA8lQdMHuqmL05wGk7UxCO4zb%2FxzC8%3D|20190116|3|Q6|01|05|1|0|||||||无||||有|有|19||O090O0M0|O9OM|1|0|null","27nVlwpQrz6efU%2BzaWjx2nMIdzVLaBZDPftSh9va5iByMyzDs9AzLpEm5o4l7KDOKJkUDiFN9nzi%0Ak8hn%2BRsB1tRgQL0NZ1vwLoaOVfvEpE1rmH4ONfY49cD5pL1rRzLYX2MflUA%2BkaFZOMT9MMEPHsb7%0ARjbFDZZVYiPW%2BVukHu5JIvip6tklfwFSXAVg%2FxLOYAsjSFiS2ubd2GjFvy3IRGW3b3vhpw81Tz8a%0AzEJ6XQBIrY7ZcTraTsE1mJmmCQi9wl1QkNRbE2Mz6GoME9DTUMxJ5fKWfql1Q1gU4aZDZIXotS3A%0A|预订|4f0000G8380F|G835|EAY|IZQ|CWQ|IZQ|18:33|21:17|02:44|Y|7v7WuINomfx1DfCInD1hU8er7ejFmD78FpgvpoNKcI1PCm30|20190116|3|Y2|10|14|1|0|||||||||||有|19|10||O0M090|OM9|1|0|null","eiG8pagHxU9t1M6OU8epQxlJmr12I7lxbhbqzAzpNmsfTPJsJI2d7%2B5REwxAIEso8sdTQ9qRjT0H%0ALxe7zZnsFCdVGbXzZtYgUKBgUn2UIzEat26SwKK1Z9xA6KWJhqZ%2FhlqI0HH9Al6rEfn61eX8Sf71%0A2wc6GQlWOd0mtzhXYsVWi4ee43%2FauCDQvsqSQ5hJSsShaJ56SFiM3tZ%2Fllpu65JICDRXHNEHJFFr%0AZUP%2BSi%2FtlZaDyMkmB8tuMiOtYlUqZGxhTUDnlRVNmtnXptiFzp%2BBHfQZ7KzbF5xvPijjm9JQf8X9%0A|预订|4e000G10210C|G1021|WHN|IOQ|CWQ|IZQ|18:38|21:22|02:44|Y|MbEVxL2eJRrtOyyEOa7JpzqFTU68t%2B3NMrd2y7cHcI657wPr|20190116|3|N2|04|08|1|0|||||||||||有|有|19||O0M090|OM9|1|0|null","BoU1RYRDPROnuaVLyRlwZ3cPIPNa3BHYzs0J59TTtYlfzZx9lVczGxFzzZpbzhp6bsRtMDAp6c6b%0Ao%2F0kRaRIyU%2FNOyHwiIC2DHS%2BwpT4QC7WJ6ksTDpeeOhvSE5s7sK%2BhLymvOSYmjmvwDV3SzgGdPjR%0A3Q%2FKxHLg%2F3x3FU6pr8Fd0qT8SgMTkJwP8P49xQpTIxnTBvjmoZkjRiMr3pMZXOC%2BDoiDn40camwM%0AgPKzn0%2BS%2BjAY3Im6KXqV7PNJRicy6sh5XSr7CDEHvOmcBtbW%2B0A6Z4GLBv8okea3hfCpPPE%2FOpub%0A|预订|6c000G61190L|G6119|CWQ|IZQ|CWQ|IZQ|18:43|21:27|02:44|Y|x4K%2Fhqj5ww3HE0SyfodPaDdKiYhVZ%2F2iG6A7pKMepGM8z3sU|20190116|3|QX|01|05|1|0|||||||||||有|有|有||O0M090|OM9|1|0|null","BScf22AuknabkvoQJe6XoQvB5arfb6i8Ycm0Qi%2BOfCiOQZiGSpaCl68PtGZ6lvtXEaQcuLGDZeQi%0AIGBCXZN%2BGZTLsCQrBZY9EDjW8tYorxZhkvamdekYXKAyjz3cWzst4l7vx7hGzqw77F804CcLkqtp%0AI4gSOXaIcGMfKeJ%2Fl3%2BW79J9TSxzyj%2FigAuXAPrJHiF%2B1GfhUuTzB4o6dXsZgSo2uXh3zm9Wfb7v%0A%2FQW608xVj%2Be8wtJ1q%2B1LejEgC0qq6LIn7HqfVkcPI6EtUu0kDHylGLmj6AUawWzckP8REwlpborX%0A|预订|5u000G140705|G1407|NXG|IZQ|CWQ|IZQ|18:53|21:42|02:49|Y|D95HTT0JGDxTjC33lSOB9FTnFTHCBKekV9mpRbc1Z4UbVqNX|20190116|3|G1|06|10|1|0|||||||||||有|有|17||O0M090|OM9|1|0|null","NMNUHsdf%2FUamdE80%2FqTmjWVFA%2FyHekR3to%2FysmJgXGhTFm8dbxCc%2BQWDFgcduecjTFHF%2Bku0ULsG%0AVp7jF1gA7cJG4CRBomoGp1Q6WfOUTL1wvxN646NU3ZUH87triMOBA8SVGBfTVUTGR%2BUkjAsNtDR3%0Adb7fyXakWwABXBfXWDvV5BW3WgUZx59r7TPYduFBS6DhwXsCSqTidDSJUwZuE2QL1kxTLvxdn7ac%0AM7JrD0ptxd12JvnvnGu%2FCuCzKigJP1Ifh01AljY0ugG5do2gJamDk%2BuqTw1XxTsPoEX%2BLX8%3D|预订|5l00000G9903|G99|AOH|XJA|CWQ|IZQ|18:59|21:32|02:33|Y|cEoyjfLT13ZFY8n5lc%2FWEnfuN4Y%2BYqnFc3vw592CKTl6Fg6f|20190116|3|X1|06|08|1|0|||||||||||有|有|5||O0M090|OM9|0|0|null","2On74FHCl7ccIruixikk801PeOBOFDbfS6lih5as6ZlaiWaPZF2UvXVKpZkQfc%2F1yP4nquf3rRvL%0AerCyrxGQ0FgSIwTOQtRbil%2FzLMtws%2FKzwm1MzcYufeP5zntjQXT0eOUdepwcv7lj6RL2fA30JI64%0AY1Fyl%2F88iaKsSxtFdRFyXFoMzQrgOibOWsiwqdmzB8GyXSdSCjVV9q6xa4O4X49Euc7i3S%2BV1Z33%0AjSU1b1lpuxzzRsbtGMwkSIKWODzoSf61Q0XN46b4iF66NJnf2Wv5FKkRAf%2ByuG%2Buu09l7Njtn%2BqV%0A|预订|4f0000G8280Q|G825|EAY|IOQ|CWQ|IZQ|19:09|21:47|02:38|Y|WKt0v95EJVORzdek6zoQ8QPUKeUTuBUpfONoMjXXBGNMagBq|20190116|3|Y2|11|14|1|0|||||||||||有|有|有||O0M090|OM9|1|0|null","Ee%2BeMHQ%2Fl87lvzEM1%2BrBdC9lesEZQoUSCCTO1XS%2FuDP%2FfllIJ%2BGVr3fQ1%2FCXxlP3qSRsRFwcxdEO%0AWl9D1ndrNMHdr9m0GKoO8meMdWkWhJEJNpIZakC9vISi6%2Bug98jZieILmEj81nk35j6GpZD9WUy5%0ASFCX60yogtADufrsgK9nDAuzvHqZFUbKCjZqto2DxZcO8MXhXshpz140sk067YJNeZWxXah5PcEF%0AQqnyLIWncIj9YUHUoNjwYjwGm1s2kL4TVzCPG8wX1%2FkTmqjDFruq3i2MPbp69tWCRuVzbx%2FzaL9W%0A|预订|39000G115402|G1151|HKN|IZQ|CWQ|IZQ|19:14|21:58|02:44|Y|4K24ivfyxznK9Jgok9%2B4OWyuvnVLx4P8H%2Bm4thLjco%2Bjb%2BKf|20190116|3|N7|05|09|1|0|||||||||||有|20|9||O0M090|OM9|1|0|null","VIq6HxzA%2BVXbpjQf1Xlr%2FDCRztjsXUFBa%2F80M2gatrk%2FyXI55hQAFStreAMGZC0h2YIoqjp6RRM2%0A8QEFP%2BVFDFjBQErLylqjxqSLmw6j8ojfE1CGjwB7EMCNFN3cd9brYXSeUWWqKQQ7MrNWut9%2Baz4G%0Axw%2F%2FVaDrl%2BwpQenjmXjwEqIQmlYNyhSGiK74QvXUEsVDUIDbhgIlC5TqUBE2qyakiYwZDxU6K9xE%0AJe1enMIemfeg%2F911jlnpih%2Bg1273EbhcfQWjhNLBeosaEi34eLy4rKO8eJ9J7x%2BB2dif0WYtuKEU%0A|预订|4f0000G8420N|G839|EAY|IOQ|CWQ|GBQ|19:19|21:45|02:26|Y|Sspd107aO8%2BNVeNcvNLBJYVe00MiqXF%2BvnfQS77JWm5uuUJj|20190116|3|Y2|08|12|1|0|||||||||||有|1|6||O0M090|OM9|0|0|null","qW4lpMhugObuirgPBNWQ39uLlcXd3OS77lOhy5KcfIiuwFTzrWzojYS3qIgCjxsfXQlT4QBnfv9L%0AK1mTywFtZD7QqJEXW%2B839suDbIQ1bkH426DslLVca6ORwup57crMPo5YTWFQKDSXXDXlrBPJjVZH%0APdIQpSL5ZJXeefu25PEkBCocRFzgxXlGu%2FJIBfc6qau5DITu1jA5hkMmMPPBkdTiQvGZuG%2F8MqYS%0AlRSuMUwMp9GEoHU02TzqRt7guGv%2F6LSVHhv6piPEHi%2B1aTIDTZYNNZKRBfrMLEyPN6Gluj9eJy%2F%2B%0AE5Ch25kCTAE%3D|预订|6c000G60270H|G6027|YIQ|IOQ|CWQ|IZQ|19:30|22:14|02:44|Y|kb2OdzOv3J5pBSXIokC1SNz8ZChbk8EeSbJdpJ6xXQg1o4SzvY4hVgk8UyY%3D|20190116|3|Q7|02|06|1|0||||||有|无||||有|有|||O0O0M0P0|OOMP|0|0|null","%2Fqx8Z%2FMEvET8W6nk1ZdHQsceJt8IFXX7d3AlPmJpSwhEU6D4A%2B2p4HNkatD%2FFIdDO06yw3IaY2yv%0ApPKpNlOcXykqnXJi7Ptqz7l14fLA4IuBv%2BOitt%2FTFVxRNXsQz2wugKEhd5KaUKsoFiaZLYI1zPCe%0AqzvrAw4dQLnMor9qIccCiYzX%2BRp4iJUG1cfwTdmiElEqcUhGhYd%2FTlvmwaUpibugFcyLgmsBlPxh%0AbSfw3eIUwxHAFZnIL%2BSBvFKdAitVBZqI8%2F8CTulvjccauEoBgSo1qlaem7zYZ24TkfCOang%3D|预订|2400000G670I|G67|BXP|IZQ|CWQ|IZQ|19:35|22:19|02:44|Y|mu1D05AvhDQAbZpvUlQcdbTg2FvRwFA48hot5oJ948su8y8j|20190116|3|P3|14|18|1|0|||||||||||有|有|有||O0M090|OM9|0|0|null","80IvznhD6opzei6Aa8zsSLO%2FkDt%2BOCatrv1xoLAUk54J9pBKpNaeyDZV8VqjayNb4stewoHRFOZZ%0AlOfI1AfAfO7XtWUM8Fy8IN7x0%2F7qnFSWwICPPVzK9H2IOnKrDDjNPpfUnL3feLViyuqqPnqrFSX2%0AW8eXAextEkVy3mTambDrwfSKol2CcYwDSJRescV1Ixl74i0%2B0tC1RV3QOBpi%2F37VjxuP70KcSNZc%0ATyTJ8x22ZDD8O8fz1iqEktGs8hhd6LhfSzaCYLnG%2Bia8UFSRqV0%2FN8TEF2UBnXVnYYonUp0j6y54%0A|预订|4e000G11350F|G1135|WHN|IZQ|CWQ|IZQ|19:40|22:24|02:44|Y|GrMUtulp%2FASRGcKc%2BfRnasW97zONeKF6qTtF5xPmCfJDa8Nt|20190116|3|N6|03|07|1|0|||||||||||有|7|9||O0M090|OM9|1|0|null","t7BsI8%2BnyEkcrQcvEoebH%2F%2BDxNu5S%2FjYWO%2Fp1aXr2JH4uDx286R3KVieJMrOHkVSZsAp5CC06%2FAH%0ArE4%2BPkEJITNdcASk5FsTzO4c6pdvfi7oJgCLDqpyGMa5mZHn8%2FmMDoyI3GS7Mqzi%2FPOzDF3WX6py%0Anl48%2Fmb6AqpTNjjM8Sl4OWK2dK2HepYlQWMZDVM4Lnc7mqYhah7cVIAMgJhAswMTyCkoaHyD1yxN%0AbTrvyy78u%2B1tZlHUYXFR2V9KNlk4CTtV1RCwtk2eQ2hgup6eo2cxfzL9EXW7CLHQR7fsgwR687mn%0AsWLUvw%3D%3D|预订|62000K901101|K9011|CSQ|OTQ|CSQ|GZQ|19:43|04:01|08:18|Y|9xRMFz3GTlLcFa2Q5s3ok3pT541cQuxI%2BnWACYFoVAEDk9MFC5SFy4F6Stg%3D|20190116|3|Q6|01|07|0|0||||14|||有||有|无|||||10401030|1413|0|0|null","C8Nu2s%2BLLUNb5M%2B7fcWRkO7Q4RdBL09g8nilyM3BhirvV9vWxKYO%2BUmfGoxlmi9xToSAcITEqwg7%0ARpYi6ikaigG4rmEDB4m2sMGtKM9Nkjy6RVw21IF8ZwgMn8Dl7D3Jx%2B6Oc0lyqqhS74xAv3D9MglH%0AnTMiKVNWGtCGPtbI7DlwKcrVAkuhV1tJVybElcuwiTITm73GTBv3hQzv0ALky2TGYz3HNf7yb%2BxQ%0AFdWMT1yFRKB7x2xaffYcnqacIoTu%2F%2BCs1WKYHglRwy6WLQlloQOhrjcOw41szNLrey2CsUxmEFtP%0A|预订|4e000G113309|G1133|WHN|IZQ|CWQ|IZQ|19:45|22:40|02:55|Y|Nbl%2BVAsYX9iRFo9ICy58TuKvRe0mF9Di19ktYeVcuU%2BZsSfF|20190116|3|N4|04|09|1|0|||||||||||有|有|10||O0M090|OM9|1|0|null","npkEtY1kRH3dcqijl%2BTd52eYr6x%2B4jIxRMEgppYQxjCclakEiBBXc%2BH3kFfKp9gOOkP0tC%2FDK8vI%0A9j7CpmJEQFuPYFQyOqe1kAFBvwlA7RkDvN%2BBtGMlu5fpPgQoa2zQMlil0uyOTM2AeOpSfkYBb1Cv%0AT3bBMFpDvcdEikL9nEDAaN%2F%2Brubnnc2Uc%2Bgk%2ByOCtqcJ3dRerrJABIv40mAiv4EuEl1KGWERdkG5%0AMxpIb2rQVDjZeomObHG7x3%2BDCX2eC0J0fVLDz41dofD63DzjEtc8%2FIO70cBNhoLQRg%3D%3D|预订|390000K4350D|K435|WCN|HCQ|CSQ|GZQ|19:50|04:25|08:35|Y|qefuY1hYZJuVKrF5O2MmRPi2gSsGo6EnAdxvc8GuQEUXBAbC|20190116|3|N6|07|13|0|0|||||||有||有|无|||||101030|113|1|0|null","Pg9GnSlGOpIdy5EISzf0K%2BEHhwP1dQOaxafGNIca9Ho7C%2FHcBjVPQLBwfo%2BKEKmCVr9CT%2FhZS3aJ%0Aaw6XITiLqFX%2BtH8YQR7gLo8cjF%2FsbM9oA%2BoEX%2FIxGMUWiARq7A6WQpBg1SWNVCZUvbDTB32lBOKH%0AP%2B50DUlJLw8FOvc%2BSVlf0d38uLGWxJFQXdo1p%2F4Ck5JwCGOLJkjc0CM2Fp6ZaTILdN%2FO2wZeQCOu%0Av1tHrPt6Du6BbGefGIqIe4hF7SUTg77rsY%2FkgVtA5QR6mS1dz9bd7guIi0Kij55eFTqlbvY%3D|预订|2400000G690A|G69|BXP|IZQ|CWQ|IZQ|19:56|22:29|02:33|Y|6MwWRDlDHcJ6RfoT9q7n0NvLKJUXLpFIBkbTDSQov3Gr2YZO|20190116|3|P4|10|12|1|0|||||||||||有|有|有||O0M090|OM9|0|0|null","6f3t3I36M5lj9Umd3V8%2BrDfLuEu3UfN8TXh1xmKxw9l39xwECedlt7QvjUdMgMT%2BKV%2F4TD3uaHE3%0A%2Bg5nlq%2Bs9I1e4P6RonX0JD06E4XX5drVfJ1WKi4SNKMLjpgHEEorHBePe8jH0y0ad%2Fke3dGIoAfe%0AdZcIEG%2Ba1t4vofVBeHcOA4lV2wk4gGEidHHUIMHtpYbOrF6kE6PDt6I96sCiG7JOiPZFExL5%2F%2F56%0AC0%2B2lR1wpQw3XIr6yicT1eQrnXbTDFAthM8%2FTh5TES0bi2cmJyBSOBOfYtLcqk9xpQjlAm3DEU5u%0AEgJmLQ%3D%3D|预订|770000K35806|K355|CUW|GZQ|CSQ|GZQ|20:14|05:12|08:58|Y|eRznhdM05imPEHl3jsy6fIu6HnhFbttoDAn2AKANRwRwFJyauDu87cL3aig%3D|20190115|3|W2|19|23|0|0||||有|||有||有|有|||||10401030|1413|1|0|null","KroLvVuiMhBZWz9rWnDIFAyT94m%2FF%2BxqaDyVrxhsEinUXpj3Tusoz1wdJcoEHny6OxKP6XNvKtuc%0AdIvjCQ1PMSEPI1Hn%2Fq3NhRNwt4ozLLhuXdDkmTy5lzIUWuHCojFSHnUZwTUWd3n5sphhJG%2B%2BgalS%0Ahp3rqab1exKpYVo9hrTJU%2FVx5X6SjXXtekNurha%2BvQujLhLuV8bjzkszqefgqx422c6BksfzpfsE%0AHYSvN6PFzvsaUbMSlIV6QaM2YgNrJ3sHEMdSkMKmfECJpRWiuqVw5OvgbOQ6232Odm13DY13W%2BXr%0A|预订|8d0000G84601|G843|LAJ|IZQ|CWQ|IZQ|20:16|23:00|02:44|Y|AReIB5f%2BDQCsryyMdXEUYjy0U6Qu4LrItj23FPTjxwxa2nsJ|20190116|3|J1|17|20|1|0|||||||||||有|有|19||O0M090|OM9|0|0|null","GyG2AcQTiZoc7sTfSsBq%2FvJW%2FFZsIrYAfarGKqYZcPclN6vNouXZM0Ef1nEry93OmBEgz6sgGDUE%0AXX%2F%2BbrGF51NIuvO%2B1ZlwDAvvGFknF5q7INkaEe6S4eIp0qrzHic4DRg%2BbNQZKN8C4TlWcVTtxwHu%0ASaHutdRPmdLWBzphBOvlVpOVmmZ2cfkpuHeGAsImr%2BgjWREuw65srn9PX2RZ6ruWl8YWlgLlZpDI%0ArUn%2Fhb031WybMXCoLGMwErqLvqQBnkKPP8ZDiP3oXmdlMgcnumH4pS1706ml1JWEEQzeh2CppB%2FJ%0A|预订|5i0000G63561|G635|ENH|IZQ|CWQ|IZQ|20:21|22:51|02:30|Y|NDwjJfh%2F7KeWhNB%2BHXEG7PG%2FYr%2BDxmJUYeoNq85D3gcTUp8R|20190116|3|H3|17|19|1|0||||||7|||||有|有|||O0P0M0|OPM|0|0|null","XMPgPdvkAsxggj0xd2bK7%2BiDLS6vRb3ml54G6tzZkApSTMP5YfyjtxZ3INWsVBTJ9NkyEeyrgTy4%0AQnKsqYg0qZEn1U0oFcXg23sCl9Hm8rrQkk1q8CdlmY2UxwA7Hk9DldyO4NLDshG8YEIRm%2BsxNHRU%0AofID75WVjYyVqy%2FM%2BrFgI5rt6dzozbzOqaI2nTXkibA3t8jS7Buivmc5tpJL3q5tIoK1pYSQN%2FfC%0Apb%2FrDpoDUTlwSXWpMSJXV8Dm%2BjIQnwYlV7kSmgyJU1YXB9pze0ik8ZqrnJTRmMk7ixG7JoxPxver%0A|预订|5l000G174340|G1743|NKH|IZQ|CWQ|IZQ|20:31|23:10|02:39|Y|PbHutgGuTUwgWbsT2i8%2FNLOzwN8YxjwDmp2hlq%2Feu1cFbib2|20190116|3|H2|07|10|1|0|||||||||||有|19|5||O0M090|OM9|0|0|null","%2B%2F%2FI8L9q4g6qLMbFec5HoKIbfvUAVhAoSRaZs5sg3qPyDS2bN91kY9ygqZWpHTRIO8GI6uo1WhmQ%0AQ4u6Ba%2B8UHso9zDb7oTb5zyvZoL0hsamfVWhY7DTHua%2Fx2iLRVB5QjQfkXT%2BbDjFianbr1xxYNgz%0AnTzK2uYIwLkyaxWavo7DZVcGUUjojKxL7LAIe2YvAboZ4XQZOu0l3eXWMlK7aReutzzl49zxjHQM%0Ah9HiLq%2B7cBG3xbsI%2BTo8gU0FK4QAnUt3st1zLyc9Z74c%2BUYH%2BGyXaSgLCNmg3dJBQFinn2akwScC%0A|预订|250000G29503|G295|TXP|IZQ|CWQ|IZQ|20:37|23:25|02:48|Y|hmzatWB%2FAiN44SPWsGB2RCxKAMvEC2xnbACFmFDGBIYfaADT|20190116|3|P4|16|20|1|0|||||||||||有|有|有||O0M090|OM9|1|0|null","|预订|380000G54708|G547|ZAF|IZQ|CWQ|IZQ|20:42|23:15|02:33|N|%2BSNHFkpJdvTh91ddXbiuXij9E1h8m%2B7WpAC5rAk7lEqgvvjI|20190116|3|F2|09|11|1|0|||||||||||无|无|无||O0M090|OM9|1|0|null","nfOV%2FyF0xKVJ0iKLqWmBFYVtAC8CbldmptJZTJwTU0I1lj7x9IWSru57XaUyTsPMKVukcXFlwYw8%0AH1kjMAEQz9Xx8UQSoZL%2BOXLVvTuXCkbS%2B4%2F4kGp1edHOpjW6p0GwlybDbBhJ0AOTxN8sBufs%2Bw65%0Adjg0WFpRcErjEHLEe4qewbwg%2F2FRj2ohJHZ2KpNlBgZSwqsivRC4g0Ukj0noSPM9ws4iQAejvGpT%0Aq9lMFEOCic1Vbd173u8EyaIZvl%2BhF0t3MPUmP1mitHX4%2FAEAC%2F%2FM9PAJe1i3DVbLQN7JXpodzEM8%0A|预订|5l000G130540|G1305|AOH|IZQ|CWQ|IZQ|20:47|23:38|02:51|Y|%2B1lxIit%2FRhCguIVSxemgmeJTQOc4mOXs8Z%2FSyQKmEw8AQxg1|20190116|3|H2|10|15|1|0|||||||||||有|有|18||O0M090|OM9|1|0|null","LfOxQoL%2BzYjubqJ8OO2jDjsfGRB2t9pULHFsPYY4NNOju0%2BeNHLJo1uJhOXdM9qujkrb0h10EQq5%0AOG8rEOwXZfFn0vwadzbFlYNfCQIwjVrvGYXM9k%2BBuetm9kbHFpbNo1UtjKa2BkJ3jWtokN3TxG6I%0A8FnC%2F5%2BiV52LzXOT5Lrcl3j3ocanU21P3RU2%2F%2BQXYLa10qn%2By7vdJW3dlxaSuHIXw7v1f925X5sC%0Azo228WVXrZDCjhlq9MnvbdmSW3p3TCp8kkkuJqmcxfiYDxlRHoLkL6cCsS%2FldZmpos89XNNyQV0J%0A|预订|5l000G174711|G1747|BMH|IZQ|CWQ|IZQ|20:52|23:43|02:51|Y|Cow7a4V%2FB8mMI18EPcSBegnGaHHEhwcDfFao%2B1S1GyTZ2T0%2F|20190116|3|H6|11|16|1|0|||||||||||有|有|有||O0M090|OM9|0|0|null","f9sP4sXjE3dMDf8hewSlwSxoNUOKfcJxNWOELic4hsrW80wsLl7jc%2FtIgWzA9QHS9I4LaWVAWjkU%0AkgYQd23RdCelRvUWPezz7s599B7ZTYdcekdochEEfS8yq4ZKEvQvxOxR8%2FeJ0XEa%2BUXHzRvkJz35%0AyoSgUhrUrngJ0sZCek0By14SlAqY9bfCa%2FP4PWeWADWeoqjPWIwJvpzBMaEopMDAGxFXT8o883na%0Ah8To7wH7maBPVuInzM9M8p6wTq8GnQTV3Xao7Oc3OFMZkLEW3qjMnTMKvIRuAnaaqqfYRLZDmrMz%0A|预订|6c000G612910|G6129|CWQ|IZQ|CWQ|IZQ|20:58|23:48|02:50|Y|mIj%2FECrgTxHMSgrsxVACy6IJs4JrG7M3DWrA%2F5N46tigRXZZ|20190116|3|QZ|01|06|1|0|||||||||||有|有|19||O0M090|OM9|0|0|null","4CKMrFwkZld4Q1s%2FhmWVYiAp%2FAblC9u%2F%2BO1%2B0APgkiijpTU1E6hYptPgwRZREL%2F2KMkoQOsNp8C6%0AMsdG%2F2Ocf8fuZ4pKH4PzCFRWkZSTOqSn2xJlIgsobKIzDTWwm2jZTlAbEF%2FcrkP5QpQQJWGUf3y%2B%0AfnaBDf0v1jazLypjnbWazslqSK1KIjHpr7r3VQxzllvI2GzGBLEiMOS9GNA0o5D3%2B6PA8WxJujUt%0A2QzRwCdWtN3e5E5NDaLwCvcyIoMGkahn5ZvyrhV0KHliHpbPIaKVtvkYiaBs31dwwIdYj35zT6Kb%0A7HEAhw%3D%3D|预订|130000T36909|T369|DLT|GZQ|CSQ|GZQ|21:19|05:30|08:11|Y|nB5S58jsVUQqfSHEsqU29BrPThMdqIjOD0rSJqMe5fHbqkxtX6W%2F0qroUtA%3D|20190115|3|T2|32|37|0|0||||有|||有||有|有|||||10401030|1413|0|0|null","nN8wLprNRSdgv1cAk8ClABXc8GYCHbS2KWNSs4AAS2VTLfdbvjEb%2FiWOWsWgjOhFw4Hzn9wfZdDt%0AiqPr6iZeH4PcEExuPdvYocAUe8SKLLxPuW0G35xsyUYJGoep%2FtEmqC20t1VqOcAY19%2BJwZDiE0TX%0ANphpffLI4yHDkCkSabMS6ZLrhtM1Zc%2BSE7efkTOHFaj0RIdbX0uiC8J4YtaDOAqpK2HeehLce%2BYM%0ANKydC%2FEm%2FIQ1h%2FcmdwxJx3xKAzZu%2FcqKyPrNaJi384UJgs%2BqSP4bUX79JL%2FQbXhL20lHmVALxHar%0A0K2HKg%3D%3D|预订|6a000K907700|K9077|AEQ|OSQ|CSQ|GZQ|21:25|05:36|08:11|Y|b1HTwhXElZdQ3JnwGZajdBzEQmwgAUNYcSufHVayiFhm1Yqgc%2Fr7QgD0uxc%3D|20190116|3|Q6|03|07|0|0||||10|||有||有|有|||||10401030|1413|0|0|null","Pp2Lz2%2F5BYAIZO7qJxgCxRR3jsmUW1FAtgyiPe%2BSjPxFYnBx86dM5xkCJnru1%2FKvXdlDysVtEpjM%0AmHrTm5H04t5Z2QEXb6kds6B6BNa8ayXPeIQTnYvwucLQNMfSLWPKS3yTOTNrV2Zvmjb4UWK77wO5%0AzztRfky993Do7Hzk1hIHJhEIBHNwvvOM1pHeKzucGPdGlrphxvL3Qc7AzCgX77hJrUObndqGtgfF%0Ai%2F0oGXzuaxwVwx8Lkg9Ed27YH76WRtVzgCay%2FFmVJDtUYyLobkmlPJKs3GjY6h7tuA%3D%3D|预订|39000K107905|K1079|WCN|GZQ|CSQ|GZQ|21:31|06:00|08:29|Y|MW%2BK9MlYimETYHQuCXswzf0kJRqn1znt%2FBuaiTw1ciX1sKo8|20190116|3|N3|06|11|0|0|||||||有||有|有|||||101030|113|1|0|null","bOZ36gpG4EtMpYiA66VxEZu4%2BSwG4hwfe2ry43kp5XgR20G6vZb%2FHRppMt7565tGJ6mIe6cbbJFP%0AnI9eEDL2MdZz1TuOxPAp6uqIUHk0oJtYPDQ5%2FZHhsHqqbnYUoSJK4aBQNhEZ%2Bd%2BzEd%2ByTzQ98DKQ%0AJGgzYmDQhuCoBNaJtHP7GIhCrMTJPG4v92xXgpLDz9xnKA2qLtYrXhDha78GYzXVLwe67DnMDDcx%0AlZAEDLYdSnBblBfLrDdnGP9oeEn2pQk0ic%2BQ87KWtlGVnYfIFUp1ktsp3HTnv8BHPDmazmolUYLc%0A5sEbrg%3D%3D|预订|64000K903801|K9035|DIQ|GZQ|CSQ|GZQ|21:53|06:12|08:19|Y|vMN2V0Wv1FvR8CkFAVSlEPhPff4%2FpP7L5C%2B%2BSB4Vh27w6bglGT3z9lqw6J0%3D|20190116|3|Q7|06|10|0|0||||有|||有||有|有|||||10401030|1413|1|0|null","QkAOdjR5xWwHK%2FP%2FC9r9FJUpaMNHQZAItqfoEDN%2BbQX2QxW8EC%2BSzfrShc%2B6Grz44fYA6M7SubAF%0ArgGmsj4jmzOgN1rIom4MmVlEZ8ZUd31iWRPLKNQ1dogXsQp0gCFey5Lfb7qWbuaHjlygaOAXWTMO%0AczulUmS%2BgkHXtOAX7Y5QflTSTLtaI54Fo2OhDkQlBSeU4sZ1GXnRdHIDc%2B0Imy3aCxN2GyacbUZU%0Awg4%2FXNJDD0k93aK8QKVlWbI0CVXhNnb32dJn9anQhlbmeDvbcvVeTXhuMs6tO5U43mv3v1HT5NI5%0AOF%2BWXg%3D%3D|预订|62000T830903|T8309|YYQ|GZQ|CSQ|GZQ|22:45|06:45|08:00|Y|I%2BysBLt0iOhndxvNcsnIaCUmIUnEyKTnfTwX72sj3OmHGhkq%2Be3bIrK5h1Q%3D|20190116|3|Q7|02|04|0|0||||有|||有||有|有|||||10401030|1413|1|0|null","Yj%2F5laNIoS%2BAHbC4ZxQUq6awfdabk1wjkOPFbOotHtXGkjR6JO8KSarQVoWzsEKU6oDqdDEzRrLo%0A9K2v4qeSYg7jtYFQr2ZyzQ7j1IE5tmFEYyuFaHbCJgShurmlevoiE6xR%2Br8JI86%2FdF8SxgLtgGgM%0At1MIL4dXONOM9b1LqfH4jwYhJM6gCYHTkbt0vkpb9UT3C%2B1BUsYLMUOPuyvOZHHKCJiEfS4B51Aj%0ADbrPQamgtrh0ZGjb0c3cCrsnDQwTjWe80Hzw2PMO8SPs4z0pRZsstX8MBljVpdIw3k2ttTgJs2rM%0A|预订|3900000T9502|T95|HKN|SZQ|CSQ|GZQ|22:52|06:20|07:28|Y|9TLJ%2BcnK%2BiQvp6fp4iqS%2Bwc8fsTRkKb8i%2F03T2wjZDJXVi5AKeVC8scIDTM%3D|20190116|3|N6|05|07|0|0||||有|||有||有|有|||||10401030|1413|1|0|null","MLnU%2BsA9%2BlUQ31a2hiDIj0PXg80z5YzAmz8UiNGL515ODPETCqwy3Zj4zQrANn1fBFdW03MTiuxv%0Aly59PHSXIi%2BPkmYG1LzHStk%2BE1ADCTrAYo4L9%2FHqh9fb4n8ItOvrFcSP2qox8hETXOSzybpVTwkd%0AATNYK3v6yR%2FPbOsV%2FzP77mRrc8MMlyY7RNPkQihE9%2FmU39bCyOI%2F72is8LCtrsfd4O5JignG73Pu%0A2uTvlavaD8Mh55G1GulBrKjs3bknmmm85fXtFuiHPNKeFVwcLusGQgKrSYKQfi5NxqCGDQJREoEF%0A%2BSkv%2BA%3D%3D|预订|64000K90630M|K9063|RDQ|OSQ|CSQ|GZQ|22:59|07:25|08:26|Y|HdauQreqTQTGCrHKJLCJJjxgPOtWUlZ5EbLtFd8ZHWKscL64m0K4XDO3Wq0%3D|20190116|3|Q6|11|16|0|0||||11|||有||有|有|||||10401030|1413|1|0|null","79U5eMoMlY0xKOMwBKdeZdXCOcTXwkPbstWhByfumY97Il%2FqYB9j%2BJpKTiPIz1WpLbOiBBOncGzz%0A%2B4I3%2F%2BmmbugJZIvAzF3BTAAofEanLiFHo%2BTfH9cUEeGdDk0%2Fai2KB3cJECw%2BhRASUlZd9Ug0%2FgMy%0AZOukiVm1branaE7LDsiHeA%2FTbMVq955djvPbGLC6lqf%2FqANqEsEGE1FdsoQUDBER%2BDVshq6dQ8Tw%0AOiGH1G53ndQdUGAqKgj8d6VwNnGF1s42f1COVqcg60VBJEdTktsEV9SlLd89X5eMG3drH6oJWK7Q%0A8QkbgA%3D%3D|预订|62000K90170K|K9017|CSQ|SZQ|CSQ|GZQ|23:05|07:31|08:26|Y|1JjU5A1xzgLRlaqR6C%2FCXDo3FJP1371cZqhnVdsn1uNi%2FcBy4xHyuwPduXc%3D|20190116|3|Q6|01|06|0|0||||14|||有||有|有|||||10401030|1413|1|0|null","kgaaeOI7b8%2FZhp04Blmjs7wZFWFFpjOPvD%2FZeLRXWZF3gSL7J9CiYHhZREsPdT9HrfhhABYbyRMr%0AD2%2Fp%2BErXo%2BixAmCmZSWd1GUK31BFPDcmsAzy2yGXmPeoRA9P3A0a5Kp25gjigncLv6NrFTBXQ%2BPM%0Az9D3uAtKSXZtfT2l2EWfaNByFdpO8t1dPcZIqazi0kc7S1NIehEJnldyuIC7W6ok1Ro1RAO6ngrn%0Ahz5BWcUb6z4oaDgCOqEBhpppoYK98qkk4iWb0r3P0yohygG0Sh88Qc9v370ltabnMp3xUFT34eW4%0AN9iUfw%3D%3D|预订|420000K93104|K931|XFN|GGQ|CSQ|GGQ|23:46|08:47|09:01|Y|0UxQgSYWapnqsNhaet96NhrR%2B8YFZH%2F83rv2tsSM4vLFxtWD2WU%2BM%2BSFumM%3D|20190116|3|N2|11|14|0|0||||15|||有||20|有|||||10401030|1413|1|0|null","9xKxRayIiwvubObBwRRu3mOiof1bkpWQwDEbsu8UAjc%2B9rxeRrGi9NCxg%2BvLjMS9zDYAnn6RvLWh%0AJ5T3fXj9XC3oyqcivpYwjhwdTb4dI%2F2CqDu2LXuxiC8urjD3YDojvGLf1M15QxJIGoHVk4tExLWc%0AoQkfVHTVnjy3T3hE84StYMGwbS7tqUQlR2Iygtpf62v%2FvjwBq%2B26T0qqtuxubB1jdlzXNRLL8diM%0Ah5U8ol%2F9rwZIsXCVyY9jSCK50siSfiOQ7Ssmiw7b5YNC9DlRS8I%2BfyWRQHxrX6FcxzS9Jyqk03Yk%0AAXSbTdcMVyE%3D|预订|62000K90030B|K9003|YYQ|BJQ|CSQ|GGQ|23:53|08:13|08:20|Y|OgbZ3dqw5OjR%2BlrAtxiVMXu8D7LCv7eoziE4o3ryfbGvu5eeHrTqWsCpmfU%3D|20190116|3|Q7|03|08|0|0||||17|||有||有|有|||||10401030|1413|1|0|null"]},"httpstatus":200,"messages":"","status":True}

for i in strs['data']['result']:
    ticket_info = i.split('|')
    # print ticket_info
    print ticket_info[3],
    print ticket_info[1],
    print ticket_info[11],
    print ticket_info[8],
    print ticket_info[9],
    print ticket_info[10]


    # if ticket_info[11] == "Y" and ticket_info[1] == "预订":
    #     print ticket_info[11]