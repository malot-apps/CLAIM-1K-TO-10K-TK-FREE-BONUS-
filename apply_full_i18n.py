import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's write the complete i18n JavaScript engine and dictionary
i18n_script = """
    /* ==========================================================
       FULL APPLICATION MULTILINGUAL I18N ENGINE (BANGLA / ENGLISH)
       ========================================================== */
    const I18N_DICTIONARY = {
      bn: {
        // Brand & Nav
        brand_tagline: "অফিসিয়াল রিওয়ার্ড প্ল্যাটফর্ম",
        ssl_title: "HTTPS 256-Bit SSL",
        ssl_sub: "Verified Encrypted",
        nav_dashboard: "ড্যাশবোর্ড",
        nav_wheel: "বোনাস হুইল",
        nav_scratch: "স্ক্র্যাচ কার্ড",
        nav_leaderboard: "লিডারবোর্ড",
        nav_vip: "ভিআইপি টায়ার",
        nav_how: "কীভাবে কাজ করে",
        nav_faq: "FAQ",
        nav_claim_btn: "বোনাস ক্লেইম করুন",
        mobile_lang_label: "ভাষা / Language",

        // Ticker
        ticker_badge: "লাইভ ক্লেইম ফিড",
        today_claim_label: "আজকের ক্লেইম:",

        // Hero
        hero_badge: "এক্সক্লুসিভ রিওয়ার্ড প্ল্যাটফর্ম",
        hero_title: "ওয়েলকাম বোনাস ও<br><span class=\\"text-accent\\">প্রিমিয়াম রিওয়ার্ড</span>",
        hero_lead: "সেরা গেমিং রিওয়ার্ড, দৈনিক ক্যাশব্যাক এবং এক্সক্লুসিভ ভিআইপি সুবিধা উপভোগ করুন সরাসরি আপনার ড্যাশবোর্ড থেকে।",
        hero_claim_btn: "বোনাস ক্লেইম করুন",
        hero_explore_btn: "ফিচার দেখুন",
        trust_metric_vip_val: "১২,৮০০+",
        trust_metric_vip_lbl: "সক্রিয় ভিআইপি মেম্বার",
        trust_metric_time_val: "৩ মিনিট",
        trust_metric_time_lbl: "তাৎক্ষণিক ক্যাশআউট সময়",
        trust_metric_fund_val: "৳৫০ লাখ+",
        trust_metric_fund_lbl: "দৈনিক রিওয়ার্ড তহবিল",

        // Dashboard
        dash_eyebrow: "লাইভ অ্যানালিটিক্স",
        dash_title: "আপনার রিওয়ার্ড ড্যাশবোর্ড",
        dash_lead: "ব্যালেন্স, চলমান স্ট্রিক এবং ক্লেইম হিস্ট্রি রিয়েল-টাইমে ট্র্যাক করুন।",
        card1_title: "মোট রিওয়ার্ড ব্যালেন্স",
        card1_action: "তাৎক্ষণিক ক্যাশআউট",
        card2_title: "দৈনিক স্ট্রিক বোনাস",
        card2_badge: "৭ দিনের স্ট্রিক",
        card2_desc: "প্রতিদিন লগইন করে আরও ৫০০ পয়েন্ট আনলক করুন।",
        card2_progress_label: "পরবর্তী বোনাস লেভেল",
        card3_title: "আজকের ক্লেইম স্ট্যাটাস",
        card3_badge: "সক্রিয় ও প্রস্তুত",
        card3_desc: "আপনার দৈনিক স্পিন এবং স্ক্র্যাচ রিওয়ার্ড প্রস্তুত।",
        card3_action: "রিওয়ার্ড ক্লেইম করুন",
        card4_title: "লাইভ রিওয়ার্ড ক্লেইম অ্যাক্টিভিটি",

        // Gamification
        game_eyebrow: "ইন্টারেক্টিভ গেমিফিকেশন রিওয়ার্ডস",
        game_title: "স্পিন হুইল ও স্ক্র্যাচ অ্যান্ড উইন",
        game_subtitle: "লাকি হুইল ঘুরিয়ে বা গোল্ডেন স্ক্র্যাচ কার্ড ঘষে সরাসরি ৳১,০০০ থেকে ৳৫০,০০০ পর্যন্ত ইনস্ট্যান্ট ক্যাশ রিওয়ার্ড আনলক করুন।",
        tab_wheel: "লাকি স্পিন হুইল (Spin Wheel)",
        tab_scratch: "স্ক্র্যাচ অ্যান্ড উইন কার্ড (Scratch Card)",

        // Wheel
        wheel_badge: "দৈনিক ফ্রি স্পিন সক্রিয়",
        wheel_h3: "হুইল ঘুরিয়ে রিওয়ার্ড জিতুন",
        wheel_p: "প্রতিটি সেগমেন্টে ৳১,০০০ থেকে ৳৫০,০০০ মেগা জ্যাকপট পর্যন্ত আকর্ষণীয় পুরস্কার সাজানো রয়েছে।",
        wheel_last_res: "সর্বশেষ স্পিন ফলাফল",
        wheel_verified: "যাচাইকৃত ক্যাশ রিওয়ার্ড প্রস্তুত",
        wheel_spin_cta: "Spin Now to Unlock (স্পিন করুন)",
        wheel_reset: "আবার চেষ্টা করুন",

        // Scratch Card
        scratch_badge: "গোল্ডেন স্ক্র্যাচ কার্ড",
        scratch_h3: "ঘষুন এবং তাত্ক্ষণিক জিতুন",
        scratch_p: "কার্ডের গোল্ডেন ফয়েলটি স্ক্র্যাচ করে ৫০% সম্পূর্ণ করলেই সম্পূর্ণ রিওয়ার্ড স্বয়ংক্রিয়ভাবে আনলক হয়ে যাবে।",
        scratch_max_label: "সর্বোচ্চ সম্ভাব্য পুরস্কার",
        scratch_max_val: "৳২৫,০০০ পর্যন্ত ইনস্ট্যান্ট বোনাস",
        scratch_payout_check: "✓ ১০০% নিশ্চিত পেআউট কোড",
        scratch_claim_cta: "Claim Reward (রিওয়ার্ড ক্লেইম)",
        scratch_auto_btn: "স্বয়ংক্রিয় স্ক্র্যাচ",
        scratch_new_btn: "নতুন কার্ড নিন",
        scratch_initial_prompt: "কার্ডের ওপর মাউস বা আঙুল ঘষুন...",

        // Features
        features_eyebrow: "প্রিমিয়াম প্ল্যাটফর্ম",
        features_title: "প্ল্যাটফর্মের প্রধান সুবিধাসমূহ",
        features_subtitle: "আধুনিক গেমিং এবং প্রিমিয়াম রিওয়ার্ড সিস্টেমের অতুলনীয় সুবিধা।",
        feat1_title: "অ্যানিমেটেড রিওয়ার্ড",
        feat1_desc: "হুইল স্পিন ও স্ক্র্যাচ কার্ডের মাধ্যমে রিয়েল-টাইম বোনাস উপভোগ করুন।",
        feat2_title: "প্রিমিয়াম ড্যাশবোর্ড",
        feat2_desc: "ব্যালেন্স, প্রগ্রেস ও হিস্ট্রি একসাথে এক নজরে নিরীক্ষণ করুন।",
        feat3_title: "লাইভ লিডারবোর্ড",
        feat3_desc: "শীর্ষ পারফরমারদের র‍্যাঙ্কিং ও দৈনিক স্কোর স্বয়ংক্রিয়ভাবে আপডেট হয়।",
        feat4_title: "মোবাইল এক্সপেরিয়েন্স",
        feat4_desc: "স্মার্টফোন, ট্যাবলেট ও ডেস্কটপে সমান মসৃণ ও দ্রুতগতি সম্পন্ন ইন্টারফেস।",
        feat5_title: "সুরক্ষিত এনক্রিপশন",
        feat5_desc: "মিলিটারি-গ্রেড 256-Bit SSL এনক্রিপশন দ্বারা আপনার অ্যাকাউন্ট তথ্য সম্পূর্ণ নিরাপদ।",
        feat6_title: "২৪/৭ লাইভ সাপোর্ট",
        feat6_desc: "যেকোনো অনুসন্ধানে সার্বক্ষণিক বন্ধুত্বপূর্ণ সহায়তা ও লাইভ চ্যাট সমাধান।",

        // VIP Tiers
        vip_eyebrow: "ভিআইপি প্রিভিলেজ ক্লাব",
        vip_title: "ভিআইপি মেম্বারশিপ টায়ার ও সুবিধা",
        vip_subtitle: "প্রতিটি লেভেলে উচ্চতর ক্যাশব্যাক রিবেট, এক্সক্লুসিভ টুর্নামেন্ট অ্যাক্সেস এবং ব্যক্তিগত কনসিয়ার্জ উপভোগ করুন।",
        vip_cashback_label: "Cashback % (ক্যাশব্যাক)",
        vip_access_label: "Exclusive Access (এক্সক্লুসিভ অ্যাক্সেস)",
        vip_cta_bronze: "ব্রোঞ্জ টায়ার ক্লেইম",
        vip_cta_silver: "সিলভার টায়ারে আপগ্রেড",
        vip_cta_gold: "গোল্ড ভিআইপি আনলক করুন",
        vip_cta_platinum: "প্লাটিনাম প্রো জয়েন করুন",
        vip_cta_diamond: "ডায়মন্ড এলিট কনসিয়ার্জ",

        // How It Works
        how_eyebrow: "সহজ গাইডলাইন",
        how_title: "কীভাবে রিওয়ার্ড ক্লেইম করবেন",
        how_subtitle: "মাত্র ৩টি সহজ ধাপে আপনার বোনাস ওয়ালেটে গ্রহণ করুন।",
        how_step1_badge: "ধাপ ০১",
        how_step1_title: "অ্যাকাউন্ট ভেরিফিকেশন",
        how_step1_desc: "আপনার ফোন নম্বর বা প্লেয়ার আইডি প্রদান করে সিকিউর ভেরিফিকেশন সম্পন্ন করুন।",
        how_step2_badge: "ধাপ ০২",
        how_step2_title: "ইন্টারেক্টিভ স্পিন বা স্ক্র্যাচ",
        how_step2_desc: "লাকি হুইল ঘুরিয়ে বা স্ক্র্যাচ কার্ড ঘষে আকর্ষণীয় ক্যাশ রিওয়ার্ড ড্র করুন।",
        how_step3_badge: "ধাপ ০৩",
        how_step3_title: "তাৎক্ষণিক ওয়ালেট ট্রান্সফার",
        how_step3_desc: "বিকাশ, নগদ বা রকেট ওয়ালেটে সরাসরি কোনো ফি ছাড়াই ক্যাশ ক্রেডিট গ্রহণ করুন।",

        // Leaderboard
        lb_eyebrow: "সেরা পারফরমার",
        lb_title: "সর্বোচ্চ বিজয়ী লিডারবোর্ড",
        lb_subtitle: "প্ল্যাটফর্মের শীর্ষ সফল খেলোয়াড় ও রিওয়ার্ড অর্জনকারীদের তালিকা।",
        lb_filter_all: "সর্বকালের সেরা",
        lb_filter_today: "আজকের সেরা",
        lb_col_rank: "র‍্যাংক",
        lb_col_user: "ব্যবহারকারী",
        lb_col_claims: "ক্লেইম সংখ্যা",
        lb_col_points: "মোট পয়েন্ট",

        // FAQ
        faq_eyebrow: "প্রশ্নোত্তর",
        faq_title: "সচরাচর জিজ্ঞাসিত প্রশ্নাবলী (FAQ)",
        faq_subtitle: "প্ল্যাটফর্ম সম্পর্কে প্রয়োজনীয় তথ্যাবলী ও সাধারণ জিজ্ঞাসা।",

        // Modal
        modal_step1_progress: "ধাপ ১ / ৩: একাউন্ট ভেরিফিকেশন",
        modal_step1_title: "আপনার অ্যাকাউন্ট ভেরিফাই করুন",
        modal_step1_desc: "যে ওয়ালেট বা অ্যাকাউন্টে ক্যাশ বোনাস গ্রহণ করতে চান তার বিবরণ প্রদান করুন।",
        modal_method_phone: "📱 বিকাশ / নগদ / রকেট",
        modal_method_id: "🆔 প্লেয়ার আইডি / ইমেইল",
        modal_ssl_guarantee: "256-Bit SSL এনক্রিপশনের মাধ্যমে সম্পূর্ণ নিরাপদে সংরক্ষিত",
        modal_step1_next_btn: "পরবর্তী ধাপ: টাস্ক সম্পন্ন করুন",
        modal_step2_progress: "ধাপ ২ / ৩: রিওয়ার্ড আনলক টাস্ক",
        modal_step2_title: "একটি সহজ টাস্ক সম্পন্ন করুন",
        modal_step2_desc: "নিচের যেকোনো ১টি ইন্টারেক্টিভ টাস্ক সম্পন্ন করে তাত্ক্ষণিকভাবে ১০০% রিওয়ার্ড আনলক করুন:",
        modal_task_whatsapp: "WhatsApp এ শেয়ার করুন",
        modal_task_whatsapp_sub: "বন্ধুদের জানিয়ে রিওয়ার্ড ১০০% নিশ্চিত করুন",
        modal_task_messenger: "Messenger এ শেয়ার করুন",
        modal_task_messenger_sub: "ফেসবুক মেসেঞ্জারে লিঙ্ক পাঠান",
        modal_task_spin: "কুইক স্পিন টাস্ক (Quick Spin)",
        modal_task_spin_sub: "১-ক্লিকে তাৎক্ষণিক স্পিন করে আনলক করুন",
        modal_step2_direct_btn: "সরাসরি রিওয়ার্ডে যান",
        modal_step3_progress: "ধাপ ৩ / ৩: রিওয়ার্ড প্রস্তুত",
        modal_step3_badge: "🎉 বোনাস সফলভাবে নির্ধারিত",
        modal_step3_title: "অভিনন্দন! আপনার রিওয়ার্ড প্রস্তুত",
        modal_step3_calc_title: "হিসাবকৃত চূড়ান্ত ক্যাশ বোনাস",
        modal_step3_recipient_lbl: "প্রাপক ওয়ালেট:",
        modal_step3_type_lbl: "ট্রানজেকশন টাইপ:",
        modal_step3_type_val: "ইনস্ট্যান্ট ক্যাশ ক্রেডিট",
        modal_step3_expiry_lbl: "অফার মেয়াদ বাকি:",
        modal_claim_to_wallet_btn: "ওয়ালেটে ট্রান্সফার করুন (Claim to Wallet)",

        // Footer
        footer_brand_desc: "অফিসিয়াল প্রিমিয়াম বোনাস ও ইনস্ট্যান্ট রিওয়ার্ড প্ল্যাটফর্ম।",
        footer_privacy: "Privacy Policy (গোপনীয়তা নীতি)",
        footer_terms: "Terms of Service (ব্যবহারের শর্তাবলী)",
        footer_disclaimer: "Disclaimer (দাবিত্যাগ)",
        footer_support: "Contact Support (২৪/৭ সহায়তা কেন্দ্র)",
        footer_copy: "© 2026 ClaimBonus24. All rights reserved.",
        footer_security_desc: "এনক্রিপ্টেড সিকিউরিটি ও ২৪/৭ নির্ভরযোগ্য কাস্টমার সাপোর্ট দ্বারা সুরক্ষিত।",
        trust_ssl: "256-Bit SSL Encrypted",
        trust_payout: "Verified Instant Payouts",
        trust_support: "২৪/৭ কাস্টমার সাপোর্ট",
        trust_responsible: "দায়িত্বশীল প্ল্যাটফর্ম"
      },
      en: {
        // Brand & Nav
        brand_tagline: "Official Rewards Platform",
        ssl_title: "HTTPS 256-Bit SSL",
        ssl_sub: "Verified Encrypted",
        nav_dashboard: "Dashboard",
        nav_wheel: "Bonus Wheel",
        nav_scratch: "Scratch Card",
        nav_leaderboard: "Leaderboard",
        nav_vip: "VIP Tiers",
        nav_how: "How It Works",
        nav_faq: "FAQ",
        nav_claim_btn: "Claim Bonus",
        mobile_lang_label: "Language / ভাষা",

        // Ticker
        ticker_badge: "Live Claim Feed",
        today_claim_label: "Today's Total Claims:",

        // Hero
        hero_badge: "Exclusive Rewards Platform",
        hero_title: "Welcome Bonus &<br><span class=\\"text-accent\\">Premium Rewards</span>",
        hero_lead: "Experience premier gaming rewards, daily cashback, and exclusive VIP privileges directly from your personal dashboard.",
        hero_claim_btn: "Claim Bonus Now",
        hero_explore_btn: "Explore Features",
        trust_metric_vip_val: "12,800+",
        trust_metric_vip_lbl: "Active VIP Members",
        trust_metric_time_val: "3 Minutes",
        trust_metric_time_lbl: "Instant Cashout Time",
        trust_metric_fund_val: "৳5,000,000+",
        trust_metric_fund_lbl: "Daily Reward Fund",

        // Dashboard
        dash_eyebrow: "Live Analytics",
        dash_title: "Your Rewards Dashboard",
        dash_lead: "Track your balance, active streaks, and recent claims in real-time.",
        card1_title: "Total Reward Balance",
        card1_action: "Instant Cashout",
        card2_title: "Daily Streak Bonus",
        card2_badge: "7 Days Active Streak",
        card2_desc: "Log in daily to unlock an extra 500 reward points.",
        card2_progress_label: "Next Tier Bonus Level",
        card3_title: "Today's Claim Status",
        card3_badge: "Active & Ready",
        card3_desc: "Your daily wheel spin and golden scratch reward are waiting.",
        card3_action: "Claim Reward Now",
        card4_title: "Live Verified Activity Stream",

        // Gamification
        game_eyebrow: "Interactive Gamification Rewards",
        game_title: "Spin the Wheel & Scratch to Win",
        game_subtitle: "Spin the lucky wheel or scratch the golden card to unlock instant cash rewards from ৳1,000 up to ৳50,000.",
        tab_wheel: "Lucky Spin Wheel",
        tab_scratch: "Scratch & Win Card",

        // Wheel
        wheel_badge: "Daily Free Spin Active",
        wheel_h3: "Spin the Wheel & Win Cash",
        wheel_p: "Every segment is loaded with verified rewards from ৳1,000 up to a ৳50,000 Mega Jackpot.",
        wheel_last_res: "Latest Spin Result",
        wheel_verified: "Verified Cash Reward Ready",
        wheel_spin_cta: "Spin Now to Unlock",
        wheel_reset: "Try Again",

        // Scratch Card
        scratch_badge: "Golden Scratch Card",
        scratch_h3: "Scratch & Win Instantly",
        scratch_p: "Scratch 50% of the golden foil to automatically reveal and unlock your full cash reward.",
        scratch_max_label: "Maximum Potential Prize",
        scratch_max_val: "Up to ৳25,000 Instant Bonus",
        scratch_payout_check: "✓ 100% Guaranteed Payout Voucher",
        scratch_claim_cta: "Claim Revealed Reward",
        scratch_auto_btn: "Auto Scratch",
        scratch_new_btn: "Get New Card",
        scratch_initial_prompt: "Scratch over the card using mouse or finger...",

        // Features
        features_eyebrow: "Premium Platform",
        features_title: "Core Platform Features",
        features_subtitle: "Unrivaled gaming perks, rapid payouts, and institutional-grade reward security.",
        feat1_title: "Gamified Rewards",
        feat1_desc: "Enjoy real-time bonuses through interactive wheel spins and holographic scratch cards.",
        feat2_title: "Pro Dashboard",
        feat2_desc: "Monitor your verified balance, milestones, and transaction ledger in one unified hub.",
        feat3_title: "Live Leaderboard",
        feat3_desc: "Real-time updates ranking the platform's highest-earning players and daily point leaders.",
        feat4_title: "Mobile-First UX",
        feat4_desc: "High-performance responsive design optimized for smartphones, tablets, and desktops.",
        feat5_title: "256-Bit SSL Encryption",
        feat5_desc: "Military-grade encryption protects your account data and transactions around the clock.",
        feat6_title: "24/7 Priority Support",
        feat6_desc: "Instant live chat and dedicated support reps available 24 hours a day, 7 days a week.",

        // VIP Tiers
        vip_eyebrow: "VIP Privilege Club",
        vip_title: "VIP Membership Tiers & Privileges",
        vip_subtitle: "Enjoy higher cashback rebates, private tournament entries, and personal concierge services at every tier.",
        vip_cashback_label: "Cashback Rebate %",
        vip_access_label: "Exclusive Privilege Access",
        vip_cta_bronze: "Claim Bronze Tier",
        vip_cta_silver: "Upgrade to Silver",
        vip_cta_gold: "Unlock Gold VIP",
        vip_cta_platinum: "Join Platinum Pro",
        vip_cta_diamond: "Diamond Elite Concierge",

        // How It Works
        how_eyebrow: "Simple Guide",
        how_title: "How to Claim Your Rewards",
        how_subtitle: "Receive your verified bonus in your wallet in just 3 quick steps.",
        how_step1_badge: "Step 01",
        how_step1_title: "Account Verification",
        how_step1_desc: "Provide your phone number or account ID for encrypted 256-bit verification.",
        how_step2_badge: "Step 02",
        how_step2_title: "Interactive Spin or Scratch",
        how_step2_desc: "Spin the lucky wheel or scratch the golden card to reveal your winning payout.",
        how_step3_badge: "Step 03",
        how_step3_title: "Instant Wallet Transfer",
        how_step3_desc: "Receive cash credits directly into your bKash, Nagad, or Rocket wallet with zero fees.",

        // Leaderboard
        lb_eyebrow: "Top Performers",
        lb_title: "Top Winners Leaderboard",
        lb_subtitle: "Official ledger celebrating the highest-earning players across the platform.",
        lb_filter_all: "All Time Top",
        lb_filter_today: "Today's Top",
        lb_col_rank: "Rank",
        lb_col_user: "Player",
        lb_col_claims: "Total Claims",
        lb_col_points: "Points Won",

        // FAQ
        faq_eyebrow: "Help Center",
        faq_title: "Frequently Asked Questions (FAQ)",
        faq_subtitle: "Essential details and answers to commonly asked questions about our rewards.",

        // Modal
        modal_step1_progress: "Step 1 / 3: Account Verification",
        modal_step1_title: "Verify Your Account",
        modal_step1_desc: "Enter the wallet or account ID where you would like to receive your instant cash bonus.",
        modal_method_phone: "📱 bKash / Nagad / Rocket",
        modal_method_id: "🆔 Player ID / Email",
        modal_ssl_guarantee: "Protected by 256-Bit SSL End-to-End Encryption",
        modal_step1_next_btn: "Proceed to Task Verification",
        modal_step2_progress: "Step 2 / 3: Interactive Reward Task",
        modal_step2_title: "Complete a Quick Task",
        modal_step2_desc: "Complete any 1 interactive task below to unlock your 100% verified cash reward:",
        modal_task_whatsapp: "Share via WhatsApp",
        modal_task_whatsapp_sub: "Share with friends to secure 100% bonus unlock",
        modal_task_messenger: "Share via Messenger",
        modal_task_messenger_sub: "Send bonus invitation via Facebook Messenger",
        modal_task_spin: "Quick Spin Task",
        modal_task_spin_sub: "1-click instant spin to unlock verified payout",
        modal_step2_direct_btn: "Proceed Directly to Reward",
        modal_step3_progress: "Step 3 / 3: Reward Ready",
        modal_step3_badge: "🎉 Bonus Successfully Calculated",
        modal_step3_title: "Congratulations! Your Reward is Ready",
        modal_step3_calc_title: "Calculated Final Cash Bonus",
        modal_step3_recipient_lbl: "Recipient Wallet:",
        modal_step3_type_lbl: "Transaction Type:",
        modal_step3_type_val: "Instant Cash Credit",
        modal_step3_expiry_lbl: "Offer Time Remaining:",
        modal_claim_to_wallet_btn: "Claim to Wallet Now",

        // Footer
        footer_brand_desc: "Official premium bonus & instant rewards platform.",
        footer_privacy: "Privacy Policy",
        footer_terms: "Terms of Service",
        footer_disclaimer: "Disclaimer",
        footer_support: "Contact Support (24/7)",
        footer_copy: "© 2026 ClaimBonus24. All rights reserved.",
        footer_security_desc: "Protected by encrypted security protocols and 24/7 customer care.",
        trust_ssl: "256-Bit SSL Encrypted",
        trust_payout: "Verified Instant Payouts",
        trust_support: "24/7 Customer Care",
        trust_responsible: "18+ Responsible Platform"
      }
    };

    let currentAppLanguage = localStorage.getItem("cb24_lang") || "bn";

    function setAppLanguage(lang) {
      if (lang !== "bn" && lang !== "en") lang = "bn";
      currentAppLanguage = lang;
      try {
        localStorage.setItem("cb24_lang", lang);
      } catch (e) {}

      // Update html lang attribute
      document.documentElement.lang = lang;

      // Update switcher button states in desktop and mobile
      document.querySelectorAll("[data-lang-btn]").forEach(btn => {
        const btnLang = btn.getAttribute("data-lang-btn");
        const isActive = btnLang === lang;
        btn.classList.toggle("active", isActive);
        btn.setAttribute("aria-pressed", isActive ? "true" : "false");
      });

      // Translate all data-i18n elements
      const dict = I18N_DICTIONARY[lang] || I18N_DICTIONARY.bn;
      document.querySelectorAll("[data-i18n]").forEach(el => {
        const key = el.getAttribute("data-i18n");
        if (dict[key] !== undefined) {
          el.innerHTML = dict[key];
        }
      });

      // Update place-holders if any
      document.querySelectorAll("[data-i18n-placeholder]").forEach(el => {
        const key = el.getAttribute("data-i18n-placeholder");
        if (dict[key] !== undefined) {
          el.placeholder = dict[key];
        }
      });

      // Re-render wheel canvas slices for the language
      if (typeof renderWheel === "function") {
        renderWheel();
      }

      // Re-init scratch card text in canvas
      if (typeof initScratchCard === "function") {
        initScratchCard();
      }

      // Re-render leaderboard for the language
      if (typeof renderLeaderboard === "function" && typeof activeLeaderboardFilter !== "undefined") {
        renderLeaderboard(activeLeaderboardFilter);
      }
    }
"""

# Let's inspect where to insert the i18n script
# We can insert it before initApp() in index.html
assert "function initApp() {" in html, "initApp() not found"
html = html.replace("function initApp() {", i18n_script + "\n    function initApp() {", 1)

# In initApp, make sure setAppLanguage(currentAppLanguage) is called to sync initial state
old_init = """    function initApp() {
      initAdSlots();"""

new_init = """    function initApp() {
      initAdSlots();
      setAppLanguage(currentAppLanguage);"""

assert old_init in html, "old_init not found"
html = html.replace(old_init, new_init, 1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
with open("public/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("I18N engine and dictionary added successfully!")
