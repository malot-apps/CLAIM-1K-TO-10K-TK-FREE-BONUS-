# BETBONUS — Premium Rewards Demo

> **IMPORTANT DISCLAIMER**  
> **Educational & UI/UX Simulation Only.**  
> This project is strictly a client-side user interface design showcase, physics simulation, and motion study. It is **NOT** a real betting service or gambling platform.  
> - **No real deposits** or banking details are ever accepted or processed.
> - **No withdrawals** or cash-outs exist.
> - **No real accounts** or credentials are created or transmitted.
> - All amounts, leaderboards, user counters, and promotional states are **100% fictional simulation data** generated locally in the browser with zero financial value.

---

## 🌟 Overview

**BETBONUS** is a standalone, ultra-premium static web application inspired by modern sports entertainment platforms, luxury dark-mode SaaS dashboards, and streaming-service interfaces. It demonstrates how to engineer high-contrast typography, physics-based canvas animations, synthesized Web Audio sound effects, and conversion-focused UI flows without external dependencies or server backends.

---

## 📁 File Structure

```text
/
├── index.html          # Self-contained, production-ready static website
├── favicon.svg         # High-resolution vector brand favicon
├── README.md           # Documentation & educational guidelines
├── assets/
│   ├── icons/          # Modular SVG icons (logo, shield, badges)
│   └── images/         # Static imagery placeholders
```

---

## 🚀 Key Features

1. **Top Announcement Bar & Live Notification Ticker**
   - Persistent `DEMO MODE · EDUCATIONAL SIMULATION · NO REAL MONEY` disclosure.
   - Smooth CSS-animated ticker rotating fictional UI simulation events.
   - Pause on hover/focus behavior with accessible ARIA announcements.

2. **Cinematic Hero Section**
   - High-contrast typography paired with electric neon accents (`#B9F34B`).
   - Interactive glassmorphic reward card featuring simulated welcome bonus (`৳500 — ৳1,000`), animated progress indicator, and randomized **Demo Sessions** counter.
   - Explicit trust indicators verifying zero deposit and fictional rewards.

3. **Interactive Simulated Bonus Wheel**
   - Responsive HTML5 Canvas rendering 8 reward segments (`৳500` to `৳1,000`).
   - Realistic deceleration physics (`cubic-bezier(0.12, 0.85, 0.15, 1)`).
   - Real-time peg click sounds and celebratory fanfare generated procedurally via the browser's **Web Audio API** (zero external sound files needed).
   - Custom standalone Canvas particle & confetti explosion engine.
   - Fictional result display with single-click demo reset.

4. **Multi-Step Modal Bonus Claim Simulation**
   - **Step 1:** Enter any arbitrary test identifier (no real email or phone number required).
   - **Step 2:** Transparent sharing screen with strictly neutral wording: *"I tried the BetBonus educational demo — no real money involved"* (with skip option).
   - **Step 3:** Animated simulated result generating random fictional rewards between `৳3,000` and `৳9,999` with automatic synchronization to the demo dashboard.

5. **Demo Dashboard & Activity Stream**
   - 4 glass metric cards: Demo Sessions, Simulated Bonus, Completion Rate, and Live Activity Stream with simulated timestamps (`1m`, `2m`, `3m`).

6. **Dedicated Advertising Inventory (4 Zones)**
   - Clear, standardized advertisement containers with visible `ADVERTISEMENT` labels.
   - Clearly separated from system controls and bonus buttons.
   - Responsive aspect-ratio placeholders (`728×90` desktop / `320×100` mobile).
   - HTML comments denoting approved insertion points:
     - `AD SLOT A` (After Dashboard)
     - `AD SLOT B` (Between Leaderboard and FAQ)
     - `AD SLOT C` (Near Lower Content Area)
     - `AD SLOT D` (Footer Area)

7. **Simulated Community Leaderboard**
   - Illustrative fictional player standings with rank-tinted badges (Gold, Silver, Bronze) and DEMO tags.

8. **Transparency Card & Accordion FAQ**
   - Prominent shield emblem emphasizing UI simulation boundaries.
   - Keyboard-accessible animated accordion addressing common educational questions.

---

## 🎨 Design System

- **Background:** `#050806` (Deep Obsidian Green)
- **Secondary Surface:** `#0A0F0C`
- **Card Background:** `#0E1511`
- **Borders:** `#233129`
- **Primary Accent:** `#B9F34B` (Electric Lime)
- **Secondary Accent:** `#D7FF78`
- **Luxury Gold Accent:** `#F5D061`
- **Primary Text:** `#F4F7F4`
- **Muted Text:** `#7C8981`
- **Typography:** Google Fonts *Space Grotesk* (Display) & *Plus Jakarta Sans* (Body/UI)

---

## 💻 Zero-Build Deployment

Because BetBonus is built with pure HTML5, CSS3, and Vanilla JavaScript, it requires **no Node.js build process, npm install, or backend database**.

You can run and deploy it immediately via:
- **Local Browser:** Double-click `index.html` or open via any local server.
- **GitHub Pages:** Push to repository and enable GitHub Pages on root.
- **Netlify / Vercel / Cloudflare Pages:** Drag-and-drop or connect repository with static output directory `./`.
- **Apache / Nginx / Shared Hosting:** Upload `index.html`, `favicon.svg`, and `assets/` to your public HTML folder.

---

## ♿ Accessibility & Motion

- Full keyboard navigation (Tab navigation, Enter activation, Escape key dismisses modals).
- Proper ARIA roles (`role="dialog"`, `aria-expanded`, `aria-label`).
- Full support for `prefers-reduced-motion` media queries for user comfort.
