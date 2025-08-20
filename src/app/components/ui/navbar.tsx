"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";

export function Navbar() {
  const pathname = usePathname();

  // Verifica se o link é o ativo
  function isActive(href: string) {
    return pathname === href;
  }

  const links = [
    { href: "/", label: "Home" },
    { href: "/catalogo", label: "Catálogo" },
    { href: "/sobre", label: "Sobre Nós" },
    { href: "/faq", label: "FAQ" },
    { href: "/contato", label: "Contato" },
  ];

  return (
    <nav>
      <ul className="flex items-center gap-4 bg-[var(--primary-color)] p-4 rounded-full">
        {links.map(({ href, label }) => {
          const active = isActive(href);
          return (
            <li key={href}>
              <Link
                href={href}
                className={`px-3 py-1 rounded-full transition duration-500 ease-in-out ${
                  active
                    ? "bg-[var(--secondary-color)] border-none text-white"
                    : "text-white hover:bg-[var(--secondary-color)] hover:shadow-sm"
                }`}
              >
                {label}
              </Link>
            </li>
          );
        })}
      </ul>
    </nav>
  );
}
