import type {Metadata} from 'next';
import './globals.css'; // Global styles

export const metadata: Metadata = {
  title: 'ClaimBonus24 — প্রিমিয়াম বোনাস ও রিওয়ার্ড প্ল্যাটফর্ম',
  description: 'ClaimBonus24 প্ল্যাটফর্মে প্রতিদিনের ফ্রি স্পিন, স্ক্র্যাচ কার্ড এবং এক্সক্লুসিভ ক্যাশ রিওয়ার্ড নিরাপদে ক্লেইম করুন।',
  openGraph: {
    title: 'ClaimBonus24 — প্রিমিয়াম বোনাস ও রিওয়ার্ড প্ল্যাটফর্ম',
    description: 'ClaimBonus24 প্ল্যাটফর্মে প্রতিদিনের ফ্রি স্পিন, স্ক্র্যাচ কার্ড এবং এক্সক্লুসিভ ক্যাশ রিওয়ার্ড নিরাপদে ক্লেইম করুন।',
    type: 'website',
    images: [
      {
        url: '/assets/preview-banner.jpg',
        width: 1200,
        height: 630,
        alt: 'ClaimBonus24 — ১০০% ফ্রি ইনস্ট্যান্ট গেম বোনাস পোর্টাল',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'ClaimBonus24 — প্রিমিয়াম বোনাস ও রিওয়ার্ড প্ল্যাটফর্ম',
    description: 'ClaimBonus24 প্ল্যাটফর্মে প্রতিদিনের ফ্রি স্পিন, স্ক্র্যাচ কার্ড এবং এক্সক্লুসিভ ক্যাশ রিওয়ার্ড নিরাপদে ক্লেইম করুন।',
    images: ['/assets/preview-banner.jpg'],
  },
};

export default function RootLayout({children}: {children: React.ReactNode}) {
  return (
    <html lang="bn">
      <body suppressHydrationWarning>{children}</body>
    </html>
  );
}
