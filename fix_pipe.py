import re

# Read the file
with open(r'd:\NoMomICantPause\MegagrantDossier\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern 6: Pipe Operators - fixed pattern
pattern6 = r'(<div class="code-snippet" style="font-size: 0\.8rem;">)<span class="code-comment">// Fluent API\s+with pipe operator</span>\s+<span class="code-keyword">auto</span> DisplayHealth = Health\s+\| Clamp\(0\.0f, 100\.0f\)\s+\| Map\(\[\]\(<span class="code-keyword">float</span> h\) \{ <span\s+class="code-keyword">return</span> h / 100\.0f; \}\)\s+\| Smooth\(0\.1f\);\s+<span class="code-comment">// Filter \+ Debounce for input</span>\s+<span class="code-keyword">auto</span> SearchQuery = RawInput\s+\| Filter\(\[\]\(<span class="code-keyword">const</span> FString&amp; s\) \{\s+<span class="code-keyword">return</span> s\.Len\(\) >= 3;\s+\}\)\s+\| Debounce\(0\.3f\);\s+</div>'

replacement6 = r'''\1<span class="code-comment">// Fluent API with pipe operator</span>
<span class="code-keyword">auto</span> DisplayHealth = Health
    | Clamp(0.0f, 100.0f)
    | Map([](<span class="code-keyword">float</span> h) { <span class="code-keyword">return</span> h / 100.0f; })
    | Smooth(0.1f);

<span class="code-comment">// Filter + Debounce for input</span>
<span class="code-keyword">auto</span> SearchQuery = RawInput
    | Filter([](<span class="code-keyword">const</span> FString&amp; s) {
        <span class="code-keyword">return</span> s.Len() >= 3;
    })
    | Debounce(0.3f);</div>'''

content, count = re.subn(pattern6, replacement6, content, flags=re.DOTALL)
print(f"Snippet 6 (Pipe Operators): {count} replacements")

if count > 0:
    with open(r'd:\NoMomICantPause\MegagrantDossier\index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("File saved successfully")
else:
    print("Pattern not matched")
