import re

# Read the file
with open(r'd:\NoMomICantPause\MegagrantDossier\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

total_changes = 0

# Pattern 3: Traditional: Damage Calc
pattern3 = r'(<div class="code-snippet" style="font-size: 0\.7rem;">)<span class="code-comment">// Must\s+recalculate when ANY input changes</span>\s+<span class="code-keyword">void</span> RecalculateDamage\(\) \{\s+FinalDamage = \(BaseDamage \+ WeaponDamage\) \* Mult;\s+OnDamageChanged\.Broadcast\(FinalDamage\);\s+\}\s+<span class="code-comment">// Must call from every setter!</span>\s+<span class="code-keyword">void</span> SetBaseDamage\(<span class="code-keyword">float</span>\s+V\) \{\s+BaseDamage = V; RecalculateDamage\(\);\s+\}\s+<span class="code-keyword">void</span> SetWeaponDamage\(<span\s+class="code-keyword">float</span> V\) \{\s+WeaponDamage = V; RecalculateDamage\(\);\s+\}\s+<span class="code-keyword">void</span> SetMultiplier\(<span class="code-keyword">float</span>\s+V\) \{\s+Mult = V; RecalculateDamage\(\);\s+\}\s+</div>'

replacement3 = r'''\1<span class="code-comment">// Must recalculate when ANY input changes</span>
<span class="code-keyword">void</span> RecalculateDamage() {
    FinalDamage = (BaseDamage + WeaponDamage) * Mult;
    OnDamageChanged.Broadcast(FinalDamage);
}

<span class="code-comment">// Must call from every setter!</span>
<span class="code-keyword">void</span> SetBaseDamage(<span class="code-keyword">float</span> V) {
    BaseDamage = V; RecalculateDamage();
}
<span class="code-keyword">void</span> SetWeaponDamage(<span class="code-keyword">float</span> V) {
    WeaponDamage = V; RecalculateDamage();
}
<span class="code-keyword">void</span> SetMultiplier(<span class="code-keyword">float</span> V) {
    Mult = V; RecalculateDamage();
}</div>'''

content, count = re.subn(pattern3, replacement3, content, flags=re.DOTALL)
print(f"Snippet 3 (Damage Calc): {count} replacements")
total_changes += count

# Pattern 4: SignalFlow: Automatic
pattern4 = r'(<div class="code-snippet" style="font-size: 0\.8rem;">)<span class="code-comment">// Define\s+source\s+signals</span>\s+<span class="code-keyword">auto</span> BaseDamage = MakeSignal\(10\.0f\);\s+<span class="code-keyword">auto</span> WeaponDamage = MakeSignal\(25\.0f\);\s+<span class="code-keyword">auto</span> Multiplier = MakeSignal\(1\.5f\);\s+<span class="code-comment">// Computed signal - auto-updates!</span>\s+<span class="code-keyword">auto</span> FinalDamage =\s+\(BaseDamage \+ WeaponDamage\) \* Multiplier;\s+<span class="code-comment">// Change any input → auto update</span>\s+WeaponDamage\.SetValue\(50\.0f\);\s+</div>'

replacement4 = r'''\1<span class="code-comment">// Define source signals</span>
<span class="code-keyword">auto</span> BaseDamage = MakeSignal(10.0f);
<span class="code-keyword">auto</span> WeaponDamage = MakeSignal(25.0f);
<span class="code-keyword">auto</span> Multiplier = MakeSignal(1.5f);

<span class="code-comment">// Computed signal - auto-updates!</span>
<span class="code-keyword">auto</span> FinalDamage =
    (BaseDamage + WeaponDamage) * Multiplier;

<span class="code-comment">// Change any input → auto update</span>
WeaponDamage.SetValue(50.0f);</div>'''

content, count = re.subn(pattern4, replacement4, content, flags=re.DOTALL)
print(f"Snippet 4 (SignalFlow Automatic): {count} replacements")
total_changes += count

# Pattern 5: Computed with Lambda  
pattern5 = r'(<div class="code-snippet" style="font-size: 0\.8rem;">)<span class="code-comment">// Explicit\s+computed with lambda</span>\s+<span class="code-keyword">auto</span> HealthPercent = Computed\(\s+\[\]\(<span class="code-keyword">float</span> h\) \{ <span class="code-keyword">return</span>\s+h /\s+100\.0f; \},\s+Health\s+\);\s+<span class="code-comment">// Complex formula with multiple deps</span>\s+<span class="code-keyword">auto</span> DPS = Computed\(\s+\[\]\(<span class="code-keyword">float</span> dmg, <span class="code-keyword">float</span>\s+rate\) \{\s+<span class="code-keyword">return</span> dmg \* rate;\s+\},\s+BaseDamage, AttackSpeed\s+\);\s+</div>'

replacement5 = r'''\1<span class="code-comment">// Explicit computed with lambda</span>
<span class="code-keyword">auto</span> HealthPercent = Computed(
    [](<span class="code-keyword">float</span> h) { <span class="code-keyword">return</span> h / 100.0f; },
    Health
);

<span class="code-comment">// Complex formula with multiple deps</span>
<span class="code-keyword">auto</span> DPS = Computed(
    [](<span class="code-keyword">float</span> dmg, <span class="code-keyword">float</span> rate) {
        <span class="code-keyword">return</span> dmg * rate;
    },
    BaseDamage, AttackSpeed
);</div>'''

content, count = re.subn(pattern5, replacement5, content, flags=re.DOTALL)
print(f"Snippet 5 (Computed Lambda): {count} replacements")
total_changes += count

# Pattern 6: Pipe Operators
pattern6 = r'(<div class="code-snippet" style="font-size: 0\.8rem;">)<span class="code-comment">// Fluent\s+API\s+with pipe operator</span>\s+<span class="code-keyword">auto</span> DisplayHealth = Health\s+\| Clamp\(0\.0f, 100\.0f\)\s+\| Map\(\[\]\(<span class="code-keyword">float</span> h\) \{ <span\s+class="code-keyword">return</span> h / 100\.0f; \}\)\s+\| Smooth\(0\.1f\);\s+<span class="code-comment">// Filter \+ Debounce for input</span>\s+<span class="code-keyword">auto</span> SearchQuery = RawInput\s+\| Filter\(\[\]\(<span class="code-keyword">const</span> FString& s\) \{\s+<span class="code-keyword">return</span> s\.Len\(\) >= 3;\s+\}\)\s+\| Debounce\(0\.3f\);\s+</div>'

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
total_changes += count

# Write back if any changes
if total_changes > 0:
    with open(r'd:\NoMomICantPause\MegagrantDossier\index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nFile saved successfully with {total_changes} total replacements")
else:
    print("\nNo changes made - patterns not matched")
