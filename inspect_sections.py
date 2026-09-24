import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Let's inspect How It Works section content
pos_how = content.find("id=\"how-it-works\"")
print("How it works section:")
print(content[pos_how:pos_how+1200])

# Let's inspect VIP Tiers section content
pos_vip = content.find("id=\"vip-tiers\"")
print("\nVIP Tiers section:")
print(content[pos_vip:pos_vip+1200])

# Let's inspect FAQ section content
pos_faq = content.find("id=\"faq\"")
print("\nFAQ section:")
print(content[pos_faq:pos_faq+1200])
