"use client";

import Image from 'next/image';
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
    <section className="w-full h-auto">
      <Image
        src={src}
        alt="Banner principal"
        width={1440}
        height={400}
        priority
        style={{ width: "100%", height: "auto", objectFit: "cover" }}
      />
    </section>
  );
}
