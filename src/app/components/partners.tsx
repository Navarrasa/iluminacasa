"use client";

import { Swiper, SwiperSlide } from 'swiper/react';
import { Autoplay } from 'swiper/modules';

export default function PartnerShips() {

    return(
        <section className="w-full flex flex-col p-4">
            <div>
                <h2>
                    Parceiros da IluminaCasa
                </h2>
            </div>
            <div>
                 <Swiper
                spaceBetween={50}
                modules={[Autoplay]}
                autoplay={{ delay: 3000, disableOnInteraction: false }}
                loop={true}
                className="w-full h-full"
                slidesPerView={6}
                onSlideChange={() => console.log('slide change')}
                onSwiper={(swiper) => console.log(swiper)}
                breakpoints={{
                    320: {
                        slidesPerView: 1,
                        spaceBetween: 10
                    },
                    768: {
                        slidesPerView: 2,
                        spaceBetween: 20
                    },
                    1024: {
                        slidesPerView: 3,
                        spaceBetween: 30
                    },
                    1280: {
                        slidesPerView: 4,
                        spaceBetween: 30
                    },
                    1440: {
                        slidesPerView: 5,
                        spaceBetween: 30
                    }

                }}
                >
                    {partners.map((item, idx) => (
                        <SwiperSlide key={idx}>
                            <PartnersCard product={item} />
                        </SwiperSlide>
                    ))}
                </Swiper>
            </div>
        </section>
    );
}