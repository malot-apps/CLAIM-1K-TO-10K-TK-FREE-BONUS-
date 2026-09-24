import type {Metadata} from 'next';
import './globals.css'; // Global styles

export const metadata: Metadata = {
  title: 'ClaimBonus24 — প্রিমিয়াম বোনাস ও রিওয়ার্ড প্ল্যাটফর্ম',
  description: 'ClaimBonus24 প্ল্যাটফর্মে প্রতিদিনের ফ্রি স্পিন, স্ক্র্যাচ কার্ড এবং এক্সক্লুসিভ ক্যাশ রিওয়ার্ড নিরাপদে ক্লেইম করুন।',
  openGraph: {
    title: 'ClaimBonus24 — প্রিমিয়াম বোনাস ও রিওয়ার্ড প্ল্যাটফর্ম',
    description: 'ClaimBonus24 প্ল্যাটফর্মে প্রতিদিনের ফ্রি স্পিন, স্ক্র্যাচ কার্ড এবং এক্সক্লুসিভ ক্যাশ রিওয়ার্ড নিরাপদে ক্লেইম করুন।',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'ClaimBonus24 — প্রিমিয়াম বোনাস ও রিওয়ার্ড প্ল্যাটফর্ম',
    description: 'ClaimBonus24 প্ল্যাটফর্মে প্রতিদিনের ফ্রি স্পিন, স্ক্র্যাচ কার্ড এবং এক্সক্লুসিভ ক্যাশ রিওয়ার্ড নিরাপদে ক্লেইম করুন।',
  },
};

export default function RootLayout({children}: {children: React.ReactNode}) {
  return (
    <html lang="bn">
      <body suppressHydrationWarning>{children}</body>
    </html>
  );
}
