"use client";
import { useMediaQuery } from "@mui/material";
import { MobileAccountMenu } from "@/app/components/ui/account_settings/mobileaccountmenu";
import { DesktopAccountMenu } from "@/app/components/ui/account_settings/desktopaccountmenu";
import { Navbar } from "@/app/components/ui/account_settings/navbar";
export function Header() {
  
  const isMobile = useMediaQuery("(max-width: 689px)");

  return (
    <header className="flex justify-between p-4 w-full h-auto fixed z-10 bg-[var(--background-color)]">
      <div className="w-full flex items-center justify-between sm:p-8 p-2">
        {/* Logo */}
        <div className="sm:text-3xl text-2xl font-federant tracking-wider pointer-events-none">IluminaCasa</div>

        {isMobile && <MobileAccountMenu />}

        {/* Navegação - agora separada */}
        {!isMobile && <Navbar />}
        {/* Menu para Desktop/Tablets */}
        {!isMobile && <DesktopAccountMenu />}
      </div>
    </header>
  );
}
