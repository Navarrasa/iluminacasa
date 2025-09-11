'use client';

import React from "react";
import Image from "next/image";

export type Product = {
  title: string;
  category: string;
  price: number;
  discount: number;
  rating: number;
  image: string[];
  tags?: string[];
};

interface ProductCardProps {
  product: Product;
}

export default function BestsellersCard({ product }: ProductCardProps) {
  return (
    <div className="w-auto rounded-2xl shadow-md overflow-hidden bg-white flex flex-col h-auto">
      {/* Tags no topo */}
      {product.tags && (
        <div className="absolute flex gap-2 p-2">
          {product.tags.map((tag, idx) => (
            <span
              key={idx}
              className="text-xs font-semibold bg-black/10 text-black/60 px-2 py-1 rounded-md"
            >
              {tag}
            </span>
          ))}
        </div>
      )}

      {/* Imagem */}
      <div className="h-full w-full p-4">
        <Image
          src={product.image[0]}
          alt={product.title}
          className="w-full h-full object-cover"
          width={500}
          height={500}
        />
      </div>

      {/* Conteúdo */}
      <div className="flex flex-col gap-1 p-4">
        <h3 className="text-lg font-semibold">{product.title}</h3>
        <p className="text-base font-bold">R$ {product.price.toFixed(2)}</p>

        <button className="mt-2 bg-blue-500 hover:bg-blue-600 text-white py-2 rounded-xl text-sm font-semibold">
          Saiba mais
        </button>
      </div>
    </div>
  );
};