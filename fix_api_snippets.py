import re

# Read the file
with open(r'd:\NoMomICantPause\MegagrantDossier\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

total_changes = 0

# Pattern 7: Core Signal API  
pattern7 = r'(<div class="code-snippet">)<span class="code-comment">// Create a mutable signal</span>\s+<span class="code-keyword">auto</span> Health = MakeSignal\(100\.0f\);\s+<span class="code-comment">// Read and write values</span>\s+<span class="code-keyword">float</span> hp = Health\.Value\(\);\s+Health\.SetValue\(75\.0f\); <span class="code-comment">// Propagates to observers</span>\s+<span class="code-comment">// Operator chaining creates computed signals</span>\s+<span class="code-keyword">auto</span> Damage = MakeSignal\(10\.0f\);\s+<span class="code-keyword">auto</span> EffectiveHP = Health - Damage;\s+</div>'

replacement7 = r'''\1<span class="code-comment">// Create a mutable signal</span>
<span class="code-keyword">auto</span> Health = MakeSignal(100.0f);

<span class="code-comment">// Read and write values</span>
<span class="code-keyword">float</span> hp = Health.Value();
Health.SetValue(75.0f); <span class="code-comment">// Propagates to observers</span>

<span class="code-comment">// Operator chaining creates computed signals</span>
<span class="code-keyword">auto</span> Damage = MakeSignal(10.0f);
<span class="code-keyword">auto</span> EffectiveHP = Health - Damage;</div>'''

content, count = re.subn(pattern7, replacement7, content, flags=re.DOTALL)
print(f"Snippet 7 (Core Signal API): {count} replacements")
total_changes += count

# Pattern 8: Network Replication
pattern8 = r'(<div class="code-snippet">)<span class="code-comment">// Create replicated signal - no\s+boilerplate!</span>\s+<span class="code-keyword">auto</span> Health = MakeSignal\(100\.0f, Key,\s+ESignalFlags::Replicated\);\s+<span class="code-comment">// Value syncs automatically to clients</span>\s+Health\.SetValue\(50\.0f\); <span class="code-comment">// ← Automatic replication</span>\s+<span class="code-comment">// Uses ASignalReplicationActor singleton</span>\s+<span class="code-comment">// \+ FFastArraySerializer for delta compression</span>\s+</div>'

replacement8 = r'''\1<span class="code-comment">// Create replicated signal - no boilerplate!</span>
<span class="code-keyword">auto</span> Health = MakeSignal(100.0f, Key,
    ESignalFlags::Replicated);

<span class="code-comment">// Value syncs automatically to clients</span>
Health.SetValue(50.0f); <span class="code-comment">// ← Automatic replication</span>

<span class="code-comment">// Uses ASignalReplicationActor singleton</span>
<span class="code-comment">// + FFastArraySerializer for delta compression</span></div>'''

content, count = re.subn(pattern8, replacement8, content, flags=re.DOTALL)
print(f"Snippet 8 (Network Replication): {count} replacements")
total_changes += count

# Pattern 9: AttributeFlow Effect System
pattern9 = r'(<div class="code-snippet">)<span class="code-comment">// Type-erased effect with builder\s+pattern</span>\s+FEffectSpec Poison = FEffectSpec::Periodic\(PoisonTag, 5\.0f, 1\.0f\)\s+\.WithAdditive&lt;<span class="code-keyword">float</span>&gt;\(TEXT\(<span\s+class="code-string">"Health"</span>\), -10\.0f\)\s+\.WithStackingPolicy\(EStackingPolicy::Aggregate, 5\);\s+<span class="code-comment">// Apply effect to SignalSet</span>\s+FGuid EffectID = EffectManager\.ApplyEffect\(SignalSet, Poison\);\s+</div>'

replacement9 = r'''\1<span class="code-comment">// Type-erased effect with builder pattern</span>
FEffectSpec Poison = FEffectSpec::Periodic(PoisonTag, 5.0f, 1.0f)
    .WithAdditive&lt;<span class="code-keyword">float</span>&gt;(TEXT(<span class="code-string">"Health"</span>), -10.0f)
    .WithStackingPolicy(EStackingPolicy::Aggregate, 5);

<span class="code-comment">// Apply effect to SignalSet</span>
FGuid EffectID = EffectManager.ApplyEffect(SignalSet, Poison);</div>'''

content, count = re.subn(pattern9, replacement9, content, flags=re.DOTALL)
print(f"Snippet 9 (AttributeFlow Effect): {count} replacements")
total_changes += count

# Pattern 10: Time-Based Operators
pattern10 = r'(<div class="code-snippet">)<span class="code-comment">// Smooth interpolation</span>\s+<span class="code-keyword">auto</span> SmoothHP = Health\.Smooth\(5\.0f\);\s+<span class="code-comment">// Rate limiting</span>\s+<span class="code-keyword">auto</span> ThrottledHP = Health\.Throttle\(0\.5f\);\s+<span class="code-comment">// Debounce and delay</span>\s+<span class="code-keyword">auto</span> StableHP = Health\.Debounce\(0\.3f\);\s+<span class="code-keyword">auto</span> DelayedHP = Health\.Delay\(1\.0f\);\s+</div>'

replacement10 = r'''\1<span class="code-comment">// Smooth interpolation</span>
<span class="code-keyword">auto</span> SmoothHP = Health.Smooth(5.0f);

<span class="code-comment">// Rate limiting</span>
<span class="code-keyword">auto</span> ThrottledHP = Health.Throttle(0.5f);

<span class="code-comment">// Debounce and delay</span>
<span class="code-keyword">auto</span> StableHP = Health.Debounce(0.3f);
<span class="code-keyword">auto</span> DelayedHP = Health.Delay(1.0f);</div>'''

content, count = re.subn(pattern10, replacement10, content, flags=re.DOTALL)
print(f"Snippet 10 (Time-Based Operators): {count} replacements")
total_changes += count

# Write back if any changes
if total_changes > 0:
    with open(r'd:\NoMomICantPause\MegagrantDossier\index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nFile saved successfully with {total_changes} total replacements")
else:
    print("\nNo changes made - patterns not matched")
