import re

with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_faq = '''            <!-- FAQ Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto">
                <div class="bg-background border border-border p-8 rounded-2xl shadow-sm">
                    <h3 class="text-primary-text font-serif font-bold text-xl mb-3"><i class="fas fa-clock text-accent mr-2 text-sm"></i> What is your typical lead time?</h3>
                    <p class="text-secondary-text text-sm leading-relaxed">Most custom dining and conference tables take between 8 to 12 weeks from the day the design is finalized and the deposit is placed. Complex resin pours may require additional curing time.</p>
                </div>
                
                <div class="bg-background border border-border p-8 rounded-2xl shadow-sm">
                    <h3 class="text-primary-text font-serif font-bold text-xl mb-3"><i class="fas fa-truck text-accent mr-2 text-sm"></i> Do you offer delivery and installation?</h3>
                    <p class="text-secondary-text text-sm leading-relaxed">Yes. We offer white-glove delivery and installation across the contiguous United States. Our team ensures heavy pieces are properly assembled and leveled in your space.</p>
                </div>
                
                <div class="bg-background border border-border p-8 rounded-2xl shadow-sm">
                    <h3 class="text-primary-text font-serif font-bold text-xl mb-3"><i class="fas fa-money-bill text-accent mr-2 text-sm"></i> What are your payment terms?</h3>
                    <p class="text-secondary-text text-sm leading-relaxed">We require a 50% non-refundable deposit to secure your slab and begin production. The remaining 50% balance is due prior to shipping or upon final installation.</p>
                </div>
                
                <div class="bg-background border border-border p-8 rounded-2xl shadow-sm">
                    <h3 class="text-primary-text font-serif font-bold text-xl mb-3"><i class="fas fa-tree text-accent mr-2 text-sm"></i> Can I supply my own wood?</h3>
                    <p class="text-secondary-text text-sm leading-relaxed">We typically prefer to use our own kiln-dried inventory to guarantee quality. However, if you have a sentimental tree that has been professionally milled and kiln-dried, we can evaluate it for a project.</p>
                </div>
            </div>'''

new_faq = '''            <!-- FAQ Accordion -->
            <div class="max-w-3xl mx-auto space-y-4">
                
                <details class="group bg-background border border-border rounded-2xl shadow-sm [&_summary::-webkit-details-marker]:hidden">
                    <summary class="flex cursor-pointer items-center justify-between p-6 md:p-8 text-primary-text font-serif font-bold text-xl transition-colors duration-300">
                        <span class="flex items-center gap-3"><i class="fas fa-clock text-accent text-sm"></i> What is your typical lead time?</span>
                        <span class="relative ml-1.5 h-5 w-5 flex-shrink-0 text-accent">
                            <svg xmlns="http://www.w3.org/2000/svg" class="absolute inset-0 h-5 w-5 opacity-100 group-open:opacity-0 transition-opacity" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" /></svg>
                            <svg xmlns="http://www.w3.org/2000/svg" class="absolute inset-0 h-5 w-5 opacity-0 group-open:opacity-100 transition-opacity" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M20 12H4" /></svg>
                        </span>
                    </summary>
                    <div class="px-6 md:px-8 pb-6 md:pb-8 pt-0 text-secondary-text text-sm leading-relaxed border-t border-border mt-2 pt-6">
                        <p>Most custom dining and conference tables take between 8 to 12 weeks from the day the design is finalized and the deposit is placed. Complex resin pours may require additional curing time.</p>
                    </div>
                </details>

                <details class="group bg-background border border-border rounded-2xl shadow-sm [&_summary::-webkit-details-marker]:hidden">
                    <summary class="flex cursor-pointer items-center justify-between p-6 md:p-8 text-primary-text font-serif font-bold text-xl transition-colors duration-300">
                        <span class="flex items-center gap-3"><i class="fas fa-truck text-accent text-sm"></i> Do you offer delivery and installation?</span>
                        <span class="relative ml-1.5 h-5 w-5 flex-shrink-0 text-accent">
                            <svg xmlns="http://www.w3.org/2000/svg" class="absolute inset-0 h-5 w-5 opacity-100 group-open:opacity-0 transition-opacity" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" /></svg>
                            <svg xmlns="http://www.w3.org/2000/svg" class="absolute inset-0 h-5 w-5 opacity-0 group-open:opacity-100 transition-opacity" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M20 12H4" /></svg>
                        </span>
                    </summary>
                    <div class="px-6 md:px-8 pb-6 md:pb-8 pt-0 text-secondary-text text-sm leading-relaxed border-t border-border mt-2 pt-6">
                        <p>Yes. We offer white-glove delivery and installation across the contiguous United States. Our team ensures heavy pieces are properly assembled and leveled in your space.</p>
                    </div>
                </details>

                <details class="group bg-background border border-border rounded-2xl shadow-sm [&_summary::-webkit-details-marker]:hidden">
                    <summary class="flex cursor-pointer items-center justify-between p-6 md:p-8 text-primary-text font-serif font-bold text-xl transition-colors duration-300">
                        <span class="flex items-center gap-3"><i class="fas fa-money-bill text-accent text-sm"></i> What are your payment terms?</span>
                        <span class="relative ml-1.5 h-5 w-5 flex-shrink-0 text-accent">
                            <svg xmlns="http://www.w3.org/2000/svg" class="absolute inset-0 h-5 w-5 opacity-100 group-open:opacity-0 transition-opacity" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" /></svg>
                            <svg xmlns="http://www.w3.org/2000/svg" class="absolute inset-0 h-5 w-5 opacity-0 group-open:opacity-100 transition-opacity" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M20 12H4" /></svg>
                        </span>
                    </summary>
                    <div class="px-6 md:px-8 pb-6 md:pb-8 pt-0 text-secondary-text text-sm leading-relaxed border-t border-border mt-2 pt-6">
                        <p>We require a 50% non-refundable deposit to secure your slab and begin production. The remaining 50% balance is due prior to shipping or upon final installation.</p>
                    </div>
                </details>

                <details class="group bg-background border border-border rounded-2xl shadow-sm [&_summary::-webkit-details-marker]:hidden">
                    <summary class="flex cursor-pointer items-center justify-between p-6 md:p-8 text-primary-text font-serif font-bold text-xl transition-colors duration-300">
                        <span class="flex items-center gap-3"><i class="fas fa-tree text-accent text-sm"></i> Can I supply my own wood?</span>
                        <span class="relative ml-1.5 h-5 w-5 flex-shrink-0 text-accent">
                            <svg xmlns="http://www.w3.org/2000/svg" class="absolute inset-0 h-5 w-5 opacity-100 group-open:opacity-0 transition-opacity" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" /></svg>
                            <svg xmlns="http://www.w3.org/2000/svg" class="absolute inset-0 h-5 w-5 opacity-0 group-open:opacity-100 transition-opacity" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M20 12H4" /></svg>
                        </span>
                    </summary>
                    <div class="px-6 md:px-8 pb-6 md:pb-8 pt-0 text-secondary-text text-sm leading-relaxed border-t border-border mt-2 pt-6">
                        <p>We typically prefer to use our own kiln-dried inventory to guarantee quality. However, if you have a sentimental tree that has been professionally milled and kiln-dried, we can evaluate it for a project.</p>
                    </div>
                </details>
            </div>'''

if old_faq in content:
    content = content.replace(old_faq, new_faq)
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("FAQ updated to accordion format.")
else:
    print("Could not find old FAQ block to replace.")

