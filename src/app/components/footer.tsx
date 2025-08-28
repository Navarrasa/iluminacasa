export function Footer() {
    return (
        <footer className="bg-[var(--primary-color)] text-white p-4 mt-10">
            <div className="max-w-4xl mx-auto text-center">
                <p>&copy; {new Date().getFullYear()} IluminaCasa. Todos os direitos reservados.</p>
            </div>
        </footer>
    );
}