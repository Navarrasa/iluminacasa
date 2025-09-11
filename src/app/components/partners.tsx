"use client";

import { Swiper, SwiperSlide } from 'swiper/react';
import { Autoplay } from 'swiper/modules';
import PartnerCards from '@/app/components/cards/PartnersCard';
import { partnerImages } from '@/data/images';

export default function PartnerShips() {

    return(
        <section className="w-full flex flex-col p-8 h-auto justify-center items-center">
            <div className='w-8/12 h-auto'>
                <div
                className='w-full flex items-center justify-center p-6 mb-4'>
                    <h2 className='text-3xl text-center'>
                        Parceiros da IluminaCasa
                    </h2>
                </div>
                <div>
                     <Swiper
                    modules={[Autoplay]}
                    autoplay={{ delay: 3000, disableOnInteraction: false }}
                    loop={true}
                    className="w-full h-full"
                    slidesPerView={6.5}
                    // onSlideChange={() => console.log('slide change')}
                    onSwiper={(swiper) => console.log(swiper)}
                    breakpoints={{
                        320: {
                            slidesPerView: 3,
                            spaceBetween: 30,
                        },
                        768: {
                            slidesPerView: 4,
                            spaceBetween: 30,
                        },
                        1024: {
                            slidesPerView: 5,
                            spaceBetween: 30,
                        },
                    }}
                    >
                        {partnerImages.map((partner, idx) => (
                            <SwiperSlide key={partner.id ?? idx}>
                                <PartnerCards image={partner.image} />
                            </SwiperSlide>
                        ))}
                    </Swiper>
                </div>
            </div>
        </section>
    );
}