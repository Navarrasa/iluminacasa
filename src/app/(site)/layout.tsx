import type { Metadata } from "next";
import { Poppins } from 'next/font/google';
import { Header } from "@/app/components/header";
import { Footer } from '@/app/components/footer';
import "@/styles/globals.css";

const poppins = Poppins({
  subsets: ['latin'],
  weight: ['400', '500', '600', '700'],
  display: 'swap',
});

export const metadata: Metadata = {
  title: "IluminaCasa",
  description: "A melhor loja digital para venda de produtos para a sua casa!",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-br">
      <body className={`${poppins.className} antialiased`}>
        <Header />
        <main className="                 sm:mt-[152px] mt-[90px]">{children}</main>
        <Footer />
      </body>
    </html>
  );
}
