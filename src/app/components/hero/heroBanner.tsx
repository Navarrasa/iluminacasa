"use client";

import Image from 'next/image';
import Link from 'next/link';
import { useMediaQuery } from '@mui/material';
import { bannerImages } from "@/data/images";

export default function HeroBanner() {
  const isMobile = useMediaQuery("(max-width:689px)");

  const getImage = () => {
    if (isMobile) return bannerImages[1].image; // mobileLight
    return bannerImages[0].image; // desktopLight
  };

  const src = getImage();

  if (!src) return null;

  return (
    <section className="w-full h-auto relative flex">
      <Image
        src={src}
        alt="Banner principal"
        width={1440}
        height={400}
        priority
        style={{ width: "100%", height: "auto", objectFit: "cover" }}
      />
      <div className='absolute z-10 bottom-0 sm:w-9/12 w-6/12 flex justify-center sm:mb-4 mb-2'>
        <Link href="/catalog" 
        className="bg-[var(--accent-color)] sm:p-4 p-2 rounded-2xl sm:w-[10rem] text-center opacity-90
        hover:scale-110 transition duration-700 hover:opacity-100 text-white font-semibold
        ">Ver Ofertas</Link>
      </div>
    </section>
  );
}
