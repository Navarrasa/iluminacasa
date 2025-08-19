"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";

export function Header() {
  const pathname = usePathname();

  // Função para checar se o link é ativo
  function isActive(href: string) {
    return pathname === href;
  }

  return (
    <header className="flex justify-between p-4 w-full h-auto">
      <div className="w-full flex items-center justify-between p-8">
        {/* Logo */}
        <div className="text-3xl">IluminaCasa</div>

        {/* Navegação */}
        <nav className="">
          <ul className="flex items-center gap-4 bg-[var(--primary-color)] p-4 rounded-full">
            {[
              { href: "/", label: "Home" },
              { href: "/catalogo", label: "Catálogo" },
              { href: "/sobre", label: "Sobre Nós" },
              { href: "/faq", label: "FAQ" },
              { href: "/contato", label: "Contato" },
            ].map(({ href, label }) => {
              const active = isActive(href);
              return (
                <li key={href}>
                  <Link
                    href={href}
                    className={`px-3 py-1 rounded-full transition duration-500 ease-in-out ${
                      active
                        ? "bg-white shadow-sm text-black"
                        : "text-white hover:bg-white hover:shadow-sm hover:text-black"
                    }`}
                  >
                    {label}
                  </Link>
                </li>
              );
            })}
          </ul>
        </nav>

        {/* Ações do usuário */}
        <div className="flex items-center gap-4">
          {/* Ícone do coração */}
          <button className="w-8 h-8 rounded-full flex items-center justify-center hover:bg-gray-200">
            ❤️
          </button>

          {/* Ícone da sacola com badge */}
          <div className="relative">
            <button className="w-8 h-8 rounded-full bg-black text-white flex items-center justify-center hover:opacity-90">
              👜
            </button>
            <span className="absolute -top-1 -right-1 text-xs bg-red-500 text-white rounded-full px-1">
              2
            </span>
          </div>

          {/* Avatar + Nome */}
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-full bg-gray-300 flex items-center justify-center text-sm">
              👤
            </div>
            <div className="text-sm text-gray-700">
              <span className="text-gray-400">Hi,</span> John Kuper
              <span className="ml-1">▼</span>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}
