"use client";

import HeroBanner from '@/app/components/heroBanner/heroBanner';
import HeroAboutTheStore from '../components/heroStoreInformation/heroAboutTheStore';

export default function Home() {

  return (
    <section className="w-full h-full">
      <HeroBanner/>
      <HeroAboutTheStore/>

    </section>  
  );
}
