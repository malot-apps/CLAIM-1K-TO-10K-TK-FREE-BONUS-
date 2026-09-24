/**
 * ==========================================================
 * BETBONUS ADVERTISING CONFIGURATION (ADSTERRA AD NETWORK)
 * ==========================================================
 */

const AD_CONFIG = {
  // Set to true to activate live advertisements across all slots
  AD_ENABLED: true,

  // Primary Direct Link (Smartlink 1)
  AD_LINK: "https://www.profitableratecpmnetwork.com/r5z436skmd?key=c86f3be0ce3e3942e6ee96398137264f",

  // Adsterra Smartlinks / Direct links
  ADSTERRA_DIRECT_LINK: "https://www.profitableratecpmnetwork.com/r5z436skmd?key=c86f3be0ce3e3942e6ee96398137264f",
  ADSTERRA_DIRECT_LINK_2: "https://www.profitableratecpmnetwork.com/yunapnbq?key=8c787f16e47543a3e5116482e196969c",
  ADSTERRA_LINK: "https://www.profitableratecpmnetwork.com/r5z436skmd?key=c86f3be0ce3e3942e6ee96398137264f",

  // Enable or disable direct link redirection on buttons (true by default)
  ADSTERRA_CLICK_ENABLED: true,

  // Universal Ad Label (Always prominently displayed above each ad slot)
  AD_LABEL: "ADVERTISEMENT",
  AD_LABEL_BN: "বিজ্ঞাপন (ADVERTISEMENT)",

  // Dedicated Ad Slot Configurations
  AD_SLOTS: {
    slotA: {
      id: "ad-slot-a",
      name: "AD SLOT A — Native Banner (After Dashboard)",
      headline: "Sponsored Featured Offer",
      headlineBn: "স্পন্সর অফার · স্পেশাল ডিল",
      description: "Adsterra Native Banner Responsive Unit",
      ctaText: "বিজ্ঞাপন দেখুন (Visit Sponsor)",
      badgeText: "SPONSORED"
    },
    slotB: {
      id: "ad-slot-b",
      name: "AD SLOT B — 728x90 Banner (Between Leaderboard & FAQ)",
      headline: "Official Partner Showcase",
      headlineBn: "ফিচার্ড পার্টনার · এক্সক্লুসিভ ব্রাউজিং",
      description: "Adsterra 728×90 Standard Responsive Banner",
      ctaText: "বিজ্ঞাপন লিংক খুলুন (Open Partner Link)",
      badgeText: "SPONSORED"
    },
    slotC: {
      id: "ad-slot-c",
      name: "AD SLOT C — Native Banner (Lower Content Section)",
      headline: "Explore Verified Partner Directory",
      headlineBn: "যাচাইকৃত পার্টনার শোপেইজ এক্সপ্লোর করুন",
      description: "Adsterra Native Banner Responsive Unit",
      ctaText: "বিজ্ঞাপন ভিজিট করুন (Visit Link)",
      badgeText: "SPONSORED"
    },
    slotD: {
      id: "ad-slot-d",
      name: "AD SLOT D — 728x90 Banner (Footer Area)",
      headline: "Community Sponsor Notice",
      headlineBn: "কমিউনিটি স্পন্সর ও পার্টনার বিজ্ঞপ্তি",
      description: "Adsterra 728×90 Standard Responsive Banner",
      ctaText: "স্পন্সর বিস্তারিত (Sponsor Info)",
      badgeText: "SPONSORED"
    }
  }
};

// Global browser window attachment
if (typeof window !== "undefined") {
  window.AD_CONFIG = AD_CONFIG;
}

// CommonJS module export support
if (typeof module !== "undefined" && module.exports) {
  module.exports = AD_CONFIG;
}
