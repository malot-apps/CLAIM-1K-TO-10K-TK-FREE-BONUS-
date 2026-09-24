import type {Metadata} from 'next';
import './globals.css'; // Global styles

export const metadata: Metadata = {
  title: 'BetBonus — প্রিমিয়াম রিওয়ার্ড ও এক্সক্লুসিভ বোনাস প্ল্যাটফর্ম',
  description: 'সেরা গেমিং রিওয়ার্ড, দৈনিক ক্যাশব্যাক এবং এক্সক্লুসিভ ভিআইপি অফার সরাসরি আপনার ড্যাশবোর্ড থেকে উপভোগ করুন।',
  openGraph: {
    title: 'BetBonus — প্রিমিয়াম রিওয়ার্ড ও এক্সক্লুসিভ বোনাস প্ল্যাটফর্ম',
    description: 'সেরা গেমিং রিওয়ার্ড, দৈনিক ক্যাশব্যাক এবং এক্সক্লুসিভ ভিআইপি অফার সরাসরি আপনার ড্যাশবোর্ড থেকে উপভোগ করুন।',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'BetBonus — প্রিমিয়াম রিওয়ার্ড ও এক্সক্লুসিভ বোনাস প্ল্যাটফর্ম',
    description: 'সেরা গেমিং রিওয়ার্ড, দৈনিক ক্যাশব্যাক এবং এক্সক্লুসিভ ভিআইপি অফার সরাসরি আপনার ড্যাশবোর্ড থেকে উপভোগ করুন।',
  },
};

export default function RootLayout({children}: {children: React.ReactNode}) {
  return (
    <html lang="bn">
      <body suppressHydrationWarning>{children}</body>
    </html>
  );
}
