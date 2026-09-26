import re

with open('home2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace 1st image in Section 3
content = content.replace(
    'src="https://images.unsplash.com/photo-1611269154421-4e27233ac5c7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"',
    'src="assets/b1.jpg"'
)

# Replace 2nd image in Section 3
content = content.replace(
    'src="https://images.unsplash.com/photo-1592078615290-07e05442b36b?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"',
    'src="assets/b2.jpg"'
)

# Replace 3rd image in Section 3
content = content.replace(
    'src="https://images.unsplash.com/photo-1533090161767-e6ffed986c88?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"',
    'src="assets/b3.jpg"'
)

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Section 3 images.")
