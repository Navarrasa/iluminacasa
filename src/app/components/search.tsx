"use client";
import { useState, useEffect } from "react";
import type { Product } from '@/app/types/types';
import ProductCard from "@/app/components/cards/ProductCard";
import { SearchBarQuery } from "@/app/api/api";

export default function Search() {
  const [searchTerm, setSearchTerm] = useState<string>(""); 
  const [query, setQuery] = useState<string>(""); 
  const [results, setResults] = useState<Product[]>([]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!searchTerm.trim()) {
      setQuery(""); 
      return;
    }
    setQuery(searchTerm.trim());
  };


  useEffect(() => {
    if (!query) {
        setResults([]);
        return;
    };
    const fetchData = async () => {
      const data = await SearchBarQuery(query);
      setResults(data);
    };
    fetchData();
  }, [query]);

  return (
    <section className="flex flex-col text-center w-full justify-center items-center p-8 gap-2">
      <h2 className="text-3xl p-4">Pesquise o produto que deseja aqui</h2>
      <form
        onSubmit={handleSubmit}
        className="flex flex-col sm:flex-row gap-2 w-full justify-center items-center"
      >
        <input
          type="text"
          placeholder="Buscar produtos..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="border border-[var(--border-color)] p-2 rounded-md sm:w-4/12"
        />
        <button
          type="submit"
          className="bg-[var(--accent-color)] text-white p-2 rounded-md hover:scale-110 transition duration-700"
        >
          Pesquisar
        </button>
      </form>

      <div className="flex flex-col w-full justify-center items-center p-8">
        <div className="flex w-full h-auto justify-center items-center gap-4">
            {results.length > 0 ? (
              results.map((item, idx) => (
                <ProductCard key={idx} product={item} />
              ))
            ) : (
              query && <p className="text-2xl">Nenhum produto encontrado.</p>
            )}
        </div>
      </div>
    </section>
  );
}
