"use client";

import { Swiper, SwiperSlide } from 'swiper/react';
import { Autoplay } from 'swiper/modules';
import { GetBestSellers } from '@/app/api/api';
import BestsellersCard  from '@/app/components/cards/bestsellersCard';
import { useEffect, useState } from 'react';
import type { Product } from "@/app/types/types";

export default function Bestsellers() {

    const [product, setProduct] = useState<Product[]>([]);

    useEffect(() => {
        const fetchData = async () => {
            const data = await GetBestSellers();
            setProduct(data);
        };
        fetchData();
    }, []);

    if (!product) {
        return (
            <div className="flex flex-col items-center justify-center text-2xl p-4">
                Carregando Produtos...
            </div>
        );
    }

    return(
        <section className="flex flex-col w-full justify-center items-center p-8 gap-2">
            <h2 className="text-3xl p-4">Produtos Mais Vendidos</h2>
            <div className="flex w-full h-auto justify-center items-center">
                <Swiper
                spaceBetween={30}
                modules={[Autoplay]}
                autoplay={{ delay: 8000, disableOnInteraction: false }}
                loop={true}
                className="w-full h-full"
                slidesPerView={5}
                // onSlideChange={() => console.log('slide change')}
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
                    {product.map((item, idx) => (
                        <SwiperSlide key={idx}>
                            <BestsellersCard product={item} />
                        </SwiperSlide>
                    ))}
                </Swiper>
            </div>
        </section>
    );
}