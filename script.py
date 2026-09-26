with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

map_section = '''<!-- SECTION: Location Map -->
    <section id="map-section" class="py-16 bg-background transition-colors duration-300">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col items-center text-center mb-12">
                <span class="text-accent font-semibold tracking-wider uppercase text-sm mb-3">Location</span>
                <h2 class="text-primary-text font-serif font-bold mb-4 text-3xl md:text-4xl">Find Our Workshop</h2>
                <p class="text-secondary-text max-w-2xl mx-auto text-lg">Located in the heart of Los Angeles. Come see where the magic happens.</p>
            </div>
            <div class="max-w-7xl mx-auto rounded-3xl overflow-hidden shadow-2xl border border-border h-[400px] md:h-[500px]">
                <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3305.733248043695!2d-118.24368492429402!3d34.05223417315682!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80c2c648fa1d4803%3A0xdec27bf11f9fd336!2sLos%20Angeles%2C%20CA!5e0!3m2!1sen!2sus!4v1700000000000!5m2!1sen!2sus" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" class="grayscale hover:grayscale-0 transition-all duration-700"></iframe>
            </div>
        </div>
    </section>'''

content = content.replace('    </section>\n\n    <!-- SECTION 5: FAQ (Grid Layout) -->', f'    </section>\n\n    {map_section}\n\n    <!-- SECTION 5: FAQ (Grid Layout) -->')

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Map section added successfully.")
