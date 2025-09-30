import { useState, useEffect } from "react";


export default function Search() {

    const [query, setQuery] = useState("");
    const [results, setResults] = useState([]);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!query) return;


    return(
        <section className="flex flex-col text-center w-full justify-center items-center p-8 gap-2">
            <h2 className="text-3xl p-4">Pesquise o produto que deseja aqui</h2>
            <form 
            onSubmit={handleSubmit}
            className="flex flex-col sm:flex-row gap-2 w-full justify-center items-center
            ">
                <input type="text" placeholder="Buscar produtos..." className="border border-[var(--border-color)] p-2 rounded-md sm:w-4/12" />
                <button className="bg-[var(--accent-color)] text-white p-2 rounded-md hover:scale-110 transition duration-700">Pesquisar</button>
            </form>
            <div>
                {/* Aqui vai os itens que a search bar encontrar */}
            </div>
        </section>
    );
}