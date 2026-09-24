import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

replacements = [
    # Hero trust metrics
    ('<span class="metric-val" id="metricActiveUsers">১২,৮০০+</span>', '<span class="metric-val" id="metricActiveUsers" data-i18n="trust_metric_vip_val">১২,৮০০+</span>'),
    ('<span class="metric-label">সক্রিয় ভিআইপি মেম্বার</span>', '<span class="metric-label" data-i18n="trust_metric_vip_lbl">সক্রিয় ভিআইপি মেম্বার</span>'),
    ('<span class="metric-val">৩ মিনিট</span>', '<span class="metric-val" data-i18n="trust_metric_time_val">৩ মিনিট</span>'),
    ('<span class="metric-label">তাৎক্ষণিক ক্যাশআউট সময়</span>', '<span class="metric-label" data-i18n="trust_metric_time_lbl">তাৎক্ষণিক ক্যাশআউট সময়</span>'),
    ('<span class="metric-val">৳৫০ লাখ+</span>', '<span class="metric-val" data-i18n="trust_metric_fund_val">৳৫০ লাখ+</span>'),
    ('<span class="metric-label">দৈনিক রিওয়ার্ড তহবিল</span>', '<span class="metric-label" data-i18n="trust_metric_fund_lbl">দৈনিক রিওয়ার্ড তহবিল</span>'),

    # Dashboard section
    ('<span class="section-eyebrow">লাইভ অ্যানালিটিক্স</span>', '<span class="section-eyebrow" data-i18n="dash_eyebrow">লাইভ অ্যানালিটিক্স</span>'),
    ('<h2 class="section-title">আপনার রিওয়ার্ড ড্যাশবোর্ড</h2>', '<h2 class="section-title" data-i18n="dash_title">আপনার রিওয়ার্ড ড্যাশবোর্ড</h2>'),
    ('<p class="section-subtitle">ব্যালেন্স, চলমান স্ট্রিক এবং ক্লেইম হিস্ট্রি রিয়েল-টাইমে ট্র্যাক করুন।</p>', '<p class="section-subtitle" data-i18n="dash_lead">ব্যালেন্স, চলমান স্ট্রিক এবং ক্লেইম হিস্ট্রি রিয়েল-টাইমে ট্র্যাক করুন।</p>'),
    ('<div class="card-title-sm">মোট রিওয়ার্ড ব্যালেন্স</div>', '<div class="card-title-sm" data-i18n="card1_title">মোট রিওয়ার্ড ব্যালেন্স</div>'),
    ('<span>তাৎক্ষণিক ক্যাশআউট</span>', '<span data-i18n="card1_action">তাৎক্ষণিক ক্যাশআউট</span>'),
    ('<div class="card-title-sm">দৈনিক স্ট্রিক বোনাস</div>', '<div class="card-title-sm" data-i18n="card2_title">দৈনিক স্ট্রিক বোনাস</div>'),
    ('<span class="stat-pill" id="userStreakPill">৭ দিনের স্ট্রিক</span>', '<span class="stat-pill" id="userStreakPill" data-i18n="card2_badge">৭ দিনের স্ট্রিক</span>'),
    ('<div class="card-title-sm">আজকের ক্লেইম স্ট্যাটাস</div>', '<div class="card-title-sm" data-i18n="card3_title">আজকের ক্লেইম স্ট্যাটাস</div>'),
    ('<span class="badge-live" id="claimStatusBadge">সক্রিয় ও প্রস্তুত</span>', '<span class="badge-live" id="claimStatusBadge" data-i18n="card3_badge">সক্রিয় ও প্রস্তুত</span>'),
    ('<div class="card-title-sm">লাইভ রিওয়ার্ড ক্লেইম অ্যাক্টিভিটি</div>', '<div class="card-title-sm" data-i18n="card4_title">লাইভ রিওয়ার্ড ক্লেইম অ্যাক্টিভিটি</div>'),

    # Gamification section
    ('<span class="section-eyebrow">ইন্টারেক্টিভ গেমিফিকেশন রিওয়ার্ডস</span>', '<span class="section-eyebrow" data-i18n="game_eyebrow">ইন্টারেক্টিভ গেমিফিকেশন রিওয়ার্ডস</span>'),
    ('<h2 class="section-title">স্পিন হুইল ও স্ক্র্যাচ অ্যান্ড উইন</h2>', '<h2 class="section-title" data-i18n="game_title">স্পিন হুইল ও স্ক্র্যাচ অ্যান্ড উইন</h2>'),
    ('<p class="section-subtitle">\n            লাকি হুইল ঘুরিয়ে বা গোল্ডেন স্ক্র্যাচ কার্ড ঘষে সরাসরি ৳১,০০০ থেকে ৳৫০,০০০ পর্যন্ত ইনস্ট্যান্ট ক্যাশ রিওয়ার্ড আনলক করুন。\n          </p>', '<p class="section-subtitle" data-i18n="game_subtitle">\n            লাকি হুইল ঘুরিয়ে বা গোল্ডেন স্ক্র্যাচ কার্ড ঘষে সরাসরি ৳১,০০০ থেকে ৳৫০,০০০ পর্যন্ত ইনস্ট্যান্ট ক্যাশ রিওয়ার্ড আনলক করুন。\n          </p>'),
    ('<span>লাকি স্পিন হুইল (Spin Wheel)</span>', '<span data-i18n="tab_wheel">লাকি স্পিন হুইল (Spin Wheel)</span>'),
    ('<span>স্ক্র্যাচ অ্যান্ড উইন কার্ড (Scratch Card)</span>', '<span data-i18n="tab_scratch">স্ক্র্যাচ অ্যান্ড উইন কার্ড (Scratch Card)</span>'),

    # Wheel module
    ('<span class="badge-live">দৈনিক ফ্রি স্পিন সক্রিয়</span>', '<span class="badge-live" data-i18n="wheel_badge">দৈনিক ফ্রি স্পিন সক্রিয়</span>'),
    ('<h3 style="font-size: 1.6rem; margin: 0.5rem 0 0.2rem;">হুইল ঘুরিয়ে রিওয়ার্ড জিতুন</h3>', '<h3 style="font-size: 1.6rem; margin: 0.5rem 0 0.2rem;" data-i18n="wheel_h3">হুইল ঘুরিয়ে রিওয়ার্ড জিতুন</h3>'),
    ('<p class="text-muted" style="font-size: 0.9rem;">প্রতিটি সেগমেন্টে ৳১,০০০ থেকে ৳৫০,০০০ মেগা জ্যাকপট পর্যন্ত আকর্ষণীয় পুরস্কার সাজানো রয়েছে।</p>', '<p class="text-muted" style="font-size: 0.9rem;" data-i18n="wheel_p">প্রতিটি সেগমেন্টে ৳১,০০০ থেকে ৳৫০,০০০ মেগা জ্যাকপট পর্যন্ত আকর্ষণীয় পুরস্কার সাজানো রয়েছে।</p>'),
    ('<span class="card-title-sm">সর্বশেষ স্পিন ফলাফল</span>', '<span class="card-title-sm" data-i18n="wheel_last_res">সর্বশেষ স্পিন ফলাফল</span>'),
    ('<p class="wheel-disclaimer" style="color: var(--accent-primary); font-size: 0.8rem; margin-top: 0.4rem;">যাচাইকৃত ক্যাশ রিওয়ার্ড প্রস্তুত</p>', '<p class="wheel-disclaimer" style="color: var(--accent-primary); font-size: 0.8rem; margin-top: 0.4rem;" data-i18n="wheel_verified">যাচাইকৃত ক্যাশ রিওয়ার্ড প্রস্তুত</p>'),
    ('<span>Spin Now to Unlock (স্পিন করুন)</span>', '<span data-i18n="wheel_spin_cta">Spin Now to Unlock (স্পিন করুন)</span>'),
    ('<button type="button" class="btn btn-secondary" id="resetWheelBtn" onclick="resetWheel()">\n                আবার চেষ্টা করুন\n              </button>', '<button type="button" class="btn btn-secondary" id="resetWheelBtn" onclick="resetWheel()" data-i18n="wheel_reset">\n                আবার চেষ্টা করুন\n              </button>'),

    # Scratch module
    ('<span class="badge-live">গোল্ডেন স্ক্র্যাচ কার্ড</span>', '<span class="badge-live" data-i18n="scratch_badge">গোল্ডেন স্ক্র্যাচ কার্ড</span>'),
    ('<h3 style="font-size: 1.6rem; margin: 0.5rem 0 0.3rem;">ঘষুন এবং তাত্ক্ষণিক জিতুন</h3>', '<h3 style="font-size: 1.6rem; margin: 0.5rem 0 0.3rem;" data-i18n="scratch_h3">ঘষুন এবং তাত্ক্ষণিক জিতুন</h3>'),
    ('<p class="text-muted" style="font-size: 0.88rem; line-height: 1.6;">\n                  কার্ডের গোল্ডেন ফয়েলটি স্ক্র্যাচ করে ৫০% সম্পূর্ণ করলেই সম্পূর্ণ রিওয়ার্ড স্বয়ংক্রিয়ভাবে আনলক হয়ে যাবে。\n                </p>', '<p class="text-muted" style="font-size: 0.88rem; line-height: 1.6;" data-i18n="scratch_p">\n                  কার্ডের গোল্ডেন ফয়েলটি স্ক্র্যাচ করে ৫০% সম্পূর্ণ করলেই সম্পূর্ণ রিওয়ার্ড স্বয়ংক্রিয়ভাবে আনলক হয়ে যাবে。\n                </p>'),
    ('<div style="font-size: 0.75rem; color: #94A3B8; margin-bottom: 0.3rem; text-transform: uppercase; font-weight: 700;">সর্বোচ্চ সম্ভাব্য পুরস্কার</div>', '<div style="font-size: 0.75rem; color: #94A3B8; margin-bottom: 0.3rem; text-transform: uppercase; font-weight: 700;" data-i18n="scratch_max_label">সর্বোচ্চ সম্ভাব্য পুরস্কার</div>'),
    ('<div style="font-size: 1.4rem; font-weight: 800; color: #F5D061;">৳২৫,০০০ পর্যন্ত ইনস্ট্যান্ট বোনাস</div>', '<div style="font-size: 1.4rem; font-weight: 800; color: #F5D061;" data-i18n="scratch_max_val">৳২৫,০০০ পর্যন্ত ইনস্ট্যান্ট বোনাস</div>'),
    ('<div style="font-size: 0.72rem; color: var(--accent-primary); margin-top: 0.2rem;">✓ ১০০% নিশ্চিত পেআউট কোড</div>', '<div style="font-size: 0.72rem; color: var(--accent-primary); margin-top: 0.2rem;" data-i18n="scratch_payout_check">✓ ১০০% নিশ্চিত পেআউট কোড</div>'),
    ('<span>Claim Reward (রিওয়ার্ড ক্লেইম)</span>', '<span data-i18n="scratch_claim_cta">Claim Reward (রিওয়ার্ড ক্লেইম)</span>'),
    ('<button type="button" class="btn btn-secondary" style="flex: 1; font-size: 0.82rem;" onclick="autoRevealScratchCard()">\n                    স্বয়ংক্রিয় স্ক্র্যাচ\n                  </button>', '<button type="button" class="btn btn-secondary" style="flex: 1; font-size: 0.82rem;" onclick="autoRevealScratchCard()" data-i18n="scratch_auto_btn">\n                    স্বয়ংক্রিয় স্ক্র্যাচ\n                  </button>'),
    ('<button type="button" class="btn btn-secondary" style="flex: 1; font-size: 0.82rem;" onclick="resetScratchCard()">\n                    নতুন কার্ড নিন\n                  </button>', '<button type="button" class="btn btn-secondary" style="flex: 1; font-size: 0.82rem;" onclick="resetScratchCard()" data-i18n="scratch_new_btn">\n                    নতুন কার্ড নিন\n                  </button>'),

    # Features
    ('<span class="section-eyebrow">প্রিমিয়াম প্ল্যাটফর্ম</span>', '<span class="section-eyebrow" data-i18n="features_eyebrow">প্রিমিয়াম প্ল্যাটফর্ম</span>'),
    ('<h2 class="section-title">প্ল্যাটফর্মের প্রধান সুবিধাসমূহ</h2>', '<h2 class="section-title" data-i18n="features_title">প্ল্যাটফর্মের প্রধান সুবিধাসমূহ</h2>'),
    ('<p class="section-subtitle">আধুনিক গেমিং এবং প্রিমিয়াম রিওয়ার্ড সিস্টেমের অতুলনীয় সুবিধা।</p>', '<p class="section-subtitle" data-i18n="features_subtitle">আধুনিক গেমিং এবং প্রিমিয়াম রিওয়ার্ড সিস্টেমের অতুলনীয় সুবিধা।</p>'),
    ('<h3>অ্যানিমেটেড রিওয়ার্ড</h3>', '<h3 data-i18n="feat1_title">অ্যানিমেটেড রিওয়ার্ড</h3>'),
    ('<p>হুইল স্পিন ও স্ক্র্যাচ কার্ডের মাধ্যমে রিয়েল-টাইম বোনাস উপভোগ করুন।</p>', '<p data-i18n="feat1_desc">হুইল স্পিন ও স্ক্র্যাচ কার্ডের মাধ্যমে রিয়েল-টাইম বোনাস উপভোগ করুন।</p>'),
    ('<h3>প্রিমিয়াম ড্যাশবোর্ড</h3>', '<h3 data-i18n="feat2_title">প্রিমিয়াম ড্যাশবোর্ড</h3>'),
    ('<p>ব্যালেন্স, প্রগ্রেস ও হিস্ট্রি একসাথে এক নজরে নিরীক্ষণ করুন।</p>', '<p data-i18n="feat2_desc">ব্যালেন্স, প্রগ্রেস ও হিস্ট্রি একসাথে এক নজরে নিরীক্ষণ করুন।</p>'),
    ('<h3>লাইভ লিডারবোর্ড</h3>', '<h3 data-i18n="feat3_title">লাইভ লিডারবোর্ড</h3>'),
    ('<p>শীর্ষ পারফরমারদের র‍্যাঙ্কিং ও দৈনিক স্কোর স্বয়ংক্রিয়ভাবে আপডেট হয়।</p>', '<p data-i18n="feat3_desc">শীর্ষ পারফরমারদের র‍্যাঙ্কিং ও দৈনিক স্কোর স্বয়ংক্রিয়ভাবে আপডেট হয়।</p>'),
    ('<h3>মোবাইল এক্সপেরিয়েন্স</h3>', '<h3 data-i18n="feat4_title">মোবাইল এক্সপেরিয়েন্স</h3>'),
    ('<p>স্মার্টফোন, ট্যাবলেট ও ডেস্কটপে সমান মসৃণ ও দ্রুতগতি সম্পন্ন ইন্টারফেস।</p>', '<p data-i18n="feat4_desc">স্মার্টফোন, ট্যাবলেট ও ডেস্কটপে সমান মসৃণ ও দ্রুতগতি সম্পন্ন ইন্টারফেস।</p>'),
    ('<h3>সুরক্ষিত এনক্রিপশন</h3>', '<h3 data-i18n="feat5_title">সুরক্ষিত এনক্রিপশন</h3>'),
    ('<p>মিলিটারি-গ্রেড 256-Bit SSL এনক্রিপশন দ্বারা আপনার অ্যাকাউন্ট তথ্য সম্পূর্ণ নিরাপদ।</p>', '<p data-i18n="feat5_desc">মিলিটারি-গ্রেড 256-Bit SSL এনক্রিপশন দ্বারা আপনার অ্যাকাউন্ট তথ্য সম্পূর্ণ নিরাপদ।</p>'),
    ('<h3>২৪/৭ লাইভ সাপোর্ট</h3>', '<h3 data-i18n="feat6_title">২৪/৭ লাইভ সাপোর্ট</h3>'),
    ('<p>যেকোনো অনুসন্ধানে সার্বক্ষণিক বন্ধুত্বপূর্ণ সহায়তা ও লাইভ চ্যাট সমাধান।</p>', '<p data-i18n="feat6_desc">যেকোনো অনুসন্ধানে সার্বক্ষণিক বন্ধুত্বপূর্ণ সহায়তা ও লাইভ চ্যাট সমাধান।</p>'),

    # VIP Tiers
    ('<span class="section-eyebrow">ভিআইপি প্রিভিলেজ ক্লাব</span>', '<span class="section-eyebrow" data-i18n="vip_eyebrow">ভিআইপি প্রিভিলেজ ক্লাব</span>'),
    ('<h2 class="section-title">ভিআইপি মেম্বারশিপ টায়ার ও সুবিধা</h2>', '<h2 class="section-title" data-i18n="vip_title">ভিআইপি মেম্বারশিপ টায়ার ও সুবিধা</h2>'),
    ('<p class="section-subtitle">প্রতিটি লেভেলে উচ্চতর ক্যাশব্যাক রিবেট, এক্সক্লুসিভ টুর্নামেন্ট অ্যাক্সেস এবং ব্যক্তিগত কনসিয়ার্জ উপভোগ করুন।</p>', '<p class="section-subtitle" data-i18n="vip_subtitle">প্রতিটি লেভেলে উচ্চতর ক্যাশব্যাক রিবেট, এক্সক্লুসিভ টুর্নামেন্ট অ্যাক্সেস এবং ব্যক্তিগত কনসিয়ার্জ উপভোগ করুন।</p>'),

    # How it works
    ('<span class="section-eyebrow">সহজ গাইডলাইন</span>', '<span class="section-eyebrow" data-i18n="how_eyebrow">সহজ গাইডলাইন</span>'),
    ('<h2 class="section-title">কীভাবে রিওয়ার্ড ক্লেইম করবেন</h2>', '<h2 class="section-title" data-i18n="how_title">কীভাবে রিওয়ার্ড ক্লেইম করবেন</h2>'),
    ('<p class="section-subtitle">মাত্র ৩টি সহজ ধাপে আপনার বোনাস ওয়ালেটে গ্রহণ করুন।</p>', '<p class="section-subtitle" data-i18n="how_subtitle">মাত্র ৩টি সহজ ধাপে আপনার বোনাস ওয়ালেটে গ্রহণ করুন।</p>'),

    # Leaderboard
    ('<span class="section-eyebrow">সেরা পারফরমার</span>', '<span class="section-eyebrow" data-i18n="lb_eyebrow">সেরা পারফরমার</span>'),
    ('<h2 class="section-title">সর্বোচ্চ বিজয়ী লিডারবোর্ড</h2>', '<h2 class="section-title" data-i18n="lb_title">সর্বোচ্চ বিজয়ী লিডারবোর্ড</h2>'),
    ('<p class="section-subtitle">প্ল্যাটফর্মের শীর্ষ সফল খেলোয়াড় ও রিওয়ার্ড অর্জনকারীদের তালিকা।</p>', '<p class="section-subtitle" data-i18n="lb_subtitle">প্ল্যাটফর্মের শীর্ষ সফল খেলোয়াড় ও রিওয়ার্ড অর্জনকারীদের তালিকা।</p>'),
    ('<button type="button" class="btn btn-sm btn-secondary active" id="filterAllTimeBtn" onclick="switchLeaderboardFilter(\'allTime\')">সর্বকালের সেরা</button>', '<button type="button" class="btn btn-sm btn-secondary active" id="filterAllTimeBtn" onclick="switchLeaderboardFilter(\'allTime\')" data-i18n="lb_filter_all">সর্বকালের সেরা</button>'),
    ('<button type="button" class="btn btn-sm btn-secondary" id="filterTodayBtn" onclick="switchLeaderboardFilter(\'today\')">আজকের সেরা</button>', '<button type="button" class="btn btn-sm btn-secondary" id="filterTodayBtn" onclick="switchLeaderboardFilter(\'today\')" data-i18n="lb_filter_today">আজকের সেরা</button>'),

    # FAQ
    ('<span class="section-eyebrow">প্রশ্নোত্তর</span>', '<span class="section-eyebrow" data-i18n="faq_eyebrow">প্রশ্নোত্তর</span>'),
    ('<h2 class="section-title">সচরাচর জিজ্ঞাসিত প্রশ্নাবলী (FAQ)</h2>', '<h2 class="section-title" data-i18n="faq_title">সচরাচর জিজ্ঞাসিত প্রশ্নাবলী (FAQ)</h2>'),
    ('<p class="section-subtitle">প্ল্যাটফর্ম সম্পর্কে প্রয়োজনীয় তথ্যাবলী ও সাধারণ জিজ্ঞাসা।</p>', '<p class="section-subtitle" data-i18n="faq_subtitle">প্ল্যাটফর্ম সম্পর্কে প্রয়োজনীয় তথ্যাবলী ও সাধারণ জিজ্ঞাসা।</p>'),

    # Footer
    ('<p>অফিসিয়াল প্রিমিয়াম বোনাস ও ইনস্ট্যান্ট রিওয়ার্ড প্ল্যাটফর্ম।</p>', '<p data-i18n="footer_brand_desc">অফিসিয়াল প্রিমিয়াম বোনাস ও ইনস্ট্যান্ট রিওয়ার্ড প্ল্যাটফর্ম।</p>'),
    ('<button type="button" class="footer-link-btn" onclick="openLegalModal(\'privacy\')">Privacy Policy (গোপনীয়তা নীতি)</button>', '<button type="button" class="footer-link-btn" onclick="openLegalModal(\'privacy\')" data-i18n="footer_privacy">Privacy Policy (গোপনীয়তা নীতি)</button>'),
    ('<button type="button" class="footer-link-btn" onclick="openLegalModal(\'terms\')">Terms of Service (ব্যবহারের শর্তাবলী)</button>', '<button type="button" class="footer-link-btn" onclick="openLegalModal(\'terms\')" data-i18n="footer_terms">Terms of Service (ব্যবহারের শর্তাবলী)</button>'),
    ('<button type="button" class="footer-link-btn" onclick="openLegalModal(\'disclaimer\')">Disclaimer (দাবিত্যাগ)</button>', '<button type="button" class="footer-link-btn" onclick="openLegalModal(\'disclaimer\')" data-i18n="footer_disclaimer">Disclaimer (দাবিত্যাগ)</button>'),
    ('<button type="button" class="footer-link-btn" onclick="openLegalModal(\'support\')">Contact Support (২৪/৭ সহায়তা কেন্দ্র)</button>', '<button type="button" class="footer-link-btn" onclick="openLegalModal(\'support\')" data-i18n="footer_support">Contact Support (২৪/৭ সহায়তা কেন্দ্র)</button>'),
    ('<div>© 2026 ClaimBonus24. All rights reserved.</div>', '<div data-i18n="footer_copy">© 2026 ClaimBonus24. All rights reserved.</div>'),
    ('<div>এনক্রিপ্টেড সিকিউরিটি ও ২৪/৭ নির্ভরযোগ্য কাস্টমার সাপোর্ট দ্বারা সুরক্ষিত।</div>', '<div data-i18n="footer_security_desc">এনক্রিপ্টেড সিকিউরিটি ও ২৪/৭ নির্ভরযোগ্য কাস্টমার সাপোর্ট দ্বারা সুরক্ষিত।</div>'),

    # Claim modal
    ('<span>ধাপ ১ / ৩: একাউন্ট ভেরিফিকেশন</span>', '<span data-i18n="modal_step1_progress">ধাপ ১ / ৩: একাউন্ট ভেরিফিকেশন</span>'),
    ('<h3 class="modal-title" id="modalTitle">আপনার অ্যাকাউন্ট ভেরিফাই করুন</h3>', '<h3 class="modal-title" id="modalTitle" data-i18n="modal_step1_title">আপনার অ্যাকাউন্ট ভেরিফাই করুন</h3>'),
    ('<p class="modal-desc">\n          যে ওয়ালেট বা অ্যাকাউন্টে ক্যাশ বোনাস গ্রহণ করতে চান তার বিবরণ প্রদান করুন。\n        </p>', '<p class="modal-desc" data-i18n="modal_step1_desc">\n          যে ওয়ালেট বা অ্যাকাউন্টে ক্যাশ বোনাস গ্রহণ করতে চান তার বিবরণ প্রদান করুন。\n        </p>'),
    ('<div class="method-pill active" id="methodPillPhone" onclick="selectClaimMethod(\'phone\')">📱 বিকাশ / নগদ / রকেট</div>', '<div class="method-pill active" id="methodPillPhone" onclick="selectClaimMethod(\'phone\')" data-i18n="modal_method_phone">📱 বিকাশ / নগদ / রকেট</div>'),
    ('<div class="method-pill" id="methodPillId" onclick="selectClaimMethod(\'id\')">🆔 প্লেয়ার আইডি / ইমেইল</div>', '<div class="method-pill" id="methodPillId" onclick="selectClaimMethod(\'id\')" data-i18n="modal_method_id">🆔 প্লেয়ার আইডি / ইমেইল</div>'),
    ('<span>256-Bit SSL এনক্রিপশনের মাধ্যমে সম্পূর্ণ নিরাপদে সংরক্ষিত</span>', '<span data-i18n="modal_ssl_guarantee">256-Bit SSL এনক্রিপশনের মাধ্যমে সম্পূর্ণ নিরাপদে সংরক্ষিত</span>'),
    ('<span>পরবর্তী ধাপ: টাস্ক সম্পন্ন করুন</span>', '<span data-i18n="modal_step1_next_btn">পরবর্তী ধাপ: টাস্ক সম্পন্ন করুন</span>'),
    ('<span>ধাপ ২ / ৩: রিওয়ার্ড আনলক টাস্ক</span>', '<span data-i18n="modal_step2_progress">ধাপ ২ / ৩: রিওয়ার্ড আনলক টাস্ক</span>'),
    ('<h3 class="modal-title">একটি সহজ টাস্ক সম্পন্ন করুন</h3>', '<h3 class="modal-title" data-i18n="modal_step2_title">একটি সহজ টাস্ক সম্পন্ন করুন</h3>'),
    ('<p class="modal-desc">\n          নিচের যেকোনো ১টি ইন্টারেক্টিভ টাস্ক সম্পন্ন করে তাত্ক্ষণিকভাবে ১০০% রিওয়ার্ড আনলক করুন:\n        </p>', '<p class="modal-desc" data-i18n="modal_step2_desc">\n          নিচের যেকোনো ১টি ইন্টারেক্টিভ টাস্ক সম্পন্ন করে তাত্ক্ষণিকভাবে ১০০% রিওয়ার্ড আনলক করুন:\n        </p>'),
    ('<span>ধাপ ৩ / ৩: রিওয়ার্ড প্রস্তুত</span>', '<span data-i18n="modal_step3_progress">ধাপ ৩ / ৩: রিওয়ার্ড প্রস্তুত</span>'),
    ('<span class="badge-live" style="margin-bottom: 0.6rem;">🎉 বোনাস সফলভাবে নির্ধারিত</span>', '<span class="badge-live" style="margin-bottom: 0.6rem;" data-i18n="modal_step3_badge">🎉 বোনাস সফলভাবে নির্ধারিত</span>'),
    ('<h3 class="modal-title">অভিনন্দন! আপনার রিওয়ার্ড প্রস্তুত</h3>', '<h3 class="modal-title" data-i18n="modal_step3_title">অভিনন্দন! আপনার রিওয়ার্ড প্রস্তুত</h3>'),
    ('<div class="card-title-sm">হিসাবকৃত চূড়ান্ত ক্যাশ বোনাস</div>', '<div class="card-title-sm" data-i18n="modal_step3_calc_title">হিসাবকৃত চূড়ান্ত ক্যাশ বোনাস</div>'),
    ('<span style="color: #94A3B8;">প্রাপক ওয়ালেট:</span>', '<span style="color: #94A3B8;" data-i18n="modal_step3_recipient_lbl">প্রাপক ওয়ালেট:</span>'),
    ('<span style="color: #94A3B8;">ট্রানজেকশন টাইপ:</span>', '<span style="color: #94A3B8;" data-i18n="modal_step3_type_lbl">ট্রানজেকশন টাইপ:</span>'),
    ('<span style="color: #4ADE80; font-weight: 700;">ইনস্ট্যান্ট ক্যাশ ক্রেডিট</span>', '<span style="color: #4ADE80; font-weight: 700;" data-i18n="modal_step3_type_val">ইনস্ট্যান্ট ক্যাশ ক্রেডিট</span>'),
    ('<span style="color: #94A3B8;">অফার মেয়াদ বাকি:</span>', '<span style="color: #94A3B8;" data-i18n="modal_step3_expiry_lbl">অফার মেয়াদ বাকি:</span>'),
    ('<span>ওয়ালেটে ট্রান্সফার করুন (Claim to Wallet)</span>', '<span data-i18n="modal_claim_to_wallet_btn">ওয়ালেটে ট্রান্সফার করুন (Claim to Wallet)</span>')
]

count = 0
for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)
        count += 1
    else:
        print("Notice: target not matched:", old[:40])

print(f"Applied {count} out of {len(replacements)} data-i18n annotations.")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
with open("public/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("data-i18n annotations saved successfully!")
