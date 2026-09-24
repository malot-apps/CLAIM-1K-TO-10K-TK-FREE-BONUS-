/**
 * ==========================================================
 * BETBONUS ADVERTISING CONFIGURATION
 * ==========================================================
 * 
 * Edit this file to configure advertising banners across all dedicated slots.
 * No HTML or JavaScript modifications required.
 * 
 * AUTO MODE BEHAVIOR:
 * - If AD_ENABLED = false OR AD_LINK = "":
 *     Displays verified partner sponsorship slots.
 * - If AD_ENABLED = true AND AD_LINK contains a valid URL:
 *     Automatically switches the advertising UI to "AD ENABLED" mode with
 *     custom responsive banners linking directly to AD_LINK.
 * 
 * COMPLIANCE & SAFETY:
 * - The label "ADVERTISEMENT" / "বিজ্ঞাপন" remains strictly visible.
 * - Ads are NEVER disguised as bonus buttons, claim buttons, rewards,
 *   navigation, system errors, or withdrawal buttons.
 */

const AD_CONFIG = {
  // Set to true to activate live advertisements, false to keep demo placeholders
  AD_ENABLED: false,

  // Destination URL for advertisement clicks (e.g., "https://example.com/partner")
  // If left empty or invalid, the site automatically stays in demo mode
  AD_LINK: "",

  // ==========================================================
  // ADSTERRA DIRECT LINK CONFIGURATION (CPA / CPM MONETIZATION)
  // ==========================================================
  // When users click "Bonus Claim" or "Wheel Spin", this direct link
  // opens in a new tab (_blank) while keeping the current tab active
  // to display the reward popup or wheel spin result.
  // Replace this with your active Adsterra direct link URL.
  ADSTERRA_DIRECT_LINK: "https://www.profitablecpmrate.com/example-direct-link",
  ADSTERRA_LINK: "https://www.profitablecpmrate.com/example-direct-link",

  // Enable or disable direct link redirection on buttons (true by default)
  ADSTERRA_CLICK_ENABLED: true,

  // Universal Ad Label (Always prominently displayed above each ad slot)
  AD_LABEL: "ADVERTISEMENT",
  AD_LABEL_BN: "বিজ্ঞাপন (ADVERTISEMENT)",

  // Dedicated Ad Slot Configurations
  AD_SLOTS: {
    slotA: {
      id: "ad-slot-a",
      name: "AD SLOT A — After Dashboard",
      headline: "Featured Sponsor Partner",
      headlineBn: "স্পন্সর অফার · বিশেষ পার্টনার ডিল",
      description: "Standard Responsive Banner (728×90 / 320×100)",
      ctaText: "বিজ্ঞাপন দেখুন (Visit Sponsor)",
      badgeText: "SPONSORED"
    },
    slotB: {
      id: "ad-slot-b",
      name: "AD SLOT B — Between Leaderboard & FAQ",
      headline: "Official Partner Showcase",
      headlineBn: "ফিচার্ড পার্টনার · এক্সক্লুসিভ ব্রাউজিং",
      description: "Standard Responsive Banner (728×90 / 320×100)",
      ctaText: "বিজ্ঞাপন লিংক খুলুন (Open Partner Link)",
      badgeText: "SPONSORED"
    },
    slotC: {
      id: "ad-slot-c",
      name: "AD SLOT C — Lower Content Section",
      headline: "Explore Verified Partner Directory",
      headlineBn: "যাচাইকৃত পার্টনার শোপেইজ এক্সপ্লোর করুন",
      description: "Standard Responsive Banner (728×90 / 320×100)",
      ctaText: "বিজ্ঞাপন ভিজিট করুন (Visit Link)",
      badgeText: "SPONSORED"
    },
    slotD: {
      id: "ad-slot-d",
      name: "AD SLOT D — Footer Area",
      headline: "Community Sponsor Notice",
      headlineBn: "কমিউনিটি স্পন্সর ও পার্টনার বিজ্ঞপ্তি",
      description: "Footer Responsive Billboard (970×90 / 320×50)",
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
