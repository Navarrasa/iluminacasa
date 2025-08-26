"use client";

import { useState, useEffect } from 'react';
import Image from 'next/image';
import { useMediaQuery } from '@mui/material';
import { bannerImages } from "@/data/images"; // ajuste o caminho

export default function HeroBanner() {
  const isMobile = useMediaQuery("(max-width: 689px)");
  const [darkmode, setDarkmode] = useState(false);

  useEffect(() => {
    const dark = localStorage.getItem('dark') === 'true'; // ou a forma que você salva o darkmode
    console.log("caralho")
    setDarkmode(dark);
  }, []);

  const getImage = () => {
    if (isMobile && darkmode) return bannerImages.find(img => img.image === bannerImages[3].image)?.image;
    if (isMobile && !darkmode) return bannerImages.find(img => img.image === bannerImages[2].image)?.image;
    if (!isMobile && darkmode) return bannerImages.find(img => img.image === bannerImages[1].image)?.image;
    return bannerImages.find(img => img.image === bannerImages[0].image)?.image;
  };

  const src = getImage();

  if (!src) return null; // fallback

  return (
    <section className="w-full h-auto">
      <Image
        src={src}
        alt="Banner principal"
        width={1000}
        height={300}
        priority
        style={{ width: "100%", height: "auto" }}
      />
    </section>
  );
}
