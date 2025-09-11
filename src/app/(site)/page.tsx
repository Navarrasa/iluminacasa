"use client";

import HeroBanner from '@/app/components/hero/heroBanner';
import Search from '@/app/components/search';
import Bestsellers from '@/app/components/bestsellers';
import PartnerShips from '@/app/components/partners';

export default function Home() {

  return (
    <section className="w-full h-full">
      <HeroBanner/>
      <Search />
      <Bestsellers />
      <PartnerShips />
    </section>  
  );
}
