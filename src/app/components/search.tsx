export default function Search() {
    return(
        <section className="flex flex-col text-center w-full justify-center items-center p-8 gap-2">
            <h2 className="text-3xl p-4">Pesquise o produto que deseja aqui</h2>
            <div className="flex flex-col sm:flex-row gap-2 w-full justify-center items-center">
                <input type="text" placeholder="Buscar produtos..." className="border border-[var(--border-color)] p-2 rounded-md sm:w-4/12" />
                <button className="bg-[var(--accent-color)] text-white p-2 rounded-md hover:scale-110 transition duration-700">Pesquisar</button>
            </div>
        </section>
    );
}