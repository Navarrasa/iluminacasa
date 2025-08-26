import { Footer } from '@/app/components/footer';
import { Poppins } from 'next/font/google';
import type { Metadata } from "next";
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

export default function LoginLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-br">
      <body className={`${poppins.className} antialiased`}>
        {children}
        <Footer />
      </body>
    </html>
  )
}
