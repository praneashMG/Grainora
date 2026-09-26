import re

with open('home2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove flex-1 from Right column items
content = content.replace('shadow-lg flex-1 md:w-1/2 lg:w-full', 'shadow-lg w-full md:w-[calc(50%-12px)] lg:w-full')

# Note: on md:w-[calc(50%-12px)] is to account for the 24px gap between the two side-by-side items so they don't wrap.
# Actually, grid-cols gap-6 doesn't apply inside the flex wrapper, the wrapper has gap-6. So w-1/2 with gap-6 will wrap!
# Yes, flex-1 was preventing wrapping by shrinking them.
# Let's use flex-1 on md only! md:flex-1 lg:flex-none.
# So let's replace it with md:flex-1 lg:flex-none w-full lg:w-full.

