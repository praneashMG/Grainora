import re

with open('home2.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_left_col = '''                <!-- Large Feature Item -->
                <div class="lg:col-span-2 relative group rounded-3xl overflow-hidden h-[400px] md:h-[500px] lg:h-[600px] shadow-lg">
                    <img src="assets/b3.jpg" alt="Smoked Resin Live Edge Table" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" />
                    <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent"></div>
                    <div class="absolute bottom-0 left-0 p-8 md:p-12 w-full text-center md:text-start">
                        <span class="bg-accent text-white text-xs font-bold px-3 py-1 rounded-full mb-3 inline-block">Flagship Style</span>
                        <h3 class="text-white font-serif text-3xl font-bold mb-2">Industrial Resin Fusion</h3>
                        <p class="text-gray-300 max-w-md mx-auto md:mx-0">Matte black epoxy seamlessly bonding ancient walnut slabs, creating a striking void effect.</p>
                    </div>
                </div>'''

new_left_col = '''                <!-- Left Column (Feature + Wide Item) -->
                <div class="lg:col-span-2 flex flex-col gap-6">
                    <!-- Large Feature Item -->
                    <div class="relative group rounded-3xl overflow-hidden h-[300px] md:h-[400px] lg:h-[400px] shadow-lg w-full">
                        <img src="assets/b3.jpg" alt="Smoked Resin Live Edge Table" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" />
                        <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent"></div>
                        <div class="absolute bottom-0 left-0 p-6 md:p-10 w-full text-center md:text-start">
                            <span class="bg-accent text-white text-xs font-bold px-3 py-1 rounded-full mb-3 inline-block">Flagship Style</span>
                            <h3 class="text-white font-serif text-3xl font-bold mb-2">Industrial Resin Fusion</h3>
                            <p class="text-gray-300 max-w-md mx-auto md:mx-0">Matte black epoxy seamlessly bonding ancient walnut slabs, creating a striking void effect.</p>
                        </div>
                    </div>
                    <!-- Bottom Wide Item -->
                    <div class="relative group rounded-3xl overflow-hidden h-[200px] md:h-[200px] lg:h-[176px] shadow-lg w-full">
                        <img src="assets/b6.jpg" alt="Custom Wood Benches" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" />
                        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
                        <div class="absolute bottom-0 left-0 p-6 w-full text-center md:text-start">
                            <h3 class="text-white font-serif text-2xl font-bold mb-1">Architectural Benches</h3>
                            <p class="text-gray-300 text-sm">Matching seating designed to complement your masterpiece.</p>
                        </div>
                    </div>
                </div>'''

if old_left_col in content:
    content = content.replace(old_left_col, new_left_col)
    with open('home2.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced left column with 2 items.")
else:
    print("Could not find old left column block.")

