"use client";

import HeroBanner from '@/app/components/heroBanner';
import Search from '@/app/components/search';
import Bestsellers from '@/app/components/bestsellers';
import Reviews from '@/app/components/reviews';

export default function Home() {

  return (
    <section className="w-full h-full">
      <HeroBanner/>
      <Search />
      <Bestsellers />
      <Reviews />
    </section>  
  );
}
