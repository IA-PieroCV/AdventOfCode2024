# Day 9: Disk Fragmenter

This day funny but also difficult to understand. This time I choose to use numpy for indexing, as this make the solution way easier by operating on vectors instead of elements. Actually, my first approach was with elements and it took like 15 minutes to finish. Of course I was refactoring the code as soon as I realize that this will take a lot of time to test. I had some conflicts with the narrative and some edge cases. I think more on the first one. This time I used AI to ask for edge cases, but it was useless (even using o1, which is pretty odd -patd reference-), but no solution provided from AI. This day was a real challenge.

## Rating
- Difficulty 🟢🟢🟢⚫️⚫️ (3/5: Medium). This day is not that difficult, but it has two points that I didn't realize. First, the ids being treated like whole numbers instead of single digits on both parts of the problem. Finally, edge cases.
- Code complexity 🟢🟢⚫️⚫️⚫️ (2/5: Barely complex). This code makes an interesting using of indexing, some tricks on that allows to solve this problem way easier.
- Narrative 🟢🟢🟢🟢⚫️ (4/5: Barely complex narrative). As I mentioned, the digit treatment is not mentioned explicitlly. This takes me to the position where I'm not getting where's the error even having a solution that comply with all of the mentioned. Maybe is also my fault and I didn't notice it.

## Leason learned
Is kind of tricky to know where to find a leason. Is pretty obvious that there's something to learn here, but I don't know exactly what. Realize about test cases was something that helped, maybe a quick action plan is going there before blaming any narrative.