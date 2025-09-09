"use client";

import { Swiper, SwiperSlide } from 'swiper/react';
import BestsellersCard  from '@/app/components/cards/bestsellersCard';




export default function Bestsellers() {
    return(
        <section className="flex flex-col w-full justify-center items-center p-8 gap-2">
            <h2 className="text-3xl p-4">Produtos Mais Vendidos</h2>
            <div className="flex gap-2 w-full justify-center items-center">
                <Swiper
                spaceBetween={50}
                slidesPerView={3}
                onSlideChange={() => console.log('slide change')}
                onSwiper={(swiper) => console.log(swiper)}
                >
                <SwiperSlide>Slide 1</SwiperSlide>
                <SwiperSlide>Slide 2</SwiperSlide>
                <SwiperSlide>Slide 3</SwiperSlide>
                <SwiperSlide>Slide 4</SwiperSlide>
                <SwiperSlide>Slide 5</SwiperSlide>
                <SwiperSlide>Slide 6</SwiperSlide>
                <SwiperSlide>Slide 7</SwiperSlide>
                <SwiperSlide>Slide 8</SwiperSlide>
                <SwiperSlide>Slide 9</SwiperSlide>
                </Swiper>
            </div>
        </section>
    );
}