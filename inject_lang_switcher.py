import re

# Read index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

print("Original length:", len(html))

# 1. Add CSS for Language Switcher
css_lang = """
    /* ==========================================================
       LANGUAGE SWITCHER COMPONENT (BANGLA / ENGLISH)
       ========================================================== */
    .lang-switcher {
      display: inline-flex;
      align-items: center;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-pill);
      padding: 2px;
      position: relative;
      user-select: none;
      backdrop-filter: blur(8px);
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }

    .lang-btn {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 0.3rem 0.65rem;
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--text-muted);
      border: none;
      background: transparent;
      border-radius: var(--radius-pill);
      cursor: pointer;
      transition: all var(--transition-fast);
      line-height: 1;
      white-space: nowrap;
    }

    .lang-btn:hover {
      color: var(--text-main);
    }

    .lang-btn.active {
      background: var(--accent-primary);
      color: #050806;
      box-shadow: 0 0 10px rgba(185, 243, 75, 0.4);
    }

    .lang-btn span.flag {
      font-size: 0.82rem;
      line-height: 1;
    }

    .mobile-lang-wrap {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.8rem 0;
      margin: 0.8rem 0;
      border-top: 1px solid var(--border-subtle);
      border-bottom: 1px solid var(--border-subtle);
    }
"""

html = html.replace("</style>", css_lang + "\n  </style>", 1)

# 2. Add Language Switcher to Desktop Header (.nav-actions)
desktop_switcher_html = """        <!-- Language Switcher Component (Bangla / English) -->
        <div class="lang-switcher" id="langSwitcherDesktop" role="group" aria-label="Language selector">
          <button type="button" class="lang-btn active" data-lang-btn="bn" onclick="setAppLanguage('bn')" aria-pressed="true" title="বাংলা ভাষা নির্বাচন করুন">
            <span class="flag">🇧🇩</span> বাং
          </button>
          <button type="button" class="lang-btn" data-lang-btn="en" onclick="setAppLanguage('en')" aria-pressed="false" title="Switch to English language">
            <span class="flag">🇬🇧</span> EN
          </button>
        </div>
"""

old_nav_actions = """      <div class="nav-actions">
        <button type="button" class="btn btn-primary btn-sm btn-pulsing-cta" id="navTryDemoBtn" onclick="handleBonusClaimAction(event)">বোনাস ক্লেইম করুন</button>"""

new_nav_actions = """      <div class="nav-actions">
""" + desktop_switcher_html + """        <button type="button" class="btn btn-primary btn-sm btn-pulsing-cta" id="navTryDemoBtn" onclick="handleBonusClaimAction(event)" data-i18n="nav_claim_btn">বোনাস ক্লেইম করুন</button>"""

assert old_nav_actions in html, "old_nav_actions not found"
html = html.replace(old_nav_actions, new_nav_actions, 1)

# 3. Add Language Switcher to Mobile Drawer Menu
old_mobile_btn = """      </ul>
      <button type="button" class="btn btn-primary" style="width: 100%; justify-content: center;" onclick="closeMobileMenu(); handleBonusClaimAction(event);">বোনাস ক্লেইম করুন</button>"""

new_mobile_btn = """      </ul>
      <!-- Mobile Language Switcher Row -->
      <div class="mobile-lang-wrap">
        <span style="font-size: 0.82rem; color: var(--text-muted); font-weight: 600;" data-i18n="mobile_lang_label">ভাষা / Language</span>
        <div class="lang-switcher" id="langSwitcherMobile" role="group" aria-label="Mobile language selector">
          <button type="button" class="lang-btn active" data-lang-btn="bn" onclick="setAppLanguage('bn')" aria-pressed="true">
            <span class="flag">🇧🇩</span> বাং
          </button>
          <button type="button" class="lang-btn" data-lang-btn="en" onclick="setAppLanguage('en')" aria-pressed="false">
            <span class="flag">🇬🇧</span> EN
          </button>
        </div>
      </div>
      <button type="button" class="btn btn-primary" style="width: 100%; justify-content: center;" onclick="closeMobileMenu(); handleBonusClaimAction(event);" data-i18n="nav_claim_btn">বোনাস ক্লেইম করুন</button>"""

assert old_mobile_btn in html, "old_mobile_btn not found"
html = html.replace(old_mobile_btn, new_mobile_btn, 1)

# 4. Add data-i18n attributes to navigation links
html = html.replace(
    '<li><a href="#dashboard" class="nav-link">ড্যাশবোর্ড</a></li>',
    '<li><a href="#dashboard" class="nav-link" data-i18n="nav_dashboard">ড্যাশবোর্ড</a></li>',
    1
)
html = html.replace(
    '<li><a href="#wheel" class="nav-link">বোনাস হুইল</a></li>',
    '<li><a href="#wheel" class="nav-link" data-i18n="nav_wheel">বোনাস হুইল</a></li>',
    1
)
html = html.replace(
    '<li><a href="#scratch-card" class="nav-link">স্ক্র্যাচ কার্ড</a></li>',
    '<li><a href="#scratch-card" class="nav-link" data-i18n="nav_scratch">স্ক্র্যাচ কার্ড</a></li>',
    1
)
html = html.replace(
    '<li><a href="#leaderboard" class="nav-link">লিডারবোর্ড</a></li>',
    '<li><a href="#leaderboard" class="nav-link" data-i18n="nav_leaderboard">লিডারবোর্ড</a></li>',
    1
)
html = html.replace(
    '<li><a href="#vip-tiers" class="nav-link">ভিআইপি টায়ার</a></li>',
    '<li><a href="#vip-tiers" class="nav-link" data-i18n="nav_vip">ভিআইপি টায়ার</a></li>',
    1
)
html = html.replace(
    '<li><a href="#how-it-works" class="nav-link">কীভাবে কাজ করে</a></li>',
    '<li><a href="#how-it-works" class="nav-link" data-i18n="nav_how">কীভাবে কাজ করে</a></li>',
    1
)
html = html.replace(
    '<li><a href="#faq" class="nav-link">FAQ</a></li>',
    '<li><a href="#faq" class="nav-link" data-i18n="nav_faq">FAQ</a></li>',
    1
)

# Header tagline
html = html.replace(
    '<span class="brand-tagline-sub">অফিসিয়াল রিওয়ার্ড প্ল্যাটফর্ম</span>',
    '<span class="brand-tagline-sub" data-i18n="brand_tagline">অফিসিয়াল রিওয়ার্ড প্ল্যাটফর্ম</span>',
    1
)

# SSL badge
html = html.replace(
    '<span class="ssl-headline"><span class="ssl-pulse-dot"></span>HTTPS 256-Bit SSL</span>',
    '<span class="ssl-headline"><span class="ssl-pulse-dot"></span><span data-i18n="ssl_title">HTTPS 256-Bit SSL</span></span>',
    1
)
html = html.replace(
    '<span class="ssl-sub">Verified Encrypted</span>',
    '<span class="ssl-sub" data-i18n="ssl_sub">Verified Encrypted</span>',
    1
)

# Ticker bar
html = html.replace(
    '<span>লাইভ ক্লেইম ফিড</span>',
    '<span data-i18n="ticker_badge">লাইভ ক্লেইম ফিড</span>',
    1
)
html = html.replace(
    '<span>আজকের ক্লেইম: <strong class="text-accent" id="todayClaimCount">৳৫,৮৪,২৫০</strong></span>',
    '<span><span data-i18n="today_claim_label">আজকের ক্লেইম:</span> <strong class="text-accent" id="todayClaimCount">৳৫,৮৪,২৫০</strong></span>',
    1
)

# Hero section
html = html.replace(
    '<span class="badge-live" style="margin-bottom: 1.2rem;">এক্সক্লুসিভ রিওয়ার্ড প্ল্যাটফর্ম</span>',
    '<span class="badge-live" style="margin-bottom: 1.2rem;" data-i18n="hero_badge">এক্সক্লুসিভ রিওয়ার্ড প্ল্যাটফর্ম</span>',
    1
)
html = html.replace(
    '<h1>\n            ওয়েলকাম বোনাস ও<br>\n            <span class="text-accent">প্রিমিয়াম রিওয়ার্ড</span>\n          </h1>',
    '<h1 data-i18n="hero_title">\n            ওয়েলকাম বোনাস ও<br>\n            <span class="text-accent">প্রিমিয়াম রিওয়ার্ড</span>\n          </h1>',
    1
)
html = html.replace(
    '<p class="hero-lead">\n            সেরা গেমিং রিওয়ার্ড, দৈনিক ক্যাশব্যাক এবং এক্সক্লুসিভ ভিআইপি সুবিধা উপভোগ করুন সরাসরি আপনার ড্যাশবোর্ড থেকে。\n          </p>',
    '<p class="hero-lead" data-i18n="hero_lead">\n            সেরা গেমিং রিওয়ার্ড, দৈনিক ক্যাশব্যাক এবং এক্সক্লুসিভ ভিআইপি সুবিধা উপভোগ করুন সরাসরি আপনার ড্যাশবোর্ড থেকে。\n          </p>',
    1
)

html = html.replace(
    '<span>বোনাস ক্লেইম করুন</span>\n              <svg width="18" height="18"',
    '<span data-i18n="hero_claim_btn">বোনাস ক্লেইম করুন</span>\n              <svg width="18" height="18"',
    1
)
html = html.replace(
    '<a href="#features" class="btn btn-secondary" id="heroExploreBtn">\n              ফিচার দেখুন\n            </a>',
    '<a href="#features" class="btn btn-secondary" id="heroExploreBtn" data-i18n="hero_explore_btn">\n              ফিচার দেখুন\n            </a>',
    1
)

# Write out progress check
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
with open("public/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Step 1 of language switcher injection complete!")
