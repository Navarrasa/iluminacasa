"use client";

import Image from 'next/image';
import { useTheme, useMediaQuery } from '@mui/material';
import { bannerImages } from "@/data/images";

export default function HeroBanner() {
  const theme = useTheme();
  const isMobile = useMediaQuery("(max-width:689px)");
  const darkmode = theme.palette.mode === 'dark';

  const getImage = () => {
    if (isMobile && darkmode) return bannerImages[3].image; // mobileDark
    if (isMobile && !darkmode) return bannerImages[2].image; // mobileLight
    if (!isMobile && darkmode) return bannerImages[1].image; // desktopDark
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
        style={{ width: "100%", height: "auto" }}
      />
    </section>
  );
}
