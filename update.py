import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title and Brand Name
content = re.sub(r'Juicora', 'Grainora', content)

# 2. Update Desktop Nav
old_desktop_nav = '''                    <a href="about.html" class="nav-link">About Us</a>
                    <a href="menu.html" class="nav-link">Our Menu</a>
                    <a href="smoothies.html" class="nav-link">Smoothies</a>
                    <a href="juices.html" class="nav-link">Fresh Juices</a>
                    <a href="gallery.html" class="nav-link">Gallery</a>
                    <a href="contact.html" class="nav-link">Contact</a>'''

new_desktop_nav = '''                    <a href="about.html" class="nav-link">About Us</a>
                    <a href="portfolio.html" class="nav-link">Portfolio</a>
                    <a href="materials.html" class="nav-link">Wood & Materials</a>
                    <a href="process.html" class="nav-link">Our Process</a>
                    <a href="contact.html" class="nav-link">Contact</a>'''

content = content.replace(old_desktop_nav, new_desktop_nav)

# 3. Update Mobile Nav
old_mobile_nav = '''                <a href="about.html" class="block text-primary-text font-semibold text-lg py-2">About Us</a>
                <a href="menu.html" class="block text-primary-text font-semibold text-lg py-2">Our Menu</a>
                <a href="smoothies.html" class="block text-primary-text font-semibold text-lg py-2">Smoothies</a>
                <a href="juices.html" class="block text-primary-text font-semibold text-lg py-2">Fresh Juices</a>
                <a href="gallery.html" class="block text-primary-text font-semibold text-lg py-2">Gallery</a>
                <a href="contact.html" class="block text-primary-text font-semibold text-lg py-2">Contact</a>'''

new_mobile_nav = '''                <a href="about.html" class="block text-primary-text font-semibold text-lg py-2">About Us</a>
                <a href="portfolio.html" class="block text-primary-text font-semibold text-lg py-2">Portfolio</a>
                <a href="materials.html" class="block text-primary-text font-semibold text-lg py-2">Wood & Materials</a>
                <a href="process.html" class="block text-primary-text font-semibold text-lg py-2">Our Process</a>
                <a href="contact.html" class="block text-primary-text font-semibold text-lg py-2">Contact</a>'''

content = content.replace(old_mobile_nav, new_mobile_nav)

# 4. Update Footer Text
old_footer_text = '''Serving fresh, delicious, and healthy smoothies, cold-pressed juices, and wholesome snacks. Fuel your day with our vibrant, nutrient-packed blends.'''
new_footer_text = '''Crafting high-quality custom woodworking and live edge furniture. Handcrafted pieces designed to bring natural beauty and timeless elegance into your home.'''
content = content.replace(old_footer_text, new_footer_text)

# 5. Update Footer Links
old_footer_menu_offerings = '''<h4 class="footer-heading font-bold text-lg mb-6">Menu Offerings</h4>
                    <ul class="space-y-4 text-sm text-gray-400">
                        <li><a href="menu.html" class="footer-link">Our Menu</a></li>
                        <li><a href="smoothies.html" class="footer-link">Fresh Juices</a></li>
                        <li><a href="smoothies.html" class="footer-link">Smoothie Bowls</a></li>
                        <li><a href="juices.html" class="footer-link">Healthy Snacks</a></li>
                    </ul>'''

new_footer_menu_offerings = '''<h4 class="footer-heading font-bold text-lg mb-6">Our Services</h4>
                    <ul class="space-y-4 text-sm text-gray-400">
                        <li><a href="portfolio.html" class="footer-link">Portfolio</a></li>
                        <li><a href="materials.html" class="footer-link">Wood & Materials</a></li>
                        <li><a href="process.html" class="footer-link">Our Process</a></li>
                        <li><a href="contact.html" class="footer-link">Custom Orders</a></li>
                    </ul>'''
content = content.replace(old_footer_menu_offerings, new_footer_menu_offerings)

old_footer_quick_links = '''<h4 class="footer-heading font-bold text-lg mb-6">Quick Links</h4>
                    <ul class="space-y-4 text-sm text-gray-400">
                        <li><a href="about.html" class="footer-link">About Us</a></li>
                        <li><a href="juices.html" class="footer-link">Our Mission</a></li>
                        <li><a href="gallery.html" class="footer-link">Gallery</a></li>
                        <li><a href="contact.html" class="footer-link">Contact Us</a></li>
                    </ul>'''

new_footer_quick_links = '''<h4 class="footer-heading font-bold text-lg mb-6">Quick Links</h4>
                    <ul class="space-y-4 text-sm text-gray-400">
                        <li><a href="about.html" class="footer-link">About Us</a></li>
                        <li><a href="process.html" class="footer-link">Our Mission</a></li>
                        <li><a href="portfolio.html" class="footer-link">Portfolio</a></li>
                        <li><a href="contact.html" class="footer-link">Contact Us</a></li>
                    </ul>'''
content = content.replace(old_footer_quick_links, new_footer_quick_links)

# 6. Replace SVGs
old_svg = '''<svg class="w-6 h-6" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <!-- Cup Body -->
                        <path d="M 25 35 L 35 85 C 36 90 40 92 45 92 L 55 92 C 60 92 64 90 65 85 L 75 35 Z" fill="url(#juiceGrad)" stroke="var(--color-accent)" stroke-width="4" stroke-linejoin="round"/>
                        <!-- Cup Lid -->
                        <path d="M 20 35 C 20 25 80 25 80 35 Z" fill="#ffffff" stroke="var(--color-accent)" stroke-width="4" stroke-linejoin="round"/>
                        <!-- Straw -->
                        <path d="M 50 25 L 50 10 L 65 10" stroke="var(--color-accent-light)" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
                        <!-- Fruit Slice -->
                        <circle cx="25" cy="45" r="12" fill="#FFA726" stroke="#ffffff" stroke-width="2"/>
                        <circle cx="25" cy="45" r="9" fill="none" stroke="#ffffff" stroke-width="1.5" stroke-dasharray="4 2"/>
                        <!-- Highlights -->
                        <path d="M 32 40 L 40 85" stroke="white" stroke-width="3" stroke-linecap="round" opacity="0.4"/>
                        <defs>
                            <linearGradient id="juiceGrad" x1="50" y1="90" x2="50" y2="35" gradientUnits="userSpaceOnUse">
                                <stop offset="0%" stop-color="#FF9800"/>
                                <stop offset="100%" stop-color="var(--color-accent)"/>
                            </linearGradient>
                        </defs>
                    </svg>'''

new_svg = '''<svg class="w-6 h-6" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <!-- Saw Blade Outline -->
                        <circle cx="50" cy="50" r="40" stroke="var(--color-accent)" stroke-width="6" stroke-dasharray="10 5" fill="none" stroke-linejoin="round" stroke-linecap="round" />
                        <!-- Inner details -->
                        <circle cx="50" cy="50" r="10" stroke="var(--color-accent-light)" stroke-width="4" fill="none" />
                        <!-- Tree inside -->
                        <path d="M50 25 L35 60 L45 60 L45 75 L55 75 L55 60 L65 60 Z" fill="var(--color-accent-light)" />
                    </svg>'''
content = content.replace(old_svg, new_svg)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates completed.")
